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

    def get_all_accounts(self):
        accounts = self.search([])
        return sorted(accounts, key=lambda x: x.parent_id.id)

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


