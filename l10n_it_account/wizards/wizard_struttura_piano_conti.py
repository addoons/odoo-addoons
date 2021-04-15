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
    sottoconto_terzo_livello = fields.Many2one('account.account', string='Sottoconto Terzo Livello')
    sottoconto_quarto_livello = fields.Many2one('account.account', string='Sottoconto Quarto Livello')

    def assegna_macro(self):
        conti = self.env['account.account'].browse(self._context['active_ids'])
        for conto in conti:
            if not conto.sottoconto_terzo_livello:
                #Siamo al secondo livello, esempio 01/0005
                if conto.parent_id.macroaggregate_id:
                    self.env.cr.execute('update account_account set macroaggregate_id = %s where id = %s' % (conto.parent_id.macroaggregate_id.id, conto.id) )
                if conto.parent_id.macroaggregate_id.user_type_id:
                    self.env.cr.execute('update account_account set user_type_id = %s where id = %s' % (conto.parent_id.macroaggregate_id.user_type_id.id, conto.id))
            if conto.sottoconto_terzo_livello:
                #Siamo al terzo livello, esempio 01/0005/0010
                if conto.sottoconto_terzo_livello.parent_id.macroaggregate_id:
                    self.env.cr.execute('update account_account set macroaggregate_id = %s where id = %s' % (conto.sottoconto_terzo_livello.parent_id.macroaggregate_id.id, conto.id) )
                if conto.sottoconto_terzo_livello.parent_id.macroaggregate_id.user_type_id:
                    self.env.cr.execute('update account_account set user_type_id = %s where id = %s' % (conto.sottoconto_terzo_livello.parent_id.macroaggregate_id.user_type_id.id, conto.id))


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
                if self.sottoconto_terzo_livello:
                    conto.sottoconto_terzo_livello = self.sottoconto_terzo_livello.id
                if self.sottoconto_quarto_livello:
                    conto.sottoconto_quarto_livello = self.sottoconto_quarto_livello.id

    def svuota_struttura_piano_conti(self):
        """
        Svuota la gerarchia per i conti selezionati
        """
        for conto in self._context['active_ids']:
            conto = self.env['account.account'].browse(conto)
            conto.macroaggregate_id = False
            conto.parent_id = False
            conto.sottoconto_terzo_livello = False
            conto.sottoconto_quarto_livello = False
