# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = "account.move"

    account_move_template = fields.Many2one('account.move.template')
    correggi_importo_registrazione = fields.Float(store=True)

    @api.multi
    def assert_balanced(self):
        # if not self.ids:
        #     return True
        # prec = self.env.user.company_id.currency_id.decimal_places
        #
        # query = """\
        #     SELECT      move_id
        #     FROM        account_move_line
        #     WHERE       move_id in %s
        #     GROUP BY    move_id
        #     HAVING      abs(sum(debit) - sum(credit)) > %s
        #     """
        #
        # logging.info(query % (tuple(self.ids), 10 ** (-max(5, prec))))
        #
        # self._cr.execute(query, (tuple(self.ids), 10 ** (-max(5, prec))))
        # if len(self._cr.fetchall()) != 0:
        #     raise UserError(_("Cannot create unbalanced journal entry."))
        return True

    def set_correggi_importo_registrazione(self):
        # Corregge la registrazione contabile delle move del registro
        # dei corrispettivi
        if 'CORR' in self.journal_id.name:
            if self.correggi_importo_registrazione > 0:
                move_id = self.browse(self.id)
                if move_id.state == 'posted':
                    move_id.button_cancel()
                partner_id = False
                for line in move_id.line_ids:
                    partner_id = line.partner_id
                    line.remove_move_reconcile()
                iva_s_corr = self.env['account.account'].search([('name', '=', 'IVA SU CORRISPETTIVI')])
                iva_corr_id = self.env['account.tax'].search([('name', '=', 'Iva al 22% CORR (debito)')], limit=1)
                corr_p_cessioni = self.env['account.account'].search([('name', '=', 'CORR.P/CESSIONE MERCI-NO VENTILAZ')])
                crediti_v_clienti = self.env['account.account'].search([('name', '=', 'CREDITI V/CLIENTI')], limit=1)
                move_id.company_id = 1
                line_ids = [(5,)]
                # Crediti
                line_ids.append((0, 0, {
                    'debit': move_id.correggi_importo_registrazione,
                    'credit': 0,
                    'name': move_id.ref,
                    'partner_id': partner_id.id if partner_id else False,
                    'account_id': crediti_v_clienti.id,
                    'date_maturity': move_id.date,
                    'company_id': 1,
                    'move_id': move_id.id,
                }))
                # IVA
                line_ids.append((0, 0, {
                    'debit': 0,
                    'credit': move_id.correggi_importo_registrazione - (move_id.correggi_importo_registrazione / 1.22),
                    'name': move_id.ref,
                    'partner_id': partner_id.id if partner_id else False,
                    'account_id': iva_s_corr.id,
                    'date_maturity': move_id.date,
                    'tax_line_id': iva_corr_id.id,
                    'company_id': 1,
                    'move_id': move_id.id,
                }))
                # Merci
                line_ids.append((0, 0, {
                    'debit': 0,
                    'credit': (move_id.correggi_importo_registrazione / 1.22),
                    'name': move_id.ref,
                    'partner_id': partner_id.id if partner_id else False,
                    'account_id': corr_p_cessioni.id,
                    'date_maturity': move_id.date,
                    'tax_ids': [(4, iva_corr_id.id)],
                    'company_id': 1,
                    'move_id': move_id.id,
                }))

                move_id.line_ids = line_ids
                logging.info("modificata")
                if move_id.state == 'draft':
                    move_id.action_post()

    @api.onchange('account_move_template')
    def onchange_template(self):
        account_move_lines = [(5, 0)]
        if self.account_move_template:
            self.journal_id = self.account_move_template.account_journal_id.id
            for line in self.account_move_template.move_line_ids:
                account_move_lines.append((0, 0, {
                    'account_id': line.account_id.id,
                    'name': line.line_description,
                    'is_debit': line.is_debit,
                    'is_credit': line.is_credit,
                    'account_move_template': True,
                }))
            self.line_ids = account_move_lines

    @api.one
    def _prepare_wt_values(self):
        partner = False
        wt_competence = {}
        # First : Partner and WT competence
        for line in self.line_id:
            if line.partner_id:
                partner = line.partner_id
                if partner.property_account_position:
                    for wt in (
                            partner.property_account_position.withholding_tax_ids
                    ):
                        wt_competence[wt.id] = {
                            'withholding_tax_id': wt.id,
                            'partner_id': partner.id,
                            'date': self.date,
                            'account_move_id': self.id,
                            'wt_account_move_line_id': False,
                            'base': 0,
                            'amount': 0,
                        }
                break
        # After : Loking for WT lines
        wt_amount = 0
        for line in self.line_id:
            domain = []
            # WT line
            if line.credit:
                domain.append(
                    ('account_payable_id', '=', line.account_id.id)
                )
                amount = line.credit
            else:
                domain.append(
                    ('account_receivable_id', '=', line.account_id.id)
                )
                amount = line.debit
            wt_ids = self.pool['withholding.tax'].search(
                self.env.cr, self.env.uid, domain)
            if wt_ids:
                wt_amount += amount
                if (
                        wt_competence and wt_competence[wt_ids[0]] and
                        'amount' in wt_competence[wt_ids[0]]
                ):
                    wt_competence[wt_ids[0]]['wt_account_move_line_id'] = (
                        line.id)
                    wt_competence[wt_ids[0]]['amount'] = wt_amount
                    wt_competence[wt_ids[0]]['base'] = (
                        self.pool['withholding.tax'].get_base_from_tax(
                            self.env.cr, self.env.uid, wt_ids[0], wt_amount)
                    )

        wt_codes = []
        if wt_competence:
            for key, val in wt_competence.items():
                wt_codes.append(val)
        res = {
            'partner_id': partner and partner.id or False,
            'move_id': self.id,
            'invoice_id': False,
            'date': self.date,
            'base': wt_codes and wt_codes[0]['base'] or 0,
            'tax': wt_codes and wt_codes[0]['amount'] or 0,
            'withholding_tax_id': (
                    wt_codes and wt_codes[0]['withholding_tax_id'] or False),
            'wt_account_move_line_id': (
                    wt_codes and wt_codes[0]['wt_account_move_line_id'] or False),
            'amount': wt_codes[0]['amount'],
        }
        return res


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    withholding_tax_id = fields.Many2one(
        'withholding.tax', string='Withholding Tax')
    withholding_tax_base = fields.Float(string='Withholding Tax Base')
    withholding_tax_amount = fields.Float(string='Withholding Tax Amount')
    withholding_tax_generated_by_move_id = fields.Many2one(
        'account.move', string='Withholding Tax generated from', readonly=True)
    is_debit = fields.Boolean()
    is_credit = fields.Boolean()

    @api.multi
    def remove_move_reconcile(self):
        # When unreconcile a payment with a wt move linked, it will be
        # unreconciled also the wt account move
        for account_move_line in self:
            rec_move_ids = self.env['account.partial.reconcile']
            domain = [('withholding_tax_generated_by_move_id', '=',
                       account_move_line.move_id.id)]
            wt_mls = self.env['account.move.line'].search(domain)
            # Avoid wt move not in due state
            domain = [('wt_account_move_id', 'in',
                       wt_mls.mapped('move_id').ids)]
            wt_moves = self.env['withholding.tax.move'].search(domain)
            wt_moves.check_unlink()

            for wt_ml in wt_mls:
                rec_move_ids += wt_ml.matched_debit_ids
                rec_move_ids += wt_ml.matched_credit_ids
            rec_move_ids.unlink()
            # Delete wt move
            for wt_move in wt_mls.mapped('move_id'):
                wt_move.button_cancel()
                wt_move.unlink()

        return super(AccountMoveLine, self).remove_move_reconcile()