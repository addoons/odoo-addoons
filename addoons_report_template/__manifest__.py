# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Addoons Report Template',
    'version': '1.1',
    'website' : '',
    'category': '',
    'depends' : ['base', 'sale', 'web'],
    'description': """
    """,
    'data': [
        'report/addoons_res_company.xml',
        'report/addoons_report_layout.xml',
        'report/addoons_report_sale.xml',
        'report/addoons_report_invoice.xml',
        'views/addoons_sale_view.xml',
        'views/addoons_crm_lead.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'auto_install': False,
}
