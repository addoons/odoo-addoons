# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)

from odoo import fields, models, api, _, exceptions
import odoo.addons.decimal_precision as dp

from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare, relativedelta

RELATED_DOCUMENT_TYPES = {
    'order': 'DatiOrdineAcquisto',
    'contract': 'DatiContratto',
    'agreement': 'DatiConvenzione',
    'reception': 'DatiRicezione',
    'invoice': 'DatiFattureCollegate',
}

fatturapa_attachment_state_mapping = {
    'ready': 'ready',
    'sent': 'sent',
    'validated': 'delivered',
    'sender_error': 'error',
    'recipient_error': 'accepted',
    'accepted': 'accepted',
    'rejected': 'error'
}


class RCType(models.Model):
    _inherit = 'account.rc.type'

    e_invoice_suppliers = fields.Boolean(
        "E-invoice suppliers",
        help="Automatically used when importing e-invoices from Italian "
             "suppliers")





class FatturapaFormat(models.Model):
    # _position = ['1.1.3']
    _name = "fatturapa.format"
    _description = 'E-invoice Format'

    name = fields.Char('Description', size=128)
    code = fields.Char('Code', size=5)


class FatturapaDocumentType(models.Model):
    # _position = ['2.1.1.1']
    _name = "fatturapa.document_type"
    _description = 'E-invoice Document Type'

    name = fields.Char('Description', size=128)
    code = fields.Char('Code', size=4)


#  used in fatturaPa import
class FatturapaPaymentData(models.Model):
    # _position = ['2.4.2.2']
    _name = "fatturapa.payment.data"
    _description = 'E-invoice Payment Data'

    #  2.4.1
    payment_terms = fields.Many2one(
        'fatturapa.payment_term', string="Electronic Invoice Payment Method")
    #  2.4.2
    payment_methods = fields.One2many(
        'fatturapa.payment.detail', 'payment_data_id',
        'Payments Details')
    invoice_id = fields.Many2one(
        'account.invoice', 'Related Invoice',
        ondelete='cascade', index=True)


class FatturapaPaymentDetail(models.Model):
    # _position = ['2.4.2']
    _name = "fatturapa.payment.detail"
    _description = "E-invoice payment details"
    recipient = fields.Char('Recipient', size=200)
    fatturapa_pm_id = fields.Many2one(
        'fatturapa.payment_method', string="Electronic Invoice Payment Method"
    )
    payment_term_start = fields.Date('Payment Term Start')
    payment_days = fields.Integer('Payment Term Days')
    payment_due_date = fields.Date('Payment Due Date')
    payment_amount = fields.Float('Payment Amount')
    post_office_code = fields.Char('Post Office Code', size=20)
    recepit_name = fields.Char("Receipt Issuer Name")
    recepit_surname = fields.Char("Receipt Issuer Surname")
    recepit_cf = fields.Char("Receipt Issuer FC")
    recepit_title = fields.Char("Receipt Issuer Title")
    payment_bank_name = fields.Char("Bank Name")
    payment_bank_iban = fields.Char("IBAN")
    payment_bank_abi = fields.Char("ABI")
    payment_bank_cab = fields.Char("CAB")
    payment_bank_bic = fields.Char("BIC")
    payment_bank = fields.Many2one(
        'res.partner.bank', string="Payment Bank")
    prepayment_discount = fields.Float('Prepayment Discount')
    max_payment_date = fields.Date('Maximum Date for Payment')
    penalty_amount = fields.Float('Amount of Penalty')
    penalty_date = fields.Date('Effective Date of Penalty')
    payment_code = fields.Char('Payment Code')
    account_move_line_id = fields.Many2one(
        'account.move.line', string="Payment Line")
    payment_data_id = fields.Many2one(
        'fatturapa.payment.data', 'Related Payments Data',
        ondelete='cascade', index=True)


class FatturapaFiscalPosition(models.Model):
    # _position = ['2.1.1.7.7', '2.2.1.14']
    _name = "fatturapa.fiscal_position"
    _description = 'Electronic Invoice Fiscal Position'

    name = fields.Char('Description', size=128)
    code = fields.Char('Code', size=4)


class WelfareFundType(models.Model):
    # _position = ['2.1.1.7.1']
    _name = "welfare.fund.type"
    _description = 'Welfare Fund Type'

    name = fields.Char('Name')
    description = fields.Char('Description')


class WelfareFundDataLine(models.Model):
    # _position = ['2.1.1.7']
    _name = "welfare.fund.data.line"
    _description = 'E-invoice Welfare Fund Data'

    name = fields.Many2one(
        'welfare.fund.type', string="Welfare Fund Type")
    kind_id = fields.Many2one('account.tax.kind', string="Non taxable nature")
    welfare_rate_tax = fields.Float('Welfare Tax Rate')
    welfare_amount_tax = fields.Float('Welfare Tax Amount')
    welfare_taxable = fields.Float('Welfare Taxable')
    welfare_Iva_tax = fields.Float('VAT Tax Rate')
    subjected_withholding = fields.Char(
        'Subjected to Withholding', size=2)
    pa_line_code = fields.Char('PA Code for this Record', size=20)
    invoice_id = fields.Many2one(
        'account.invoice', 'Related Invoice',
        ondelete='cascade', index=True
    )

class WithholdingDataLine(models.Model):
    _name = "withholding.data.line"
    _description = 'E-invoice Withholding Data'

    name = fields.Selection(
        selection=[
            ('RT01', 'Natural Person'),
            ('RT02', 'Legal Person'),
            ('RT03', 'INPS'),
            ('RT04', 'ENASARCO'),
            ('RT05', 'ENPAM'),
            ('RT06', 'OTHER'),
        ],
        string='Withholding Type'
    )
    amount = fields.Float('Withholding amount')
    invoice_id = fields.Many2one(
        'account.invoice', 'Related Invoice',
        ondelete='cascade', index=True
    )


