# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)
from odoo import models, fields,_


class DateRange(models.Model):
    _inherit = "date.range"

    vat_statement_id = fields.Many2one('account.vat.period.end.statement', "VAT statement")
