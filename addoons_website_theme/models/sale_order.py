import datetime
import logging

from odoo import api, fields, models

class SaleOrderLineInherit(models.Model):

    _inherit = 'sale.order.line'

    @api.model
    def get_portal_pricelist_price(self, params):

        partner_id = self.env['res.users'].sudo().browse(params['user_id']).partner_id
        prodotto_sviluppo = self.env['product.product'].sudo().search([('default_code', '=', 'prodotto_ore_sviluppo')])
        prodotto_formazione = self.env['product.product'].sudo().search([('default_code', '=', 'prodotto_ore_formazione')])

        totale = 0

        prodotto_sviluppo = prodotto_sviluppo.with_context(
            lang=partner_id.lang,
            partner=partner_id,
            quantity=params['qty_sviluppo'],
            date=datetime.datetime.now(),
            pricelist=partner_id.property_product_pricelist.id,
            uom=prodotto_sviluppo.uom_id.id,
            fiscal_position=partner_id.property_account_position_id,
        )
        prodotto_formazione = prodotto_formazione.with_context(
            lang=partner_id.lang,
            partner=partner_id,
            quantity=params['qty_formazione'],
            date=datetime.datetime.now(),
            pricelist=partner_id.property_product_pricelist.id,
            uom=prodotto_formazione.uom_id.id,
            fiscal_position=partner_id.property_account_position_id,
        )
        product_context = dict(self.env.context, partner_id=partner_id.id, date=datetime.datetime.now(),
                               uom=prodotto_sviluppo.uom_id.id)

        price_unit_sviluppo, rule_id_s = partner_id.property_product_pricelist.with_context(product_context).get_product_price_rule(prodotto_sviluppo, params['qty_sviluppo'], partner_id)

        price_unit_formazione, rule_id_f = partner_id.property_product_pricelist.with_context(product_context).\
            get_product_price_rule(prodotto_formazione, params['qty_formazione'], partner_id)

        totale = round((price_unit_formazione*params['qty_formazione']) + (price_unit_sviluppo*params['qty_sviluppo']),2)

        return {'price_unit_sviluppo': price_unit_sviluppo, 'price_unit_formazione': price_unit_formazione, 'totale': self.format_value_float(round(totale,2))}

    def format_value_float(self, value):
        return "{:,.2f}".format(value).replace(",", "X").replace(".", ",").replace("X", ".")


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    @api.model
    def create_from_portal(self, data):
        order_line = []
        partner_id = self.env['res.users'].sudo().browse(data['user_id']).partner_id
        if partner_id.parent_id:
            partner_id = partner_id.parent_id

        data['qty_sviluppo'] = float(data['qty_sviluppo'].replace('h', ''))
        data['qty_formazione'] = float(data['qty_formazione'].replace('h', ''))

        tassa = self.env['account.tax'].sudo().search(
            [('amount', '=', 22), ('type_tax_use', '=', 'sale'),
             ('price_include', '=', False)], limit=1)
        if data['qty_sviluppo'] > 0:
            prodotto_sviluppo = self.env['product.product'].sudo().search(
                [('default_code', '=', 'prodotto_ore_sviluppo')])

            order_line.append((0, 0, {
                'product_id': prodotto_sviluppo.id,
                'product_uom_qty': data['qty_sviluppo'],
                'name': 'Ore Sviluppo',
                'product_uom': prodotto_sviluppo.uom_id.id,
                'price_unit': float(data['prezzo_sviluppo']),
                'tax_id': [(4,tassa.id)]
            }))

        if data['qty_formazione'] > 0:
            prodotto_formazione = self.env['product.product'].sudo().search([('default_code', '=', 'prodotto_ore_formazione')])

            order_line.append((0, 0, {
                'product_id': prodotto_formazione.id,
                'product_uom_qty': data['qty_formazione'],
                'name': 'Ore Sviluppo',
                'product_uom': prodotto_formazione.uom_id.id,
                'price_unit': float(data['prezzo_formazione']),
                'tax_id': [(4,tassa.id)]
            }))

        vals = {
            'partner_id': partner_id.id,
            'partner_invoice_id': partner_id.id,
            'partner_shipping_id': partner_id.id,
            'pricelist_id': partner_id.property_product_pricelist.id,
            'order_line': order_line,
            'vendita_pacchetto_ore': True,
            'payment_term_id': 1
        }
        logging.info(vals)
        try:
            ordine = self.env['sale.order'].sudo().create(vals)
            ordine.action_confirm()
            if ordine:
                return {'success': True, 'name': ordine.name, 'id': ordine.id}
            else:
                return {'success': False, 'name': "C'è stato un problema durante la creazione dell'ordine"}
        except Exception as e:
            logging.info(e)
            return {'success': False, 'name': "C'è stato un problema durante la creazione dell'ordine"}
