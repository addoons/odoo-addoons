# Copyright 2014 Abstract (http://www.abstract.it)
# Copyright Davide Corio <davide.corio@abstract.it>
# Copyright 2014-2018 Agile Business Group (http://www.agilebg.com)
# Copyright 2015 Apulia Software s.r.l. (http://www.apuliasoftware.it)
# Copyright Francesco Apruzzese <f.apruzzese@apuliasoftware.it>
# Copyright 2018 Simone Rubino - Agile Business Group
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'DDT',
    'version': '12.0.1.1.0',
    'category': 'Localization/Italy',
    'summary': "DDT",
    "author": "servizi@addoons.it",
    'website': 'www.addoons.it',
    'license': 'AGPL-3',
    'depends': [
        'sale_stock',
        'stock_account',
        'stock_picking_package_preparation_line',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/ddt_data.xml',
        'views/stock_picking_package_preparation.xml',
        'views/partner.xml',
        'views/account.xml',
        'views/sale.xml',
        'views/stock_location.xml',
        'wizard/add_picking_to_ddt.xml',
        'wizard/ddt_from_picking.xml',
        'views/stock_picking.xml',
        'wizard/ddt_create_invoice.xml',
        'wizard/ddt_invoicing.xml',
        'views/report_ddt.xml',
        'data/mail_template_data.xml',
    ],
    'installable': True
}
