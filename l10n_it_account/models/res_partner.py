# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)

from odoo import models, fields, api,_


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