from odoo import models, fields, api

class WizardBilancioVerifica(models.TransientModel):
    _name = 'wizard.bilancio.verifica'

    date_from = fields.Date()
    date_to = fields.Date()
    show_balance_zero = fields.Boolean()


    def get_macroaggregati(self, internal_group):
        ids = self.env['account.account'].search(['&', ('hierarchy_type_id', '=', self.env.ref('l10n_it_account.account_type_macroaggregate').id),
                                                  ('user_type_id.internal_group', '=', internal_group)])
        return ids

    def get_aggregati(self, macro_id):
        ids = self.env['account.account'].search(['&', ('hierarchy_type_id', '=', self.env.ref('l10n_it_account.account_type_aggregate').id),
                                                  ('macroaggregate_id.id', '=', macro_id.id)])
        return ids

    def get_account_from_aggregate(self, aggregate_id):
        ids = self.env['account.account'].search(['&', ('hierarchy_type_id', '=', False),
                                                  ('parent_id.id', '=', aggregate_id.id)])
        return ids


    def get_balance_from_date(self, account):
        move_lines = self.env['account.move.line'].search(['&', '&', ('account_id', '=', account.id), ('date', '>=', self.date_from), ('date', '<=', self.date_to)])
        debit = 0
        credit = 0
        for move in move_lines:
            debit += move.debit
            credit += move.credit
        return debit - credit


    def print_bilancio(self):
        """
        Attività = asset
        Passività = liability
        Ricavi = income
        Costi = expense
        """

        data = {
            'asset': [],
            'liability': [],
            'income': [],
            'expense': [],
        }

        #Algoritmo che ritorna una struttura dati come questa:
        total = 0
        for key, value in data.items():
            """
               'asset': [
                   'dati_macro': ...,
                   'aggregati': {
                       'conti': .....
                   },
                   'dati_macro2': ...,
                   'aggregati2': {
                       'conti2': .....
                   }
               ],
               'liability': [],
               'income': [],
               'expense': [],
           """
            macro_ids = self.get_macroaggregati(key)
            for macro in macro_ids:
                aggregate_ids = self.get_aggregati(macro)
                aggregate_data = []
                macro_balance = 0
                for aggregate in aggregate_ids:
                    account_ids = self.get_account_from_aggregate(aggregate)
                    account_data = []
                    aggregate_balance = 0
                    for account in account_ids:
                        # aggregate_balance += account.balance
                        account_balance = self.get_balance_from_date(account)
                        aggregate_balance += account_balance
                        if (self.show_balance_zero and account_balance == 0) or account_balance != 0:
                            account_data.append({
                                'name': account.name,
                                'code': account.code,
                                'id': account.id,
                                'balance': account_balance
                            })
                    aggregate_data.append({
                        'name': aggregate.name,
                        'code': aggregate.code,
                        'id': aggregate.id,
                        'balance': aggregate_balance,
                        'accounts': account_data
                    })
                    macro_balance += aggregate_balance
                total += macro_balance
                macro_data = {
                    'name': macro.name,
                    'code': macro.code,
                    'id': macro.id,
                    'balance': macro_balance,
                    'aggregate': aggregate_data,
                }
                data[key].append(macro_data)
            data[key].append({'total': total})

        datas = {
            'ids': [],
            'model': 'wizard.bilancio.verifica',
            'form': data,
        }
        return self.env.ref('l10n_it_account.report_bilancio').report_action(self, data=datas)


class ReportBilancioVerifica(models.AbstractModel):
    """
    Ereditare il report per modificare la funzione render_html
    e aggiungere i parametri passati dal wizard
    """
    _name = 'report.l10n_it_account.report_bilancio_verifica'

    @api.model
    def _get_report_values(self, docids, data=None):


        valore_della_produzione = 0
        costi_della_produzione = 0
        oneri_finanziari_costi = 0
        proventi_finanziari_ricavi = 0
        rettifiche_di_valore_costi = 0
        rettifiche_di_valore_ricavi = 0

        for x in data['form']['expense']:
            if 'id' in x:
                if x['id'] == self.env.ref('l10n_it_account.macro_ce_costi_b').id:
                    costi_della_produzione = x['balance']
                if x['id'] == self.env.ref('l10n_it_account.macro_ce_costi_c').id:
                    oneri_finanziari_costi = x['balance']
                if x['id'] == self.env.ref('l10n_it_account.macro_ce_costi_d').id:
                    rettifiche_di_valore_costi = x['balance']
        for x in data['form']['income']:
            if 'id' in x:
                if x['id'] == self.env.ref('l10n_it_account.macro_ce_ricavi_a').id:
                    valore_della_produzione = x['balance']
                if x['id'] == self.env.ref('l10n_it_account.macro_ce_ricavi_c').id:
                    proventi_finanziari_ricavi = x['balance']
                if x['id'] == self.env.ref('l10n_it_account.macro_ce_ricavi_d').id:
                    rettifiche_di_valore_ricavi = x['balance']


        # REDDITO ANTE IMPOSTE CONTO ECONOMICO(Si calcola (A - B) +- C +- D
        RAI = (valore_della_produzione - costi_della_produzione) + (proventi_finanziari_ricavi - oneri_finanziari_costi) + (rettifiche_di_valore_ricavi - rettifiche_di_valore_costi)


        datas = {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'asset': data['form']['asset'],
            'liability': data['form']['liability'],
            'income': data['form']['income'],
            'expense': data['form']['expense'],
            'rai': RAI
        }
        return datas