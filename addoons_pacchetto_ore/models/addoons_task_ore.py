import logging

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

        task = self.env['project.task'].browse(self.id)
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

    """
    Va ad assegnare la riga di lavoro di una task 
    al primo pacchetto ore disponibile(pacchetto con data di creazione più vecchia e che ha ancora ore disponibili).
    Le ore disponibili del pacchetto vengono scalate in base all somma delle ore di lavoro assegnate al quel pacchetto
    """
    def write(self, vals):
        super(taskOreInherit, self).write(vals)

        for type in ['developing', 'training']:
            new_lines = []
            ore_nuovo_pacchetto = 0
            data_pacchetto = False
            for line in self.timesheet_ids:
                if not line.pacchetto_ore_id and line.type == type:
                    if not self.partner_id.parent_id:
                        cliente = self.partner_id.id
                    else:
                        cliente = self.partner_id.parent_id.id

                    pacchetto_valido = self.env['pacchetti.ore'].search([('type', '=', line.type), ('ore_residue', '>', 0),
                                         ('partner_id', '=', cliente)], order='create_date asc', limit=1)
                    if pacchetto_valido:

                        if pacchetto_valido.ore_residue - line.unit_amount >= 0:

                            # se con il pacchetto trovato riesco coprire tutte le ore della riga le assegno al pacchetto.
                            pacchetto_valido.write({'ore_lines': [(4, line.id)]})
                            line.pacchetto_ore_id = pacchetto_valido.id
                        else:
                            # Le ore del pacchetto non bastano quindi faccio uno split.
                            # Alla riga corrente assegnamo le ore disponibili del pacchetto
                            differenza_ore = line.unit_amount - pacchetto_valido.ore_residue

                            if not data_pacchetto:
                                # modifico la riga inserendo le ore residue del pacchetto
                                line.unit_amount = pacchetto_valido.ore_residue
                                pacchetto_valido.write({'ore_lines': [(4, line.id)]})
                                line.pacchetto_ore_id = pacchetto_valido.id

                            # cerco altri pacchetti disponibili e assegno le ore rimaste a questi creando nuove righe
                            while pacchetto_valido and differenza_ore > 0:
                                pacchetto_valido = self.env['pacchetti.ore'].search(
                                    [('type', '=', line.type), ('ore_residue', '>', 0),
                                     ('partner_id', '=', cliente)], order='create_date asc', limit=1)
                                if pacchetto_valido:
                                    vals_nuova_riga = {
                                        'date': line.date,
                                        'employee_id': line.employee_id.id,
                                        'name': line.name,
                                        'type': line.type,
                                        'pacchetto_ore_id': pacchetto_valido.id,
                                        'unit_amount': 0,
                                        'account_id': line.account_id.id
                                    }
                                    if pacchetto_valido.ore_residue > differenza_ore :
                                        vals_nuova_riga['unit_amount'] = differenza_ore
                                        differenza_ore = 0
                                    else:
                                        vals_nuova_riga['unit_amount'] = pacchetto_valido.ore_residue
                                        differenza_ore -= pacchetto_valido.ore_residue

                                    nuova_riga = self.env['account.analytic.line'].create(vals_nuova_riga)
                                    pacchetto_valido.write({'ore_lines': [(4, nuova_riga.id)]})
                                    super(taskOreInherit, self).write({'timesheet_ids': [(4, nuova_riga.id)]})

                            # se ci sono ancora ore rimaste da assegnare ad un pacchetto ma non ce ne sono più disponibili,
                            # si crea un nuovo pacchetto
                            if differenza_ore > 0:
                                ore_nuovo_pacchetto += differenza_ore
                                data_pacchetto = {
                                    'name': 'pacchetto aggiuntivo ' + datetime.today().date().strftime("%d/%m/%Y"),
                                    'type': pacchetto_valido.type,
                                    'hours': 0,
                                    'partner_id': cliente
                                }
                                new_lines.append({
                                    'date': line.date,
                                    'employee_id': line.employee_id.id,
                                    'name': line.name,
                                    'type': line.type,
                                    'pacchetto_ore_id': 0,
                                    'unit_amount': differenza_ore,
                                    'account_id': line.account_id.id
                                })
                    else:
                        ore_nuovo_pacchetto += line.unit_amount
                        if not data_pacchetto:
                            data_pacchetto = {
                                'name': self.partner_id.name + ' pacchetto aggiuntivo ' + datetime.today().date().strftime(
                                    "%d/%m/%Y"),
                                'type': type,
                                'hours': 0,
                                'partner_id': cliente
                            }

            if data_pacchetto:
                # devo creare un nuovo pacchetto e le relative righe
                data_pacchetto['hours'] = ore_nuovo_pacchetto
                nuovo_pacchetto = self.env['pacchetti.ore'].create(data_pacchetto)
                for line in new_lines:
                    line['pacchetto_ore_id'] = nuovo_pacchetto.id
                    id = self.env['account.analytic.line'].create(line).id
                    nuovo_pacchetto.write({'ore_lines': [(4, id)]})
                    super(taskOreInherit, self).write({'timesheet_ids': [(4, id)]})
                for line in self.timesheet_ids:
                    if not line.pacchetto_ore_id and line.type == type:
                        line.pacchetto_ore_id = nuovo_pacchetto.id
                        nuovo_pacchetto.write({'ore_lines': [(4, line.id)]})