class DiscountRisePrice(models.Model):
    # _position = ['2.1.1.8', '2.2.1.10']
    _name = "discount.rise.price"
    _description = 'E-invoice Discount Supplement Data'

    name = fields.Selection(
        [('SC', 'Discount'), ('MG', 'Supplement')], 'Type')
    percentage = fields.Float('Percentage')
    amount = fields.Float('Amount', digits=dp.get_precision('Discount'))
    invoice_line_id = fields.Many2one(
        'account.invoice.line', 'Related Invoice from line',
        ondelete='cascade', index=True
    )
    invoice_id = fields.Many2one(
        'account.invoice', 'Related Invoice',
        ondelete='cascade', index=True
    )
    e_invoice_line_id = fields.Many2one(
        'einvoice.line', 'Related E-bill Line', readonly=True
    )
    ftpa_withholding_ids = fields.One2many(
        'withholding.data.line', 'invoice_id',
        'Withholding', copy=False
    )


class FatturapaRelatedDocumentType(models.Model):
    _name = 'fatturapa.related_document_type'
    _description = 'E-invoice Related Document Type'

    type = fields.Selection(
        [
            ('order', 'Order'),
            ('contract', 'Contract'),
            ('agreement', 'Agreement'),
            ('reception', 'Reception'),
            ('invoice', 'Related Invoice'),
        ],
        'Document Type', required=True
    )
    name = fields.Char('Document ID', size=20, required=True)
    lineRef = fields.Integer('Line Ref.')
    invoice_line_id = fields.Many2one(
        'account.invoice.line', 'Related Invoice Line',
        ondelete='cascade', index=True)
    invoice_id = fields.Many2one(
        'account.invoice', 'Related Invoice',
        ondelete='cascade', index=True)
    date = fields.Date('Date')
    numitem = fields.Char('Item Num.', size=20)
    code = fields.Char('Order Agreement Code', size=100)
    cig = fields.Char('CIG Code', size=15)
    cup = fields.Char('CUP Code', size=15)
    partner_id = fields.Many2one('res.partner')

    @api.model
    def create(self, vals):
        if vals.get('invoice_line_id'):
            line_obj = self.env['account.invoice.line']
            line = line_obj.browse(vals['invoice_line_id'])
            vals['lineRef'] = line.sequence
        return super(FatturapaRelatedDocumentType, self).create(vals)


class FaturapaActivityProgress(models.Model):
    # _position = ['2.1.7']
    _name = "faturapa.activity.progress"
    _description = "E-invoice activity progress"

    fatturapa_activity_progress = fields.Integer('Activity Progress')
    invoice_id = fields.Many2one(
        'account.invoice', 'Related Invoice',
        ondelete='cascade', index=True)


class FatturaAttachments(models.Model):
    # _position = ['2.5']
    _name = "fatturapa.attachments"
    _description = "E-invoice attachments"
    _inherits = {'ir.attachment': 'ir_attachment_id'}

    ir_attachment_id = fields.Many2one(
        'ir.attachment', 'Attachment', required=True, ondelete="cascade")
    compression = fields.Char('Compression', size=10)
    format = fields.Char('Format', size=10)
    invoice_id = fields.Many2one(
        'account.invoice', 'Related Invoice',
        ondelete='cascade', index=True)


class FatturapaRelatedDdt(models.Model):
    # _position = ['2.1.2', '2.2.3', '2.1.4', '2.1.5', '2.1.6']
    _name = 'fatturapa.related_ddt'
    _description = 'E-invoice Related DDT'

    name = fields.Char('Document ID', size=20, required=True)
    date = fields.Date('Date')
    lineRef = fields.Integer('Line Ref.')
    invoice_line_id = fields.Many2one(
        'account.invoice.line', 'Related Invoice Line',
        ondelete='cascade', index=True)
    invoice_id = fields.Many2one(
        'account.invoice', 'Related Invoice',
        ondelete='cascade', index=True)

    @api.model
    def create(self, vals):
        if vals.get('invoice_line_id'):
            line_obj = self.env['account.invoice.line']
            line = line_obj.browse(vals['invoice_line_id'])
            vals['lineRef'] = line.sequence
        return super(FatturapaRelatedDdt, self).create(vals)


class AltriDatiGestionali(models.Model):
    _name = 'altri.dati.gestionali'

    name = fields.Char("Data Type")
    text_ref = fields.Char("Text Reference")
    num_ref = fields.Float("Number Reference")
    date_ref = fields.Date("Date Reference")
    invoice_line_id = fields.Many2one('account.invoice.line')

class AccountInvoiceLine(models.Model):
    # _position = ['2.2.1']
    _inherit = "account.invoice.line"

    related_documents = fields.One2many(
        'fatturapa.related_document_type', 'invoice_line_id',
        'Related Documents Type', copy=False
    )
    ftpa_related_ddts = fields.One2many(
        'fatturapa.related_ddt', 'invoice_line_id',
        'Related DDT', copy=False
    )
    admin_ref = fields.Char('Admin. ref.', size=20, copy=False)
    discount_rise_price_ids = fields.One2many(
        'discount.rise.price', 'invoice_line_id',
        'Discount or Supplement Details', copy=False
    )
    ftpa_line_number = fields.Integer("Line Number", readonly=True, copy=False)
    is_stamp_line = fields.Boolean(
        related='product_id.is_stamp',
        readonly=True)

    altri_dati_gestionali_ids = fields.One2many('altri.dati.gestionali', 'invoice_line_id')

    @api.multi
    def _set_rc_flag(self, invoice):
        self.ensure_one()
        if 'fatturapa.attachment.in' in self.env.context.get(
                'active_model', []
        ):
            # this means we are importing an e-invoice,
            # so RC flag is already set, where needed
            return
        return super(AccountInvoiceLine, self)._set_rc_flag(invoice)


