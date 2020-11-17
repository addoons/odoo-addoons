# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)

{
    'name': 'SEPA',
    'version': '12.0.1.2.6',
    'category': 'Localization/Italy',
    'summary': 'Gestione Distinte pagamenti SEPA CBI 00.04.00',
    "author": "servizi@addoons.it",
    'website': 'www.addoons.it',
    'license': 'LGPL-3',
    "depends": [
        'account_sepa',
        'account_batch_payment'
    ],
    "data": [
        'views/sepa.xml'
    ],
    'installable': True,
    'external_dependencies': {
        'python': [
            'pyxb',
        ],
    }
}
