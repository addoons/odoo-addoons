# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)

from odoo import models, fields, api
from odoo.tools.translate import _
from odoo.exceptions import UserError


class RemovePeriod(models.TransientModel):

    def _get_period_ids(self):
        statement_model = self.env['account.vat.period.end.statement']
        res = []
        if 'active_id' in self.env.context:
            statement = statement_model.browse(self.env.context['active_id'])
            for period in statement.date_range_ids:
                res.append((period.id, period.name))
        return res

    _name = 'remove.period.from.vat.statement'
    _description = "Remove period from VAT Statement"

    period_id = fields.Selection(_get_period_ids, 'Period', required=True)

    @api.multi
    def remove_period(self):
        self.ensure_one()
        if 'active_id' not in self.env.context:
            raise UserError(_('Current statement not found'))
        period = self.env['date.range'].browse(int(self.period_id))
        period.vat_statement_id = False
        statement = self.env['account.vat.period.end.statement'].browse(
            self.env.context['active_id'])
        statement.set_fiscal_year()
        statement.compute_amounts()
        return {
            'type': 'ir.actions.act_window_close',
        }
