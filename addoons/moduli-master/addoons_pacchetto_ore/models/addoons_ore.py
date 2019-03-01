from odoo import models,api,fields, _
from datetime import datetime
from odoo.exceptions import ValidationError

class pacchettoOre(models.Model):
    _name = 'pacchetti.ore'
    partner_id = fields.Many2one('res.partner')
    description = fields.Text()
    start_date = fields.Date()
    end_date = fields.Date()
    hours = fields.Float()
    type = fields.Selection([
        ('developing', 'Sviluppo'),
        ('training', 'Formazione/consulenza')
    ])
