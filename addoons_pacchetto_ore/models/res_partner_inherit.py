from odoo import models,api,fields,_

class PartnerInherit(models.Model):

    _inherit = 'res.partner'

    ore_sviluppo_disponibili = fields.Float(string='ore', compute='_get_ore_sviluppo_disponibili')
    ore_formazione_consulenza_disponibili = fields.Float(compute='_get_ore_formazione_disponibili')

    soglia_ore_sviluppo = fields.Float(default=10)
    soglia_ore_formazione = fields.Float(default=10)

    notifica_sviluppo = fields.Boolean()
    notifica_formazione = fields.Boolean()

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

    def check_soglia_ore(self):
        for record in self:
            users = self.env['res.partner'].search([('email', 'in', ['f.ranieri@addoons.it', 's.sganzerla@addoons.it'])]).ids
            users.append(record.id)
            author = self.env['res.partner'].search([('email', '=', 'sales@addoons.it')]).id
            if record.ore_sviluppo_disponibili <= record.soglia_ore_sviluppo and not record.notifica_sviluppo:
                message = "Attenzione le ore SVILUPPO disponibili di %s stanno per terminare. \n" \
                          "Le ore residue sono minori di %s h"  % (record.name, record.soglia_ore_sviluppo)
                subject = "Esaurimento ore SVILUPPO %s" % record.name

                record.message_post(body=message, subject=subject, message_type='comment', subtype='mail.mt_comment',
                                    partner_ids=users, author_id=author)
                record.notifica_sviluppo = True
            if record.ore_formazione_consulenza_disponibili <= record.soglia_ore_formazione and not record.notifica_formazione:
                message = "Attenzione le ore FORMAZIONE/CONSULENZA disponibili di %s stanno per terminare. \n" \
                          "Le ore residue sono minori di %s h" % (record.name, record.soglia_ore_sviluppo)
                subject = "Esaurimento ore FORMAZIONE/CONSULENZA %s" % record.name
                record.message_post(body=message, subject=subject, message_type='comment', subtype='mail.mt_comment',
                                    partner_ids=users, author_id=author)
                record.notifica_formazione = True