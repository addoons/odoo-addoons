# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)

{
    'name': 'Fattura elettronica',
    'version': '12.0.1.2.6',
    'category': 'Localization/Italy',
    'summary': 'Gestione delle fatture elettroniche',
    "author": "servizi@addoons.it",
    'website': 'www.addoons.it',
    'license': 'LGPL-3',
    "depends": [
        'l10n_it_account',
        'document',
        'base_iban',
        'partner_firstname',
        "l10n_it_ddt",
        'product',
        'fetchmail',
    ],
    "data": [
        'data/fatturapa_data.xml',
        'data/welfare.fund.type.csv',
        'data/fetchmail_data.xml',
        'data/bollo_virtuale.xml',
        'data/config_parameter.xml',
        'security/groups.xml',
        'security/security.xml',
        'wizard/send_pec_view.xml',
        'wizard/wizard_export_fatturapa_view.xml',
        'wizard/wizard_import_fatturapa_view.xml',
        'views/company_view.xml',
        'views/partner_view.xml',
        'views/account_invoice_out.xml',
        'views/account_invoice_in.xml',
        'views/fatturapa_attachment_in.xml',
        'views/fatturapa_attachment_out.xml',
        'views/invoice_view.xml',
        'views/fetchmail_view.xml',
        'views/product_view.xml',
        'views/ir_mail_server.xml',
        'views/sdi_view.xml',
        'security/ir.model.access.csv',
        'wizard/link_to_existing_invoice.xml',
        'wizard/send_to_aruba.xml',
        'data/fatturapa_attachment_in_cron.xml',
    ],
    'installable': True,
    'external_dependencies': {
        'python': [
            'pyxb',  # pyxb 1.2.5
            'asn1crypto'
        ],
    }
}
