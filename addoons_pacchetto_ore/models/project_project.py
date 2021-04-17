from odoo import models, api, fields, _
import datetime
import pytz
import re


switch_color = {
    0: '#008784',  # No color (doesn't work actually...)
    1: '#EE4B39',  # Red
    2: '#F29648',  # Orange
    3: '#F4C609',  # Yellow
    4: '#55B7EA',  # Light blue
    5: '#71405B',  # Dark purple
    6: '#E86869',  # Salmon pink
    7: '#008784',  # Medium blue
    8: '#267283',  # Dark blue
    9: '#BF1255',  # Fushia
    10: '#2BAF73',  # Green
    11: '#8754B0'  # Purple
}


class Project(models.Model):
    _inherit = 'project.project'

    duration = fields.Float(default=40)
    start_date = fields.Datetime(default=datetime.datetime.now()-datetime.timedelta(days=9))
    end_date = fields.Datetime(default=datetime.datetime.now()+datetime.timedelta(days=30))
    open = fields.Boolean(default=True)
    parent = fields.Integer()

    @api.multi
    def action_open_gantt(self):
        action = self.env.ref('addoons_pacchetto_ore.project_gant_action_client').read()[0]
        action['params'] = {
            'project_ids': self.ids,
        }
        action['search_view_id'] = [self.env.ref('project.view_task_search_form').id]
        action['pushState'] = False
        action['context'] = {
            'active_model': 'project.task',
            'search_default_project_id': self.id,
        }
        return action

    @api.model
    def get_data(self, domain=None):
        for element in domain:
            if isinstance(element, list):
                element = tuple(element)

        tasks = self.env['project.task'].sudo().search(domain)
        projects = []
        project_ids = []
        data = []
        links = []
        for task in tasks:
            if task.project_id.id not in project_ids and task.project_id:
                project_ids.append(task.project_id.id)
                projects.append(task.project_id)
            data.append({
                'id': task.id,
                'text': task.name,
                'start_date': task.start_date,
                'duration': task.duration,
                'progress': round(task.progress/100,2),
                'open': True,
                'parent': -task.project_id.id if task.project_id else False,
                'color': switch_color[task.project_id.color] if task.project_id.color else switch_color[4]
            })

        for project in projects:
            data.append({
                'id': -project.id,
                'text': project.name,
                'start_date': project.start_date,
                'duration': project.duration,
                'progress': 0,
                'open': True,
                'color': switch_color[project.color] if project.color else switch_color[4]
            })

        link_ids = self.env['gantt.link'].sudo().search(['|', '|', '|', ('source_project_id', 'in', project_ids),
            ('source_task_id', 'in', tasks.ids), ('destination_project_id', 'in', project_ids), ('destination_task_id', 'in', tasks.ids)])

        for link in link_ids:
            if link.source_project_id:
                source_id = -link.source_project_id.id
            else:
                source_id = link.source_task_id.id
            if link.destination_project_id:
                destination_id = -link.destination_project_id.id
            else:
                destination_id = link.destination_task_id.id
            links.append({'id': int(link.gantt_id), 'source': source_id, 'target': destination_id, 'type': link.type})

        return {'data': data, 'links': links}

    @api.model
    def update_task(self, task):
        if task['id'] > 0:
            to_update = self.env['project.task'].sudo().browse(task['id'])
        else:
            to_update = self.env['project.project'].sudo().browse(-task['id'])
        self.clean_dates(task)
        print(task)
        to_update.write({
            'name': task['text'],
            'duration': task['duration'],
            'start_date': task['start_date'],
            'end_date': task['end_date'],
            'open': task['open'],
            'parent': task['parent']
        })
        return True

    @api.model
    def create_task(self, task):
        self.clean_dates(task)
        print(task)
        vals = {
            'name': task['text'],
            'duration': task['duration'],
            'start_date': task['start_date'],
            'end_date': task['end_date'],
            'parent': task['parent']
        }
        if task['parent'] != 0:
            vals['project_id'] = abs(int(task['parent']))
            to_create = self.env['project.task'].sudo().create(vals)
            return to_create.id
        else:
            to_create = self.env['project.project'].sudo().create(vals)
            return -to_create.id

    @api.model
    def delete_task(self, task_id):
        if task_id < 0:
            da_eliminare = self.env['project.project'].sudo().browse(-task_id)
        else:
            da_eliminare = self.env['project.task'].sudo().browse(task_id)
        if da_eliminare.exists():
            da_eliminare.unlink()

        return True

    @api.model
    def create_link(self, link):
        link['source'] = int(link['source'])
        link['target'] = int(link['target'])
        vals = {
            'source_project_id': -link['source'] if link['source'] < 0 else 0,
            'source_task_id': link['source'] if link['source'] > 0 else 0,
            'destination_project_id': -link['target'] if link['target'] < 0 else 0,
            'destination_task_id': link['target'] if link['target'] > 0 else 0,
            'type': link['type'],
            'gantt_id': str(link['id'])
        }
        self.env['gantt.link'].sudo().create(vals)
        return True

    @api.model
    def update_link(self, link):
        link['source'] = int(link['source'])
        link['target'] = int(link['target'])
        to_update = self.env['gantt.link'].sudo().seach([('gantt_id', '=', str(link['id']))])
        vals = {
            'source_project_id': -link['source'] if link['source'] < 0 else 0,
            'source_task_id': link['source'] if link['source'] > 0 else 0,
            'destination_project_id': -link['target'] if link['target'] < 0 else 0,
            'destination_task_id': link['target'] if link['target'] > 0 else 0,
            'type': link['type'],
            'gantt_id': str(link['id'])
        }
        if to_update:
            to_update.write(vals)
        return True

    @api.model
    def delete_link(self, link_id):

        da_eliminare = self.env['gantt.link'].sudo().search([('gantt_id', '=', str(link_id))])
        if da_eliminare:
            da_eliminare.unlink()
        return True

    def clean_dates(self, task):
        """
        pulisce le date di una task con il fuso orario e il formato giusto in modo che vengano accettate dall'ORM di odoo
        :param task:
        :return:
        """
        user_tz = self.env.user.tz or pytz.utc
        if len(task['start_date']) > 16:
            task['start_date'] = datetime.datetime.strptime(
                task['start_date'][:-8], "%Y-%m-%dT%H:%M").astimezone(pytz.timezone(user_tz)).strftime('%Y-%m-%d %H:%M')
        if len(task['end_date']) > 16:
            task['end_date'] = datetime.datetime.strptime(
                task['end_date'][:-8], "%Y-%m-%dT%H:%M").strftime('%Y-%m-%d %H:%M')