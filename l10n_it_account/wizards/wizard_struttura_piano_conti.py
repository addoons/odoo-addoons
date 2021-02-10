from odoo import api, fields, models


class WizardStrutturaPianoConti(models.TransientModel):
    """
    Configura massivamente i seguenti campi per i conti selezionati:
    - Macroaggregato
    - Aggregato
    """
    _name = 'wizard.struttura.piano.conti'

    macroaggregate_id = fields.Many2one('account.account')
    aggregate_id = fields.Many2one('account.account')

    def aggiorna_struttura_piano_conti(self):
        """
        Assegna Macroaggregato e Aggregato ai conti selezionati
        """
        for conto in self._context['active_ids']:
            conto = self.env['account.account'].browse(conto)
            if conto:
                if self.macroaggregate_id:
                    conto.macroaggregate_id = self.macroaggregate_id.id
                if self.aggregate_id:
                    conto.parent_id = self.aggregate_id.id

    def svuota_struttura_piano_conti(self):
        """
        Svuota la gerarchia per i conti selezionati
        """
        for conto in self._context['active_ids']:
            conto = self.env['account.account'].browse(conto)
            conto.macroaggregate_id = False
            conto.parent_id = False
