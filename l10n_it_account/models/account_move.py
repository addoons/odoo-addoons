# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = "account.move"

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