from odoo import models,api,fields,_

class PartnerInherit(models.Model):

    _inherit = 'res.partner'

    ore_sviluppo_disponibili = fields.Float(string='ore', compute='_get_ore_sviluppo_disponibili')
    ore_formazione_consulenza_disponibili = fields.Float(compute='_get_ore_formazione_disponibili')
    soglia_notifica_ore = fields.Float(default=10)

    def _get_ore_formazione_disponibili(self):
        for record in self:
            if record.parent_id:
                #conto le ore assegnate alla compagnia
                company = record.parent_id
            else:
                company = record
            ore_disponibili = 0

            pacchetti_ore = self.env['pacchetti.ore'].search([('partner_id', '=', company.id),
                                                              ('type', '=', 'training'), ('ore_residue', '>', 0)])

            for pacchetto in pacchetti_ore:
                ore_disponibili += pacchetto.ore_residue

            record.ore_formazione_consulenza_disponibili = ore_disponibili

    def _get_ore_sviluppo_disponibili(self):
        for record in self:
            if record.parent_id:
                company = record.parent_id
            else:
                company = record

            ore_disponibili = 0

            pacchetti_ore = self.env['pacchetti.ore'].search(
                [('partner_id', '=', company.id), ('type', '=', 'developing')])

            for pacchetto in pacchetti_ore:
                ore_disponibili += pacchetto.ore_residue

            record.ore_sviluppo_disponibili = ore_disponibili

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