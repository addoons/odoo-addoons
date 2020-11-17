from odoo import api, fields, models,_


class WizardInvoiceDueDate(models.TransientModel):
    """
    Assegna la data di scadenza a tutti i documenti fiscali selezionati
    """
    _name = 'wizard.invoice.due.date'

    date_due = fields.Date()

    def set_invoice_due_date(self):
        for invoice in self._context['active_ids']:
            invoice = self.env['account.invoice'].browse(invoice)
            invoice.write({'date_due': self.date_due})
