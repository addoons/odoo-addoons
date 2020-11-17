from odoo import models, fields, api, _
from odoo.exceptions import UserError


#Cambio Conti
class CambioContiLine(models.TransientModel):
    _name = 'cambio.conti.line'
    conto_sorgente = fields.Many2one('account.account')
    conto_destinazione = fields.Many2one('account.account')
    id_conto = fields.Many2one('cambio.conti')

#Cambio Imposte Applicate da Imposta Sorgente
class CambioImposteLine(models.TransientModel):
    _name = 'cambio.imposte.line'

    imposta_sorgente = fields.Many2one('account.tax')
    imposta_destinazione = fields.Many2one('account.tax')
    id_conto = fields.Many2one('cambio.conti')

#Cambio Imposte Applicate da Conto Sorgente
class InserimentoImposteLine(models.TransientModel):
    _name = 'inserimento.imposte.line'

    conto_sorgente = fields.Many2one('account.account')
    imposta_destinazione = fields.Many2one('account.tax')
    id_conto = fields.Many2one('cambio.conti')


class CambioCreatoImposteLine(models.TransientModel):
    _name = 'cambio.creato.imposte.line'

    imposta_sorgente = fields.Many2one('account.tax')
    imposta_destinazione = fields.Many2one('account.tax')
    id_conto = fields.Many2one('cambio.conti')

class InserimentoCreatoImposteLine(models.TransientModel):
    _name = 'inserimento.creato.imposte.line'

    conto_sorgente = fields.Many2one('account.account')
    imposta_destinazione = fields.Many2one('account.tax')
    id_conto = fields.Many2one('cambio.conti')

