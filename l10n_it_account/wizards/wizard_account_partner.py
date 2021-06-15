from odoo import api, fields, models


class WizardAccountPartner(models.TransientModel):
    """
    Configura massivamente i seguenti campi per i partner selezionati:
    - conto di credito
    - conto di debito
    - conto di costo
    - conto di ricavo
    """
    _name = 'wizard.account.partner'

    debit_account = fields.Many2one('account.account')
    credit_account = fields.Many2one('account.account')
    cost_account = fields.Many2one('account.account')
    revenue_account = fields.Many2one('account.account')

    def associa_conti(self):
        for partner in self._context['active_ids']:
            partner = self.env['res.partner'].browse(partner)
            if partner:
                if self.credit_account:
                    partner.property_account_receivable_id = self.credit_account.id
                if self.debit_account:
                    partner.property_account_payable_id = self.debit_account.id
                if self.cost_account:
                    partner.costi_account = self.cost_account.id
                if self.revenue_account:
                    partner.ricavi_account = self.revenue_account.id

