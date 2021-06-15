# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)

from odoo import models, fields,_


class AtecoCategory(models.Model):

    _name = 'ateco.category'
    _description = 'ATECO Code'

    name = fields.Char(required=True)
    code = fields.Char(string='ATECO Code', size=9, required=False)
    description = fields.Text()
    parent_id = fields.Many2one(
        'ateco.category', string='Parent Category', index=True)
    child_ids = fields.One2many(
        'ateco.category', 'parent_id', string='Child Categories')
    partner_ids = fields.Many2many(
        'res.partner', 'ateco_category_partner_rel',
        'ateco_id', 'partner_id', string='Partners'
    )
