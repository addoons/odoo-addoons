from odoo import models,api,fields, _
import datetime


class taskOreInherit(models.Model):

    _inherit = 'project.task'

    # CAMPI VISTA GANTT
    duration = fields.Float(default=3)
    start_date = fields.Datetime(default=datetime.datetime.now())
    end_date = fields.Datetime(default=datetime.datetime.now()+datetime.timedelta(days=3))
    open = fields.Boolean(default=True)
    parent = fields.Integer(compute='_compute_parent', store=True)




