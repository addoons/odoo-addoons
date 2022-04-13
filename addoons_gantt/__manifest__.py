{
    'name': 'Gantt view',
    'version': '1.0',
    'category': 'all',
    'description': 'gantt view',
    'summary': 'ore',
    'author': 'addOons srl',
    'website': 'www.addoons.it',
    'support': 'support@addoons.it',
    'depends': [
        'base', 'sale', 'sale_management', 'account', 'project', 'addoons_reports', 'hr_timesheet', 'hr_attendance', 'report_xlsx', 'addoons_pacchetto_ore'
    ],
    'data': [
        'views/project_gant.xml',
        'security/ir.model.access.csv',
        'views/project_assets.xml',
        'views/project_task_view_inherit.xml'
    ],

    'qweb': [
        'static/src/xml/project_gant_templates.xml'
    ],
    'installable': True,

}