from odoo import models, api, fields


class WizardFillInvoiceSequence(models.TransientModel):
    _name = 'wizard.fill.invoice.sequence'

    current_invoice = fields.Many2one('account.invoice')
    invoice_not_validated_with_sequence = fields.Many2one('account.invoice')
    sequence_to_fill = fields.Char()



    def fill_invoice_sequence(self):
        """
        La funzione assegna alla fattura corrente:
        - data fattura
        - numero
        - registrazione contabile (se presente)
        dalla fattura che ha causato il buco e resetta quest'ultima in bozza
        senza riferimenti a registrazioni e sequenze
        """
        self.current_invoice.journal_id.sequence_number_next -= 1
        if self.invoice_not_validated_with_sequence.move_id:
            move_id = self.invoice_not_validated_with_sequence.move_id
        else:
            self.current_invoice.move_id.ref = self.invoice_not_validated_with_sequence.reference
            self.current_invoice.move_id.name = self.sequence_to_fill
            move_id = self.current_invoice.move_id
        self.current_invoice.write({
            'date_invoice': self.invoice_not_validated_with_sequence.date_invoice,
            'number': self.sequence_to_fill,
            'reference': self.invoice_not_validated_with_sequence.reference,
            'move_id': move_id.id,
            'move_name': move_id.name,
        })
        self.invoice_not_validated_with_sequence.write({
            'date_invoice': False,
            'reference': False,
            'move_id': False,
            'move_name': False,
            'date': False,
            'state': 'draft',
        })
