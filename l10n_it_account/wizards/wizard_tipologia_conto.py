from odoo import api, fields, models


class WizardTipologiaConto(models.TransientModel):
    """
    Configura massivamente i seguenti campi per i macroaggregati selezionati e i conti figli:
    - Tipologia (Attività, Passività, ecc...)
    """
    _name = 'wizard.tipologia.conto'

    macroaggregate_ids = fields.Many2many('account.account')
    account_type_id = fields.Many2one('account.account.type', domain=[('internal_group', '!=', False)])

    def aggiorna_tipologia_piano_conti(self):
        """
        Assegna Tipologia ai macroaggregati selezionati e ai figli
        """
        for macro in self.macroaggregate_ids:
            account_ids = self.env['account.account'].search([('macroaggregate_id', '=', macro.id)])
            for account in account_ids:
                account.user_type_id = self.account_type_id

