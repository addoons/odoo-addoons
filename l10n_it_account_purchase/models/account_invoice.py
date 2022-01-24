from odoo import api, models, fields
from odoo.exceptions import UserError


class AccountInvoicePurchaseLine(models.Model):
    _inherit = 'account.invoice.line'

    purchase_order_association_id = fields.Many2one('purchase.order')


class AccountInvoicePurchase(models.Model):
    _inherit = 'account.invoice'

    differenza_ordini = fields.Float(compute="compute_differenza_ordini", store=True,
                                     help="Calcola la differenza tra il totale delle righe di fattura e il totale delle righe degli ordini di acquisto collegati."
                                          "Se = 0, la fattura combacia, se < 0 significa che non sono state fatturate tutte le righe di acquisto o tutte le quantità,"
                                          "se > 0 significa che il totale della fattura è maggiore di quello dell'ordine.")
    purchase_order_id = fields.Many2one('purchase.order')

    def compute_differenza_ordini(self):
        for invoice in self:
            if invoice.type == 'in_invoice':
                diff_ordini = 0
                list_ordini = []
                tot_ordini_acquisto_selezionato = invoice.purchase_order_id.amount_total
                tot_righe_fattura = 0
                # per ogni riga di fattura:
                # - se l'ordine di acquisto collegato non è stato considerato: somma il suo totale
                # - sottrae al calcolo della differenza ogni totale di riga
                for line in invoice.invoice_line_ids:
                    if line.purchase_order_association_id:
                        if line.purchase_order_association_id.id == invoice.purchase_order_id.id:
                            if line.purchase_order_association_id.id not in list_ordini:
                                list_ordini.append(line.purchase_order_association_id.id)
                                diff_ordini += line.purchase_order_association_id.amount_total
                            diff_ordini -= line.price_total
                            tot_righe_fattura += line.price_total
                tot_righe_fattura_current_invoice = tot_righe_fattura

                # cerca altre righe associate a quest'ordine di fatture diverse
                invoice_line_ids_same_order = self.env['account.invoice.line'].search([('purchase_order_association_id', '=', self.purchase_order_id.id), ('invoice_id', '!=', invoice.id)])
                invoice_list = []

                for invoice_line in invoice_line_ids_same_order:
                    if not invoice_line.invoice_id in invoice_list:
                        invoice_list.append(invoice_line.invoice_id)
                    diff_ordini -= invoice_line.price_total
                    tot_righe_fattura += invoice_line.price_total

                for other_invoice in invoice_list:
                    other_invoice.differenza_ordini -= tot_righe_fattura_current_invoice

                # se la somma delle righe di fattura è maggiore del totale dell'ordine
                # non è possibile associarle
                if tot_ordini_acquisto_selezionato < tot_righe_fattura and tot_ordini_acquisto_selezionato > 0:
                    raise UserError(
                        "ATTENZIONE: l'ordine di acquisto selezionato ha un importo MINORE della somma delle righe selezionate.")
                if len(list_ordini) > 0:
                    invoice.differenza_ordini += diff_ordini
                else:
                    invoice.differenza_ordini = 0
            else:
                invoice.differenza_ordini = 0

    @api.one
    @api.depends('invoice_line_ids.price_subtotal', 'tax_line_ids.amount', 'tax_line_ids.amount_rounding',
                 'currency_id', 'company_id', 'date_invoice', 'type', 'date', 'invoice_line_ids.purchase_id')
    def _compute_amount(self):
        super(AccountInvoicePurchase, self)._compute_amount()

    def apply_partner_account(self):
        if self.partner_id:
            order_name_list = ""
            for l in self.invoice_line_ids:
                if l.selected and (not self.row_description or self.row_description in l.name):
                    if self.am_account_id:
                        l.account_id = self.am_account_id.id
                    if self.am_analytic_account:
                        l.account_analytic_id = self.am_analytic_account.id
                    if self.am_tax_id:
                        l.invoice_line_tax_ids = [(5,0), (4, self.am_tax_id.id)]
                    if self.am_rda:
                        l.invoice_line_tax_wt_ids = [(5,0), (4, self.am_rda.id)]
                    if self.am_rc != l.rc:
                        l.rc = self.am_rc
                    if self.purchase_order_id and self.purchase_order_id.state == 'purchase':
                        # associa l'ordine di acquisto ad ogni riga selezionata
                        l.purchase_order_association_id = self.purchase_order_id.id

                if l.purchase_order_association_id:
                    if not l.purchase_order_association_id.name in order_name_list:
                        order_name_list += l.purchase_order_association_id.name + ', '
                l.selected = False
            order_name_list = order_name_list[:-2]
            self.origin = order_name_list
            self.compute_taxes()
            #self._onchange_invoice_line_wt_ids()
            self.compute_differenza_ordini()

    def delete_purchase_order_association(self):
        """
        Cancella l'associazione di tutte le righe legate all'ordine di acquisto selezionato
        Ricalcola la differenza ordine
        """
        if self.partner_id:
            amount_to_exclude = 0
            amount_to_exclude_other_invoice = 0
            for l in self.invoice_line_ids:
                if l.purchase_order_association_id.id == self.purchase_order_id.id:
                    amount_to_exclude += l.price_total
                    l.purchase_order_association_id = False

            invoice_line_ids_same_order = self.env['account.invoice.line'].search(
                [('purchase_order_association_id', '=', self.purchase_order_id.id), ('invoice_id', '!=', self.id)])
            invoice_list = []

            for invoice_line in invoice_line_ids_same_order:
                if not invoice_line.invoice_id in invoice_list:
                    invoice_list.append(invoice_line.invoice_id)
                amount_to_exclude_other_invoice += invoice_line.price_total

            self.differenza_ordini -= self.purchase_order_id.amount_total + amount_to_exclude + amount_to_exclude_other_invoice

            for other_invoice in invoice_list:
                other_invoice.differenza_ordini += amount_to_exclude

