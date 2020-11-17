from odoo import models, fields, api

class BolletteDoganali(models.Model):
    _name = 'bollette.doganali'

    name = fields.Char()
    diritti_doganali_id = fields.Many2one('account.account')
    conto_transitorio_id = fields.Many2one('account.account')
    debiti_spese_anticipate_id = fields.Many2one('account.account')
