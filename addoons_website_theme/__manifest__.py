{
    'name': 'addoons website',
    'version': '1.0',
    'category': 'all',
    'description': 'addoons website',
    'summary': 'ore',
    'author': 'addoons',
    'website': 'www.hexcode.it',
    'support': 'federico@hexcode.it',
    'depends': [
        'base', 'website', 'website_blog', 'sale', 'project', 'addoons_pacchetto_ore',
    ],
    'data': [
        'views/ore_snippet.xml',
        'views/snippet_options.xml',
        'views/assets.xml',
        'views/project_portal.xml',

    ],

    'installable': True,

}