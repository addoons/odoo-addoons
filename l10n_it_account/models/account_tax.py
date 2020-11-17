# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)

from odoo import models, fields,_


class AccountTax(models.Model):
    _inherit = 'account.tax'

    cee_type = fields.Selection([('sale', 'Sale'),('purchase', 'Purchase')], string='Include in VAT register', help="Use in the case of tax with 'VAT integration'. This "
                                                                                                                    "specifies the VAT register (sales / purchases) where the "
                                                                                                                    "tax must be computed.")
    parent_tax_ids = fields.Many2many( 'account.tax', 'account_tax_filiation_rel', 'child_tax', 'parent_tax', string='Parent Taxes')
    kind_id = fields.Many2one('account.tax.kind', string="Exemption Kind")
    law_reference = fields.Char('Law reference')
    payability = fields.Selection([
        ('I', 'Immediate payability'),
        ('D', 'Deferred payability'),
        ('S', 'Split payment'),
    ], string="VAT payability")
    vat_statement_account_id = fields.Many2one('account.account', "Account used for VAT statement", help="The tax balance will be associated to this account after "
                                                                                                         "selecting the period in VAT statement")
    vsc_exclude_operation = fields.Boolean(string='Exclude from active / passive operations')
    vsc_exclude_vat = fields.Boolean(string='Exclude from VAT payable / deducted')

    def _get_tax_amount(self):
        self.ensure_one()
        res = 0.0
        if self.amount_type == 'group':
            for child in self.children_tax_ids:
                res += child.amount
        else:
            res = self.amount
        return res

    def _get_tax_name(self):
        self.ensure_one()
        name = self.name
        if self.parent_tax_ids and len(self.parent_tax_ids) == 1:
            name = self.parent_tax_ids[0].name
        return name

    def _compute_totals_tax(self, data):
        """
        Args:
            data: date range, journals and registry_type
        Returns:
            A tuple: (tax_name, base, tax, deductible, undeductible)

        """
        self.ensure_one()
        context = {
            'from_date': data['from_date'],
            'to_date': data['to_date'],
        }
        registry_type = data.get('registry_type', 'customer')
        if data.get('journal_ids'):
            context['vat_registry_journal_ids'] = data['journal_ids']

        tax = self.env['account.tax'].with_context(context).browse(self.id)
        tax_name = tax._get_tax_name()


        #TOTALI
        amount_untaxed = 0 #Imponibile
        amount_tax = 0 #Imposte
        amount_tax_exig = 0 #Esigibili


        if 'cash_move_ids' in data:
            for move in data['move_ids']:
                move_id = self.env['account.move'].browse(int(move))
                # 1° Calcolo quali sarebbero le imposte e l'imponibile
                for line in move_id.line_ids:
                    if line.tax_line_id.id == tax.id:
                        amount_untaxed += line.tax_base_amount
                        amount_tax += line.credit

            for move, cash_move_ids in data['cash_move_ids'].items():
                # 2° Calcolo in reale imponibile ed imposte Esigibili, guardando i giroconti del Principio di Cassa
                for cash_move in cash_move_ids:
                    cash_move_id = self.env['account.move'].browse(int(cash_move))
                    for line in cash_move_id.line_ids:
                        if line.tax_line_id.id == tax.id:
                            amount_tax_exig += line.credit_cash_basis
        else:
            amount_untaxed = tax.base_balance
            amount_tax = tax.balance
            amount_tax_exig = amount_tax

        #Non Esigibili
        amount_tax_no_exig = amount_tax - amount_tax_exig

        if not tax.children_tax_ids:
            if registry_type == 'supplier':
                amount_untaxed = -amount_untaxed
                amount_tax_exig = -amount_tax_exig
                amount_tax_no_exig = -amount_tax_no_exig
                amount_tax = -amount_tax
            return (
                tax_name, abs(amount_untaxed), amount_tax, amount_tax_exig, amount_tax_no_exig
            )
        else:
            base_balance = tax.base_balance
            tax_balance = 0
            deductible = 0
            undeductible = 0
            for child in tax.children_tax_ids:
                child_balance = child.balance
                if (
                    (
                        data['registry_type'] == 'customer' and
                        child.cee_type == 'sale'
                    ) or
                    (
                        data['registry_type'] == 'supplier' and
                        child.cee_type == 'purchase'
                    )
                ):
                    # Prendo la parte di competenza di ogni registro e lo
                    # sommo sempre
                    child_balance = child_balance

                elif child.cee_type:
                    continue

                tax_balance += child_balance
                if child.account_id:
                    deductible += child_balance
                else:
                    undeductible += child_balance
            if registry_type == 'supplier':
                base_balance = -base_balance
                tax_balance = -tax_balance
                deductible = -deductible
                undeductible = -undeductible
            return (
                tax_name, base_balance, tax_balance, deductible, undeductible
            )
