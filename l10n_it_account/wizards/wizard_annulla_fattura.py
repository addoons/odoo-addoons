from odoo import api, fields, models


class WizardInvoiceDueDate(models.TransientModel):
    """
    Annulla le fatture selezionate (se già pagate, stacca il pagamento)
    """
    _name = 'wizard.annulla.fattura'

    text = fields.Char(default="Annullare le fatture selezionate?", readonly=1)

    def annulla_fattura(self):
        for invoice in self._context['active_ids']:
            invoice = self.env['account.invoice'].browse(invoice)
            invoice.action_cancel()

