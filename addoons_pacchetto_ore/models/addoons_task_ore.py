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
    ore_sviluppo_disponibili = fields.Float(related='partner_id.ore_sviluppo_disponibili')
    ore_formazione_consulenza_disponibili = fields.Float(related='partner_id.ore_formazione_consulenza_disponibili')
    avviso_ore_terminate = fields.Html(compute='compute_avviso_ore_terminate')

    def compute_avviso_ore_terminate(self):
        for rec in self:
            if not self.partner_id.parent_id:
                cliente = self.partner_id
            else:
                cliente = self.partner_id.parent_id
            rec.avviso_ore_terminate = ''
            if rec.ore_sviluppo_disponibili <= cliente.soglia_ore_sviluppo:
                rec.avviso_ore_terminate += "<h1 style='color: red;'>ATTENZIONE! ORE SVILUPPO IN ESAURIMENTO o ESAURITE</h1>"

            if rec.ore_formazione_consulenza_disponibili <= cliente.soglia_ore_formazione:
                rec.avviso_ore_terminate += "<h1 style='color: red;'>ATTENZIONE! ORE FORMAZIONE IN ESAURIMENTO o ESAURITE</h1>"


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


    def write(self, vals):
        """
            Va ad assegnare la riga di lavoro di una task al primo pacchetto
            ore disponibile(pacchetto con data di creazione più vecchia e che ha ancora ore disponibili).
            Le ore disponibili del pacchetto vengono scalate in base all somma delle ore di lavoro assegnate a quel pacchetto
        """
        super(taskOreInherit, self).write(vals)

        if not self.partner_id:
            raise ValidationError(
                'Devi selezionare un cliente per salvare il record:')
        if not self.partner_id.parent_id:
            cliente = self.partner_id
        else:
            cliente = self.partner_id.parent_id
        for type in ['developing', 'training']:
            for line in self.timesheet_ids:
                if not line.pacchetto_ore_id and line.type == type:

                    pacchetto_valido = self.env['pacchetti.ore'].search([('type', '=', line.type), ('ore_residue', '>', 0),
                                         ('partner_id', '=', cliente.id)], order='create_date asc', limit=1)
                    if pacchetto_valido:

                        if pacchetto_valido.ore_residue - line.unit_amount >= 0:

                            # se con il pacchetto trovato riesco coprire tutte le ore della riga le assegno al pacchetto
                            pacchetto_valido.write({'ore_lines': [(4, line.id)]})
                            line.pacchetto_ore_id = pacchetto_valido.id
                        else:
                            # Le ore del pacchetto non bastano quindi faccio uno split.
                            # Alla riga corrente assegnamo le ore disponibili del pacchetto
                            differenza_ore = line.unit_amount - pacchetto_valido.ore_residue

                            # modifico la riga inserendo le ore residue del pacchetto
                            line.unit_amount = pacchetto_valido.ore_residue
                            pacchetto_valido.write({'ore_lines': [(4, line.id)]})
                            line.pacchetto_ore_id = pacchetto_valido.id

                            # cerco altri pacchetti disponibili e assegno le ore rimaste a questi creando nuove righe
                            while pacchetto_valido and differenza_ore > 0:
                                pacchetto_valido = self.env['pacchetti.ore'].search(
                                    [('type', '=', line.type), ('ore_residue', '>', 0),
                                     ('partner_id', '=', cliente.id)], order='create_date asc', limit=1)
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
                                    if pacchetto_valido.ore_residue > differenza_ore:
                                        vals_nuova_riga['unit_amount'] = differenza_ore
                                        differenza_ore = 0
                                    else:
                                        vals_nuova_riga['unit_amount'] = pacchetto_valido.ore_residue
                                        differenza_ore -= pacchetto_valido.ore_residue

                                    nuova_riga = self.env['account.analytic.line'].create(vals_nuova_riga)
                                    pacchetto_valido.write({'ore_lines': [(4, nuova_riga.id)]})
                                    super(taskOreInherit, self).write({'timesheet_ids': [(4, nuova_riga.id)]})

                            # rimangono delle ore da assegnare ai pacchetti ma non ci sono piu pacchetti disponibili
                            if differenza_ore > 0:
                                raise ValidationError(_('Attenzione il cliente non ha abbastanza ore disponibili'
                                                        ' per registrare le ore di lavoro.'))

                    else:
                        raise ValidationError(_('Attenzione il cliente non ha abbastanza ore disponibili'
                                                ' per registrare le ore di lavoro.'))

        for line in self.timesheet_ids:
            # assegno le ore interne al campo sul cliente (ore interne ids)
            if line.type == 'internal':
                cliente.write({'ore_interne_ids': [(4, line.id)]})

