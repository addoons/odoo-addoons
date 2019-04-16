{
    'name': 'addoons calcolatore app',
    'version': '1.0',
    'category': 'all',
    'description': 'addoons calcolatore app',
    'summary': 'ore',
    'author': 'addoons',
    'website': 'www.hexcode.it',
    'support': 'federico@hexcode.it',
    'depends': [
        'base', 'sale', 'sale_management'
    ],
    'data': [
        'views/odoo_apps_quotation_views.xml',
        'security/ir.model.access.csv',
		'data/odoo_apps_data.xml'

    ],
	
    'installable': True,

}