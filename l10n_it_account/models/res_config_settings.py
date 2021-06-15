from odoo import models,fields,api


class AccountConfigSettingsInh(models.TransientModel):
    _inherit = 'res.config.settings'

    activate_check_invoice_date = fields.Boolean(help="Attivare per evitare salti nelle sequenze di fatturazione o "
                                                      "validazioni di documenti non in ordine cronologico.",
                                                 default=False)

    @api.multi
    def set_values(self):
        super(AccountConfigSettingsInh, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('l10n_it_account.account_controllo_protocollo', self.activate_check_invoice_date)

    @api.model
    def get_values(self):
        res = super(AccountConfigSettingsInh, self).get_values()
        res.update(activate_check_invoice_date=self.env['ir.config_parameter'].sudo().get_param('l10n_it_account.account_controllo_protocollo'))
        return res