class CambioConti(models.TransientModel):
    _name = 'cambio.conti'

    conti_ids = fields.One2many('cambio.conti.line', 'id_conto')
    imposte_ids = fields.One2many('cambio.imposte.line', 'id_conto')
    ins_imposta_ids = fields.One2many('inserimento.imposte.line', 'id_conto')
    creato_imposte_ids = fields.One2many('cambio.creato.imposte.line', 'id_conto')
    ins_creato_imposta_ids = fields.One2many('inserimento.creato.imposte.line', 'id_conto')
    add_analytic = fields.Boolean()
    account_ids = fields.Many2many('account.account')
    fiscal_position_id = fields.Many2one('account.fiscal.position')
    inverti = fields.Boolean()
    analytic_account_id = fields.Many2one('account.analytic.account')
    conti_doppi_crediti = fields.Boolean()



    @api.onchange('fiscal_position_id', 'inverti')
    def onchange_fiscal_position_id(self):
        conti = [(5, )]
        solo_sorgente = [(5, )]
        analytic = []

        if not self.inverti:
            for account in self.fiscal_position_id.account_ids:
                conti.append((0, 0 , {'conto_sorgente': account.account_src_id.id, 'conto_destinazione': account.account_dest_id.id}))
                solo_sorgente.append((0, 0, {'conto_sorgente': account.account_src_id.id}))
                analytic.append(account.account_src_id.id)

        else:
            for account in self.fiscal_position_id.account_ids:
                conti.append((0, 0 , {'conto_sorgente': account.account_dest_id.id, 'conto_destinazione': account.account_src_id.id}))
                solo_sorgente.append((0, 0, {'conto_sorgente': account.account_dest_id.id}))
                analytic.append(account.account_dest_id.id)

        self.conti_ids = conti
        self.ins_imposta_ids = solo_sorgente
        self.ins_creato_imposta_ids = solo_sorgente
        self.account_ids = analytic



    def get_iva_imponibile_errato(self):

        errate = []
        move_ids = self.env['account.move'].search([('move_type','not in', ['payable', 'payable_refund']), ('date', '>=', '2020-03-01'),('date', '<=', '2020-03-31')])
        for move in move_ids:
            tot_iva = 0
            tot_impo = 0
            for l in move.line_ids:
                if l.tax_line_id:
                    tot_iva += l.credit
                if l.tax_ids:
                    tot_impo += l.credit

            if tot_iva > 0 or tot_impo > 0:
                imposta = tot_impo * 0.22
                diff = abs(tot_iva - imposta)
                if diff > 0.05:
                    errate.append(move.id)

        return {
            'name': 'Registrazioni Errate',
            'type': 'ir.actions.act_window',
            'view_type': 'list',
            'view_mode': 'list,form',
            'res_model': 'account.move',
            'target': 'current',
            'domain': [('id', 'in', errate)]
        }




    def set_unbalanced(self):
        context = dict(self._context or {})
        active_ids = context.get('active_ids', []) or []
        crediti_v_clienti = self.env['account.account'].search([('name', '=', 'CREDITI V/CLIENTI')], limit=1)
        merci_c_vendite = self.env['account.account'].search([('name', '=', 'MERCI C/VENDITE')])
        corr_p_cessioni = self.env['account.account'].search([('name', '=', 'CORR.P/CESSIONE MERCI-NO VENTILAZ')])
        iva_s_vendite = self.env['account.account'].search([('name', '=', 'IVA SU VENDITE')])
        iva_s_corr = self.env['account.account'].search([('name', '=', 'IVA SU CORRISPETTIVI')])
        iva_id = self.env['account.tax'].search([('name', '=', 'Iva al 22% FATT (inclusa)')], limit=1)
        iva_corr_id = self.env['account.tax'].search([('name', '=', 'Iva al 22% CORR (debito)')], limit=1)

        for registrazione in self.env['account.move'].browse(active_ids):

            account_analytic = self.env['account.analytic.account'].search([('name', 'like', registrazione.journal_id.name[:3])], limit=1)

            if registrazione.state == 'posted':
                # La registrazione è generata, la reimposta in bozza
                registrazione.button_cancel()

            difference = 0
            debit = 0
            credit = 0
            for line in registrazione.line_ids:
                debit += line.debit
                credit += line.credit



            difference = abs(debit - credit)

            #ci sono più valori in DEBIT
            more_debit = False
            find_debit = False
            for line in registrazione.line_ids:
                if line.debit > 0 and find_debit:
                    more_debit = True
                if line.debit > 0:
                    find_debit = True

            registrazione.line_ids.remove_move_reconcile()

            for line in registrazione.line_ids:

                if 'BONUS MOBILI' in line.account_id.name:
                    break

                if not more_debit:
                    #Se ce un solo valore in debit aumenta i crediti v/clienti oppure l'iva
                    if credit > debit:
                    # Aumentare crediti v/clienti
                        if line.account_id.name != 'CREDITI V/CLIENTI' and line.account_id.name != 'IVA SU VENDITE' and line.account_id.name != 'IVA SU CORRISPETTIVI':
                            if line.credit - difference > 0:
                                line.credit -= difference
                                break
                    else:
                        # Aumentare iva
                        if line.account_id.name == 'IVA SU VENDITE' or line.account_id.name == 'IVA SU CORRISPETTIVI':
                            line.credit += difference
                            break
                else:
                    #Se ci sono più valori in DEBIT fa altro, cerca il pagamento
                    order = self.env['pos.order'].search([('name', '=', registrazione.ref)], limit=1)
                    if order:
                        #Cerco il pagamento più simile
                        scostamento_pagamento = 1000000000
                        payment_found = False
                        for payment in order.statement_ids:
                            if abs(payment.amount - registrazione.amount) < scostamento_pagamento:
                                scostamento_pagamento = abs(payment.amount - registrazione.amount)
                                payment_found = payment

                        if payment_found:
                            crediti = payment_found.amount
                            merci = (crediti / 1.22)
                            iva = (merci * 0.22)
                            registrazione.line_ids = [(5, )]

                            registrazione.line_ids = [(0, 0, {
                                            'account_id': crediti_v_clienti.id,
                                            'debit': abs(float(crediti)),
                                            'partner_id': order.partner_id.id,
                                            }),
                                            (0, 0, {
                                                'account_id': iva_s_vendite.id if 'FATT' in registrazione.journal_id.name else iva_s_corr.id,
                                                'credit': abs(float(iva)),
                                                'partner_id': order.partner_id.id,
                                                'tax_line_id': iva_id.id if 'FATT' in registrazione.journal_id.name else iva_corr_id.id
                                            }),
                                            (0, 0, {
                                                'account_id': merci_c_vendite.id if 'FATT' in registrazione.journal_id.name else corr_p_cessioni.id,
                                                'credit': abs(float(merci)),
                                                'partner_id': order.partner_id.id,
                                                'analytic_account_id': account_analytic.id,
                                                'tax_ids': [(4, iva_id.id)] if 'FATT' in registrazione.journal_id.name else [(4, iva_corr_id.id)]
                                            }),]


            if registrazione.state == 'draft':
                #La registrazione è in bozza, la reimposta in generata
                registrazione.action_post()


    def view_unbalanced(self):
        move_unbalanced = []

        move_ids = self.env['account.move'].search([])
        for move in move_ids:
            debit = 0
            credit = 0
            print("Controllata")
            for line in move.line_ids:
                debit += line.debit
                credit += line.credit

            if abs(debit - credit) >= 0.01:
                print("Sbilanciata")
                move_unbalanced.append(move.id)

        return {
            'name': 'Registrazioni Sbilanciate',
            'type': 'ir.actions.act_window',
            'view_type': 'list',
            'view_mode': 'list,form',
            'res_model': 'account.move',
            'target': 'current',
            'domain': [('id', 'in', move_unbalanced)]
        }


    @api.multi
    def applica_regole_conto(self):
        context = dict(self._context or {})
        active_ids = context.get('active_ids', []) or []
        crediti_v_clienti = self.env['account.account'].search([('name', '=', 'CREDITI V/CLIENTI')], limit=1)



        for registrazione in self.env['account.move'].browse(active_ids):

            if registrazione.state == 'posted':
                # La registrazione è generata, la reimposta in bozza
                registrazione.button_cancel()

            for line in registrazione.line_ids:

                if 'BONUS MOBILI' in line.account_id.name:
                    break

                id_cambio_conto = 0


                for ins in self.ins_imposta_ids:
                    if line.account_id.id == ins.conto_sorgente.id:
                        #Cambio l'imposta
                        if ins.imposta_destinazione:
                            line.write({'tax_ids': [(5,), (4, ins.imposta_destinazione.id)]})
                        else:
                            line.write({'tax_ids': [(5,)]})

                for regola in self.conti_ids:
                    if line.account_id.id == regola.conto_sorgente.id:
                        id_cambio_conto = regola.conto_destinazione.id
                if id_cambio_conto > 0:
                    line.write({'account_id': id_cambio_conto})

                if len(line.tax_ids) > 0:
                    id_cambio_imposta = 0
                    for regola in self.imposte_ids:

                        if line.tax_ids[0].id == regola.imposta_sorgente.id:
                            id_cambio_imposta = regola.imposta_destinazione.id
                    if id_cambio_imposta > 0:
                        line.write({'tax_ids': [(6, 0, [id_cambio_imposta])]})


                if line.tax_line_id:
                    for regola in self.creato_imposte_ids:
                        if line.tax_line_id.id == regola.imposta_sorgente.id:
                            line.write({'tax_line_id': regola.imposta_destinazione.id})

                if line.account_id:
                    for regola in self.ins_creato_imposta_ids:
                        if line.account_id.id == regola.conto_sorgente.id:
                            line.write({'tax_line_id': regola.imposta_destinazione.id})


                if self.conti_doppi_crediti:
                    if line.credit != 0:
                        line.account_id = crediti_v_clienti.id


                if self.analytic_account_id:
                    if line.account_id in self.account_ids:
                        #Per tutte le account.move.line che hanno conto finanziario soggetto e conto analitico mancante
                        line.analytic_account_id = self.analytic_account_id.id

                if self.add_analytic:
                    if line.account_id in self.account_ids:
                        #Per tutte le account.move.line che hanno conto finanziario soggetto e conto analitico mancante
                        if registrazione.ref:
                            analytic_code = registrazione.ref[:3]
                            if analytic_code:
                                analytic_account = self.env.cr.execute(
                                    "select id from account_analytic_account where name like '%s%%' and length(name) > 3" % (
                                    analytic_code,))
                                analytic_account = self.env.cr.fetchall()
                                if analytic_account:
                                    line.analytic_account_id = analytic_account[0][0]
                                else:
                                    if 'FATTURE' not in registrazione.journal_id.name:
                                        analytic_code = registrazione.journal_id.name[:3]
                                        if analytic_code:
                                            analytic_account = self.env.cr.execute("select id from account_analytic_account where name like '%s%%' and length(name) > 3" % (analytic_code, ))
                                            analytic_account = self.env.cr.fetchall()
                                            if analytic_account:
                                                line.analytic_account_id = analytic_account[0][0]
                                    else:
                                        analytic_code = registrazione.ref[:3]
                                        if analytic_code:
                                            analytic_account = self.env.cr.execute(
                                                "select id from account_analytic_account where name like '%s%%' and length(name) > 3" % (
                                                analytic_code,))
                                            analytic_account = self.env.cr.fetchall()
                                            if analytic_account:
                                                line.analytic_account_id = analytic_account[0][0]



            if registrazione.state == 'draft':
                #La registrazione è in bozza, la reimposta in generata
                registrazione.action_post()
