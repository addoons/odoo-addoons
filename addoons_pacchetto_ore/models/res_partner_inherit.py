from odoo import models,api,fields,_

class PartnerInherit(models.Model):

    _inherit = 'res.partner'

    ore_sviluppo_disponibili = fields.Float(string='ore', compute='_get_ore_sviluppo_disponibili')
    ore_formazione_consulenza_disponibili = fields.Float(compute='_get_ore_formazione_disponibili')
    ore_interne_accumulate = fields.Float(compute='_get_ore_interne')

    soglia_ore_sviluppo = fields.Float(default=10)
    soglia_ore_formazione = fields.Float(default=10)

    notifica_sviluppo = fields.Boolean()
    notifica_formazione = fields.Boolean()

    ore_interne_ids = fields.Many2many('account.analytic.line')

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

    def _get_ore_interne(self):
        ore_interne = 0
        for record in self:
            if record.parent_id:
                company = record.parent_id
            else:
                company = record
            for ore in company.ore_interne_ids:
                if ore.type == 'internal':
                    ore_interne += ore.unit_amount
            record.ore_interne_accumulate = ore_interne

    def addoons_action_view_ore_dev(self):
        return {
            'name': _('Ore sviluppo'),
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
            'view_mode': 'tree',
            'res_model': 'pacchetti.ore',
            'context': {'search_default_partner_id': self.id,
                        'search_default_type': 'training'},
            'type': 'ir.actions.act_window',
            'target': 'current',
        }

    def addoons_action_view_ore_internal(self):
        return {
            'name': _('Ore Interne'),
            'view_mode': 'tree',
            'res_model': 'account.analytic.line',
            'domain':['|',('partner_id','=',self.id),('partner_id','in',self.child_ids.ids),('type','=','internal')],
            'type': 'ir.actions.act_window',
            'target': 'current',
        }

