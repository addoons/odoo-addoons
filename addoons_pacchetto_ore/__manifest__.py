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
        'base', 'sale', 'sale_management', 'account', 'project', 'addoons_reports', 'hr_timesheet', 'hr_attendance', 'report_xlsx'
    ],
    'data': [
        'views/addoons_ore_views.xml',
        'views/project_task_view_inherit.xml',
        'views/res_partner_view_inherit.xml',
        'views/sale_order.xml',
        'views/hr_attendance.xml',
        'views/project_gant.xml',
        'security/ir.model.access.csv',
        'report/reports.xml',
        'report/report_sommario_ore.xml',
        'report/report_sommario_ore_interne.xml',
        'wizard/wizard_report_presenze.xml',
        'views/project_assets.xml',
    ],

    'qweb': [
        'static/src/xml/project_gant_templates.xml'
    ],
    'installable': True,

}