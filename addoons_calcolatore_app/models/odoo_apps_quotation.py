
from odoo import api, fields, models, _, http


class AppsQuotation(models.Model):

    _name = 'odoo.app.lines'

    name = fields.Char()
    monthly_price = fields.Float()
    include = fields.Boolean()


class SaleOrderInherit(models.Model):
    _inherit = "sale.order"
    odoo_app_ids = fields.Many2many('odoo.app.lines')
    users_count = fields.Integer()

    cpu = fields.Integer()
    memory = fields.Integer()
    disk = fields.Integer()
    os = fields.Char()

    def create_app_orderlines(self):
        app_count = 0
        app_total_monthly = 0
        for app in self.odoo_app_ids:
            if app.include:
                app_total_monthly += app.monthly_price
                app_count += 1

        odoo_apps_product = self.env["product.product"].search([("name", "=", "Odoo Apps")])
        if not odoo_apps_product:
            category = self.env['product.category'].create({'name': 'odoo'})
            odoo_apps_product = self.env["product.product"].create({
                'name': "Odoo Apps",
                'sale_ok': True,
                'purchase_ok': True,
                'category': category.id,
                'product_type': 'service'
            })

        odoo_apps_users = self.env["product.product"].search([("name", "=", "Users")])
        if not odoo_apps_users:
            category = self.env['product.category'].create({'name': 'Users'})
            odoo_apps_users = self.env["product.product"].create({
                'name': "Users",
                'sale_ok': True,
                'purchase_ok': True,
                'category': category.id,
                'product_type': 'service',
            })

        order_lines = []
        order_lines.append((0, 0, {
            'product_id': odoo_apps_product.id,
            'name': str(app_count) + ' app di odoo',
            'product_uom_qty': 12,
            'price_unit': app_total_monthly
        }))
        order_lines.append((0, 0, {
            'product_id': odoo_apps_users.id,
            'name': str(self.users_count) + ' utenze odoo',
            'product_uom_qty': 12,
            'price_unit': (18 * self.users_count)
        }))
        self.order_line = order_lines

    @api.multi
    @api.onchange('partner_id')
    def onchange_partner_id(self):
        """
        Update the following fields when the partner is changed:
        - Pricelist
        - Payment terms
        - Invoice address
        - Delivery address
        """
        odoo_apps = self.env['odoo.app.lines'].search([('name', '!=', False)])
        app_ids = []
        for app in odoo_apps:

            app_ids.append(app.id)
            app.write({'include': False})
        self.odoo_app_ids = [(6, 0, app_ids)]

        if not self.partner_id:
            self.update({
                'partner_invoice_id': False,
                'partner_shipping_id': False,
                'payment_term_id': False,
                'fiscal_position_id': False,
            })
            return

        addr = self.partner_id.address_get(['delivery', 'invoice'])
        values = {
            'pricelist_id': self.partner_id.property_product_pricelist and self.partner_id.property_product_pricelist.id or False,
            'payment_term_id': self.partner_id.property_payment_term_id and self.partner_id.property_payment_term_id.id or False,
            'partner_invoice_id': addr['invoice'],
            'partner_shipping_id': addr['delivery'],
            'user_id': self.partner_id.user_id.id or self.env.uid
        }
        if self.env['ir.config_parameter'].sudo().get_param(
                'sale.use_sale_note') and self.env.user.company_id.sale_note:
            values['note'] = self.with_context(lang=self.partner_id.lang).env.user.company_id.sale_note

        if self.partner_id.team_id:
            values['team_id'] = self.partner_id.team_id.id
        self.update(values)




