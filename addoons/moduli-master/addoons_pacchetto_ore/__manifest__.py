{
    'name': 'Pacchetti ore',
    'version': '1.0',
    'category': 'all',
    'description': 'pacchetti ore',
    'summary': 'ore',
    'author': 'addOons srl',
    'website': 'www.addoons.it',
    'support': 'support@addoons.it',
    'depends': [
        'base', 'sale', 'sale_management', 'account', 'project'
    ],
    'data': [
        'views/addoons_ore_views.xml',
        'views/project_task_view_inherit.xml',
        'views/res_partner_view_inherit.xml',
        'security/ir.model.access.csv'
    ],

    'installable': True,

}