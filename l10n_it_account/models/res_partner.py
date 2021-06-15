# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)
import logging
from odoo import models, fields, api,_


region_dict = {
    'AG':'Sicilia',
    'AL':'Piemonte',
    'AN':'Marche',
    'AO': "Valle d'Aosta",
    'AR':'Toscana',
    'AP':'Marche',
    'AT':'Piemonte',
    'AV':'Campania',
    'BA':'Puglia',
    'BT':'Puglia',
    'BL':'Veneto',
    'BN':'Campania',
    'BG':'Lombardia',
    'BI':'Piemonte',
    'BO':'Emilia Romagna',
    'BZ':'Trentino Alto Adige',
    'BS':'Lombardia',
    'BR':'Puglia',
    'CA':'Sardegna',
    'CL':'Sicilia',
    'CB':'Molise',
    'CI':'Sardegna',
    'CE':'Campania',
    'CT':'Sicilia',
    'CZ':'Calabria',
    'CH':'Abruzzo',
    'CO':'Lombardia',
    'CS':'Calabria',
    'CR':'Lombardia',
    'KR':'Calabria',
    'CN':'Piemonte',
    'EN':'Sicilia',
    'FM':'Marche',
    'FE':'Emilia Romagna',
    'FI':'Toscana',
    'FG':'Puglia',
    'FC':'Emilia Romagna',
    'FR':'Lazio',
    'GE':'Liguria',
    'GO':'Friuli Venezia Giulia',
    'GR':'Toscana',
    'IM':'Liguria',
    'IS':'Molise',
    'SP':'Liguria',
    'AQ':'Abruzzo',
    'LT':'Lazio',
    'LE':'Puglia',
    'LC':'Lombardia',
    'LI':'Toscana',
    'LO':'Lombardia',
    'LU':'Toscana',
    'MC':'Marche',
    'MN':'Lombardia',
    'MS':'Toscana',
    'MT':'Basilicata',
    'VS':'Sardegna',
    'ME':'Sicilia',
    'MI':'Lombardia',
    'MO':'Emilia Romagna',
    'MB':'Lombardia',
    'NA':'Campania',
    'NO':'Piemonte',
    'NU':'Sardegna',
    'OG':'Sardegna',
    'OT':'Sardegna',
    'OR':'Sardegna',
    'PD':'Veneto',
    'PA':'Sicilia',
    'PR':'Emilia Romagna',
    'PV':'Lombardia',
    'PG':'Umbria',
    'PU':'Marche',
    'PE':'Abruzzo',
    'PC':'Emilia Romagna',
    'PI':'Toscana',
    'PT':'Toscana',
    'PN':'Friuli Venezia Giulia',
    'PZ':'Basilicata',
    'PO':'Toscana',
    'RG':'Sicilia',
    'RA':'Emilia Romagna',
    'RC':'Calabria',
    'RE':'Emilia Romagna',
    'RI':'Lazio',
    'RN':'Emilia Romagna',
    'RM':'Lazio',
    'RO':'Veneto',
    'SA':'Campania',
    'SS':'Sardegna',
    'SV':'Liguria',
    'SI':'Toscana',
    'SR':'Sicilia',
    'SO':'Lombardia',
    'SU':'',
    'TA':'Puglia',
    'TE':'Abruzzo',
    'TR':'Umbria',
    'TO':'Piemonte',
    'TP':'Sicilia',
    'TN':'Trentino Alto Adige',
    'TV':'Veneto',
    'TS':'Friuli Venezia Giulia',
    'UD':'Friuli Venezia Giulia',
    'VA':'Lombardia',
    'VE':'Veneto',
    'VB':'Piemonte',
    'VC':'Piemonte',
    'VR':'Veneto',
    'VV':'Calabria',
    'VI':'Veneto',
    'VT':'Lazio',
}


class AlphaRegion(models.Model):
    _name = 'alpha.region'

    name = fields.Char()

class ResCountryState(models.Model):
    _inherit = 'res.country.state'

    region_id = fields.Many2one('alpha.region')


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.multi
    def check_fiscalcode(self):
        for partner in self:
            if not partner.fiscalcode:
                # Because it is not mandatory
                continue
            elif partner.company_type == 'person':
                # Person case
                if partner.company_name:
                    # In E-commerce, if there is company_name,
                    # the user might insert VAT in fiscalcode field.
                    # Perform the same check as Company case
                    continue
                if len(partner.fiscalcode) != 16 and len(partner.fiscalcode) != 11:
                    # Check fiscalcode of a person
                    return False
        return True

    costi_account = fields.Many2one('account.account')
    ricavi_account = fields.Many2one('account.account')

    use_corrispettivi = fields.Boolean(string='Use Receipts')
    out_fiscal_document_type = fields.Many2one(
        'fiscal.document.type', string="Out Fiscal Document Type",)
    in_fiscal_document_type = fields.Many2one(
        'fiscal.document.type', string="In Fiscal Document Type",)
    fiscalcode = fields.Char(
        'Fiscal Code', size=16, help="Italian Fiscal Code")
    ateco_category_ids = fields.Many2many(
        comodel_name='ateco.category',
        relation='ateco_category_partner_rel',
        column1='partner_id',
        column2='ateco_id',
        string='Ateco categories'
    )
    is_dogana = fields.Boolean()

    _constraints = [
        (check_fiscalcode,
         "The fiscal code doesn't seem to be correct.", ["fiscalcode"])
    ]
    pec_mail = fields.Char(string='PEC Mail')

    rea_office = fields.Many2one(
        'res.country.state', string='Office Province')
    rea_code = fields.Char('REA Code', size=20)
    rea_capital = fields.Float('Share Capital')
    rea_member_type = fields.Selection(
        [('SU', 'Unique Member'),
         ('SM', 'Multiple Members')], 'Member Type')
    rea_liquidation_state = fields.Selection(
        [('LS', 'In liquidation'),
         ('LN', 'Not in liquidation')], 'Liquidation State')

    #region_id = fields.Many2one('alpha.region')


    def compute_region(self):
        partner_ids = self.env['res.partner'].search([])
        for partner in partner_ids:
            partner.get_region()


    # @api.depends('state_id')
    # def get_region(self):
    #     for partner in self:
    #         if partner.state_id.country_id.code == 'IT':
    #             if partner.state_id.code in region_dict:
    #                 region_name = region_dict.get(partner.state_id.code)
    #                 region_id = self.env['alpha.region'].sudo().search([('name', '=', region_name)])
    #                 partner.region_id = region_id.id
    #                 logging.info("Regione Calcolata")
    #                 self.env.cr.commit()
    #             else:
    #                 logging.info('Provincia non trovata')






    @api.onchange('use_corrispettivi')
    def onchange_use_corrispettivi(self):
        if self.use_corrispettivi:
            # Partner is receipts, assign a receipts (corrispettivi)
            # fiscal position only if there is none
            if not self.property_account_position_id:
                company = self.company_id or \
                          self.default_get(['company_id'])['company_id']
                self.property_account_position_id = \
                    self.env['account.fiscal.position'] \
                        .get_corr_fiscal_pos(company)
        else:
            # Unset the fiscal position only if it was receipts (corrispettivi)
            if self.property_account_position_id.corrispettivi:
                self.property_account_position_id = False