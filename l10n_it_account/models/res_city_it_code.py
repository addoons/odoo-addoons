# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)

from odoo import models, fields, tools,_


class ResCityItCode(models.Model):
    _name = "res.city.it.code"
    _description = "National city codes"

    national_code = fields.Char('National code', size=4)
    cadastre_code = fields.Char(
        'Belfiore cadastre code (not used anymore)',
        size=4)
    province = fields.Char('Province', size=5)
    name = fields.Char('Name')
    notes = fields.Char('Notes', size=4)
    national_code_var = fields.Char('National code variation', size=4)
    cadastre_code_var = fields.Char('Cadastre code variation', size=4)
    province_var = fields.Char('Province variation', size=5)
    name_var = fields.Char('Name variation', size=100)
    creation_date = fields.Date('Creation date')
    var_date = fields.Date('Variation date')


class ResCityItCodeDistinct(models.Model):
    _name = 'res.city.it.code.distinct'
    _description = "National city codes distinct"
    _auto = False

    name = fields.Char('Name', size=100)

    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute(
            """
            CREATE OR REPLACE VIEW res_city_it_code_distinct AS (
            SELECT name, MAX(id) AS id FROM res_city_it_code
            GROUP BY name)
            """)
