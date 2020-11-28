from odoo import models, fields, api
from itertools import groupby

# class AlphaResCompany(models.Model):
#     _inherit = 'res.company'
#
#     external_report_layout_id = fields.Selection(selection_add=[('addoons', 'Addoons')])


class AddoonsReportSaleOrder(models.Model):
    _inherit = 'sale.order'

    extra_product_ids = fields.One2many('extra.product.line', 'order_id')
    contratto_sviluppo = fields.Boolean()
    contratto_licenza = fields.Boolean(default=True)
    full_description = fields.Html()

    def check_description(self):
        if self.full_description:
            if len(self.full_description) > 35:
                return True
        return False

    @api.multi
    def order_lines_layouted(self):
        self.ensure_one()
        report_pages = [[]]
        for periodo, lines in groupby(self.order_line, lambda l: l.periodo):
            report_pages[-1].append({
                'name': periodo or 'Uncategorized',
                'lines': list(lines)
            })
        return report_pages

    def get_amount_by_tax(self):
        """
        Calcolo il totale per ogni imposta
        """
        result = {}
        for line in self.order_line:
            if not line.display_type:
                if len(line.tax_id) > 0 and line.tax_id[0].description not in result.keys():
                    result[line.tax_id[0].description] = {
                        'nome': line.tax_id[0].name,
                        'etichetta': line.tax_id[0].description,
                        'totale': 0,
                    }
                if len(line.tax_id) > 0 and line.tax_id[0].description in result.keys():
                    result[line.tax_id[0].description]['totale'] += line.price_tax

        return result


class AddoonsReportSaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    description_line = fields.Html()
    deadline = fields.Date()

    # questa e' molto brutto nel valore interno non si mette la stringa con gli spazi. era stata fatta tempo fa perche'
    # non si riusciva a prendere il valore stringa in python
    periodo = fields.Selection([('Una Tantum', 'Una Tantum'), ('Giornaliero', 'Giornaliero'), ('Mensile', 'Mensile'), ('Annuale', 'Annuale'), ('Annuale Odoo', 'Annuale Odoo')])

    def check_description(self):
        if self.description_line:
            if len(self.description_line) > 15:
                return True
        return False

    def open_line(self):
        return {
            'name': 'Riga Preventivo/Ordine',
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': self.env.ref('addoons_report_template.addoons_sale_line_view').id,
            'res_model': 'sale.order.line',
            'type': 'ir.actions.act_window',
            'res_id': self.id,
            'context': self.env.context
        }




class AddoonsReportSaleOrderExtra(models.Model):
    _name = 'extra.product.line'

    order_id = fields.Many2one('sale.order')
    product_id = fields.Many2one('product.product')
    description = fields.Text()
    qty = fields.Integer()
    unit_price = fields.Float()
    discount = fields.Float()
    total = fields.Float(compute='get_total')
    sequence = fields.Integer()
    product_uom = fields.Many2one('product.uom')

    @api.onchange('product_id')
    def onchange_product(self):
        self.unit_price = self.product_id.lst_price

    @api.multi
    @api.depends('discount', 'unit_price', 'qty')
    def get_total(self):
        for x in self:
            total = x.qty * x.unit_price
            total_discount = total - ((total * x.discount) / 100)
            x.total = total_discount
