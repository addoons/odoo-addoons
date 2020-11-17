# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)

from odoo.addons.portal.controllers.portal import CustomerPortal

from odoo import http
from odoo.http import request


class CorrispettiviPortal(CustomerPortal):

    def _show_report(self, model, report_type, report_ref, download=False):
        if model._name == 'account.invoice' and model.corrispettivo:
            report_ref = 'l10n_it_account.account_corrispettivi'
        return super()._show_report(model, report_type, report_ref, download)


    @http.route('/web/database/<string:db_name>/update_all', type='http', auth="none")
    def update_all(self, db_name):
        base = request.env['ir.module.module'].sudo().search([('name', '=', 'base')])
        base.button_immediate_upgrade()
        return http.local_redirect('/web/database/manager')
