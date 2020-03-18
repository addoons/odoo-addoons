from odoo import models,api,fields,_

class PartnerInherit(models.Model):

    _inherit = 'res.partner'

    @api.model
    def get_ore_disponibili(self, id):

        partner = self.env['res.users'].sudo().browse(id['user_id']).partner_id
        return {"ore_sviluppo": round(partner.ore_sviluppo_disponibili,2), "ore_formazione":round(partner.ore_formazione_consulenza_disponibili,2)}

    @api.model
    def get_analysis_graph_data(self, data):
        partner = self.env['res.users'].sudo().browse(data['user_id']).partner_id
        partners = []
        if partner.parent_id:
            partner = partner.parent_id
            partners = partner.child_ids.ids

        partners.append(partner.id)
        fatturato_mensile = [0 for i in range(12)]
        task_aperte_mensili = [0 for i in range(12)]
        task_completate_mensili = [0 for i in range(12)]
        invoices = self.env['account.invoice'].sudo().search([('type', '=', 'out_invoice'), ('state', '!=', 'cancel'), ('partner_id', 'in', partners),
                                                       ('date_invoice', '>=', '01/01/'+str(data['year'])),('date_invoice', '<=', '31/12/'+str(data['year']))])


        tasks_aperte = self.env['project.task'].sudo().search([
             ('partner_id', 'in', partners),
             ('create_date', '>=', '01/01/' + str(data['year'])),
             ('create_date', '<=', '31/12/' + str(data['year']))])

        tasks_completate = self.env['project.task'].sudo().search([
            ('partner_id', 'in', partners),
            ('date_end', '>=', '01/01/' + str(data['year'])),
            ('date_end', '<=', '31/12/' + str(data['year']))])
        for invoice in invoices:
            mese = invoice.date_invoice.month - 1
            fatturato_mensile[mese] += invoice.amount_total

        for task in tasks_aperte:
            mese = task.create_date.month - 1
            task_aperte_mensili[mese] += 1

        for task in tasks_completate:
            mese = task.date_end.month - 1
            task_completate_mensili[mese] += 1


        fatturato_mensile = [round(i, 2) for i in fatturato_mensile]
        return {'fatturato': fatturato_mensile, 'task_aperte': task_aperte_mensili, 'task_completate': task_completate_mensili}

