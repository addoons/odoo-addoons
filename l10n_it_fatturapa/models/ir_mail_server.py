# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)

from odoo import models, fields, api


class IrMailServer(models.Model):
    _inherit = "ir.mail_server"

    is_fatturapa_pec = fields.Boolean("E-invoice PEC server")
    email_from_for_fatturaPA = fields.Char(
        "Sender Email Address")

    @api.multi
    def test_smtp_connection(self):
        self.ensure_one()
        if self.is_fatturapa_pec:
            # self.env.user.email is used to test SMTP connection
            self.env.user.email = self.email_from_for_fatturaPA
        # no need to revert to correct email: UserError is always raised and
        # rollback done
        return super(IrMailServer, self).test_smtp_connection()
