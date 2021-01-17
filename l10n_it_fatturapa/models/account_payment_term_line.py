from odoo import models, fields, api

class AccountPaymentTermLine(models.Model):
    _inherit = 'account.payment.term.line'

    fatturapa_payment_method_id = fields.Many2one('fatturapa.payment_method')