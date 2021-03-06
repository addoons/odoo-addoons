# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class ResCompany(models.Model):
    _inherit = 'res.company'

    fatturapa_fiscal_position_id = fields.Many2one(
        'fatturapa.fiscal_position', 'Fiscal Position',
        help="Fiscal position used by electronic invoice",
        )
    fatturapa_sequence_id = fields.Many2one(
        'ir.sequence', 'E-invoice Sequence',
        help="The univocal progressive of the file is represented by "
             "an alphanumeric sequence of maximum length 5, "
             "its values are included in 'A'-'Z' and '0'-'9'"
        )
    fatturapa_art73 = fields.Boolean('Art. 73')
    fatturapa_pub_administration_ref = fields.Char(
        'Public Administration Reference Code', size=20,
        )
    fatturapa_tax_representative = fields.Many2one(
        'res.partner', 'Legal Tax Representative'
        )
    fatturapa_sender_partner = fields.Many2one(
        'res.partner', 'Third Party/Sender',
        help="Data of Third-Party Issuer Intermediary who emits the "
             "invoice on behalf of the seller/provider"
        )
    fatturapa_stabile_organizzazione = fields.Many2one(
        'res.partner', 'Stable Organization',
        help='The fields must be entered only when the seller/provider is '
             'non-resident, with a stable organization in Italy'
        )

    sconto_maggiorazione_product_id = fields.Many2one(
        'product.product', 'Discount Supplement Product',
        help="Product used to model ScontoMaggiorazione XML element on bills."
    )
    tax_stamp_product_id = fields.Many2one(
        'product.product', 'Tax Stamp Product',
        help="Product used as Tax Stamp in customer invoices."
    )

    enasarco_relax_checks = fields.Boolean('Relax checks for Enasarco')
    in_invoice_registration_date = fields.Selection([
        ('inv_date', 'Invoice Date'),
        ('rec_date', 'Received Date'),
    ], string='Vendor invoice registration default date',
        default='inv_date')

    sdi_channel_id = fields.Many2one(
        'sdi.channel', string='ES channel')
    sdi_channel_type = fields.Selection(
        related='sdi_channel_id.channel_type', readonly=True)
    email_from_for_fatturaPA = fields.Char(
        string='Sender Email Address',
        related='sdi_channel_id.pec_server_id.email_from_for_fatturaPA',
        readonly=True)
    email_exchange_system = fields.Char(
        string='Exchange System Email Address',
        related='sdi_channel_id.email_exchange_system', readonly=True)

    sp_account_id = fields.Many2one(
        'account.account',
        string='Split Payment Write-off Account',
        help='Account used to write off the VAT amount', readonly=False)

    arrotondamenti_attivi_account_id = fields.Many2one('account.account')
    arrotondamenti_passivi_account_id = fields.Many2one('account.account')
    arrotondamenti_tax_id = fields.Many2one('account.tax')

    cassa_previdenziale_product_id = fields.Many2one(
        'product.product', 'Welfare Fund Data Product',
        help="Product used to model DatiCassaPrevidenziale XML element "
             "on bills."
    )

    @api.multi
    @api.constrains(
        'fatturapa_sequence_id'
    )
    def _check_fatturapa_sequence_id(self):
        for company in self:
            if company.fatturapa_sequence_id:
                if company.fatturapa_sequence_id.use_date_range:
                    raise ValidationError(_(
                        "Sequence %s can't use subsequences."
                    ) % company.fatturapa_sequence_id.name)
                journal = self.env['account.journal'].search([
                    ('sequence_id', '=', company.fatturapa_sequence_id.id)
                ], limit=1)
                if journal:
                    raise ValidationError(_(
                        "Sequence %s already used by journal %s. Please select"
                        " another one."
                    ) % (company.fatturapa_sequence_id.name, journal.name))


class AccountConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    fatturapa_fiscal_position_id = fields.Many2one(
        related='company_id.fatturapa_fiscal_position_id',
        string="Fiscal Position",
        help='Fiscal position used by electronic invoice'
        )
    fatturapa_sequence_id = fields.Many2one(
        related='company_id.fatturapa_sequence_id',
        string="Sequence",
        help="The univocal progressive of the file is represented by "
             "an alphanumeric sequence of maximum length 5, "
             "its values are included in 'A'-'Z' and '0'-'9'",
        readonly=False
        )
    fatturapa_art73 = fields.Boolean(
        related='company_id.fatturapa_art73',
        string="Art. 73",
        help="Indicates whether the document has been issued according to "
             "methods and terms laid down in a ministerial decree under "
             "the terms of Article 73 of Italian Presidential Decree "
             "633/72 (this enables the company to issue in the same "
             "year several documents with same number)",
        readonly=False
        )
    fatturapa_pub_administration_ref = fields.Char(
        related='company_id.fatturapa_pub_administration_ref',
        string="Public Administration Reference Code",
        readonly=False
        )
    fatturapa_rea_office = fields.Many2one(
        related='company_id.rea_office',
        string="REA Office",
        readonly=False
        )
    fatturapa_rea_number = fields.Char(
        related='company_id.rea_code',
        string="REA Number",
        readonly=False
        )
    fatturapa_rea_capital = fields.Float(
        related='company_id.rea_capital',
        string="REA Capital",
        readonly=False
        )
    fatturapa_rea_partner = fields.Selection(
        related='company_id.rea_member_type',
        string="REA Copartner",
        readonly=False
        )
    fatturapa_rea_liquidation = fields.Selection(
        related='company_id.rea_liquidation_state',
        string="REA Liquidation",
        readonly=False
        )
    fatturapa_tax_representative = fields.Many2one(
        related='company_id.fatturapa_tax_representative',
        string="Legal Tax Representative",
        help='The fields must be entered only when the seller/provider makes '
             'use of a tax representative in Italy',
        readonly=False
        )
    fatturapa_sender_partner = fields.Many2one(
        related='company_id.fatturapa_sender_partner',
        string="Third Party/Sender",
        help="Data of Third-Party Issuer Intermediary who emits the "
             "invoice on behalf of the seller/provider",
        readonly=False
        )
    fatturapa_stabile_organizzazione = fields.Many2one(
        related='company_id.fatturapa_stabile_organizzazione',
        string="Stable Organization",
        help="The fields must be entered only when the seller/provider is "
             "non-resident, with a stable organization in Italy",
        readonly=False
        )
    tax_stamp_product_id = fields.Many2one(
        related='company_id.tax_stamp_product_id',
        string="Tax Stamp Product",
        help="Product used as Tax Stamp in customer invoices.",
        readonly=False
    )
    sdi_channel_id = fields.Many2one(
        related='company_id.sdi_channel_id', string='ES channel',
        readonly=False)
    sdi_channel_type = fields.Selection(
        related='sdi_channel_id.channel_type', readonly=True)
    email_from_for_fatturaPA = fields.Char(
        string='Sender Email Address',
        related='sdi_channel_id.pec_server_id.email_from_for_fatturaPA',
        readonly=True)
    email_exchange_system = fields.Char(
        string='Exchange System Email Address',
        related='sdi_channel_id.email_exchange_system', readonly=True)

    sp_account_id = fields.Many2one(
        related='company_id.sp_account_id',
        string='Split Payment Write-off account',
        help='Account used to write off the VAT amount', readonly=False)
    sconto_maggiorazione_product_id = fields.Many2one(
        related='company_id.sconto_maggiorazione_product_id',
        string="Discount Supplement Product",
        help='Product used to model ScontoMaggiorazione XML element on bills',
        readonly=False
        )

    enasarco_relax_checks = fields.Boolean(
        related='company_id.enasarco_relax_checks', readonly=False
    )
    in_invoice_registration_date = fields.Selection(
        related='company_id.in_invoice_registration_date', readonly=False
    )

    cassa_previdenziale_product_id = fields.Many2one(
        related='company_id.cassa_previdenziale_product_id',
        readonly=False
    )
    arrotondamenti_attivi_account_id = fields.Many2one(
        related='company_id.arrotondamenti_attivi_account_id',
        readonly=False
    )
    arrotondamenti_passivi_account_id = fields.Many2one(
        related='company_id.arrotondamenti_passivi_account_id',
        readonly=False
    )
    arrotondamenti_tax_id = fields.Many2one(
        related='company_id.arrotondamenti_tax_id',
        readonly=False
    )
    fatturapa_codice_tipo = fields.Char(default=lambda self: self.env['ir.config_parameter'].get_param('fatturapa_codice_tipo'), required=True,
                                        help="Imposta il valore del campo XML CodiceTipo all'interno di ogni riga di fattura. "
                                             "Essendo un campo obbligatorio, di default è impostato 'ODOO'")

    @api.multi
    def write(self, vals):
        self.env['ir.config_parameter'].sudo().set_param('fatturapa_codice_tipo',self.fatturapa_codice_tipo)
        super(AccountConfigSettings, self).write(vals)


    @api.onchange('company_id')
    def onchange_company_id(self):
        if self.company_id:
            company = self.company_id
            default_sequence = self.env['ir.sequence'].search([
                ('code', '=', 'account.invoice.fatturapa')
            ])
            default_sequence = (
                default_sequence[0].id if default_sequence else False)
            self.tax_stamp_product_id = (
                    company.tax_stamp_product_id and
                    company.tax_stamp_product_id.id or False)
            self.fatturapa_fiscal_position_id = (
                company.fatturapa_fiscal_position_id and
                company.fatturapa_fiscal_position_id.id or False
                )
            self.fatturapa_sequence_id = (
                company.fatturapa_sequence_id and
                company.fatturapa_sequence_id.id or default_sequence
                )
            self.fatturapa_art73 = (
                company.fatturapa_art73 or False
                )
            self.fatturapa_pub_administration_ref = (
                company.fatturapa_pub_administration_ref or False
                )
            self.fatturapa_rea_office = (
                company.rea_office and
                company.rea_office.id or False
                )
            self.fatturapa_rea_number = company.rea_code or False
            self.fatturapa_rea_capital = (
                company.rea_capital or False
                )
            self.fatturapa_rea_partner = (
                company.rea_member_type or False
                )
            self.fatturapa_rea_liquidation = (
                company.rea_liquidation_state or False
                )
            self.fatturapa_tax_representative = (
                company.fatturapa_tax_representative and
                company.fatturapa_tax_representative.id or False
                )
            self.fatturapa_sender_partner = (
                company.fatturapa_sender_partner and
                company.fatturapa_sender_partner.id or False
                )
            self.fatturapa_stabile_organizzazione = (
                company.fatturapa_stabile_organizzazione and
                company.fatturapa_stabile_organizzazione.id or False
                )
            self.sconto_maggiorazione_product_id = (
                    company.sconto_maggiorazione_product_id and
                    company.sconto_maggiorazione_product_id.id or False
            )
        else:
            self.fatturapa_fiscal_position_id = False
            self.fatturapa_sequence_id = False
            self.fatturapa_art73 = False
            self.fatturapa_pub_administration_ref = False
            self.fatturapa_rea_office = False
            self.fatturapa_rea_number = False
            self.fatturapa_rea_capital = False
            self.fatturapa_rea_partner = False
            self.fatturapa_rea_liquidation = False
            self.fatturapa_tax_representative = False
            self.fatturapa_sender_partner = False
            self.fatturapa_stabile_organizzazione = False
            self.tax_stamp_product_id = False
            self.sconto_maggiorazione_product_id = False