class FaturapaSummaryData(models.Model):
    # _position = ['2.2.2']
    _name = "faturapa.summary.data"
    _description = "E-invoice summary data"
    tax_rate = fields.Float('Tax Rate')
    non_taxable_nature = fields.Selection([
        ('N1', 'excluding ex Art. 15'),
        ('N2', 'not subject'),
        ('N2.1', 'not subject ex Artt. from 7 to 7-septies of DPR 633/72'),
        ('N2.2', 'not subject – other'),
        ('N3', 'not taxable'),
        ('N3.1', 'not taxable – export'),
        ('N3.2', 'not taxable – intercommunity cession'),
        ('N3.3', 'not taxable – cession to San Marino'),
        ('N3.4', 'not taxable – operation similar to export cession'),
        ('N3.5', 'not taxable – following declarations of intent'),
        ('N3.6', 'not taxable – other operations that do not contribute to the formation of the ceiling'),
        ('N4', 'exempt'),
        ('N5', 'margin regime'),
        ('N6', 'reverse charge'),
        ('N6.1', 'reverse charge – disposal of scrap and other recycled materials'),
        ('N6.2', 'reverse charge – supply of gold and pure silver'),
        ('N6.3', 'reverse charge – subcontracting in the construction sector'),
        ('N6.4', 'reverse charge – sale of buildings'),
        ('N6.5', 'reverse charge – transfer of cell phones'),
        ('N6.6', 'reverse charge – sale of electronic products'),
        ('N6.7', 'reverse charge – construction sector and related sectors'),
        ('N6.8', 'reverse charge – energy sector operations'),
        ('N6.9', 'reverse charge – other cases'),
        ('N7', 'VAT paid in another EU country')
    ], string="Non taxable nature")
    incidental_charges = fields.Float('Incidental Charges')
    rounding = fields.Float('Rounding')
    amount_untaxed = fields.Float('Amount Untaxed')
    amount_tax = fields.Float('Amount Tax')
    payability = fields.Selection([
        ('I', 'Immediate payability'),
        ('D', 'Deferred payability'),
        ('S', 'Split payment'),
    ], string="VAT payability")
    law_reference = fields.Char(
        'Law reference', size=128)
    invoice_id = fields.Many2one(
        'account.invoice', 'Related Invoice',
        ondelete='cascade', index=True)


