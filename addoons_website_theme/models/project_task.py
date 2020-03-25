from datetime import date
import datetime
from odoo import models,api,fields,_

class projectTask(models.Model):

    _inherit = 'project.task'


    def get_data_report(self,partner_id, project_id, date_from, date_to):
        tasks = self.env['project.task'].search([('partner_id', '=', partner_id.id),('project_id', '=', int(project_id)), ('create_date', '>=', date_from),('create_date', '<=', date_to)])
        return tasks
