from odoo import models,api,fields, _
from datetime import datetime
from odoo.exceptions import ValidationError

class taskPacchettoOre(models.Model):
    _name = 'task.pacchetto.ore'

    task_id = fields.Many2one('project.task')
    requested_hours = fields.Float()
    type = fields.Selection([
        ('developing', 'Sviluppo'),
        ('training', 'Formazione/consulenza')
    ])

class taskOreInherit(models.Model):

    _inherit = 'project.task'
    ore_lines = fields.One2many('task.pacchetto.ore', 'task_id')

    @api.onchange('ore_lines')
    def _onchange_ore_task(self):

        task = self.env['project.task'].browse(self.id);
        ore_task_formazione = 0
        ore_task_sviluppo = 0
        for ore in task.ore_lines:
            if ore.type == 'training':
                ore_task_formazione += ore.requested_hours
            if ore.type == 'developing':
                ore_task_sviluppo += ore.requested_hours

        ore_task_formazione_modifiche = 0
        ore_task_sviluppo_modifiche = 0
        for ore in self.ore_lines:
            if ore.type == 'training':
                ore_task_formazione_modifiche += ore.requested_hours
            if ore.type == 'developing':
                ore_task_sviluppo_modifiche += ore.requested_hours

        if self.partner_id.ore_sviluppo_disponibili + ore_task_sviluppo - ore_task_sviluppo_modifiche < 0:
            raise ValidationError(_('Non ci sono più ore di sviluppo disponibili per assegnare il task'))

        if self.partner_id.ore_formazione_consulenza_disponibili + ore_task_formazione - ore_task_formazione_modifiche < 0:
            raise ValidationError(_('Non ci sono più ore di formazione/consulenza disponibili per assegnare il task'))

    @api.onchange('partner_id')
    def _onchange_partner_id(self):


        ore_task_formazione_modifiche = 0
        ore_task_sviluppo_modifiche = 0
        for ore in self.ore_lines:
            if ore.type == 'training':
                ore_task_formazione_modifiche += ore.requested_hours
            if ore.type == 'developing':
                ore_task_sviluppo_modifiche += ore.requested_hours

        if self.partner_id.ore_sviluppo_disponibili - ore_task_sviluppo_modifiche < 0:
            raise ValidationError(_('Non ci sono più ore di sviluppo disponibili per assegnare il task'))

        if self.partner_id.ore_formazione_consulenza_disponibili - ore_task_formazione_modifiche < 0:
            raise ValidationError(_('Non ci sono più ore di formazione/consulenza disponibili per assegnare il task'))
