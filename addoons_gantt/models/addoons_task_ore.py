from odoo import models,api,fields, _
import datetime


class taskOreInherit(models.Model):

    _inherit = 'project.task'

    # CAMPI VISTA GANTT
    duration = fields.Float(default=3)
    start_date = fields.Datetime(default=datetime.datetime.now())
    end_date = fields.Datetime(default=datetime.datetime.now()+datetime.timedelta(days=3))
    open = fields.Boolean(default=True)
    parent = fields.Integer(compute='_compute_parent', store=True)


class ProductProduct(models.Model):

    _inherit = 'product.product'

    recalculate_stock_value_9 = fields.Integer(compute='_recompute_stock_value', store=True)

    def _recompute_stock_value(self):
        product_ids = self.search([])
        for p in product_ids:
            moves = self.env['stock.move'].search([('product_id', '=', p.id)])
            for m in moves:
                self.env['product.price.history'].create({
                    'product_id': p.id,
                    'datetime': m.date,
                    'cost': m.value
                })
            p._compute_stock_value()
            print("FATTO")

