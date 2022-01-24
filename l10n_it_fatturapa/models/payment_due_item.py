from odoo import models, fields, api

class PaymentDueItem(models.Model):
    _name = 'payment.due.item'
    _description = "modello contentente le righe di scadenza delle fatture in" \
                   "base ai termini di pagamento scelti"

    date = fields.Date()
    amount = fields.Float()
    fatturapa_payment_method_id = fields.Many2one('fatturapa.payment_method')
    account_move_line_id = fields.Many2one('account.move.line')
    invoice_id = fields.Many2one('account.invoice')






