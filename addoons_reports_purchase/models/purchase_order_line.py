from odoo import models, fields, api, _


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    def find_seller_product_code(self):
        if not self.product_id:
            return
        params = {'order_id': self.order_id}
        seller = self.product_id._select_seller(
            partner_id=self.partner_id,
            quantity=self.product_qty,
            date=self.order_id.date_order and self.order_id.date_order.date(),
            uom_id=self.product_uom,
            params=params)

        return seller.product_code
