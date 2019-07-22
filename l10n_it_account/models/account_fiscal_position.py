# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)

from odoo import models, fields,api


class AccountFiscalPosition(models.Model):
    _inherit = 'account.fiscal.position'

    fiscal_document_type_id = fields.Many2one(
        'fiscal.document.type',
        string="Fiscal Document Type",
        readonly=False)
    withholding_tax_ids = fields.Many2many(
        'withholding.tax', 'account_fiscal_position_withholding_tax_rel',
        'fiscal_position_id', 'withholding_tax_id', string='Withholding Tax')

    corrispettivi = fields.Boolean(string='Receipts')

    @api.model
    def get_corr_fiscal_pos(self, company_id=None):
        if not company_id:
            company_id = self.env.user.company_id
        corr_fiscal_pos = self.search(
            [
                ('company_id', '=', company_id.id),
                ('corrispettivi', '=', True),
            ],
            limit=1
        )
        if not corr_fiscal_pos:
            # Fall back to fiscal positions without company
            corr_fiscal_pos = self.search(
                [
                    ('company_id', '=', False),
                    ('corrispettivi', '=', True),
                ],
                limit=1
            )

        return corr_fiscal_pos
