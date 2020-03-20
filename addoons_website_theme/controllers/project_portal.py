import datetime
from collections import OrderedDict
from operator import itemgetter

from odoo import http, _
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
from odoo.tools import groupby as groupbyelem, base64

from odoo.osv.expression import OR



class CustomerPortal(CustomerPortal):
    @http.route(['/my/tasks', '/my/tasks/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_tasks(self, page=1, date_begin=None, date_end=None, sortby=None, filterby=None, search=None, search_in='content', groupby='project', **kw):
        values = self._prepare_portal_layout_values()
        searchbar_sortings = {
            'date': {'label': _('Newest'), 'order': 'create_date desc'},
            'name': {'label': _('Title'), 'order': 'name'},
            'stage': {'label': _('Stage'), 'order': 'stage_id'},
            'update': {'label': _('Last Stage Update'), 'order': 'date_last_stage_update desc'},
            'deadline': {'label': 'Data di Scadenza', 'order': 'date_deadline asc'},
        }
        searchbar_filters = {
            'all': {'label': _('All'), 'domain': []},
            'open':{'label': 'Aperti', 'domain': [('stage_id.fold', '=', False)]},
        }
        searchbar_inputs = {
            'content': {'input': 'content', 'label': _('Search <span class="nolabel"> (in Content)</span>')},
            'message': {'input': 'message', 'label': _('Search in Messages')},
            'customer': {'input': 'customer', 'label': _('Search in Customer')},
            'stage': {'input': 'stage', 'label': _('Search in Stages')},
            'all': {'input': 'all', 'label': _('Search in All')},
        }
        searchbar_groupby = {
            'none': {'input': 'none', 'label': _('None')},
            'project': {'input': 'project', 'label': _('Project')},
        }

        # extends filterby criteria with project the customer has access to
        projects = request.env['project.project'].search([])
        for project in projects:
            searchbar_filters.update({
                str(project.id): {'label': project.name, 'domain': [('project_id', '=', project.id)]}
            })

        # extends filterby criteria with project (criteria name is the project id)
        # Note: portal users can't view projects they don't follow
        project_groups = request.env['project.task'].read_group([('project_id', 'not in', projects.ids)],
                                                                ['project_id'], ['project_id'])
        for group in project_groups:
            proj_id = group['project_id'][0] if group['project_id'] else False
            proj_name = group['project_id'][1] if group['project_id'] else _('Others')
            searchbar_filters.update({
                str(proj_id): {'label': proj_name, 'domain': [('project_id', '=', proj_id)]}
            })

        # default sort by value
        if not sortby:
            sortby = 'deadline'
        order = searchbar_sortings[sortby]['order']
        # default filter by value
        if not filterby:
            filterby = 'all'
        domain = searchbar_filters[filterby]['domain']

        # archive groups - Default Group By 'create_date'
        archive_groups = self._get_archive_groups('project.task', domain)
        if date_begin and date_end:
            domain += [('create_date', '>', date_begin), ('create_date', '<=', date_end)]

        # search
        if search and search_in:
            search_domain = []
            if search_in in ('content', 'all'):
                search_domain = OR([search_domain, ['|', ('name', 'ilike', search), ('description', 'ilike', search)]])
            if search_in in ('customer', 'all'):
                search_domain = OR([search_domain, [('partner_id', 'ilike', search)]])
            if search_in in ('message', 'all'):
                search_domain = OR([search_domain, [('message_ids.body', 'ilike', search)]])
            if search_in in ('stage', 'all'):
                search_domain = OR([search_domain, [('stage_id', 'ilike', search)]])
            domain += search_domain

        domain.append(('partner_id', '=', request.env.user.partner_id.id))
        # task count
        task_count = request.env['project.task'].search_count(domain)
        # pager
        pager = portal_pager(
            url="/my/tasks",
            url_args={'date_begin': date_begin, 'date_end': date_end, 'sortby': sortby, 'filterby': filterby, 'search_in': search_in, 'search': search},
            total=task_count,
            page=page,
            step=self._items_per_page
        )
        # content according to pager and archive selected
        if groupby == 'project':
            order = "project_id, %s" % order  # force sort on project first to group by project in view
        tasks = request.env['project.task'].search(domain, limit=self._items_per_page, offset=(page - 1) * self._items_per_page)
        request.session['my_tasks_history'] = tasks.ids[:100]
        if groupby == 'project':
            grouped_tasks = [request.env['project.task'].concat(*g) for k, g in groupbyelem(tasks, itemgetter('project_id'))]
        else:
            grouped_tasks = [tasks]

        progetti = request.env['project.project'].sudo().search([('partner_id', '=', request.env.user.partner_id.id)])
        values.update({
            'today': datetime.datetime.today(),
            'date': date_begin,
            'date_end': date_end,
            'grouped_tasks': grouped_tasks,
            'page_name': 'task',
            'archive_groups': archive_groups,
            'default_url': '/my/tasks',
            'pager': pager,
            'searchbar_sortings': searchbar_sortings,
            'searchbar_groupby': searchbar_groupby,
            'searchbar_inputs': searchbar_inputs,
            'search_in': search_in,
            'sortby': sortby,
            'groupby': groupby,
            'searchbar_filters': OrderedDict(sorted(searchbar_filters.items())),
            'filterby': filterby,
            'projects': progetti
        })
        return request.render("project.portal_my_tasks", values)

    @http.route(['/my/tasks/create_task'], type='http', auth="user", website=True)
    def crea_task(self, redirect=None, **post):

        task = request.env['project.task'].sudo().create({
            'name': post['name'],
            'description': post['description'],
            'user_id': False,
            'partner_id': request.env.user.partner_id.id,
            'project_id': int(post['project_id'])
        })

        for data in request.httprequest.files.getlist('attachments'):

            file = base64.b64encode(data.read())
            if (data.filename and data.filename != ''):
                request.env['ir.attachment'].sudo().create({
                    'name': data.filename,
                    'type': 'binary',
                    'datas': file,
                    'datas_fname': data.filename,
                    'store_fname': data.filename,
                    'res_model': 'project.task',
                    'res_id': task.id,
                })
        task.sudo().write({'partner_id': request.env.user.partner_id.id})
        return request.redirect('/my/tasks')

    @http.route(['/my/task/write_task'], type='http', auth="user", website=True)
    def edit_task(self, redirect=None, **post):

        task = request.env['project.task'].sudo().browse(int(post['id_task']))
        if task:
            task.sudo().write({
                'name': post['name'],
                'description': post['description'],
                'project_id': int(post['project_id'])
            })

            for data in request.httprequest.files.getlist('attachments'):

                file = base64.b64encode(data.read())
                if(data.filename and data.filename != ''):
                    request.env['ir.attachment'].sudo().create({
                        'name': data.filename,
                        'type': 'binary',
                        'datas': file,
                        'datas_fname': data.filename,
                        'store_fname': data.filename,
                        'res_model': 'project.task',
                        'res_id': task.id,
                    })

        return request.redirect('/my/task/' + str(task.id))


    @http.route(['/my/task/<int:task_id>'], type='http', auth="public", website=True)
    def portal_my_task(self, task_id, access_token=None, **kw):
        try:
            task_sudo = self._document_check_access('project.task', task_id, access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        # ensure attachment are accessible with access token inside template
        for attachment in task_sudo.attachment_ids:
            attachment.generate_access_token()
        values = self._task_get_page_view_values(task_sudo, access_token, **kw)
        progetti = request.env['project.project'].sudo().search([('partner_id', '=', request.env.user.partner_id.id)])
        values.update({
            'projects': progetti,
        })
        return request.render("project.portal_my_task", values)