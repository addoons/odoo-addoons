from odoo import models,api,fields,_

class PartnerInherit(models.Model):

    _inherit = 'res.partner'

    @api.model
    def get_ore_disponibili(self, id):

        partner = self.env['res.users'].sudo().browse(id['user_id']).partner_id
        return {"ore_sviluppo": round(partner.ore_sviluppo_disponibili,2), "ore_formazione":round(partner.ore_formazione_consulenza_disponibili,2)}