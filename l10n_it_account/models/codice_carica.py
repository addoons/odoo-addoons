# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class CodiceCarica(models.Model):
    _name = 'codice.carica'
    _description = 'Role Code'

    code = fields.Char(string='Code', size=2)
    name = fields.Char(string='Name')

    @api.constrains('code')
    def _check_code(self):
        for codice in self:
            domain = [('code', '=', codice.code)]
            elements = self.search(domain)
            if len(elements) > 1:
                raise ValidationError(
                    _("The element with code %s already exists") % codice.code)

