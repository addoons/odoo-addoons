from odoo import models,api,fields,_

class PartnerInherit(models.Model):

    _inherit = 'res.partner'

    ore_sviluppo_disponibili = fields.Float(string='ore', compute='_get_ore_sviluppo_disponibili')
    ore_formazione_consulenza_disponibili = fields.Float(compute='_get_ore_formazione_disponibili')

    def _get_ore_formazione_disponibili(self):
        for record in self:
            if record.parent_id:
                #conto le ore assegnate alla compagnia
                company = record.parent_id
            else:
                company = record

            ore_task = 0
            ore_pacchetti = 0
            tasks = self.env['project.task'].search([('partner_id', '=', company.id)])
            pacchetti_ore = self.env['pacchetti.ore'].search([('partner_id', '=', company.id), ('type', '=', 'training')])

            for task in tasks:
                for ore in task.ore_lines:
                    if ore.type == 'training':
                        ore_task += ore.requested_hours
            for pacchetto in pacchetti_ore:
                ore_pacchetti += pacchetto.hours

            #conto le ore assegnate ai figli della compagnia cioe ai contact
            for worker in company.child_ids:
                tasks = self.env['project.task'].search([('partner_id', '=', worker.id)])
                pacchetti_ore =self.env['pacchetti.ore'].search([('partner_id', '=', worker.id), ('type', '=', 'training')])

                for task in tasks:
                    for ore in task.ore_lines:
                        if ore.type=='training':
                            ore_task += ore.requested_hours

                for pacchetto in pacchetti_ore:
                    ore_pacchetti += pacchetto.hours
            record.ore_formazione_consulenza_disponibili = ore_pacchetti - ore_task



    def _get_ore_sviluppo_disponibili(self):
        for record in self:
            if record.parent_id:
                company = record.parent_id
            else:
                company = record

            ore_task = 0
            ore_pacchetti = 0
            tasks = self.env['project.task'].search([('partner_id', '=', company.id)])
            pacchetti_ore = self.env['pacchetti.ore'].search(
                [('partner_id', '=', company.id), ('type', '=', 'developing')])
            # conto le ore assegnate alla compagnia
            for task in tasks:
                for ore in task.ore_lines:
                    if ore.type == 'developing':
                        ore_task += ore.requested_hours
            for pacchetto in pacchetti_ore:
                ore_pacchetti += pacchetto.hours

            # conto le ore assegnate ai figli della compagnia cioe ai contact
            for worker in company.child_ids:
                tasks = self.env['project.task'].search([('partner_id', '=', worker.id)])
                pacchetti_ore = self.env['pacchetti.ore'].search(
                    [('partner_id', '=', worker.id), ('type', '=', 'developing')])

                for task in tasks:
                    for ore in task.ore_lines:
                        if ore.type == 'developing':
                            ore_task += ore.requested_hours

                for pacchetto in pacchetti_ore:
                    ore_pacchetti += pacchetto.hours
            record.ore_sviluppo_disponibili = ore_pacchetti - ore_task
    def addoons_action_view_ore_dev(self):
        return {
            'name': _('Ore sviluppo'),
            # 'view_type': 'tree',
            'view_mode': 'tree',
            'res_model': 'pacchetti.ore',
            'context': {'search_default_partner_id': self.id,
                        'search_default_type': 'developing'},
            'type': 'ir.actions.act_window',
            'target': 'current',
        }

    def addoons_action_view_ore_training(self):
        return {
            'name': _('Ore formazione/consulenza'),
            # 'view_type': 'tree',
            'view_mode': 'tree',
            'res_model': 'pacchetti.ore',
            'context': {'search_default_partner_id': self.id,
                        'search_default_type': 'training'},
            'type': 'ir.actions.act_window',
            'target': 'current',
        }