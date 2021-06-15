from odoo import models, fields, api, _
from odoo.exceptions import UserError


class InvoiceNotaCredito(models.TransientModel):
    _name = 'invoice.nota.credito'

    nc_type = fields.Selection([('select_lines', 'Seleziona Righe'), ('all_lines', 'Tutte le righe')])
    invoice_line_ids = fields.Many2many('account.invoice.line')

    @api.onchange('nc_type')
    def onchange_adv(self):

        lines = []
        partners = []
        amount_computed = 0.0

        context = dict(self._context or {})
        active_ids = context.get('active_ids', []) or []
        for invoice in self.env['account.invoice'].browse(active_ids):
            if invoice.partner_id.id not in partners:
                partners.append(invoice.partner_id.id)
            for line in invoice.invoice_line_ids:
                lines.append((4, line.id))
                amount_computed += line.price_subtotal
            self.amount = amount_computed
        if len(partners) > 1:
            raise UserError('Fatture Appartenenti a clienti diversi')
        self.invoice_line_ids = lines

    @api.multi
    def crea_note_credito(self):
        lines = []
        partners = []
        amount_computed = 0.0
        tipo_documento = self.env.ref('l10n_it_fatturapa.fatturapa_TD04')
        context = dict(self._context or {})
        active_ids = context.get('active_ids', []) or []
        if(self.nc_type == 'all_lines'):
            for invoice in self.env['account.invoice'].browse(active_ids):
                if invoice.partner_id.id not in partners:
                    partners.append(invoice.partner_id.id)
                for line in invoice.invoice_line_ids:
                    taxes = []
                    for tax in line.invoice_line_tax_ids:
                        taxes.append((4, tax.id))
                    lines.append((0, 0, {'uom_id': line.uom_id.id, 'product_id': line.product_id.id, 'account_id': line.account_id.id,
                                         'price_unit': line.price_unit, 'price_subtotal': line.price_subtotal,
                                         'price_subtotal_signed': -line.price_subtotal_signed, 'quantity': line.quantity,
                                         'company_id': line.company_id.id, 'partner_id': partners[0], 'currency_id': line.currency_id.id,
                                         'is_rounding_line': line.is_rounding_line, 'name': line.name, 'invoice_line_tax_ids': taxes
                                         }))
                    amount_computed += line.price_subtotal
        else:
            for invoice in self.env['account.invoice'].browse(active_ids):
                if invoice.partner_id.id not in partners:
                    partners.append(invoice.partner_id.id)
            for line in self.invoice_line_ids:
                taxes = []
                for tax in line.invoice_line_tax_ids:
                    taxes.append((4, tax.id))
                lines.append((0, 0, {'uom_id': line.uom_id.id, 'product_id': line.product_id.id, 'account_id': line.account_id.id,
                                         'price_unit': line.price_unit, 'price_subtotal': line.price_subtotal,
                                         'price_subtotal_signed': -line.price_subtotal_signed, 'quantity': line.quantity,
                                         'company_id': line.company_id.id, 'partner_id': partners[0], 'currency_id': line.currency_id.id,
                                         'is_rounding_line': line.is_rounding_line, 'name': line.name, 'invoice_line_tax_ids': taxes
                                         }))

        self.env['account.invoice'].create({'partner_id': partners[0], 'invoice_line_ids': lines, 'fiscal_document_type_id': tipo_documento.id, 'type': 'out_refund'})
