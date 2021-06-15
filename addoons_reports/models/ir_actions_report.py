from odoo import api, models, fields


class IrActionsReport(models.Model):
    _inherit = 'ir.actions.report'

    @api.multi
    def write(self, vals):

        if 'report_name' in vals.keys():
            document_model_id = self.env['res.config.settings'].search([], limit=1)

            if document_model_id.external_report_layout_id.name == 'addoons_reports_external_layout':

                # Prendo il paper format
                paper_format = self.env.ref('addoons_reports.addoons_reports_a4_portrait')

                try:
                    # Imposto il report personalizzato nel modulo Vendite
                    report_sale = self.env.ref('sale.action_report_saleorder')
                    report_addoons_sale = self.env.ref('addoons_reports_sale.report_layout_sale_orders')
                    if report_sale.id == self.id:
                        report_sale.paperformat_id = paper_format.id
                        vals['report_name'] = 'addoons_reports_sale.report_layout_sale_orders'
                except:
                    pass

                try:
                    # Imposto il report personalizzato nel modulo Fatturazione
                    report_invoice = self.env.ref('account.account_invoices')
                    report_addoons_invoice = self.env.ref('addoons_reports_invoice.report_layout_invoice_orders')
                    if report_invoice.id == self.id:
                        report_invoice.paperformat_id = paper_format.id
                        vals['report_name'] = 'addoons_reports_invoice.report_layout_invoice_orders'
                except:
                    pass

                try:
                    # Imposto il report personalizzato nel modulo Acquisti
                    report_purchase = self.env.ref('purchase.action_report_purchase_order')
                    report_addoons_purchase = self.env.ref('addoons_reports_purchase.report_layout_purchase_orders')
                    if report_purchase.id == self.id:
                        report_purchase.paperformat_id = paper_format.id
                        vals['report_name'] = 'addoons_reports_purchase.report_layout_purchase_orders'
                except:
                    pass

        res = super(IrActionsReport, self).write(vals)
        return res
