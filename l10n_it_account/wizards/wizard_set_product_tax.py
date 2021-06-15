from odoo import models, fields, api
from odoo.exceptions import UserError


class WizardSetProductTax(models.TransientModel):
    _name = "wizard.set.product.tax"

    tax_ids = fields.Many2many('account.tax')
    product_to_exclude_ids = fields.Many2many('product.template')
    esegui_acquisti = fields.Boolean()

    def set_taxes(self):
        product_ids = self.env['product.template'].search([('id', 'in', self.env.context['active_ids']),
                                                           ('id', 'not in', self.product_to_exclude_ids.ids)])
        for product in product_ids:
            for tax in self.tax_ids:
                if not self.esegui_acquisti:
                    if tax.id not in product.taxes_id.ids:
                        product.taxes_id += tax
                else:
                    if tax.id not in product.supplier_taxes_id.ids:
                        product.supplier_taxes_id += tax

    def delete_taxes(self):
        product_ids = self.env['product.template'].search([('id', 'in', self.env.context['active_ids']),
                                                           ('id', 'not in', self.product_to_exclude_ids.ids)])
        for product in product_ids:
            for tax in self.tax_ids:
                if not self.esegui_acquisti:
                    if tax.id in product.taxes_id.ids:
                        product.taxes_id -= tax
                else:
                    if tax.id in product.supplier_taxes_id.ids:
                        product.supplier_taxes_id -= tax
