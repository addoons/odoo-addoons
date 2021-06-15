from odoo import api, models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    @api.multi
    def set_values(self):
        super(ResConfigSettings, self).set_values()

        # In base al modello documento selezionato nelle impostazioni
        # vengono cambiati i report base chiamati nei moduli
        # Fatturazione, Vendite e Acquisti

        if self.external_report_layout_id.name == 'addoons_reports_external_layout':

            try:
                # Imposto il report personalizzato nel modulo Vendite
                report_sale = self.env.ref('sale.action_report_saleorder')
                report_addoons_sale = self.env.ref('addoons_reports_sale.report_layout_sale_orders')
                report_sale.report_name = 'addoons_reports_sale.report_layout_sale'
            except:
                pass

            try:
                # Imposto il report personalizzato nel modulo Fatturazione
                report_invoice = self.env.ref('account.account_invoices')
                report_addoons_invoice = self.env.ref('addoons_reports_invoice.report_layout_invoice_orders')
                report_invoice.report_name = 'addoons_reports_invoice.report_layout_invoice_orders'
            except:
                pass

            try:
                # Imposto il report personalizzato nel modulo Acquisti
                report_purchase = self.env.ref('purchase.action_report_purchase_order')
                report_addoons_purchase = self.env.ref('addoons_reports_purchase.report_layout_purchase_orders')
                report_purchase.report_name = 'addoons_reports_purchase.report_layout_purchase_orders'
            except:
                pass
        else:

            try:
                # Imposto il report di default nel modulo Vendite
                report_sale = self.env.ref('sale.action_report_saleorder')
                report_sale.paperformat_id = False
                report_sale.report_name = 'sale.report_saleorder'
            except:
                pass

            try:
                # Imposto il report di default nel modulo Fatturazione
                report_invoice = self.env.ref('account.account_invoices')
                report_invoice.paperformat_id = False
                report_invoice.report_name = 'account.report_invoice_with_payments'
            except:
                pass

            try:
                # Imposto il report di default nel modulo Acquisti
                report_purchase = self.env.ref('purchase.action_report_purchase_order')
                report_purchase.paperformat_id = False
                report_purchase.report_name = 'purchase.report_purchaseorder'
            except:
                pass
