# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)
from odoo import api, fields, models,_
from odoo.exceptions import ValidationError


class AccountAccountInherit(models.Model):
    _inherit = 'account.account'

    hierarchy_type_id = fields.Many2one('account.account.type')
    macroaggregate_id = fields.Many2one('account.account', string="Macroaggregato")
    parent_id = fields.Many2one('account.account', string='Aggregato')
    code = fields.Char(size=64, required=False, index=True)
    child_ids = fields.One2many('account.account', 'parent_id')
    area = fields.Selection([('conto_economico', 'Conto Economico'), ('stato_patrimoniale', 'Stato Patrimoniale'),
                             ('conti_ordine', "Conti D'ordine")], default='conto_economico')
    account_move_lines = fields.One2many('account.move.line', 'account_id', string='Move Lines', copy=False)
    credit = fields.Monetary(string='Credit', readonly=True, compute='_find_account_balance', store=True)
    debit = fields.Monetary(string='Debit', readonly=True, compute='_find_account_balance', store=True)
    balance = fields.Monetary(string='Balance', readonly=True, compute='_find_account_balance', store=True)

    sottoconto_terzo_livello = fields.Many2one('account.account', string='Sottoconto Terzo Livello')
    sottoconto_quarto_livello = fields.Many2one('account.account', string='Sottoconto Quarto Livello')
    sottoconto_quinto_livello = fields.Many2one('account.account', string='Sottoconto Quinto Livello')
    sottoconto_sesto_livello = fields.Many2one('account.account', string='Sottoconto Sesto Livello')

    _sql_constraints = [
        ('code_company_uniq', 'unique (code,company_id,create_date)', 'The code of the account must be unique per company !')
    ]

    def get_terzo_liv_balance(self):
        accounts = self.env['account.account'].search([('sottoconto_terzo_livello.id', '=', self.id)])
        balance_aggregate = 0
        for account in accounts:
            balance_aggregate += account.balance
        self.balance = balance_aggregate
        return balance_aggregate

    def get_quarto_liv_balance(self):
        accounts = self.env['account.account'].search([('sottoconto_quarto_livello.id', '=', self.id)])
        balance_aggregate = 0
        for account in accounts:
            balance_aggregate += account.balance
        self.balance = balance_aggregate
        return balance_aggregate

    @api.depends('account_move_lines')
    def _find_account_balance(self):
        """
        Funzione che calcola il totale crediti, debiti e saldo di ogni conto
        """
        return
        # for account in self:
        #     total_debit = 0.0
        #     total_credit = 0.0
        #     for value in account.account_move_lines:
        #         total_debit = total_debit + value.debit
        #         total_credit = total_credit + value.credit
        #     balance = total_debit - total_credit
        #
        #     account.debit = total_debit
        #     account.credit = total_credit
        #     account.balance = balance


    @api.multi
    @api.constrains('code')
    def _check_code(self):
        """
        Funzione che controlla che il campo codice possa essere nullo solamente se il conto è un Macroaggregato,
        ovvero non possiede nessun padre (parent_id)
        """
        for account in self:
            if account.parent_id and not account.code:
                raise ValidationError(('Il campo codice è obbligatorio per i conti e aggregati. (Nome Conto: %s)') % account.name)

    @api.multi
    def name_get(self):
        """
        name_get, se il conto possiede il codice lo concatena con il nome
        altrimenti mostra solo il nome
        """
        result = []
        for account in self:
            if account.code:
                name = account.code + ' ' + account.name
            else:
                name = account.name
            result.append((account.id, name))
        return result


    # @api.model
    # def name_search(self, name='', args=None, operator='ilike', limit=100):
    #     """
    #     Nascondere tutti i conti che sono Macroaggregati e Aggregati,
    #     Quindi conti non utilizzabili per operazioni contabili
    #     """
    #     if not args:
    #         args = []
    #     records = self.search(['&', ('hierarchy_type_id', '=', False), '|', ('name', operator, name), ('code', operator, name)] + args, limit=limit)
    #     return records.name_get()


    @api.onchange('parent_id', 'macroaggregate_id')
    def onchange_aggregate(self):
        """
        Al cambio dell'aggregato viene impostato di default anche il macroaggregato
        Anche l'area (Conto Economico, Stato Patrimoniale) viene impostata in automatico
        """
        if not self.macroaggregate_id and self.parent_id:
            self.macroaggregate_id = self.parent_id.macroaggregate_id.id

        if self.macroaggregate_id:
            if self.parent_id and self.parent_id.macroaggregate_id.id != self.macroaggregate_id.id:
                self.parent_id = False
            return {
                'domain': {
                    'parent_id': ['&', '&', ('area', '=', self.area),
                                  ('macroaggregate_id', '=', self.macroaggregate_id.id),
                                  ('hierarchy_type_id', '=', self.env.ref('l10n_it_account.account_type_aggregate').id)]
                }
            }


    # controllo sul prefisso per suddividere le righe in gruppi ordinati sulle prime tre cifre
    def check_prefix(self, prev, prefix):
        result = fields.Boolean()
        if prefix == prev:
            result = False
        elif prefix != prev:
            result = True
        return result

    # prende il prefisso di 3 caratteri
    def print_prefix(self, code):
        return code[:3]

    def _get_not_assigned_account(self, hierarchy_level, current_account, accounts_list):
        """
        Restituisce i conti normali dopo il terzo livello
        """
        domain = [('hierarchy_type_id', '=', False)]
        if hierarchy_level == 'aggregate':
            domain.append(('parent_id.id', '=', current_account.id))
            domain.append(('sottoconto_terzo_livello', '=', False))
        if hierarchy_level == 'third_level':
            domain.append(('sottoconto_terzo_livello.id', '=', current_account.id))
            domain.append(('sottoconto_quarto_livello', '=', False))
        if hierarchy_level == 'fourth_level':
            domain.append(('sottoconto_quarto_livello.id', '=', current_account.id))
            domain.append(('sottoconto_quinto_livello', '=', False))
        if hierarchy_level == 'fifth_level':
            domain.append(('sottoconto_quinto_livello.id', '=', current_account.id))
            domain.append(('sottoconto_sesto_livello', '=', False))
        if hierarchy_level == 'sixth_level':
            domain.append(('sottoconto_sesto_livello.id', '=', current_account.id))
        not_assigned_account_list = self.env['account.account'].search(domain)
        for not_assigned_account in not_assigned_account_list:
            accounts_list.append(not_assigned_account)

    def get_all_accounts(self):
        macro = self.env.ref('l10n_it_account.account_type_macroaggregate').id
        aggregate = self.env.ref('l10n_it_account.account_type_aggregate').id
        third_level = self.env.ref('l10n_it_account.account_type_sottoconto_3').id
        fourth_level = self.env.ref('l10n_it_account.account_type_sottoconto_4').id
        fifth_level = self.env.ref('l10n_it_account.account_type_sottoconto_5').id
        sixthlevel = self.env.ref('l10n_it_account.account_type_sottoconto_6').id
        accounts_macro = self.search([('hierarchy_type_id.id', '=', macro)], order='code asc')
        accounts_aggregate = self.search([('hierarchy_type_id.id', '=', aggregate)], order='code asc')
        accounts_third_level = self.search([('hierarchy_type_id.id', '=', third_level)], order='code asc')
        accounts_fourth_level = self.search([('hierarchy_type_id.id', '=', fourth_level)], order='code asc')
        accounts_fifth_level = self.search([('hierarchy_type_id.id', '=', fifth_level)], order='code asc')
        accounts_sixthlevel = self.search([('hierarchy_type_id.id', '=', sixthlevel)])
        accounts_list = []

        # aggiunge il macro alla lista
        for macro_account in accounts_macro:
            accounts_list.append(macro_account)
            # per ogni aggregato: se è figlio del macro -> aggiunto
            for aggregate_account in accounts_aggregate:
                if aggregate_account.macroaggregate_id.id == macro_account.id:
                    accounts_list.append(aggregate_account)
                    # terzo liv: se ha come parent l'aggregato -> aggiunto.
                    # Aggiunti i conti senza gerarchia
                    self._get_not_assigned_account('aggregate', aggregate_account, accounts_list)
                    for third_level_account in accounts_third_level:
                        if third_level_account.parent_id.id == aggregate_account.id:
                            accounts_list.append(third_level_account)
                            # quarto liv: se ha come parent il conto di terzo livello -> aggiunto.
                            # Aggiunti i conti senza gerarchia
                            self._get_not_assigned_account('third_level', third_level_account, accounts_list)
                            for fourth_level_account in accounts_fourth_level:
                                if fourth_level_account.sottoconto_terzo_livello.id == third_level_account.id:
                                    accounts_list.append(fourth_level_account)
                                    # quinto liv: se ha come parent il conto di quarto livello -> aggiunto.
                                    # Aggiunti i conti senza gerarchia
                                    self._get_not_assigned_account('fourth_level', fourth_level_account, accounts_list)
                                    for fifth_level_account in accounts_fifth_level:
                                        if fifth_level_account.sottoconto_quarto_livello.id == fourth_level_account.id:
                                            accounts_list.append(fifth_level_account)
                                            # quinto liv: se ha come parent il conto di quarto livello -> aggiunto.
                                            # Aggiunti i conti senza gerarchia
                                            self._get_not_assigned_account('fifth_level', fifth_level_account,
                                                                           accounts_list)
                                            for sixth_level_account in accounts_sixthlevel:
                                                if sixth_level_account.sottoconto_quinto_livello.id == fifth_level_account.id:
                                                    accounts_list.append(sixth_level_account)
                                                    # sesto liv: se ha come parent il conto di quinto livello -> aggiunto.
                                                    # Aggiunti i conti senza gerarchia
                                                    self._get_not_assigned_account('sixth_level', sixth_level_account,
                                                                                   accounts_list)
        return accounts_list

    def get_aggregate_balance(self):
        accounts = self.env['account.account'].search([('parent_id.id', '=', self.id)])
        balance_aggregate = 0
        for account in accounts:
            balance_aggregate += account.balance
        self.balance = balance_aggregate
        return balance_aggregate

    def get_macro_balance(self):
        accounts = self.env['account.account'].search([('macroaggregate_id.id', '=', self.id),
                                                       ('hierarchy_type_id.name', '=', 'Aggregato')])
        balance_macro = 0
        for account in accounts:
            balance_macro += account.balance
        self.balance = balance_macro
        return balance_macro

    def get_not_defined_balance(self):
        accounts = self.env['account.account'].search([('macroaggregate_id', '=', False),
                                                       ('parent_id', '=', False),
                                                       ('hierarchy_type_id', '=', False)])
        balance_undefined = 0
        for account in accounts:
            balance_undefined += account.balance
        return balance_undefined


