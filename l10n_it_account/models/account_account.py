# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)
from odoo import api, fields, models


class AccountAccountInherit(models.Model):
    _inherit = 'account.account'

    # controllo sul prefisso per suddividere le righe in gruppi ordinati sulle prime tre cifre
    def check_prefix(self, prev, prefix):
        result = fields.Boolean()
        if prefix == prev:
            result = False
        elif prefix != prev:
            result = True
        return result

    # prende il prefisso di 3 caratteri
    def print_prefix(self, code):
        return code[:3]




