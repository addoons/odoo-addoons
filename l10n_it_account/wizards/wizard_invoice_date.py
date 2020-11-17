from odoo import api, fields, models,_


class WizardInvoiceDate(models.TransientModel):
    """
    Assegna la data a tutti i documenti fiscali selezionati
    """
    _name = 'wizard.invoice.date'

    date_invoice = fields.Date()

    def set_invoice_date(self):
        for invoice in self._context['active_ids']:
            invoice = self.env['account.invoice'].search([('id', '=', invoice)])
            invoice.write({'date_invoice': self.date_invoice})
