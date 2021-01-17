# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)
import datetime

from odoo import models, fields, api, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import ValidationError, UserError
from odoo.tools import float_is_zero, relativedelta


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    # campi per assegnamento massivo righe fattura
    am_account_id = fields.Many2one('account.account')
    row_description = fields.Char()
    am_analytic_account = fields.Many2one('account.analytic.account')
    am_tax_id = fields.Many2one('account.tax')
    am_rda = fields.Many2one('withholding.tax')
    am_rc = fields.Boolean()
    data_ricezione = fields.Date(default=datetime.date.today())
    select_all_rows = fields.Boolean()
    date_due = fields.Date(string='Due Date',
                           readonly=False, index=True, copy=False,
                           help="If you use payment terms, the due date will be computed automatically at the generation "
                                "of accounting entries. The Payment terms may compute several due dates, for example 50% "
                                "now and 50% in one month, but if you want to force a due date, make sure that the payment "
                                "term is not set on the invoice. If you keep the Payment terms and the due date empty, it "
                                "means direct payment.")
    giroconto_bolletta_doganale_id = fields.Many2one('account.move')
    is_dogana = fields.Boolean(related='partner_id.is_dogana')
    purchase_order_id = fields.Many2one('purchase.order')
    differenza_ordini = fields.Float(compute="compute_differenza_ordini", store=True)
    invoice_year = fields.Integer(compute='get_year', store=True)


    #Fix: Odoo non permette in anni differenti di avere la stessa sequenza di fattura
    _sql_constraints = [
        ('number_uniq', 'unique(number, company_id, journal_id, type, invoice_year)', 'Invoice Number must be unique per Company!'),
    ]





    @api.depends('date_invoice')
    def get_year(self):
        for x in self:
            if x.date_invoice:
                date = datetime.datetime.strptime(str(x.date_invoice), '%Y-%m-%d')
                x.invoice_year = date.year

    def compute_differenza_ordini(self):
        i = 0
        for invoice in self:
            if invoice.type == 'in_invoice':
                i += 1
                diff_ordini = 0
                list_ordini = []
                for line in invoice.invoice_line_ids:
                    if line.purchase_order_id and line.purchase_order_id.id not in list_ordini:
                        list_ordini.append(line.purchase_order_id.id)
                        diff_ordini -= line.purchase_order_id.amount_total
                    if line.purchase_order_id:
                        diff_ordini += line.price_total

                if len(list_ordini) > 0:
                    invoice.differenza_ordini = diff_ordini
                else:
                    invoice.differenza_ordini = 0
                print(i)
            else:
                invoice.differenza_ordini = 0

    @api.one
    @api.depends('invoice_line_ids.price_subtotal', 'tax_line_ids.amount', 'tax_line_ids.amount_rounding',
                 'currency_id', 'company_id', 'date_invoice', 'type', 'date', 'invoice_line_ids.purchase_order_id')
    def _compute_amount(self):
        super(AccountInvoice, self)._compute_amount()
        self.compute_differenza_ordini()

    def set_fiscal_positon(self):

        #Metto sulle fatture la posizione fiscale del Partner ID
        inv_ids = self.sudo().search([('fiscal_position_id', '=', False)])
        for inv in inv_ids:
            inv.fiscal_position_id = inv.partner_id.property_account_position_id.id



    @api.onchange('select_all_rows')
    def onchange_select_all_rows(self):
        for line in self.invoice_line_ids:
            line.selected = self.select_all_rows

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        if self.journal_id.type == 'sale':
            self.am_account_id = self.partner_id.ricavi_account.id
        else:
            self.am_account_id = self.partner_id.costi_account.id


    @api.one
    @api.depends(
        'state', 'currency_id', 'invoice_line_ids.price_subtotal',
        'move_id.line_ids.amount_residual',
        'move_id.line_ids.currency_id')
    def _compute_residual(self):
        residual = 0.0
        residual_company_signed = 0.0
        sign = self.type in ['in_refund', 'out_refund'] and -1 or 1
        for line in self._get_aml_for_amount_residual():
            residual_company_signed += line.amount_residual
            if line.currency_id == self.currency_id:
                residual += line.amount_residual_currency if line.currency_id else line.amount_residual
            else:
                if line.currency_id:
                    residual += line.currency_id._convert(line.amount_residual_currency, self.currency_id,
                                                          line.company_id, line.date or fields.Date.today())
                else:
                    residual += line.company_id.currency_id._convert(line.amount_residual, self.currency_id,
                                                                     line.company_id, line.date or fields.Date.today())
        self.residual_company_signed = abs(residual_company_signed) * sign
        self.residual_signed = abs(residual) * sign
        self.residual = abs(residual)
        digits_rounding_precision = self.currency_id.rounding
        if float_is_zero(self.residual, precision_rounding=digits_rounding_precision):
            self.reconciled = True
        else:
            self.reconciled = False


    @api.multi
    @api.depends(
        'invoice_line_ids.price_subtotal', 'withholding_tax_line_ids.tax',
        'currency_id', 'company_id', 'date_invoice', 'payment_move_line_ids')
    def _amount_withholding_tax(self):
        dp_obj = self.env['decimal.precision']
        for invoice in self:
            withholding_tax_amount = 0.0
            for wt_line in invoice.withholding_tax_line_ids:
                withholding_tax_amount += wt_line.tax
            invoice.amount_net_pay = invoice.amount_total - \
                                     withholding_tax_amount
            amount_net_pay_residual = invoice.amount_net_pay
            invoice.withholding_tax_amount = withholding_tax_amount
            for line in invoice.payment_move_line_ids:
                if not line.withholding_tax_generated_by_move_id:
                    amount_net_pay_residual -= (line.debit or line.credit)
            invoice.amount_net_pay_residual = amount_net_pay_residual

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
    comunicazione_dati_iva_escludi = fields.Boolean(
        string='Exclude from invoices communication')

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
        wt_tax_lines = [(5, 0, 0)]
        for tax in wt_taxes_grouped.values():
            wt_tax_lines.append((0, 0, tax))
        self.withholding_tax_line_ids = wt_tax_lines
        if len(wt_tax_lines) > 1:
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
                wt_rate = inv.withholding_tax_amount / rate_num
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
                'wt_type': '',
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

    def _compute_taxes_in_company_currency(self, vals):
        try:
            exchange_rate = (
                    self.amount_total_signed /
                    self.amount_total_company_signed)
        except ZeroDivisionError:
            exchange_rate = 1
        vals['ImponibileImporto'] = vals['ImponibileImporto'] / exchange_rate
        vals['Imposta'] = vals['Imposta'] / exchange_rate

    def _get_tax_comunicazione_dati_iva(self):
        self.ensure_one()
        fattura = self
        tax_model = self.env['account.tax']

        tax_lines = []
        tax_grouped = {}
        for tax_line in fattura.tax_line_ids:
            tax = tax_line.tax_id
            aliquota = tax.amount
            parent = tax_model.search([('children_tax_ids', 'in', [tax.id])])
            if parent:
                main_tax = parent
                aliquota = parent.amount
                if (
                        tax.cee_type and
                        tax.amount < 0 and
                        main_tax.kind_id.code == 'N6'
                ):
                    continue
            else:
                main_tax = tax
            kind_id = main_tax.kind_id.id
            payability = main_tax.payability
            imposta = tax_line.amount
            base = tax_line.base
            if main_tax.id not in tax_grouped:
                tax_grouped[main_tax.id] = {
                    'ImponibileImporto': 0,
                    'Imposta': imposta,
                    'Aliquota': aliquota,
                    'Natura_id': kind_id,
                    'EsigibilitaIVA': payability,
                    'Detraibile': 0.0,
                }
                if fattura.type in ('in_invoice', 'in_refund'):
                    tax_grouped[main_tax.id]['Detraibile'] = 100.0
            else:
                tax_grouped[main_tax.id]['Imposta'] += imposta
            if tax.account_id:
                # account_id è valorizzato per la parte detraibile dell'imposta
                # In questa tax_line è presente il totale dell'imponibile
                # per l'imposta corrente
                tax_grouped[main_tax.id]['ImponibileImporto'] += base

        for tax_id in tax_grouped:
            tax = tax_model.browse(tax_id)
            vals = tax_grouped[tax_id]
            if tax.children_tax_ids:
                parte_detraibile = 0.0
                for child_tax in tax.children_tax_ids:
                    if child_tax.account_id:
                        parte_detraibile = child_tax.amount
                        break
                if vals['Aliquota'] and parte_detraibile:
                    vals['Detraibile'] = (
                            100 / (vals['Aliquota'] / parte_detraibile)
                    )
                else:
                    vals['Detraibile'] = 0.0
            vals = self._check_tax_comunicazione_dati_iva(tax, vals)
            fattura._compute_taxes_in_company_currency(vals)
            tax_lines.append((0, 0, vals))

        return tax_lines

    def _check_tax_comunicazione_dati_iva(self, tax, val=None):
        if not val:
            val = {}
        if val['Aliquota'] == 0 and not val['Natura_id']:
            raise ValidationError(
                _(
                    "Please specify exemption kind for tax: {} - Invoice {}"
                ).format(tax.name, self.number or False))
        if not val['EsigibilitaIVA']:
            raise ValidationError(
                _(
                    "Please specify VAT payability for tax: {} - Invoice {}"
                ).format(tax.name, self.number or False))
        return val

    rc_self_invoice_id = fields.Many2one(
        comodel_name='account.invoice',
        string='RC Self Invoice',
        copy=False, readonly=True)
    rc_purchase_invoice_id = fields.Many2one(
        comodel_name='account.invoice',
        string='RC Purchase Invoice', copy=False, readonly=True)
    rc_self_purchase_invoice_id = fields.Many2one(
        comodel_name='account.invoice',
        string='RC Self Purchase Invoice', copy=False, readonly=True)

    @api.onchange('fiscal_position_id')
    def onchange_rc_fiscal_position_id(self):
        for line in self.invoice_line_ids:
            line._set_rc_flag(self)

    @api.onchange('partner_id', 'company_id')
    def _onchange_partner_id(self):
        res = super(AccountInvoice, self)._onchange_partner_id()
        # In some cases (like creating the invoice from PO),
        # fiscal position's onchange is triggered
        # before than being changed by this method.
        self.onchange_rc_fiscal_position_id()
        return res

    def rc_inv_line_vals(self, line):
        return {
            'product_id': line.product_id.id,
            'name': line.name,
            'uom_id': line.product_id.uom_id.id,
            'price_unit': line.price_unit,
            'quantity': line.quantity,
            'discount': line.discount,
        }

    def rc_inv_vals(self, partner, account, rc_type, lines, currency):
        if self.type == 'in_invoice':
            type = 'out_invoice'
        else:
            type = 'out_refund'

        comment = _(
            "Reverse charge self invoice.\n"
            "Supplier: %s\n"
            "Reference: %s\n"
            "Date: %s\n"
            "Internal reference: %s") % (
                      self.partner_id.display_name, self.reference or '', self.date,
                      self.number
                  )
        return {
            'partner_id': partner.id,
            'type': type,
            'account_id': account.id,
            'journal_id': rc_type.journal_id.id,
            'invoice_line_ids': lines,
            'date_invoice': self.date,
            'date': self.date,
            'origin': self.number,
            'rc_purchase_invoice_id': self.id,
            'name': rc_type.self_invoice_text,
            'currency_id': currency.id,
            'fiscal_position_id': False,
            'payment_term_id': False,
            'comment': comment,
        }

    def get_inv_line_to_reconcile(self):
        for inv_line in self.move_id.line_ids:
            if (self.type == 'in_invoice') and inv_line.credit:
                return inv_line
            elif (self.type == 'in_refund') and inv_line.debit:
                return inv_line
        return False

    def get_rc_inv_line_to_reconcile(self, invoice):
        for inv_line in invoice.move_id.line_ids:
            if (invoice.type == 'out_invoice') and inv_line.debit:
                return inv_line
            elif (invoice.type == 'out_refund') and inv_line.credit:
                return inv_line
        return False

    def rc_payment_vals(self, rc_type):
        return {
            'journal_id': rc_type.payment_journal_id.id,
            # 'period_id': self.period_id.id,
            'date': self.date,
        }

    def compute_rc_amount_tax(self):
        rc_amount_tax = 0.0
        round_curr = self.currency_id.round
        rc_lines = self.invoice_line_ids.filtered(lambda l: l.rc)
        for rc_line in rc_lines:
            price_unit = \
                rc_line.price_unit * (1 - (rc_line.discount or 0.0) / 100.0)
            taxes = rc_line.invoice_line_tax_ids.compute_all(
                price_unit,
                self.currency_id,
                rc_line.quantity,
                product=rc_line.product_id,
                partner=rc_line.partner_id)['taxes']
            rc_amount_tax += sum([tax['amount'] for tax in taxes])

        # convert the amount to main company currency, as
        # compute_rc_amount_tax is used for debit/credit fields
        invoice_currency = self.currency_id.with_context(
            date=self.date_invoice)
        main_currency = self.company_currency_id.with_context(
            date=self.date_invoice)
        if invoice_currency != main_currency:
            round_curr = main_currency.round
            rc_amount_tax = invoice_currency.compute(
                rc_amount_tax, main_currency)

        return round_curr(rc_amount_tax)

    def rc_credit_line_vals(self, journal):
        credit = debit = 0.0
        amount_rc_tax = self.compute_rc_amount_tax()

        if self.type == 'in_invoice':
            credit = amount_rc_tax
        else:
            debit = amount_rc_tax

        return {
            'name': self.number,
            'credit': credit,
            'debit': debit,
            'account_id': journal.default_credit_account_id.id,
        }

    def rc_debit_line_vals(self, amount=None):
        credit = debit = 0.0

        if self.type == 'in_invoice':
            if amount:
                debit = amount
            else:
                debit = self.compute_rc_amount_tax()
        else:
            if amount:
                credit = amount
            else:
                credit = self.compute_rc_amount_tax()
        return {
            'name': self.number,
            'debit': debit,
            'credit': credit,
            'account_id': self.get_inv_line_to_reconcile().account_id.id,
            'partner_id': self.partner_id.id,
        }

    def rc_invoice_payment_vals(self, rc_type):
        return {
            'journal_id': rc_type.payment_journal_id.id,
            # 'period_id': self.period_id.id,
            'date': self.date,
        }

    def rc_payment_credit_line_vals(self, invoice):
        credit = debit = 0.0
        if invoice.type == 'out_invoice':
            credit = self.get_rc_inv_line_to_reconcile(invoice).debit
        else:
            debit = self.get_rc_inv_line_to_reconcile(invoice).credit
        return {
            'name': invoice.number,
            'credit': credit,
            'debit': debit,
            'account_id': self.get_rc_inv_line_to_reconcile(
                invoice).account_id.id,
            'partner_id': invoice.partner_id.id,
        }

    def rc_payment_debit_line_vals(self, invoice, journal):
        credit = debit = 0.0
        if invoice.type == 'out_invoice':
            debit = self.get_rc_inv_line_to_reconcile(invoice).debit
        else:
            credit = self.get_rc_inv_line_to_reconcile(invoice).credit
        return {
            'name': invoice.number,
            'debit': debit,
            'credit': credit,
            'account_id': journal.default_credit_account_id.id,
        }

    def reconcile_supplier_invoice(self):
        rc_type = self.fiscal_position_id.rc_type_id

        move_model = self.env['account.move']
        move_line_model = self.env['account.move.line']

        rc_payment_data = self.rc_payment_vals(rc_type)
        rc_invoice = self.rc_self_invoice_id
        payment_credit_line_data = self.rc_payment_credit_line_vals(
            rc_invoice)
        payment_debit_line_data = self.rc_debit_line_vals(
            payment_credit_line_data['credit'])
        rc_payment_data['line_ids'] = [
            (0, 0, payment_debit_line_data),
            (0, 0, payment_credit_line_data),
        ]
        rc_payment = move_model.create(rc_payment_data)
        for move_line in rc_payment.line_ids:
            if move_line.debit:
                payment_debit_line = move_line
            elif move_line.credit:
                payment_credit_line = move_line
        rc_payment.post()

        lines_to_rec = move_line_model.browse([
            self.get_inv_line_to_reconcile().id,
            payment_debit_line.id
        ])
        lines_to_rec.reconcile()

        rc_lines_to_rec = move_line_model.browse([
            self.get_rc_inv_line_to_reconcile(rc_invoice).id,
            payment_credit_line.id
        ])
        rc_lines_to_rec.reconcile()

    def partially_reconcile_supplier_invoice(self, rc_payment):
        move_line_model = self.env['account.move.line']
        for move_line in rc_payment.line_ids:
            # testa se nota credito o debito
            if (self.type == 'in_invoice') and move_line.debit:
                payment_debit_line = move_line
            elif (self.type == 'in_refund') and move_line.credit:
                payment_debit_line = move_line
        inv_lines_to_rec = move_line_model.browse(
            [self.get_inv_line_to_reconcile().id,
             payment_debit_line.id])
        inv_lines_to_rec.reconcile()

    def reconcile_rc_invoice(self):
        rc_type = self.fiscal_position_id.rc_type_id
        move_model = self.env['account.move']
        rc_payment_data = self.rc_payment_vals(rc_type)
        payment_credit_line_data = self.rc_credit_line_vals(
            rc_type.payment_journal_id)
        payment_debit_line_data = self.rc_debit_line_vals()
        rc_invoice = self.rc_self_invoice_id
        rc_payment_credit_line_data = self.rc_payment_credit_line_vals(
            rc_invoice)
        rc_payment_debit_line_data = self.rc_payment_debit_line_vals(
            rc_invoice, rc_type.payment_journal_id)
        rc_payment_data['line_ids'] = [
            (0, 0, payment_debit_line_data),
            (0, 0, payment_credit_line_data),
            (0, 0, rc_payment_debit_line_data),
            (0, 0, rc_payment_credit_line_data),
        ]
        rc_payment = move_model.create(rc_payment_data)

        move_line_model = self.env['account.move.line']
        rc_payment.post()
        inv_line_to_reconcile = self.get_rc_inv_line_to_reconcile(rc_invoice)
        for move_line in rc_payment.line_ids:
            if move_line.account_id.id == inv_line_to_reconcile.account_id.id:
                rc_payment_line_to_reconcile = move_line

        rc_lines_to_rec = move_line_model.browse(
            [inv_line_to_reconcile.id,
             rc_payment_line_to_reconcile.id])
        rc_lines_to_rec.reconcile()
        return rc_payment

    def generate_self_invoice(self):
        rc_type = self.fiscal_position_id.rc_type_id
        if not rc_type.payment_journal_id.default_credit_account_id:
            raise UserError(
                _('There is no default credit account defined \n'
                  'on journal "%s".') % rc_type.payment_journal_id.name)
        if rc_type.partner_type == 'other':
            rc_partner = rc_type.partner_id
        else:
            rc_partner = self.partner_id
        rc_currency = self.currency_id
        rc_account = rc_partner.property_account_receivable_id

        rc_invoice_lines = []
        for line in self.invoice_line_ids:
            if line.rc:
                rc_invoice_line = self.rc_inv_line_vals(line)
                line_tax_ids = line.invoice_line_tax_ids
                if not line_tax_ids:
                    raise UserError(_(
                        "Invoice line\n%s\nis RC but has not tax") % line.name)
                tax_ids = list()
                for tax_mapping in rc_type.tax_ids:
                    for line_tax_id in line_tax_ids:
                        if tax_mapping.purchase_tax_id == line_tax_id:
                            tax_ids.append(tax_mapping.sale_tax_id.id)
                if not tax_ids:
                    raise UserError(_("Tax code used is not a RC tax.\nCan't "
                                      "find tax mapping"))
                if line_tax_ids:
                    rc_invoice_line['invoice_line_tax_ids'] = [
                        (6, False, tax_ids)]
                rc_invoice_line[
                    'account_id'] = rc_type.transitory_account_id.id
                rc_invoice_lines.append([0, False, rc_invoice_line])
        if rc_invoice_lines:
            inv_vals = self.rc_inv_vals(
                rc_partner, rc_account, rc_type, rc_invoice_lines, rc_currency)

            # create or write the self invoice
            if self.rc_self_invoice_id:
                # this is needed when user takes back to draft supplier
                # invoice, edit and validate again
                rc_invoice = self.rc_self_invoice_id
                rc_invoice.invoice_line_ids.unlink()
                rc_invoice.period_id = False
                rc_invoice.write(inv_vals)
                rc_invoice.compute_taxes()
            else:
                rc_invoice = self.create(inv_vals)
                self.rc_self_invoice_id = rc_invoice.id
            rc_invoice.action_invoice_open()

            if rc_type.with_supplier_self_invoice:
                self.reconcile_supplier_invoice()
            else:
                rc_payment = self.reconcile_rc_invoice()
                self.partially_reconcile_supplier_invoice(rc_payment)

    def generate_supplier_self_invoice(self):
        rc_type = self.fiscal_position_id.rc_type_id
        if not len(rc_type.tax_ids) == 1:
            raise UserError(_(
                "Can't find 1 tax mapping for %s" % rc_type.name))
        if not self.rc_self_purchase_invoice_id:
            supplier_invoice = self.copy()
        else:
            supplier_invoice_vals = self.copy_data()
            supplier_invoice = self.rc_self_purchase_invoice_id
            supplier_invoice.invoice_line_ids.unlink()
            supplier_invoice.write(supplier_invoice_vals[0])

        # because this field has copy=False
        supplier_invoice.date = self.date
        supplier_invoice.date_invoice = self.date
        supplier_invoice.date_due = self.date
        supplier_invoice.partner_id = rc_type.partner_id.id
        supplier_invoice.journal_id = rc_type.supplier_journal_id.id
        for inv_line in supplier_invoice.invoice_line_ids:
            inv_line.invoice_line_tax_ids = [
                (6, 0, [rc_type.tax_ids[0].purchase_tax_id.id])]
            inv_line.account_id = rc_type.transitory_account_id.id
        self.rc_self_purchase_invoice_id = supplier_invoice.id

        # temporary disabling self invoice automations
        supplier_invoice.fiscal_position_id = None
        supplier_invoice.compute_taxes()
        supplier_invoice.check_total = supplier_invoice.amount_total
        supplier_invoice.action_invoice_open()
        supplier_invoice.fiscal_position_id = self.fiscal_position_id.id


    def create_fattura_spedizioniere(self):
        """
        Funzione per creare la fattura dello spedizioniere
        """
        bollette_doganali_conf_id = self.env['bollette.doganali'].browse(1)
        amount_spese_anticipate = 0
        for line in self.giroconto_bolletta_doganale_id.line_ids:
            if line.account_id.id == bollette_doganali_conf_id.debiti_spese_anticipate_id.id:
                amount_spese_anticipate = line.credit
        vals = {
            'invoice_line_ids': [(0, 0, {
                'name': 'Spese Anticipate Spedizioniere',
                'account_id': bollette_doganali_conf_id.debiti_spese_anticipate_id.id,
                'quantity': 1,
                'price_unit': amount_spese_anticipate
            })
        ]}
        invoice_spedizioniere_id = self.create(vals)
        return {
            "type": "ir.actions.act_window",
            "name": "Fattura Spedizioniere",
            "res_model": 'account.invoice',
            "views": [[False, "form"]],
            "res_id": invoice_spedizioniere_id.id,
            "target": "current",
        }


    def create_giroconto_dogana(self):
        """
        Funzione Chiamata quando il fornitore ha il flag "is_dogana"
        Crea la movimentazione contabile del giroconto e l'aggancia alla fattura della bolletta doganale
        """
        account_move_id = self.env['account.move']
        journal_varie_id = self.env['account.journal'].search([('code', '=', 'VARIE')])
        amount_conto_transitorio = 0
        amount_spese_anticipate = 0
        bollette_doganali_conf_id = self.env['bollette.doganali'].browse(1)
        if not journal_varie_id:
            raise UserError("Impossibile trovare il registro con codice breve 'VARIE' ")
        else:
            if not bollette_doganali_conf_id:
                raise UserError("Impostare le configurazioni delle bollette doganali")
            else:
                for line in self.move_id.line_ids:
                    if line.account_id.id == bollette_doganali_conf_id.conto_transitorio_id.id:
                        amount_conto_transitorio = line.debit
                    if line.debit > 0 and line.account_id.id != bollette_doganali_conf_id.conto_transitorio_id.id:
                        amount_spese_anticipate += line.debit
                vals = {
                    'journal_id': journal_varie_id.id,
                    'date': self.date_invoice,
                    'ref': 'Giroconto Bolletta Doganale ' + self.number,
                    'move_type': 'other',
                    'line_ids': [
                        (0, 0, {
                            'account_id': self.partner_id.property_account_payable_id.id,
                            'debit': amount_conto_transitorio,
                            'partner_id': self.partner_id.id,
                            'name': 'Bolla Doganale'
                        }),
                        (0, 0, {
                            'account_id': bollette_doganali_conf_id.conto_transitorio_id.id,
                            'credit': amount_conto_transitorio,
                            'partner_id': self.partner_id.id,
                            'name': 'c/Transitorio',
                        }),
                        (0, 0, {
                            'account_id': self.partner_id.property_account_payable_id.id,
                            'debit': amount_spese_anticipate,
                            'partner_id': self.partner_id.id,
                            'name': 'Bolla Doganale'
                        }),
                        (0, 0, {
                            'account_id': bollette_doganali_conf_id.debiti_spese_anticipate_id.id,
                            'credit': amount_spese_anticipate,
                            'partner_id': self.partner_id.id,
                            'name': 'Spese Anticipate Spedizioniere'
                        })
                    ]
                }
                giroconto_bolletta_doganale_id = account_move_id.create(vals)
                giroconto_bolletta_doganale_id.action_post()
                self.giroconto_bolletta_doganale_id = giroconto_bolletta_doganale_id.id

    @api.multi
    def invoice_validate(self):
        res = super(AccountInvoice, self).invoice_validate()
        for invoice in self:
            fp = invoice.fiscal_position_id

            if invoice.partner_id.is_dogana:
                #Registrazione Bolletta Doganale
                self.create_giroconto_dogana()

            rc_type = fp and fp.rc_type_id
            if not rc_type:
                continue
            if rc_type.method == 'selfinvoice' and invoice.amount_total:
                if not rc_type.with_supplier_self_invoice:
                    invoice.generate_self_invoice()
                else:
                    # See with_supplier_self_invoice field help
                    invoice.generate_supplier_self_invoice()
                    invoice.rc_self_purchase_invoice_id.generate_self_invoice()
            elif rc_type.method == 'integration':
                raise UserError(
                    _("VAT integration RC type, "
                      "defined in fiscal position {fp}, is not managed yet")
                        .format(fp=fp.display_name))
        return res

    def remove_rc_payment(self):
        inv = self
        if inv.payment_move_line_ids:
            if len(inv.payment_move_line_ids) > 1:
                raise UserError(
                    _('There are more than one payment line.\n'
                      'In that case account entries cannot be canceled'
                      'automatically. Please proceed manually'))
            payment_move = inv.payment_move_line_ids[0].move_id

            # remove move reconcile related to the supplier invoice
            move = inv.move_id
            rec_partial = move.mapped('line_ids').filtered(
                'matched_debit_ids').mapped('matched_debit_ids')
            rec_partial_lines = (
                    rec_partial.mapped('credit_move_id') |
                    rec_partial.mapped('debit_move_id')
            )
            rec_partial_lines.remove_move_reconcile()

            # also remove full reconcile, in case of with_supplier_self_invoice
            rec_partial_lines = move.mapped('line_ids').filtered(
                'full_reconcile_id'
            ).mapped('full_reconcile_id.reconciled_line_ids')
            rec_partial_lines.remove_move_reconcile()
            # remove move reconcile related to the self invoice
            move = inv.rc_self_invoice_id.move_id
            rec_lines = move.mapped('line_ids').filtered(
                'full_reconcile_id'
            ).mapped('full_reconcile_id.reconciled_line_ids')
            rec_lines.remove_move_reconcile()
            # cancel self invoice
            self_invoice = self.browse(
                inv.rc_self_invoice_id.id)
            self_invoice.action_invoice_cancel()
            # invalidate and delete the payment move generated
            # by the self invoice creation
            payment_move.button_cancel()
            payment_move.unlink()

    @api.multi
    def action_cancel(self):
        for inv in self:
            rc_type = inv.fiscal_position_id.rc_type_id
            if (
                    rc_type and
                    rc_type.method == 'selfinvoice' and
                    inv.rc_self_invoice_id
            ):
                inv.remove_rc_payment()
            elif (
                    rc_type and
                    rc_type.method == 'selfinvoice' and
                    inv.rc_self_purchase_invoice_id
            ):
                inv.rc_self_purchase_invoice_id.remove_rc_payment()
                inv.rc_self_purchase_invoice_id.action_invoice_cancel()
        return super(AccountInvoice, self).action_cancel()

    @api.multi
    def action_invoice_draft(self):
        # super(AccountInvoice, self).action_invoice_draft()

        self.write({'state': 'draft', 'date': False})
        # Delete former printed invoice
        try:
            report_invoice = self.env['ir.actions.report']._get_report_from_name('account.report_invoice')
        except IndexError:
            report_invoice = False
        if report_invoice and report_invoice.attachment:
            for invoice in self:
                with invoice.env.do_in_draft():
                    invoice.number, invoice.state = invoice.move_name, 'open'
                    attachment = self.env.ref('account.account_invoices').retrieve_attachment(invoice)
                if attachment:
                    attachment.unlink()

        invoice_model = self.env['account.invoice']
        for inv in self:
            if inv.rc_self_invoice_id:
                self_invoice = invoice_model.browse(
                    inv.rc_self_invoice_id.id)
                self_invoice.action_invoice_draft()
            if inv.rc_self_purchase_invoice_id:
                self_purchase_invoice = invoice_model.browse(
                    inv.rc_self_purchase_invoice_id.id)
                self_purchase_invoice.action_invoice_draft()
        return True

    def apply_partner_account(self):
        if self.partner_id:
            for l in self.invoice_line_ids:
                if l.selected and (not self.row_description or self.row_description in l.name):
                    if self.am_account_id:
                        l.account_id = self.am_account_id.id
                    if self.am_analytic_account:
                        l.account_analytic_id = self.am_analytic_account.id
                    if self.am_tax_id:
                        l.invoice_line_tax_ids = [(5,0), (4, self.am_tax_id.id)]
                    if self.am_rda:
                        l.invoice_line_tax_wt_ids = [(5,0), (4, self.am_rda.id)]
                    if self.am_rc != l.rc:
                        l.rc = self.am_rc
                    if self.purchase_order_id:
                        l.purchase_order_id = self.purchase_order_id.id
                l.selected = False
            self.compute_taxes()
            self._onchange_invoice_line_wt_ids()
            self.compute_differenza_ordini()


    def get_tax_amount_added_for_rc(self):
        res = 0
        for line in self.invoice_line_ids:
            if line.rc:
                price_unit = line.price_unit * (
                        1 - (line.discount or 0.0) / 100.0)
                taxes = line.invoice_line_tax_ids.compute_all(
                    price_unit, self.currency_id, line.quantity,
                    line.product_id, self.partner_id)['taxes']
                for tax in taxes:
                    res += tax['amount']
        return res