class AccountInvoice(models.Model):
    # _position = ['2.1', '2.2', '2.3', '2.4', '2.5']
    _inherit = "account.invoice"
    protocol_number = fields.Char('Protocol Number', size=64, copy=False)
    # 1.2 -- partner_id
    # 1.3
    tax_representative_id = fields.Many2one(
        'res.partner', string="Tax Representative")
    #  1.4 company_id
    #  1.5
    intermediary = fields.Many2one(
        'res.partner', string="Intermediary")
    #  1.6
    sender = fields.Selection(
        [('CC', 'Assignee / Partner'), ('TZ', 'Third Person')], 'Sender')

    #  2.1.1.5
    ftpa_withholding_ids = fields.One2many(
        'withholding.data.line', 'invoice_id',
        'Withholding', copy=False
    )
    #  2.1.1.5.2 2.1.1.5.3 2.1.1.5.4 mapped to l10n_it_withholding_tax fields

    #  2.1.1.7
    welfare_fund_ids = fields.One2many(
        'welfare.fund.data.line', 'invoice_id',
        'Welfare Fund', copy=False
    )
    #  2.1.2 - 2.1.6
    related_documents = fields.One2many(
        'fatturapa.related_document_type', 'invoice_id',
        'Related Documents', copy=False
    )
    #  2.1.7
    activity_progress_ids = fields.One2many(
        'faturapa.activity.progress', 'invoice_id',
        'Phase of Activity Progress', copy=False
    )
    #  2.1.8
    ftpa_related_ddts = fields.One2many(
        'fatturapa.related_ddt', 'invoice_id',
        'Related DDT', copy=False
    )
    #  2.1.9
    carrier_id = fields.Many2one(
        'res.partner', string="Carrier", copy=False)
    transport_vehicle = fields.Char('Vehicle', size=80, copy=False)
    transport_reason = fields.Char('Reason', size=80, copy=False)
    number_items = fields.Integer('Number of Items', copy=False)
    description = fields.Char('Description', size=100, copy=False)
    unit_weight = fields.Char('Weight Unit', size=10, copy=False)
    gross_weight = fields.Float('Gross Weight', copy=False)
    net_weight = fields.Float('Net Weight', copy=False)
    pickup_datetime = fields.Datetime('Pick up', copy=False)
    transport_date = fields.Date('Transport Date', copy=False)
    delivery_address = fields.Text(
        'Delivery Address for E-invoice', copy=False)
    delivery_datetime = fields.Datetime('Delivery Date Time', copy=False)
    ftpa_incoterms = fields.Char(string="E-inv Incoterms", copy=False)
    #  2.1.10
    related_invoice_code = fields.Char('Related Invoice Code', copy=False)
    related_invoice_date = fields.Date('Related Invoice Date', copy=False)
    #  2.2.1 invoice lines
    #  2.2.2
    fatturapa_summary_ids = fields.One2many(
        'faturapa.summary.data', 'invoice_id',
        'Electronic Invoice Summary Data', copy=False
    )
    #  2.3
    vehicle_registration = fields.Date('Vehicle Registration', copy=False)
    total_travel = fields.Char('Travel in hours or Km', size=15, copy=False)
    #  2.4
    fatturapa_payments = fields.One2many(
        'fatturapa.payment.data', 'invoice_id',
        'Electronic Invoice Payment Data', copy=False
    )
    #  2.5
    fatturapa_doc_attachments = fields.One2many(
        'fatturapa.attachments', 'invoice_id',
        'Electronic Invoice Attachments', copy=False
    )
    # 1.2.3
    efatt_stabile_organizzazione_indirizzo = fields.Char(
        string="Organization Address",
        help="The fields must be entered only when the seller/provider is "
             "non-resident, with a stable organization in Italy. Address of "
             "the stable organization in Italy (street name, square, etc.)",
        readonly=True, copy=False)
    efatt_stabile_organizzazione_civico = fields.Char(
        string="Organization Street Number",
        help="Street number of the address (no need to specify if already "
             "present in the address field)",
        readonly=True, copy=False)
    efatt_stabile_organizzazione_cap = fields.Char(
        string="Organization ZIP",
        help="ZIP Code",
        readonly=True, copy=False)
    efatt_stabile_organizzazione_comune = fields.Char(
        string="Organization Municipality",
        help="Municipality or city to which the Stable Organization refers",
        readonly=True, copy=False)
    efatt_stabile_organizzazione_provincia = fields.Char(
        string="Organization Province",
        help="Acronym of the Province to which the municipality indicated "
             "in the information element 1.2.3.4 <Comune> belongs. "
             "Must be filled if the information element 1.2.3.6 <Nazione> is "
             "equal to IT",
        readonly=True, copy=False)
    efatt_stabile_organizzazione_nazione = fields.Char(
        string="Organization Country",
        help="Country code according to the ISO 3166-1 alpha-2 code standard",
        readonly=True, copy=False)
    # 2.1.1.10
    efatt_rounding = fields.Float(
        "Rounding", readonly=True,
        help="Possible total amount rounding on the document (negative sign "
             "allowed)", copy=False
    )
    art73 = fields.Boolean(
        'Art. 73', readonly=True,
        help="Indicates whether the document has been issued according to "
             "methods and terms laid down in a ministerial decree under the "
             "terms of Article 73 of Italian Presidential Decree 633/72 (this "
             "enables the seller/provider to issue in the same year several "
             "documents with same number)", copy=False)
    electronic_invoice_subjected = fields.Boolean(
        'Subjected to Electronic Invoice',
        related='partner_id.electronic_invoice_subjected', readonly=True)

    fatturapa_attachment_in_id = fields.Many2one(
        'fatturapa.attachment.in', 'E-bill Import File',
        ondelete='restrict', copy=False)
    inconsistencies = fields.Text('Import Inconsistencies', copy=False)
    e_invoice_line_ids = fields.One2many(
        "einvoice.line", "invoice_id", string="Lines Detail",
        readonly=True, copy=False)

    fatturapa_state = fields.Selection(
        [('ready', 'Ready to Send'),
         ('sent', 'Sent'),
         ('delivered', 'Delivered'),
         ('accepted', 'Accepted'),
         ('error', 'Error')],
        string='E-invoice State',
        compute='_compute_fatturapa_state',
        store='true',
    )
    fatturapa_state_sdi = fields.Char(related='fatturapa_attachment_out_id.aruba_sdi_state')
    tax_stamp = fields.Boolean(
        "Tax Stamp", readonly=True, states={'draft': [('readonly', False)]})
    auto_compute_stamp = fields.Boolean(related='company_id.tax_stamp_product_id.auto_compute')

    amount_sp = fields.Float(
        string='Split Payment',
        digits=dp.get_precision('Account'),
        store=True,
        readonly=True,
        compute='_compute_amount')
    split_payment = fields.Boolean(
        'Is Split Payment',
        related='fiscal_position_id.split_payment')

    e_invoice_received_date = fields.Date(
        string='E-Bill Received Date')

    e_invoice_amount_untaxed = fields.Monetary(
        string='E-Invoice Untaxed Amount', readonly=True)
    e_invoice_amount_tax = fields.Monetary(string='E-Invoice Tax Amount',
                                           readonly=True)
    e_invoice_amount_total = fields.Monetary(string='E-Invoice Total Amount',
                                             readonly=True)

    e_invoice_reference = fields.Char(
        string="E-invoice vendor reference",
        readonly=True)

    e_invoice_date_invoice = fields.Date(
        string="E-invoice date",
        readonly=True)

    e_invoice_validation_error = fields.Boolean(
        compute='_compute_e_invoice_validation_error')

    e_invoice_validation_message = fields.Text(
        compute='_compute_e_invoice_validation_error')

    e_invoice_force_validation = fields.Boolean(
        string='Force E-Invoice Validation')

    payment_due_ids = fields.One2many('payment.due.item', 'invoice_id')


    @api.onchange('partner_id')
    def onchange_partner_id(self):
        """
        Al cambiamento del partner, aggiunge i dati dell'appalto/investimento SE non sono già presenti.
        In caso di partner che non usa gare d'appalto/investimenti pubblici, vengono rimossi tutti i record legati
        a partner che li usano
        """
        if self.partner_id:
            if self.partner_id.is_pa:
                doc_found = False
                doc_ids = self.related_documents.ids
                # cerca se i dati dell'appalto sono presenti nei documenti collegati
                for doc in self.related_documents:
                    if doc.type == self.partner_id.procurement_type \
                            and doc.name == self.partner_id.procurement_name:
                        doc_found = True
                        break
                # se non sono stati inseriti crea un nuovo record e popola la tabella dei doc collegati
                if not doc_found:
                    new_doc = self.env['fatturapa.related_document_type'].create({
                        'type': self.partner_id.procurement_type,
                        'name': self.partner_id.procurement_name,
                        'code': self.partner_id.procurement_code,
                        'date': self.partner_id.procurement_date,
                        'cig': self.partner_id.procurement_cig,
                        'cup': self.partner_id.procurement_cup,
                        'partner_id': self.partner_id.id
                    })
                    doc_ids.append(new_doc.id)
                    self.related_documents = [(6, 0, doc_ids)]
            # ad ogni cambiamento del partner sono eliminati i documenti
            # collegati che hanno partner DIVERSO da quello selezionato
            doc_to_remove = []
            for doc in self.related_documents:
                if doc.partner_id and doc.partner_id.id != self.partner_id.id:
                    doc_to_remove.append((2, doc.id))
            if len(doc_to_remove) > 0:
                self.related_documents = doc_to_remove


    @api.depends('move_id')
    def onchange_move_id(self):
        move_line = []
        if self.move_id:
            move_line = [(5, )]
            for line in self.move_id.line_ids:
                if line.account_id.internal_type == 'payable':
                    move_line.append((0, 0, {
                        'date': line.date_maturity,
                        'amount': line.credit,
                        'account_move_line_id': line.id
                    }))
        return move_line


    @api.multi
    def write(self, vals_list):
        res = super(AccountInvoice, self).write(vals_list)
        return res



    @api.model
    def create(self, vals_list):
        res = super(AccountInvoice, self).create(vals_list)
        res.onchange_partner_id()
        return res

    @api.onchange('payment_term_id')
    def compute_payment_due_ids(self):
        date_ref = self.date_invoice or fields.Date.today()
        amount = self.amount_total
        sign = 1 < 0 and -1 or 1
        due_ids = [(5,)]
        result = []
        if self.env.context.get('currency_id'):
            currency = self.env['res.currency'].browse(self.env.context['currency_id'])
        else:
            currency = self.env.user.company_id.currency_id
        for line in self.payment_term_id.line_ids:
            if line.value == 'fixed':
                amt = sign * currency.round(line.value_amount)
            elif line.value == 'percent':
                amt = currency.round(self.amount_total * (line.value_amount / 100.0))
            elif line.value == 'balance':
                amt = currency.round(amount)
            if amt:
                next_date = fields.Date.from_string(date_ref)
                if line.option == 'day_after_invoice_date':
                    next_date += relativedelta(days=line.days)
                    if line.day_of_the_month > 0:
                        months_delta = (line.day_of_the_month < next_date.day) and 1 or 0
                        next_date += relativedelta(day=line.day_of_the_month, months=months_delta)
                elif line.option == 'after_invoice_month':
                    next_first_date = next_date + relativedelta(day=1, months=1)  # Getting 1st of next month
                    next_date = next_first_date + relativedelta(days=line.days - 1)
                elif line.option == 'day_following_month':
                    next_date += relativedelta(day=line.days, months=1)
                elif line.option == 'day_current_month':
                    next_date += relativedelta(day=line.days, months=0)
                result.append((fields.Date.to_string(next_date), amt))

                # Aggiungo la riga all'array
                due_ids.append((0, 0, {
                    'amount': amt,
                    'date': next_date,
                    'fatturapa_payment_method_id': line.fatturapa_payment_method_id.id
                }))
                amount -= amt


        self.payment_due_ids = due_ids


    def process_negative_lines(self):
        self.ensure_one()
        for line in self.invoice_line_ids:
            if line.price_unit >= 0:
                return
        # if every line is negative, change them all
        for line in self.invoice_line_ids:
            line.price_unit = -line.price_unit
        self.compute_taxes()

    @api.model
    def compute_xml_amount_untaxed(self, FatturaBody):
        amount_untaxed = float(
            FatturaBody.DatiGenerali.DatiGeneraliDocumento.Arrotondamento
            or 0.0)
        for Riepilogo in FatturaBody.DatiBeniServizi.DatiRiepilogo:
            rounding = float(Riepilogo.Arrotondamento or 0.0)
            amount_untaxed += float(Riepilogo.ImponibileImporto) + rounding
        return amount_untaxed


    @api.multi
    def invoice_validate(self):
        for invoice in self:
            if (invoice.e_invoice_validation_error and
                    not invoice.e_invoice_force_validation):
                raise ValidationError(
                    _("The invoice '%s' doesn't match the related e-invoice : %s") %
                    (invoice.display_name, invoice.e_invoice_validation_message))
        return super(AccountInvoice, self).invoice_validate()

    def e_inv_check_amount_untaxed(self):
        error_message = ''
        if (self.e_invoice_amount_untaxed and
                float_compare(self.amount_untaxed,
                              # Using abs because odoo invoice total can't be negative,
                              # while XML total can.
                              # See process_negative_lines method
                              abs(self.e_invoice_amount_untaxed),
                              precision_rounding=self.currency_id
                              .rounding) != 0):
            error_message = (
                _("Untaxed amount ({bill_amount_untaxed}) "
                  "does not match with "
                  "e-bill untaxed amount ({e_bill_amount_untaxed})")
                .format(
                    bill_amount_untaxed=self.amount_untaxed or 0,
                    e_bill_amount_untaxed=self.e_invoice_amount_untaxed
                ))
        return error_message

    # def e_inv_check_amount_tax(self):
    #     error_message = ''
    #     if (self.e_invoice_amount_tax and
    #             float_compare(self.amount_tax,
    #                           abs(self.e_invoice_amount_tax),
    #                           precision_rounding=self.currency_id
    #                           .rounding) != 0):
    #         error_message = (
    #             _("Taxed amount ({bill_amount_tax}) "
    #               "does not match with "
    #               "e-bill taxed amount ({e_bill_amount_tax})")
    #             .format(
    #                 bill_amount_tax=self.amount_tax or 0,
    #                 e_bill_amount_tax=self.e_invoice_amount_tax
    #             ))
    #     return error_message

    # def e_inv_check_amount_total(self):
    #     error_message = ''
    #     if (self.e_invoice_amount_total and
    #             float_compare(self.amount_total,
    #                           abs(self.e_invoice_amount_total),
    #                           precision_rounding=self.currency_id
    #                           .rounding) != 0):
    #         error_message = (
    #             _("Total amount ({bill_amount_total}) "
    #               "does not match with "
    #               "e-bill total amount ({e_bill_amount_total})")
    #             .format(
    #                 bill_amount_total=self.amount_total or 0,
    #                 e_bill_amount_total=self.e_invoice_amount_total
    #             ))
    #     return error_message

    @api.depends('type', 'state', 'fatturapa_attachment_in_id',
                 'amount_untaxed', 'amount_tax', 'amount_total',
                 'reference', 'date_invoice')
    def _compute_e_invoice_validation_error(self):
        bills_to_check = self.filtered(
            lambda inv:
            inv.type in ['in_invoice', 'in_refund'] and
            inv.state in ['draft', 'open', 'paid'] and
            inv.fatturapa_attachment_in_id)
        for bill in bills_to_check:
            error_messages = list()

            # error_message = bill.e_inv_check_amount_untaxed()
            # if error_message:
            #     error_messages.append(error_message)
            #Viene disattivato il controllo sul subtotale (imponibile)
            #Questo perchè esistono fatture XML che possiedono arrotondamenti
            #I quali non è possibile ricostrituire l'XML in fattura.

            error_message = bill.e_inv_check_amount_tax()
            if error_message:
                error_messages.append(error_message)

            error_message = bill.e_inv_check_amount_total()
            if error_message:
                error_messages.append(error_message)

            if (bill.e_invoice_reference and
                    bill.reference != bill.e_invoice_reference):
                error_messages.append(
                    _("Vendor reference ({bill_vendor_ref}) "
                      "does not match with "
                      "e-bill vendor reference ({e_bill_vendor_ref})")
                        .format(
                        bill_vendor_ref=bill.reference or "",
                        e_bill_vendor_ref=bill.e_invoice_reference
                    ))

            if (bill.e_invoice_date_invoice and
                    bill.e_invoice_date_invoice != bill.date_invoice):
                error_messages.append(
                    _("Invoice date ({bill_date_invoice}) "
                      "does not match with "
                      "e-bill invoice date ({e_bill_date_invoice})")
                        .format(
                        bill_date_invoice=bill.date_invoice or "",
                        e_bill_date_invoice=bill.e_invoice_date_invoice
                    ))

            if not error_messages:
                continue
            bill.e_invoice_validation_error = True
            bill.e_invoice_validation_message = \
                ",\n".join(error_messages) + "."

    @api.model
    def compute_xml_amount_tax(self, DatiRiepilogo):
        amount_tax = 0.0
        for Riepilogo in DatiRiepilogo:
            amount_tax += float(Riepilogo.Imposta)
        return amount_tax

    def set_einvoice_data(self, fattura):
        self.ensure_one()
        amount_untaxed = self.compute_xml_amount_untaxed(fattura)
        amount_tax = self.compute_xml_amount_tax(
            fattura.DatiBeniServizi.DatiRiepilogo)
        amount_total = float(
            fattura.DatiGenerali.DatiGeneraliDocumento.
            ImportoTotaleDocumento or 0.0)
        reference = fattura.DatiGenerali.DatiGeneraliDocumento.Numero
        date_invoice = fields.Date.from_string(
            fattura.DatiGenerali.DatiGeneraliDocumento.Data)

        self.update({
            'e_invoice_amount_untaxed': amount_untaxed,
            'e_invoice_amount_tax': amount_tax,
            'e_invoice_amount_total': amount_total,
            'e_invoice_reference': reference,
            'e_invoice_date_invoice': date_invoice,
        })

    def e_inv_check_amount_tax(self):
        if (
                    any(self.invoice_line_ids.mapped('rc')) and
                    self.e_invoice_amount_tax
        ):
            error_message = ''
            amount_added_for_rc = self.get_tax_amount_added_for_rc()
            amount_tax = self.amount_tax - amount_added_for_rc
            if float_compare(
                    amount_tax, self.e_invoice_amount_tax,
                    precision_rounding=self.currency_id.rounding
            ) != 0:
                error_message = (
                    _("Taxed amount ({bill_amount_tax}) "
                      "does not match with "
                      "e-bill taxed amount ({e_bill_amount_tax})")
                        .format(
                        bill_amount_tax=amount_tax or 0,
                        e_bill_amount_tax=self.e_invoice_amount_tax
                    ))
            return error_message


    def e_inv_check_amount_total(self):
        if (
                    any(self.invoice_line_ids.mapped('rc')) and
                    self.e_invoice_amount_total
        ):
            error_message = ''
            amount_added_for_rc = self.get_tax_amount_added_for_rc()
            amount_total = self.amount_total - amount_added_for_rc
            if float_compare(
                    amount_total, self.e_invoice_amount_total,
                    precision_rounding=self.currency_id.rounding
            ) != 0:
                error_message = (
                    _("Total amount ({bill_amount_total}) "
                      "does not match with "
                      "e-bill total amount ({e_bill_amount_total})")
                        .format(
                        bill_amount_total=amount_total or 0,
                        e_bill_amount_total=self.e_invoice_amount_total
                    ))
            return error_message



    @api.one
    @api.depends(
        'invoice_line_ids.price_subtotal', 'tax_line_ids.amount',
        'tax_line_ids.amount_rounding',
        'currency_id', 'company_id', 'date_invoice', 'type'
    )
    def _compute_amount(self):
        super(AccountInvoice, self)._compute_amount()
        self.amount_sp = 0
        if self.fiscal_position_id.split_payment:
            self.amount_sp = self.amount_tax
            self.amount_tax = 0
        self.amount_total = self.amount_untaxed + self.amount_tax

    def _build_debit_line(self):
        if not self.company_id.sp_account_id:
            raise UserError(
                _("Please set 'Split Payment Write-off Account' field in"
                  " accounting configuration"))
        vals = {
            'name': _('Split Payment Write Off'),
            'partner_id': self.partner_id.id,
            'account_id': self.company_id.sp_account_id.id,
            'journal_id': self.journal_id.id,
            'date': self.date_invoice,
            'debit': self.amount_sp,
            'credit': 0,
        }
        if self.type == 'out_refund':
            vals['debit'] = 0
            vals['credit'] = self.amount_sp
        return vals

    @api.multi
    def get_receivable_line_ids(self):
        # return the move line ids with the same account as the invoice self
        self.ensure_one()
        return self.move_id.line_ids.filtered(
            lambda r: r.account_id.id == self.account_id.id).ids

    @api.multi
    def _compute_split_payments(self):
        for invoice in self:
            receivable_line_ids = invoice.get_receivable_line_ids()
            move_line_pool = self.env['account.move.line']
            for receivable_line in move_line_pool.browse(receivable_line_ids):
                inv_total = invoice.amount_sp + invoice.amount_total
                if invoice.type == 'out_invoice':
                    if inv_total:
                        receivable_line_amount = (
                                                         invoice.amount_total * receivable_line.debit
                                                 ) / inv_total
                    else:
                        receivable_line_amount = 0
                    receivable_line.with_context(
                        check_move_validity=False
                    ).write(
                        {'debit': receivable_line_amount})
                elif invoice.type == 'out_refund':
                    if inv_total:
                        receivable_line_amount = (
                                                         invoice.amount_total * receivable_line.credit
                                                 ) / inv_total
                    else:
                        receivable_line_amount = 0
                    receivable_line.with_context(
                        check_move_validity=False
                    ).write(
                        {'credit': receivable_line_amount})

    @api.multi
    def action_move_create(self):
        res = super(AccountInvoice, self).action_move_create()
        for invoice in self:
            if invoice.split_payment:
                if invoice.type in ['in_invoice', 'in_refund']:
                    raise UserError(
                        _("Can't handle supplier invoices with split payment"))
                if invoice.move_id.state == 'posted':
                    posted = True
                    invoice.move_id.state = 'draft'
                self._compute_split_payments()
                line_model = self.env['account.move.line']
                write_off_line_vals = invoice._build_debit_line()
                write_off_line_vals['move_id'] = invoice.move_id.id
                line_model.with_context(
                    check_move_validity=False
                ).create(write_off_line_vals)
                if posted:
                    invoice.move_id.state = 'posted'
        return res

    def is_tax_stamp_applicable(self):
        stamp_product_id = self.env.user.with_context(
            lang=self.partner_id.lang).company_id.tax_stamp_product_id
        if not stamp_product_id:
            raise exceptions.Warning(
                _('Missing tax stamp product in company settings!')
            )
        total_tax_base = 0.0
        for inv_tax in self.tax_line_ids:
            if (
                    inv_tax.tax_id.id in
                    stamp_product_id.stamp_apply_tax_ids.ids
            ):
                total_tax_base += inv_tax.base
        if total_tax_base >= stamp_product_id.stamp_apply_min_total_base:
            return True
        else:
            return False

    @api.onchange('tax_line_ids')
    def _onchange_tax_line_ids(self):
        if self.auto_compute_stamp:
            self.tax_stamp = self.is_tax_stamp_applicable()

    @api.multi
    def add_tax_stamp_line(self):
        for inv in self:
            if not inv.tax_stamp:
                raise exceptions.Warning(_("Tax stamp is not applicable"))
            stamp_product_id = self.env.user.with_context(
                lang=inv.partner_id.lang).company_id.tax_stamp_product_id
            if not stamp_product_id:
                raise exceptions.Warning(
                    _('Missing tax stamp product in company settings!')
                )
            for l in inv.invoice_line_ids:
                if l.product_id and l.product_id.is_stamp:
                    raise exceptions.Warning(_(
                        "Tax stamp line %s already present. Remove it first."
                    ) % l.name)
            stamp_account = stamp_product_id.property_account_income_id
            if not stamp_account:
                raise exceptions.Warning(
                    _('Missing account income configuration for'
                      ' %s') % stamp_product_id.name)
            self.env['account.invoice.line'].create({
                'invoice_id': inv.id,
                'product_id': stamp_product_id.id,
                'name': stamp_product_id.description_sale,
                'sequence': 99999,
                'account_id': stamp_account.id,
                'price_unit': stamp_product_id.list_price,
                'quantity': 1,
                'uom_id': stamp_product_id.uom_id.id,
                'invoice_line_tax_ids': [
                    (6, 0, stamp_product_id.taxes_id.ids)],
                'account_analytic_id': None,
            })
            inv.compute_taxes()

    def is_tax_stamp_line_present(self):
        for l in self.invoice_line_ids:
            if l.product_id and l.product_id.is_stamp:
                return True
        return False

    def _build_tax_stamp_lines(self, product):
        if (
                not product.property_account_income_id or
                not product.property_account_expense_id
        ):
            raise exceptions.Warning(_(
                "Product %s must have income and expense accounts"
            ) % product.name)

        income_vals = {
            'name': _('Tax Stamp Income'),
            'partner_id': self.partner_id.id,
            'account_id': product.property_account_income_id.id,
            'journal_id': self.journal_id.id,
            'date': self.date_invoice,
            'debit': 0,
            'credit': product.list_price,
        }
        if self.type == 'out_refund':
            income_vals['debit'] = product.list_price
            income_vals['credit'] = 0

        expense_vals = {
            'name': _('Tax Stamp Expense'),
            'partner_id': self.partner_id.id,
            'account_id': product.property_account_expense_id.id,
            'journal_id': self.journal_id.id,
            'date': self.date_invoice,
            'debit': product.list_price,
            'credit': 0,
        }
        if self.type == 'out_refund':
            income_vals['debit'] = 0
            income_vals['credit'] = product.list_price

        return income_vals, expense_vals

    @api.multi
    def action_move_create(self):
        res = super(AccountInvoice, self).action_move_create()
        for inv in self:
            if inv.tax_stamp and not inv.is_tax_stamp_line_present():
                if inv.move_id.state == 'posted':
                    posted = True
                    inv.move_id.state = 'draft'
                line_model = self.env['account.move.line']
                stamp_product_id = self.env.user.with_context(
                    lang=inv.partner_id.lang).company_id.tax_stamp_product_id
                if not stamp_product_id:
                    raise exceptions.Warning(
                        _('Missing tax stamp product in company settings!')
                    )
                income_vals, expense_vals = self._build_tax_stamp_lines(
                    stamp_product_id)
                income_vals['move_id'] = inv.move_id.id
                expense_vals['move_id'] = inv.move_id.id
                line_model.with_context(
                    check_move_validity=False
                ).create(income_vals)
                line_model.with_context(
                    check_move_validity=False
                ).create(expense_vals)
                if posted:
                    inv.move_id.state = 'posted'
        return res
    @api.multi
    @api.depends('fatturapa_attachment_out_id.state')
    def _compute_fatturapa_state(self):
        for record in self:
            record.fatturapa_state = fatturapa_attachment_state_mapping.get(
                record.fatturapa_attachment_out_id.state)

    @api.multi
    def name_get(self):
        result = super(AccountInvoice, self).name_get()
        res = []
        for tup in result:
            invoice = self.browse(tup[0])
            if invoice.type in ('in_invoice', 'in_refund'):
                name = "%s, %s" % (tup[1], invoice.partner_id.name)
                if invoice.amount_total_signed:
                    name += ', %s %s' % (
                        invoice.amount_total_signed, invoice.currency_id.symbol
                    )
                if invoice.origin:
                    name += ', %s' % invoice.origin
                res.append((invoice.id, name))
            else:
                res.append(tup)
        return res

    @api.multi
    def remove_attachment_link(self):
        self.ensure_one()
        self.fatturapa_attachment_in_id = False
        return {'type': 'ir.actions.client', 'tag': 'reload'}

    fatturapa_attachment_out_id = fields.Many2one(
        'fatturapa.attachment.out', 'E-invoice Export File',
        readonly=True, copy=False)

    has_pdf_invoice_print = fields.Boolean(
        related='fatturapa_attachment_out_id.has_pdf_invoice_print',
        readonly=True)

    def preventive_checks(self):
        # hook for preventive checks. Override and raise exception, in case
        return

    @api.multi
    def action_invoice_cancel(self):
        for invoice in self:
            if invoice.fatturapa_attachment_out_id:
                raise UserError(_(
                    "Invoice %s has XML and can't be canceled. "
                    "Delete the XML before."
                ) % invoice.number)
        res = super(AccountInvoice, self).action_invoice_cancel()
        return res

    class fatturapa_article_code(models.Model):
        # _position = ['2.2.1.3']
        _name = "fatturapa.article.code"
        _description = 'E-bill Article Code'

        name = fields.Char('Code Type')
        code_val = fields.Char('Code Value')
        e_invoice_line_id = fields.Many2one(
            'einvoice.line', 'Related E-bill Line', readonly=True
        )

    class AccountInvoiceLine(models.Model):
        # _position = [
        #     '2.2.1.3', '2.2.1.6', '2.2.1.7',
        #     '2.2.1.8', '2.1.1.10'
        # ]
        _inherit = "account.invoice.line"

        fatturapa_attachment_in_id = fields.Many2one(
            'fatturapa.attachment.in', 'E-bill Import File',
            readonly=True, related='invoice_id.fatturapa_attachment_in_id')

    class EInvoiceLine(models.Model):
        _name = 'einvoice.line'
        _description = 'E-invoice line'
        invoice_id = fields.Many2one(
            "account.invoice", "Bill", readonly=True)
        line_number = fields.Integer('Line Number', readonly=True)
        service_type = fields.Char('Sale Provision Type', readonly=True)
        cod_article_ids = fields.One2many(
            'fatturapa.article.code', 'e_invoice_line_id',
            'Articles Code', readonly=True
        )
        name = fields.Char("Description", readonly=True)
        qty = fields.Float(
            "Quantity", readonly=True,
            digits=dp.get_precision('Product Unit of Measure')
        )
        uom = fields.Char("Unit of measure", readonly=True)
        period_start_date = fields.Date("Period Start Date", readonly=True)
        period_end_date = fields.Date("Period End Date", readonly=True)
        unit_price = fields.Float(
            "Unit Price", readonly=True,
            digits=dp.get_precision('Product Price')
        )
        discount_rise_price_ids = fields.One2many(
            'discount.rise.price', 'e_invoice_line_id',
            'Discount and Supplement Details', readonly=True
        )
        total_price = fields.Float("Total Price", readonly=True)
        tax_amount = fields.Float("VAT Rate", readonly=True)
        wt_amount = fields.Char("Tax Withholding", readonly=True)
        tax_kind = fields.Char("Nature", readonly=True)
        admin_ref = fields.Char("Administration Reference", readonly=True)
        other_data_ids = fields.One2many(
            "einvoice.line.other.data", "e_invoice_line_id",
            string="Other Administrative Data", readonly=True)

    class EInvoiceLineOtherData(models.Model):
        _name = 'einvoice.line.other.data'
        _description = 'E-invoice line other data'

        e_invoice_line_id = fields.Many2one(
            'einvoice.line', 'Related E-bill Line', readonly=True
        )
        name = fields.Char("Data Type", readonly=True)
        text_ref = fields.Char("Text Reference", readonly=True)
        num_ref = fields.Float("Number Reference", readonly=True)
        date_ref = fields.Char("Date Reference", readonly=True)

    class AccountTax(models.Model):
        _inherit = 'account.tax'
        is_split_payment = fields.Boolean(
            "Is split payment", compute="_compute_is_split_payment")

        @api.multi
        def _compute_is_split_payment(self):
            for tax in self:
                fp_lines = self.env['account.fiscal.position.tax'].search(
                    [('tax_dest_id', '=', tax.id)])
                tax.is_split_payment = any(
                    fp_line.position_id.split_payment for fp_line in fp_lines
                )

    class AccountFiscalPosition(models.Model):
        _inherit = 'account.fiscal.position'

        split_payment = fields.Boolean('Split Payment')

    class FatturapaPaymentTerm(models.Model):
        # _position = ['2.4.1']
        _name = "fatturapa.payment_term"
        _description = 'Fiscal Payment Term'

        name = fields.Char('Description', size=128)
        code = fields.Char('Code', size=4)

    class FatturapaPaymentMethod(models.Model):
        # _position = ['2.4.2.2']
        _name = "fatturapa.payment_method"
        _description = 'Fiscal Payment Method'

        name = fields.Char('Description', size=128)
        code = fields.Char('Code', size=4)

    #  used in fatturaPa export
    class AccountPaymentTerm(models.Model):
        # _position = ['2.4.2.2']
        _inherit = 'account.payment.term'

        fatturapa_pt_id = fields.Many2one(
            'fatturapa.payment_term', string="Fiscal Payment Term")
        fatturapa_pm_id = fields.Many2one(
            'fatturapa.payment_method', string="Fiscal Payment Method")
