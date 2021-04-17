from odoo import models, fields, api, _

class GanttLink(models.Model):

    _name = 'gantt.link'

    gantt_id = fields.Char()
    source_project_id = fields.Many2one('project.project')
    destination_project_id = fields.Many2one('project.project')
    source_task_id = fields.Many2one('project.task')
    destination_task_id = fields.Many2one('project.task')
    type = fields.Char()

