# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)
from odoo import api, fields, models


class WizardSchedeContabili(models.TransientModel):
    """
    Le schede contabili sono report Dinamici/PDF utilizzati
    Per verificare lo stato dare/avere e saldo di determinati conti o Partners
    Questo Wizard permette la generazione di un report
    """
    _name = 'wizard.schede.contabili'

    type = fields.Selection([('conto', 'Per Conto'), ('partner', 'Per Partner')], default="conto")
    all_accounts = fields.Boolean(default=True)
    account_ids = fields.Many2many('account.account')
    all_partners = fields.Boolean(default=True)
    partner_ids = fields.Many2many('res.partner')
    only_suppliers = fields.Boolean()
    only_customers = fields.Boolean()
    from_date = fields.Date('From date', required=True)
    to_date = fields.Date('To date', required=True)
    journal_ids = fields.Many2many('account.journal', default=lambda self: self.env['account.journal'].search([]))

    @api.multi
    def print_scheda_contabile(self):
        """
        Funzione chiamata dal wizard delle schede contabili.
        Genera un report PDF contenente tutte le registrazioni (account.move.line)
        In base alle configurazioni inserite
        :return: 'ir.actions.report.xml' (Report Scheda Contabile)
        """
        self.ensure_one()

        domain = [('move_id.date', '>=', self.from_date), ('move_id.date', '<=', self.to_date)]
        domain_previous = [('move_id.date', '<', self.from_date)]

        partner_ids = []
        account_ids = []
        if not self.all_accounts:
            account_ids = [x.id for x in self.account_ids]
            domain.append(('account_id', 'in', account_ids))
            domain_previous.append(('account_id', 'in', account_ids))
        if not self.all_partners:
            partner_ids = [x.id for x in self.partner_ids]
            domain.append(('partner_id', 'in', partner_ids))
            domain_previous.append('|', ('move_id.partner_id', 'in', partner_ids), ('partner_id', 'in', partner_ids))
        if self.only_customers:
            domain.append(('partner_id.customer', '=', True))
            domain_previous.append(('partner_id.customer', '=', True))
        if self.only_suppliers:
            domain.append(('partner_id.supplier', '=', True))
            domain_previous.append(('partner_id.supplier', '=', True))

        # Calcolo Del Saldo Precedente
        move_line_ids_before_start_date = self.env['account.move.line'].search(domain_previous, order='account_id desc')
        saldo_precedente = {}

        for l in move_line_ids_before_start_date:
            key = False
            if self.type == 'conto':
                # Per codice: 2000 - Iva n/Credito
                key = l.account_id.code + ' - ' + l.account_id.name
            if self.type == 'partner':
                # Per Partner: addoons srl
                key = l.partner_id.name

            balance_prec = l.debit - l.credit
            if key not in saldo_precedente:
                # La chiave non esiste, la creo e aggiungo i primi valori
                saldo_precedente[key] = {'saldo_dare_prec': l.debit,
                                         'saldo_avere_prec': l.credit,
                                         'saldo_prec': balance_prec}
            else:
                # La chiave esiste gia, non la creo e sommo i valori
                saldo_precedente[key]['saldo_dare_prec'] += l.debit
                saldo_precedente[key]['saldo_avere_prec'] += l.credit
                saldo_precedente[key]['saldo_prec'] += balance_prec

        # Prendo tutte le movimentazioni contabili in base ai criteri di ricerca inseriti
        move_line_ids = self.env['account.move.line'].search(domain, order='date asc, move_id desc')

        lines_account = {}

        for l in move_line_ids:
            # Ciclo tutte le movimentazioni trovate

            # Genero la chiave della struttura dati
            key = False
            if self.type == 'conto':
                # Per codice: 2000 - Iva n/Credito
                key = l.account_id.code + ' - ' + l.account_id.name
            if self.type == 'partner':
                # Per Partner: addoons srl
                key = l.partner_id.name

            if key not in lines_account:
                # Se la chiave non esiste la creo
                lines_account[key] = []

            lines_account[key].append({
                'date': l.date,
                'move_id': l.move_id.name,
                'account_id': l.account_id.code + ' - ' + l.account_id.name,
                'journal_id': l.journal_id.name,
                'debit': l.debit,
                'credit': l.credit,
                'partner': l.partner_id.name,
                'ref': l.ref,
                'name': l.name,
            })

        # CALCOLO DEL SALDO (BALANCE)
        for key, value in lines_account.items():
            # Inizio a decurtare/incrementare il saldo partendo dal saldo precedente
            if key in saldo_precedente:
                balance = saldo_precedente[key]['saldo_prec']
            else:
                balance = 0
            for elem in value:
                balance += elem['debit'] - elem['credit']
                elem['balance'] = balance

        journals = [x.name for x in self.journal_ids]
        datas_form = {
            'type': self.type,
            'all_accounts': self.all_accounts,
            'account_ids': account_ids,
            'partner_ids': partner_ids,
            'all_partners': self.all_partners,
            'only_suppliers': self.only_suppliers,
            'only_customers': self.only_customers,
            'from_date': self.from_date,
            'to_date': self.to_date,
            'lines_account': lines_account,
            'journal_ids': journals,
            'saldo_precedente': saldo_precedente,
        }

        datas = {
            'ids': [x.id for x in move_line_ids],
            'model': 'account.move.line',
            'form': datas_form,
        }
        return self.env.ref('l10n_it_account.report_schede_contabili').report_action(self, data=datas)


class ReportSchedaContabile(models.AbstractModel):
    """
    Ereditare il report per modificare la funzione render_html
    e aggiungere i parametri passati dal wizard
    """
    _name = 'report.l10n_it_account.report_scheda_contabile'

    @api.model
    def _get_report_values(self, docids, data=None):

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'data': data['form'],  # Parametri passati
            'docs': self.env['account.move.line'].browse(data['ids']),
            'env': self.env,
            'type': data['form']['type'],
            'all_accounts': data['form']['all_accounts'],
            'account_ids': data['form']['account_ids'],
            'partner_ids': data['form']['partner_ids'],
            'all_partners': data['form']['all_partners'],
            'only_suppliers': data['form']['only_suppliers'],
            'only_customers': data['form']['only_customers'],
            'from_date': data['form']['from_date'],
            'to_date': data['form']['to_date'],
            'lines_account': data['form']['lines_account'],
            'journal_ids': data['form']['journal_ids'],
            'saldo_precedente': data['form']['saldo_precedente'],
        }
