# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)

from odoo import models, fields, api
from odoo.addons import decimal_precision as dp


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.onchange('partner_id', 'journal_id', 'type', 'fiscal_position_id')
    def _set_document_fiscal_type(self):
        dt = self._get_document_fiscal_type(
            self.type, self.partner_id, self.fiscal_position_id,
            self.journal_id)
        if dt:
            self.fiscal_document_type_id = dt[0]

    def _get_document_fiscal_type(self, type=None, partner=None,
                                  fiscal_position=None, journal=None):
        dt = []
        doc_id = False
        if not type:
            type = 'out_invoice'

        # Partner
        if partner:
            if type in ('out_invoice', 'out_refund'):
                doc_id = partner.out_fiscal_document_type.id or False
            elif type in ('in_invoice', 'in_refund'):
                doc_id = partner.in_fiscal_document_type.id or False
        # Fiscal Position
        if not doc_id and fiscal_position:
            doc_id = fiscal_position.fiscal_document_type_id.id or False
        # Journal
        if not doc_id and journal:
            dt = self.env['fiscal.document.type'].search([
                ('journal_ids', 'in', [journal.id])]).ids
        if not doc_id and not dt:
            dt = self.env['fiscal.document.type'].search([
                (type, '=', True)]).ids
        if doc_id:
            dt.append(doc_id)
        return dt

    fiscal_document_type_id = fields.Many2one(
        'fiscal.document.type',
        string="Fiscal Document Type",
        readonly=False)

    @api.multi
    @api.depends(
        'invoice_line_ids.price_subtotal', 'withholding_tax_line_ids.tax',
        'currency_id', 'company_id', 'date_invoice', 'payment_move_line_ids')
    def _amount_withholding_tax(self):
        dp_obj = self.env['decimal.precision']
        for invoice in self:
            withholding_tax_amount = 0.0
            for wt_line in invoice.withholding_tax_line_ids:
                withholding_tax_amount += round(
                    wt_line.tax, dp_obj.precision_get('Account'))
            invoice.amount_net_pay = invoice.amount_total - \
                                     withholding_tax_amount
            amount_net_pay_residual = invoice.amount_net_pay
            invoice.withholding_tax_amount = withholding_tax_amount
            for line in invoice.payment_move_line_ids:
                if not line.withholding_tax_generated_by_move_id:
                    amount_net_pay_residual -= (line.debit or line.credit)
            invoice.amount_net_pay_residual = amount_net_pay_residual

    withholding_tax = fields.Boolean('Withholding Tax')
    withholding_tax_line_ids = fields.One2many(
        'account.invoice.withholding.tax', 'invoice_id',
        'Withholding Tax Lines', copy=True,
        readonly=True, states={'draft': [('readonly', False)]})
    withholding_tax_amount = fields.Float(
        compute='_amount_withholding_tax',
        digits=dp.get_precision('Account'), string='Withholding tax Amount',
        store=True, readonly=True)
    amount_net_pay = fields.Float(
        compute='_amount_withholding_tax',
        digits=dp.get_precision('Account'), string='Net To Pay',
        store=True, readonly=True)
    amount_net_pay_residual = fields.Float(
        compute='_amount_withholding_tax',
        digits=dp.get_precision('Account'), string='Residual Net To Pay',
        store=True, readonly=True)

    @api.model
    def _default_partner_id(self):
        if not self._context.get('default_corrispettivi', False):
            # If this is not a receipts (corrispettivi), do nothing
            return False
        return self.env.ref('base.public_user').partner_id.id

    @api.model
    def _default_journal(self):
        if not self._context.get('default_corrispettivi', False):
            # If this is not a receipts (corrispettivi), do nothing
            return super(AccountInvoice, self)._default_journal()
        company_id = self._context.get(
            'company_id', self.env.user.company_id)
        return self.env['account.journal'] \
            .get_corr_journal(company_id)

    # set default option on inherited field
    corrispettivo = fields.Boolean(
        string='Receipt', related="journal_id.corrispettivi",
        readonly=True, store=True)
    partner_id = fields.Many2one(default=_default_partner_id)
    journal_id = fields.Many2one(default=_default_journal)

    @api.onchange('company_id')
    def onchange_company_id_corrispettivi(self):
        if not self._context.get('default_corrispettivi', False):
            # If this is not a receipts (corrispettivi), do nothing
            return

        self.set_corr_journal()

    @api.onchange('partner_id')
    def onchange_partner_id_corrispettivi(self):
        if not self.partner_id or not self.partner_id.use_corrispettivi:
            # If partner is not set or its use_corrispettivi flag is disabled,
            # do nothing
            return

        self.set_corr_journal()

    @api.multi
    def set_corr_journal(self):
        for invoice in self:
            invoice.journal_id = self.env['account.journal'] \
                .get_corr_journal(invoice.company_id)

    @api.multi
    def corrispettivo_print(self):
        """ Print the receipt and mark it as sent"""
        self.ensure_one()
        self.sent = True
        return self.env.ref('l10n_it_account.account_corrispettivi') \
            .report_action(self)

    @api.model
    def create(self, vals):
        invoice = super(AccountInvoice,self.with_context(mail_create_nolog=True)).create(vals)
        if any(line.invoice_line_tax_wt_ids for line in
               invoice.invoice_line_ids) \
                and not invoice.withholding_tax_line_ids:
            invoice.compute_taxes()
        if not invoice.fiscal_document_type_id:
            dt = self._get_document_fiscal_type(
                invoice.type, invoice.partner_id, invoice.fiscal_position_id,
                invoice.journal_id)
            if dt:
                invoice.fiscal_document_type_id = dt[0]

        return invoice


    @api.onchange('invoice_line_ids')
    def _onchange_invoice_line_wt_ids(self):
        self.ensure_one()
        wt_taxes_grouped = self.get_wt_taxes_values()
        wt_tax_lines = []
        for tax in wt_taxes_grouped.values():
            wt_tax_lines.append((0, 0, tax))
        self.withholding_tax_line_ids = wt_tax_lines
        if wt_tax_lines:
            self.withholding_tax = True
        else:
            self.withholding_tax = False

    @api.multi
    def action_move_create(self):
        '''
        Split amount withholding tax on account move lines
        '''
        dp_obj = self.env['decimal.precision']
        res = super(AccountInvoice, self).action_move_create()

        for inv in self:
            # Rates
            rate_num = 0
            for move_line in inv.move_id.line_ids:
                if move_line.account_id.internal_type not in ['receivable',
                                                              'payable']:
                    continue
                rate_num += 1
            if rate_num:
                wt_rate = round(inv.withholding_tax_amount / rate_num,
                                dp_obj.precision_get('Account'))
            wt_residual = inv.withholding_tax_amount
            # Re-read move lines to assign the amounts of wt
            i = 0
            for move_line in inv.move_id.line_ids:
                if move_line.account_id.internal_type not in ['receivable',
                                                              'payable']:
                    continue
                i += 1
                if i == rate_num:
                    wt_amount = wt_residual
                else:
                    wt_amount = wt_rate
                wt_residual -= wt_amount
                # update line
                move_line.write({'withholding_tax_amount': wt_amount})
            # Create WT Statement
            self.create_wt_statement()
        return res

    @api.multi
    def get_wt_taxes_values(self):
        tax_grouped = {}
        for invoice in self:
            for line in invoice.invoice_line_ids:
                taxes = []
                for wt_tax in line.invoice_line_tax_wt_ids:
                    res = wt_tax.compute_tax(line.price_subtotal)
                    tax = {
                        'id': wt_tax.id,
                        'sequence': wt_tax.sequence,
                        'base': res['base'],
                        'tax': res['tax'],
                    }
                    taxes.append(tax)

                for tax in taxes:
                    val = {
                        'invoice_id': invoice.id,
                        'withholding_tax_id': tax['id'],
                        'tax': tax['tax'],
                        'base': tax['base'],
                        'sequence': tax['sequence'],
                    }

                    key = self.env['withholding.tax'].browse(
                        tax['id']).get_grouping_key(val)

                    if key not in tax_grouped:
                        tax_grouped[key] = val
                    else:
                        tax_grouped[key]['tax'] += val['tax']
                        tax_grouped[key]['base'] += val['base']
        return tax_grouped

    @api.one
    def create_wt_statement(self):
        """
        Create one statement for each withholding tax
        """
        wt_statement_obj = self.env['withholding.tax.statement']
        for inv_wt in self.withholding_tax_line_ids:
            wt_base_amount = inv_wt.base
            wt_tax_amount = inv_wt.tax
            if self.type in ['in_refund', 'out_refund']:
                wt_base_amount = -1 * wt_base_amount
                wt_tax_amount = -1 * wt_tax_amount
            val = {
                'date': self.move_id.date,
                'move_id': self.move_id.id,
                'invoice_id': self.id,
                'partner_id': self.partner_id.id,
                'withholding_tax_id': inv_wt.withholding_tax_id.id,
                'base': wt_base_amount,
                'tax': wt_tax_amount,
            }
            wt_statement_obj.create(val)

    @api.model
    def _get_payments_vals(self):
        payment_vals = super(AccountInvoice, self)._get_payments_vals()
        if self.payment_move_line_ids:
            for payment_val in payment_vals:
                move_line = self.env['account.move.line'].browse(
                    payment_val['payment_id'])
                if move_line.withholding_tax_generated_by_move_id:
                    payment_val['wt_move_line'] = True
                else:
                    payment_val['wt_move_line'] = False
        return payment_vals



class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    @api.model
    def _default_withholding_tax(self):
        result = []
        fiscal_position_id = self._context.get('fiscal_position_id', False)
        if fiscal_position_id:
            fp = self.env['account.fiscal.position'].browse(fiscal_position_id)
            wt_ids = fp.withholding_tax_ids.mapped('id')
            result.append((6, 0, wt_ids))
        return result

    invoice_line_tax_wt_ids = fields.Many2many(
        comodel_name='withholding.tax', relation='account_invoice_line_tax_wt',
        column1='invoice_line_id', column2='withholding_tax_id', string='W.T.',
        default=_default_withholding_tax,
    )