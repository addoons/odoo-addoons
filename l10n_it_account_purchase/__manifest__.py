# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)

{
    'name': 'Contabilità Italiana - Acquisti',
    'version': '1.0',
    'category': 'Hidden',
    "author": "servizi@addoons.it",
    'website': 'www.addoons.it',
    'license': 'AGPL-3',
    "depends": [
        'l10n_it_account',
        'purchase'
    ],
    "data": [
        'views/account_invoice.xml'
    ],
    'installable': True,
}