class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    selected = fields.Boolean()
    purchase_order_id = fields.Many2one('purchase.order')

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

    rc = fields.Boolean("RC")

    def open_line(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Riga Fattura",
            "res_model": 'account.invoice.line',
            "views": [[False, "form"]],
            "res_id": self.id,
            "target": "current",
        }

    @api.multi
    def _set_rc_flag(self, invoice):
        self.ensure_one()
        if invoice.type in ['in_invoice', 'in_refund']:
            fposition = invoice.fiscal_position_id
            self.rc = bool(fposition.rc_type_id)

    @api.onchange('invoice_line_tax_ids')
    def onchange_invoice_line_tax_id(self):
        self._set_rc_flag(self.invoice_id)


    def _set_additional_fields(self, invoice):
        res = super(AccountInvoiceLine, self)._set_additional_fields(invoice)
        self._set_rc_flag(invoice)
        return res


class AccountInvoiceConfirmInh(models.TransientModel):

    _inherit = "account.invoice.confirm"

    @api.multi
    def invoice_confirm(self):
        context = dict(self._context or {})
        active_ids = context.get('active_ids', []) or []
        records = self.env['account.invoice'].browse(active_ids)
        sorted_records = records.sorted(key=lambda x: x.date_invoice)
        for record in sorted_records:
            if record.state != 'draft':
                raise UserError("Selected invoice(s) cannot be confirmed as they are not in 'Draft' state.")
            record.action_invoice_open()
        return {'type': 'ir.actions.act_window_close'}
