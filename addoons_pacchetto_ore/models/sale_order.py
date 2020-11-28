from odoo import api, fields, models

class SaleOrderInherit(models.Model):

    _inherit = 'sale.order'

    vendita_pacchetto_ore = fields.Boolean()
    pacchetti_ore_ids = fields.One2many('pacchetti.ore', 'order_id')
    counter_pacchetti_ore = fields.Integer(compute="_compute_numero_pacchetti")

    def _compute_numero_pacchetti(self):
        for record in self:
            record.counter_pacchetti_ore = len(record.pacchetti_ore_ids)

    def crea_pacchetto(self):
        """
            Funzione che crea i pacchetti ore associati all'ordine di vendita nato dal portale.
        """
        if self.vendita_pacchetto_ore:
            pacchetti_ids = []
            if not self.partner_id.parent_id:
                cliente = self.partner_id
            else:
                cliente = self.partner_id.parent_id

            for line in self.order_line:
                data_pacchetto = False

                if line.product_id.default_code == 'prodotto_ore_sviluppo' and line.product_uom_qty > 0:
                    data_pacchetto = {
                        'name': 'Pacchetto ' + cliente.name,
                        'type': 'developing',
                        'hours': line.product_uom_qty,
                        'partner_id': cliente.id,
                        'order_id': self.id
                    }

                if line.product_id.default_code == 'prodotto_ore_formazione' and line.product_uom_qty > 0:
                    data_pacchetto = {
                        'name': 'Pacchetto ' + cliente.name,
                        'type': 'training',
                        'hours': line.product_uom_qty,
                        'partner_id': cliente.id,
                        'order_id': self.id
                    }

                if data_pacchetto:
                    id_pacchetto = self.env['pacchetti.ore'].create(data_pacchetto).id
                    pacchetti_ids.append(id_pacchetto)
            if len(pacchetti_ids):
                return {
                    'name': 'Pacchetti ordine ' + self.name,
                    'view_mode': 'tree,form',
                    'res_model': 'pacchetti.ore',
                    'domain': [('id', 'in', pacchetti_ids)],
                    'type': 'ir.actions.act_window',
                    'target': 'current',
                }

