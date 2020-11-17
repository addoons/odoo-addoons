# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)

from odoo import models, fields, api,_
from odoo.tools import formatLang


class ResCompany(models.Model):
    _inherit = 'res.company'
    fiscalcode = fields.Char(
        related='partner_id.fiscalcode', store=True, readonly=False)

    rea_office = fields.Many2one(
        'res.country.state', string='Office Province',
        related='partner_id.rea_office', store=True, readonly=False)
    rea_code = fields.Char(
        'REA Code', size=20, related='partner_id.rea_code',
        store=True, readonly=False)
    rea_capital = fields.Float(
        'Share Capital', related='partner_id.rea_capital',
        store=True, readonly=False)
    rea_member_type = fields.Selection(
        [('SU', 'Unique Member'),
         ('SM', 'Multiple Members')], 'Member Type',
        related='partner_id.rea_member_type', store=True, readonly=False)
    rea_liquidation_state = fields.Selection(
        [('LS', 'In liquidation'),
         ('LN', 'Not in liquidation')], 'Liquidation State',
        related='partner_id.rea_liquidation_state',
        store=True, readonly=False)
    of_account_end_vat_statement_interest = fields.Boolean(
        'Interest on End Vat Statement',
        help="Apply interest on end vat statement")
    of_account_end_vat_statement_interest_percent = fields.Float(
        'Interest on End Vat Statement - %',
        help="Apply interest on end vat statement")
    of_account_end_vat_statement_interest_account_id = fields.Many2one(
        'account.account', 'Interest on End Vat Statement - Account',
        help="Apply interest on end vat statement")

    vsc_supply_code = fields.Char(
        'Vat statement communication supply code',
        default="IVP18",
        help="IVP18",
    )

    @api.onchange(
        "rea_office", "rea_code", "rea_capital", "rea_member_type",
        "rea_liquidation_state"
    )
    def onchange_rea_data(self):
        self.company_registry = ''
        rea_member_type = ''
        if (
                self.rea_office or self.rea_code or self.rea_capital or
                self.rea_member_type or self.rea_liquidation_state
        ):
            if self.rea_member_type:
                rea_member_type = dict(
                    self.env['res.partner']._fields[
                        'rea_member_type'
                    ]._description_selection(self.env)
                )[self.rea_member_type]
            rea_liquidation_state = ''
            if self.rea_liquidation_state:
                rea_liquidation_state = dict(
                    self.env['res.partner']._fields[
                        'rea_liquidation_state'
                    ]._description_selection(self.env)
                )[self.rea_liquidation_state]
            # using always €, as this is a registry of Italian companies
            company_registry = _("%s - %s / Share Cap. %s € / %s / %s") % (
                self.rea_office.code or '', self.rea_code or '',
                formatLang(self.env, self.rea_capital), rea_member_type,
                rea_liquidation_state
            )
            self.company_registry = company_registry
