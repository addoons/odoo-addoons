# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)

from odoo.addons.portal.controllers.portal import CustomerPortal


class CorrispettiviPortal(CustomerPortal):

    def _show_report(self, model, report_type, report_ref, download=False):
        if model._name == 'account.invoice' and model.corrispettivo:
            report_ref = 'l10n_it_account.account_corrispettivi'
        return super()._show_report(model, report_type, report_ref, download)
