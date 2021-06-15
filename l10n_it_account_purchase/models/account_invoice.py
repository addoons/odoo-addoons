from odoo import api, models, fields


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
                # per ogni riga di fattura:
                # - se l'ordine di acquisto collegato non è stato considerato: sottrae il suo totale
                # - somma al calcolo della differenza ogni totale di riga
                for line in invoice.invoice_line_ids:
                    if line.purchase_id and line.purchase_id.id not in list_ordini:
                        list_ordini.append(line.purchase_id.id)
                        diff_ordini -= line.purchase_id.amount_total
                    if line.purchase_id:
                        diff_ordini += line.price_total

                # caso di più fatture di un singolo ordine
                if invoice.origin and invoice.id:
                    origin_elements = invoice.origin.split(',')
                    invoice_ids = self.env['account.invoice'].search([('type', '=', 'in_invoice'),('origin', 'in', origin_elements), ('id', '!=',invoice.id)])
                    # se ci sono più fatture legate ad uno stesso ordine bisogna comprendere
                    # tutti i totali nel calcolo della differenza
                    for element in invoice_ids:
                        diff_ordini += element.amount_total
                    # aggiorna la differenza ordini anche sulle altre fatture legate allo stesso ordine di acquisto
                    for element in invoice_ids:
                        element.differenza_ordini = diff_ordini
                if len(list_ordini) > 0:
                    invoice.differenza_ordini = diff_ordini
                else:
                    invoice.differenza_ordini = 0
            else:
                invoice.differenza_ordini = 0

    @api.one
    @api.depends('invoice_line_ids.price_subtotal', 'tax_line_ids.amount', 'tax_line_ids.amount_rounding',
                 'currency_id', 'company_id', 'date_invoice', 'type', 'date', 'invoice_line_ids.purchase_id')
    def _compute_amount(self):
        super(AccountInvoicePurchase, self)._compute_amount()
        self.compute_differenza_ordini()

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
                        if not l.purchase_line_id:
                            # cerca la riga nell'ordine di acquisto selezionato per effettuare il legame
                            # se il nome o il codice del prodotto sono nella riga di fattura faccio il match
                            for purchase_line in self.purchase_order_id.order_line:
                                if l.name and (purchase_line.product_id.name.lower() in l.name.lower()
                                or (purchase_line.product_id.default_code and purchase_line.product_id.default_code.lower() in l.name.lower())):
                                    l.purchase_line_id = purchase_line.id
                if l.purchase_line_id and l.purchase_id:
                    if not l.purchase_id.name in order_name_list:
                        order_name_list += l.purchase_id.name + ', '
                l.selected = False
            order_name_list = order_name_list[:-2]
            self.origin = order_name_list
            self.compute_taxes()
            self._onchange_invoice_line_wt_ids()
            self.compute_differenza_ordini()