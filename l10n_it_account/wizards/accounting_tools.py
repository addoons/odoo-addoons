import json
from base64 import b64decode

import logging
from datetime import datetime

from odoo import models, fields, api,_
import xlrd

from odoo import sql_db


class WizardToolPianoDeiConti(models.TransientModel):
    _name = 'wizard.tool.piano.conti'

    file = fields.Binary()


    def on_delete(self):
        """
        Svuota l'attuale piano dei conti, per poterne caricare uno nuovo
        """
        self.env.cr.execute('UPDATE account_tax SET account_id = NULL, refund_account_id = NULL')
        self.env.cr.execute("DELETE FROM account_account")





    def on_upload(self):
        """
        Al Caricamento del piano dei Conti Leggo il contenuto del foglio excel e inizio
        Ad elaborare i valori, caricando Macroaggregati, Aggregati, Conti
        """
        if self.file:
            wb = xlrd.open_workbook(file_contents=b64decode(self.file))
            sheet = wb.sheet_by_index(0)
            sheet.cell_value(0, 0)
            accounts = []
            macroaggregato = self.env.ref('l10n_it_account.account_type_macroaggregate').id
            aggregato = self.env.ref('l10n_it_account.account_type_aggregate').id
            passivita = self.env.ref('account.data_account_type_current_liabilities').id
            attivita = self.env.ref('account.data_account_type_current_assets').id
            costi = self.env.ref('account.data_account_type_expenses').id
            ricavi = self.env.ref('account.data_account_type_revenue').id

            for row in range(0, sheet.nrows):
                account = {}
                for column in range(0, sheet.ncols):
                    if column == 0:
                        #Prima Colonna, contiene il codice conto
                        cell = sheet.cell(row, column)
                        if isinstance(cell.value, str):
                            account_account_split = cell.value.split('/')
                            if len(account_account_split) == 3:
                                #Significa che effettivamente è un conto
                                if account_account_split[2] == '****' and account_account_split[1] == '****':
                                    #MacroAggregato
                                    account['hierarchy_type_id'] = macroaggregato
                                    account['code'] = account_account_split[0]
                                if account_account_split[2] == '****' and account_account_split[1] != '****' and account_account_split[0] != '****':
                                    #Aggregato
                                    account['hierarchy_type_id'] = aggregato
                                    account['code'] = account_account_split[0] + '/' + account_account_split[1]
                                    self.env.cr.execute("SELECT id FROM account_account WHERE code = '%s' " % account_account_split[0])
                                    macro_id = self.env.cr.fetchall()
                                    if macro_id:
                                        account['macroaggregate_id'] = macro_id[0][0]
                                if account_account_split[2] != '****' and account_account_split[1] != '****' and account_account_split[0] != '****':
                                    #Conto
                                    account['hierarchy_type_id'] = False
                                    account['code'] = account_account_split[0] + '/' + account_account_split[1] + '/' + account_account_split[2]
                                    self.env.cr.execute("SELECT id FROM account_account WHERE code = '%s' " % account_account_split[0])
                                    macro_id = self.env.cr.fetchall()
                                    if macro_id:
                                        account['macroaggregate_id'] = macro_id[0][0]
                                    self.env.cr.execute("SELECT id FROM account_account WHERE code = '%s' " % (account_account_split[0] + '/' + account_account_split[1]))
                                    aggregate_id = self.env.cr.fetchall()
                                    if aggregate_id:
                                        account['parent_id'] = aggregate_id[0][0]

                    if 'code' in account:
                        if column == 4:
                            #Quarta Colonna, contiene il nome del conto
                            cell = sheet.cell(row, column)
                            if isinstance(cell.value, str):
                                account['name'] = cell.value
                        if column == 11:
                            #Undicesima Colonna, area di ambito: Economico, Patrimoniale
                            cell = sheet.cell(row, column)
                            if cell.value == 'Economico':
                                account['area'] = 'conto_economico'
                            if cell.value == 'Patrimoniale':
                                account['area'] = 'stato_patrimoniale'
                                account['user_type_id'] = attivita
                        if column == 25:
                            cell = sheet.cell(row, column)
                            #Tipo di Conto
                            if 'area' in account:
                                if account['area'] == 'conto_economico':
                                    if cell.value == 'Costi':
                                        account['user_type_id'] = costi
                                    if cell.value == 'Ricavi':
                                        account['user_type_id'] = ricavi
                            else:
                                account['user_type_id'] = ricavi

                if account != {}:
                    self.env['account.account'].create(account)
                    self.env.cr.commit()
                    print("Creato")


class DaneaPartner(models.Model):
    _name = 'danea.partner'

    name = fields.Char()
    city = fields.Char()
    vat = fields.Char()
    fiscalcode = fields.Char()
    street = fields.Char()
    zip = fields.Char()
    pec_destinatario = fields.Char()
    codice_destinatario = fields.Char()
    email = fields.Char()


DaneaPartner()



class WizardCaricaClienti(models.TransientModel):
    _name = 'wizard.partner.import'

    file = fields.Binary()
    file2 = fields.Binary()
    file3 = fields.Binary()
    file4 = fields.Binary()
    file5 = fields.Binary()
    file6 = fields.Binary()
    json = fields.Text()

    def getNewEnv(self):
        ctx = self.env.context.copy()
        ctx.update({'bulk_import': True})
        uid = self.env.uid
        new_cr = sql_db.db_connect(self.env.cr.dbname).cursor()
        new_env = api.Environment(new_cr, 1, ctx)
        return new_env


    def close_session(self):
        session_ids = self.env['pos.session'].search([('state', '=', 'opened')])
        for session in session_ids:
            session.sudo(user=session.user_id.id).action_pos_session_closing_control()

    def on_upload(self):

        if self.file6:
            #IMPORT INGRESSI
            env1 = self.getNewEnv()
            wb = xlrd.open_workbook(file_contents=b64decode(self.file6))
            sheet = wb.sheet_by_index(0)
            sheet.cell_value(0, 0)

            for row in range(0, sheet.nrows):
                if row >= 1:
                    entries = {}

                    codice_negozio = ''
                    analytic_account = False
                    data = ''
                    ingressi = 0

                    for column in range(0, sheet.ncols):
                        cell = sheet.cell(row, column)
                        value = cell.value



                        if column == 0:
                            codice_negozio_id = env1['pos.config'].search([('codice_conto_ingressi', '=', value)], limit=1)
                            if codice_negozio_id:
                                codice_negozio = codice_negozio_id.codice_conto_ingressi
                                analytic_account = codice_negozio_id.analytic_account_id.id
                        if column == 1:
                            data = xlrd.xldate_as_tuple(value, wb.datemode)
                            data = str(data[0]) + '-' + str(data[1]) + '-' + str(data[2])
                        if column == 2:
                            ingressi = int(value)

                        if codice_negozio and analytic_account and data and ingressi > 0:
                            entries = {
                                'date': data,
                                'analytic_account': analytic_account,
                                'shop_code': codice_negozio,
                                'ingressi': ingressi
                            }
                            env1['dondi.ingressi'].create(entries)
                            logging.info("Creato")

            env1.cr.commit()





        if self.file2:
            #IMPORT FATTURE
            env1 = self.getNewEnv()

            wb = xlrd.open_workbook(file_contents=b64decode(self.file2))
            sheet = wb.sheet_by_index(0)
            sheet.cell_value(0, 0)

            crediti_v_clienti = env1['account.account'].search([('name', '=', 'CREDITI V/CLIENTI')], limit=1)
            merci_c_vendite = env1['account.account'].search([('name', '=', 'MERCI C/VENDITE')])
            iva_s_vendite = env1['account.account'].search([('name', '=', 'IVA SU VENDITE')])
            journal_id = env1['account.journal'].search([('id', '=', 2)])


            treviso = env1['account.journal'].search([('name', 'like', 'TREVISO')])
            roma = env1['account.journal'].search([('name', 'like', 'ROMA')])
            levata = env1['account.journal'].search([('name', 'like', 'LEVATA')])
            senago = env1['account.journal'].search([('name', 'like', 'SENAGO')])

            numero_registro = ''

            for row in range(0, sheet.nrows):
                if row >= 1:
                    import_row = True

                    move_vals = {}
                    for column in range(0, sheet.ncols):
                        cell = sheet.cell(row, column)
                        value = cell.value

                        # if column == 0:
                        #     if value == '-':
                        #         import_row = False
                        if column == 1:
                            numero = value
                        if column == 2:
                            #Numero Registro
                            numero_registro = value
                        if column == 3:
                            tipo_fattura = value
                        if column == 4:
                            #Data Fattura
                            data = value
                            data = data.replace('/', '-')
                            data = datetime.strptime(data, '%d-%m-%Y')
                        if column == 5:
                            #Riferimento
                            if value and value != "":
                                riferimento = value
                                codice_negozio = value[:3]
                                account_analytic = env1['account.analytic.account'].search(
                                    [('name', 'like', codice_negozio)], limit=1)
                            else:
                                riferimento = value
                                codice_negozio = value[:3]
                                account_analytic = env1['account.analytic.account'].search(
                                    [('name', 'like', 'AMM')], limit=1)


                        if column == 6:
                            #Nome Cliente
                            nome_cliente = value
                        if column == 7:
                            #Imponibile
                            imponibile = value
                        if column == 8:
                            #percentuale iva
                            perc_iva = value
                        if column == 9:
                            #iva
                            iva = value
                        if column == 10:
                            #Crediti v/clienti
                            totale = value
                        if column == 11:
                            #Codice Negozio
                            negozio = value



                    if import_row:
                        partner_id = env1['res.partner'].search([('name', '=', nome_cliente)], limit=1)
                        if not partner_id:
                            partner_id = env1['res.partner'].create({
                                'name': nome_cliente,
                            })

                        registro = journal_id.id,
                        if 'TREVISO' in negozio:
                            registro = treviso.id
                        if 'ROMA' in negozio:
                            registro = roma.id
                        if 'LEVATA' in negozio:
                            registro = levata.id
                        if 'SENAGO' in negozio:
                            registro = senago.id

                        iva_id = env1['account.tax'].search([('id', '=', int(perc_iva) )], limit=1)
                        if not iva_id:
                            iva_id = env1['account.tax'].search([('id', '=', 1)], limit=1)

                        if isinstance(totale, str):
                            totale = totale.replace('.', '').replace(',', '.')
                        if isinstance(iva, str):
                            iva = iva.replace('.', '').replace(',', '.')
                        if isinstance(imponibile, str):
                            iva = imponibile.replace('.', '').replace(',', '.')

                        if not iva:
                            iva = 0

                        if tipo_fattura != 'Nota di Credito':
                            move_vals = {
                                'date': data,
                                'ref': str(numero_registro) + ' Fattura N° '+ str(numero) + ' - ' + str(riferimento) + ' - ' + str(negozio),
                                'journal_id': registro,
                                'partner_id': partner_id.id,
                                'line_ids': [
                                    (0, 0, {
                                        'account_id': crediti_v_clienti.id,
                                        'debit': abs(float(totale)),
                                        'partner_id': partner_id.id,
                                    }),
                                    (0, 0, {
                                        'account_id': iva_s_vendite.id,
                                        'credit': abs(float(iva)),
                                        'partner_id': partner_id.id,
                                        'tax_line_id': iva_id.id
                                    }),
                                    (0, 0, {
                                        'account_id': journal_id.default_debit_account_id.id,
                                        'credit': abs(float(imponibile)),
                                        'partner_id': partner_id.id,
                                        'analytic_account_id': account_analytic.id,
                                        'tax_ids': [(4, iva_id.id)]
                                    }),
                                ]
                            }
                        else:
                            move_vals = {
                                'date': data,
                                'ref': str(numero_registro) + 'Nota Credito N° ' + str(numero) + ' - ' + str(riferimento) + ' - ' + str(
                                    negozio),
                                'journal_id': registro,
                                'partner_id': partner_id.id,
                                'line_ids': [
                                    (0, 0, {
                                        'account_id': crediti_v_clienti.id,
                                        'credit': abs(float(totale)),
                                        'partner_id': partner_id.id,

                                    }),
                                    (0, 0, {
                                        'account_id': iva_s_vendite.id,
                                        'debit': abs(float(iva)),
                                        'partner_id': partner_id.id,
                                        'tax_line_id': iva_id.id
                                    }),
                                    (0, 0, {
                                        'account_id': journal_id.default_credit_account_id.id,
                                        'debit': abs(float(imponibile)),
                                        'partner_id': partner_id.id,
                                        'analytic_account_id': account_analytic.id,
                                        'tax_ids': [(4, iva_id.id)]
                                    }),
                                ]
                            }

                        env1['account.move'].create(move_vals)
                        env1.cr.commit()
                        logging.info("IMPORTATA FATTURA")



        if self.file3:
            #PRIMA NOTA POS

            env2 = self.getNewEnv()
            wb = xlrd.open_workbook(file_contents=b64decode(self.file3))

            sheet = wb.sheet_by_index(0)
            sheet.cell_value(0, 0)
            riga = 1

            crediti_v_clienti = env2['account.account'].search([('name', '=', 'CREDITI V/CLIENTI')], limit=1)
            unicredit_id = self.env['account.account'].search([('code', '=', '24/0005/0001')], limit=1)
            journal_varie = self.env['account.journal'].search([('name', '=', 'Operazioni varie')], limit=1)

            for row in range(0, sheet.nrows):
                if row >= 1:
                    logging.info("Fatto")
                    riga += 1
                    importo = 0
                    descrizione = ''
                    cliente = ''
                    punto_vendita = ''
                    for column in range(0, sheet.ncols):
                        cell = sheet.cell(row, column)
                        value = cell.value

                        if column == 0:
                            # Data
                            try:
                                data = xlrd.xldate_as_tuple(value, wb.datemode)
                                data = str(data[0]) + '-' + str(data[1]) + '-' + str(data[2])
                            except:
                                data = '2020-01-26'
                                logging.info('errore')
                        if column == 3:
                            importo = float(value)
                        if column == 4:
                            descrizione = value
                        if column == 5:
                            cliente = value
                        if column == 6:
                            if not 'MAG' in value:
                                punto_vendita = value[:3]
                            else:
                                punto_vendita = value[:6]



                    negozio_id = env2['pos.config'].search([('name', 'like', punto_vendita)], limit=1)


                    if negozio_id:


                        if not cliente or cliente == '':
                            partner_id = False
                        else:
                            partner_id = env2['res.partner'].search([('name', '=', cliente)], limit=1)
                            if not partner_id:
                                partner_id = env2['res.partner'].create({
                                    'name': cliente,
                                })


                        registro_negozio = False
                        for journal in negozio_id.journal_ids:
                            if 'POS' in journal.name:
                                registro_negozio = journal
                                break

                        if crediti_v_clienti:

                            move_vals = {
                                'date': data.replace('/', '-'),
                                'ref': descrizione,
                                'journal_id': registro_negozio.id if registro_negozio else journal_varie.id,
                                'partner_id': partner_id.id if partner_id else False,
                                'line_ids': [
                                    (0, 0, {
                                        'account_id': registro_negozio.default_credit_account_id.id,
                                        'debit': importo,
                                        'partner_id': partner_id.id if partner_id else False,
                                        'name': descrizione
                                    }),
                                    (0, 0, {
                                        'account_id': crediti_v_clienti.id,
                                        'credit': importo,
                                        'partner_id': partner_id.id if partner_id else False,
                                        'name': descrizione
                                    }),
                                ]
                            }

                            env2['account.move'].create(move_vals)
                            env2.cr.commit()


        if self.file4:
            #PRIMA NOTA BB

            env2 = self.getNewEnv()
            wb = xlrd.open_workbook(file_contents=b64decode(self.file4))

            sheet = wb.sheet_by_index(0)
            sheet.cell_value(0, 0)
            riga = 1

            crediti_v_clienti = env2['account.account'].search([('name', '=', 'CREDITI V/CLIENTI')], limit=1)
            unicredit_id = self.env['account.account'].search([('code', '=', '24/0005/0001')], limit=1)
            ritenute_id = self.env['account.account'].search([('code', '=', '18/0020/0050')], limit=1)
            journal_varie = self.env['account.journal'].search([('name', '=', 'UNICREDIT BANCA SPA')], limit=1)

            for row in range(0, sheet.nrows):
                if row >= 1:
                    logging.info("Fatto")
                    riga += 1
                    importo = 0
                    ritenuta = 0
                    bonifico = 0
                    descrizione = ''
                    cliente = ''
                    punto_vendita = ''
                    for column in range(0, sheet.ncols):
                        cell = sheet.cell(row, column)
                        value = cell.value

                        if column == 0:
                            # Data
                            try:
                                data = xlrd.xldate_as_tuple(value, wb.datemode)
                                data = str(data[0]) + '-' + str(data[1]) + '-' + str(data[2])
                            except:
                                data = '2020-01-26'
                                logging.info('errore')
                        if column == 3:
                            importo = float(value)
                        if column == 4:
                            ritenuta = float(value)
                        if column == 5:
                            bonifico = float(value)
                        if column == 7:
                            descrizione = value
                        if column == 6:
                            cliente = value



                    if not cliente or cliente == '':
                        partner_id = False
                    else:
                        partner_id = env2['res.partner'].search([('name', '=', cliente)], limit=1)
                        if not partner_id:
                            partner_id = env2['res.partner'].create({
                                'name': cliente,
                            })

                    if crediti_v_clienti:

                        if ritenuta > 0:
                            move_vals = {
                                'date': data.replace('/', '-'),
                                'ref': descrizione,
                                'journal_id': journal_varie.id,
                                'partner_id': partner_id.id if partner_id else False,
                                'line_ids': [
                                    (0, 0, {
                                        'account_id': unicredit_id.id,
                                        'debit': bonifico,
                                        'partner_id': partner_id.id if partner_id else False,
                                        'name': descrizione
                                    }),
                                    (0, 0, {
                                        'account_id': ritenute_id.id,
                                        'debit': ritenuta,
                                        'partner_id': partner_id.id if partner_id else False,
                                        'name': descrizione
                                    }),
                                    (0, 0, {
                                        'account_id': crediti_v_clienti.id,
                                        'credit': importo,
                                        'partner_id': partner_id.id if partner_id else False,
                                        'name': descrizione
                                    }),
                                ]
                            }
                        else:
                            move_vals = {
                                'date': data.replace('/', '-'),
                                'ref': descrizione,
                                'journal_id': journal_varie.id,
                                'partner_id': partner_id.id if partner_id else False,
                                'line_ids': [
                                    (0, 0, {
                                        'account_id': unicredit_id.id,
                                        'debit': bonifico,
                                        'partner_id': partner_id.id if partner_id else False,
                                        'name': descrizione
                                    }),
                                    (0, 0, {
                                        'account_id': crediti_v_clienti.id,
                                        'credit': importo,
                                        'partner_id': partner_id.id if partner_id else False,
                                        'name': descrizione
                                    }),
                                ]
                            }

                        env2['account.move'].create(move_vals)
                        env2.cr.commit()



        if self.file5:
            #PRIMA NOTA FIN

            env2 = self.getNewEnv()
            wb = xlrd.open_workbook(file_contents=b64decode(self.file5))

            sheet = wb.sheet_by_index(0)
            sheet.cell_value(0, 0)
            riga = 1

            crediti_v_clienti = env2['account.account'].search([('name', '=', 'CREDITI V/CLIENTI')], limit=1)
            agos_id = self.env['account.account'].search([('code', '=', '36/0005/0501')], limit=1)
            journal_varie = self.env['account.journal'].search([('name', '=', 'Operazioni varie')], limit=1)

            for row in range(0, sheet.nrows):
                if row >= 1:
                    logging.info("Fatto")
                    riga += 1
                    importo = 0
                    ritenuta = 0
                    bonifico = 0
                    descrizione = ''
                    cliente = ''
                    punto_vendita = ''
                    for column in range(0, sheet.ncols):
                        cell = sheet.cell(row, column)
                        value = cell.value

                        if column == 0:
                            # Data
                            try:
                                data = value.split('/')
                                data = str(data[2]) + '-' + str(data[1]) + '-' + str(data[0])
                            except Exception as e:
                                data = '2020-01-26'
                                logging.info('errore')
                        if column == 2:
                            descrizione += value
                        if column == 3:
                            descrizione += '- N° Finanziaria: ' + value
                        if column == 4:
                            descrizione += '- Commissione: ' + value
                        if column == 5:
                            cliente = value
                        if column == 6:
                            importo = float(value)
                        if column == 7:
                            descrizione += '- Tabella: ' + value


                    if not cliente or cliente == '':
                        partner_id = False
                    else:
                        partner_id = env2['res.partner'].search([('name', '=', cliente)], limit=1)
                        if not partner_id:
                            partner_id = env2['res.partner'].create({
                                'name': cliente,
                            })

                    if crediti_v_clienti:

                        move_vals = {
                            'date': data.replace('/', '-'),
                            'ref': descrizione,
                            'journal_id': journal_varie.id,
                            'partner_id': partner_id.id if partner_id else False,
                            'line_ids': [
                                (0, 0, {
                                    'account_id': agos_id.id,
                                    'debit': importo,
                                    'partner_id': partner_id.id if partner_id else False,
                                    'name': descrizione
                                }),
                                (0, 0, {
                                    'account_id': crediti_v_clienti.id,
                                    'credit': importo,
                                    'partner_id': partner_id.id if partner_id else False,
                                    'name': descrizione
                                }),
                            ]
                        }

                        env2['account.move'].create(move_vals)
                        env2.cr.commit()


        if self.file:
            #PRIMA NOTA CONTANTE ASSEGNI

            env2 = self.getNewEnv()
            wb = xlrd.open_workbook(file_contents=b64decode(self.file))
            sheet = wb.sheet_by_index(0)
            sheet.cell_value(0, 0)
            riga = 1

            crediti_v_clienti = env2['account.account'].search([('name', '=', 'CREDITI V/CLIENTI')], limit=1)
            unicredit_id = self.env['account.account'].search([('code', '=', '24/0005/0001')], limit=1)
            mantova_id = self.env['account.account'].search([('code', '=', '24/0005/0002')], limit=1)
            transitorio_id = self.env['account.account'].search([('code', '=', '41/0005/0501')], limit=1)
            journal_varie = self.env['account.journal'].search([('name', '=', 'Operazioni varie')], limit=1)

            for row in range(0, sheet.nrows):
                if row >= 1:
                    logging.info("Fatto")
                    riga += 1
                    move_vals = {}
                    tipo_movimento = 1 #1 = pagamento, #2 versamento
                    natura = 'contante' #assegni
                    importo = 0
                    dare = False
                    avere = False
                    descrizione = ''
                    cliente = ''
                    punto_vendita = ''
                    for column in range(0, sheet.ncols):
                        cell = sheet.cell(row, column)
                        value = cell.value

                        if column == 0:
                            #Data
                            data = xlrd.xldate_as_tuple(value, wb.datemode)
                            data = str(data[0]) + '-' + str(data[1]) + '-' + str(data[2])
                        if column == 1:
                            if value == 'Versamento':
                                tipo_movimento = 2
                        if column == 2:
                            if value == 'Assegno':
                                natura = 'assegno'
                        if column == 3:
                            importo = float(value)
                        if column == 6:
                            if value == '24/0005/0001':
                                dare = unicredit_id.id
                            if value == '24/0005/0002':
                                dare = mantova_id.id
                            if value == '41/0005/0501':
                                dare = transitorio_id.id
                        if column == 7:
                            if value != 'Conto Cassa':
                                avere = crediti_v_clienti.id
                        if column == 8:
                            descrizione = value
                        if column == 9:
                            cliente = value
                        if column == 10:
                            if not 'MAG' in value:
                                punto_vendita = value[:3]
                            else:
                                punto_vendita = value[:6]



                    negozio_id = env2['pos.config'].search([('name', 'like', punto_vendita)], limit=1)


                    if negozio_id:


                        if not cliente or cliente == '':
                            partner_id = False
                        else:
                            partner_id = env2['res.partner'].search([('name', '=', cliente)], limit=1)
                            if not partner_id:
                                partner_id = env2['res.partner'].create({
                                    'name': cliente,
                                })


                        registro_negozio = False
                        for journal in negozio_id.journal_ids:
                            if natura == 'contante':
                                if 'CONT' in journal.name:
                                    registro_negozio = journal
                                    if not dare:
                                        dare = journal.default_credit_account_id.id
                                    if not avere:
                                        avere = journal.default_credit_account_id.id
                                    break
                            if natura == 'assegno':
                                if 'ASS' in journal.name:
                                    registro_negozio = journal
                                    if not dare:
                                        dare = journal.default_credit_account_id.id,
                                    if not avere:
                                        avere = journal.default_credit_account_id.id
                                    break

                        if crediti_v_clienti:
                            if tipo_movimento == 2: #Versamento
                                move_vals = {
                                    'ref': 'Versamento Casse ' + negozio_id.name,
                                    'date': data.replace('/', '-'),
                                    'journal_id': journal_varie.id,
                                    'line_ids': [
                                        (0, 0, {
                                            'account_id': dare ,
                                            'debit': importo
                                        }),
                                        (0, 0, {
                                            'account_id': avere,
                                            'credit': importo
                                        })
                                    ]
                                }
                                move_id =env2['account.move'].create(move_vals)
                            else:
                                move_vals = {
                                    'date': data.replace('/', '-'),
                                    'ref': descrizione,
                                    'journal_id': registro_negozio.id if registro_negozio else journal_varie.id,
                                    # 'partner_id': partner_id.id if partner_id else False,
                                    'line_ids': [
                                        (0, 0, {
                                            'account_id': dare,
                                            'debit': importo,
                                            'partner_id': partner_id.id if partner_id else False,
                                            'name': descrizione
                                        }),
                                        (0, 0, {
                                            'account_id': avere,
                                            'credit': importo,
                                            'partner_id': partner_id.id if partner_id else False,
                                            'name': descrizione
                                        }),
                                    ]
                                }

                                env2['account.move'].create(move_vals)
                            env2.cr.commit()
                        else:
                            logging.info("ERRORE RIGA " +  str(riga))




        # json_load = json.loads(self.json)
        # counter = 1
        # env3 = self.getNewEnv()
        # #Anagrafica
        # for elem in json_load:
        #     anagrafica = elem['anagrafica']
        #     banche = elem['banche']
        #
        #     #Creo l'anagrafica se non esiste
        #     exist_anagrafica = env3['res.partner'].search([('name', '=', anagrafica['ragsoc'])], limit=1)
        #     state_id = env3['res.country.state'].search([('code', '=', anagrafica['prov']), ('country_id.name', '=', 'Italia')])
        #     country_id = env3['res.country'].search([('name', '=', 'Italia')])
        #
        #     bank_ids = []
        #     for banca in banche:
        #         exist_banca = env3['res.bank'].search([('name', '=', banca['rag_soc'])])
        #         payment = env3['account.payment.term'].search([('name', '=', banca['descrizione_pagamento'])])
        #         partner_bank = False
        #
        #         if not exist_banca:
        #             vals_banca = {
        #                 'name': banca['rag_soc'],
        #                 'abi': banca['idbanca'],
        #                 'cab': banca['idagenzia']
        #             }
        #             exist_banca = env3['res.bank'].create(vals_banca)
        #
        #         counter += 1
        #         bank_ids.append((0, 0, {
        #                                 'bank_id': exist_banca.id,
        #                                 'acc_number': banca['iban'] if 'iban' in banca else str(counter) }
        #                           ))
        #
        #
        #
        #     if not exist_anagrafica:
        #         try:
        #             vals_anagrafica = {
        #                 'name': anagrafica['ragsoc'],
        #                 'company_type': 'company',
        #                 'street': anagrafica['indirizzo'],
        #                 'zip': anagrafica['cap'],
        #                 'city': anagrafica['citta'],
        #                 'electronic_invoice_subjected': True if country_id and anagrafica['citta'] and anagrafica['indirizzo'] and state_id and anagrafica['piva'] and anagrafica['cap'] else False,
        #                 'vat': anagrafica['piva'].replace(' ', ''),
        #                 'phone': anagrafica['tel'],
        #                 'mobile': anagrafica['tel2'],
        #                 'state_id': state_id.id if state_id else False,
        #                 'country_id': country_id.id if country_id else False,
        #                 'bank_ids': bank_ids,
        #                 'supplier': True,
        #                 'property_payment_term_id': payment.id if payment else '',
        #                 'property_supplier_payment_term_id': payment.id if payment else ''
        #             }
        #             env3['res.partner'].create(vals_anagrafica)
        #             env3.cr.commit()
        #             logging.info("FATTO")
        #         except Exception as e:
        #             print(e)



        # """
        # Al Caricamento del piano dei Conti Leggo il contenuto del foglio excel e inizio
        # Ad elaborare i valori, caricando Macroaggregati, Aggregati, Conti
        # """
        # if self.file:
        #     wb = xlrd.open_workbook(file_contents=b64decode(self.file))
        #     sheet = wb.sheet_by_index(0)
        #     sheet.cell_value(0, 0)
        #
        #     for row in range(0, sheet.nrows):
        #         partner_vals = {}
        #         partner_to_update = []
        #         for column in range(0, sheet.ncols):
        #             cell = sheet.cell(row, column)
        #             value = cell.value
        #             if column == 2 and isinstance(value, str) and value:
        #                 #Nome
        #                 partner_vals['name'] = value.replace("'", ' ')
        #             if column == 3 and isinstance(value, str) and value:
        #                 #Città
        #                 partner_vals['city'] = value.replace("'", ' ')
        #             if column == 5 and value:
        #                 #Partita Iva
        #                 partner_vals['vat'] = 'IT' + value
        #                 partner_id = self.env.cr.execute("select id from res_partner where vat = '%s' " % value)
        #                 partner_id = self.env.cr.fetchall()
        #                 if partner_id:
        #                     #Aggiungo La Fatturazione
        #                     partner_to_update.append(partner_id[0][0])
        #
        #                     # if partner_id[0][1]:
        #                     #     # Aggiungo L'Intestazione
        #                     #     partner_to_update.append(partner_id[0][1])
        #                     #     child_ids = self.env.cr.execute("select id from res_partner where parent_id = '%s' " % partner_id[0][1])
        #                     #     child_ids = self.env.cr.fetchall()
        #                     #     if len(child_ids) > 2:
        #                     #         for child in child_ids:
        #                     #             partner_to_update.append(child[0])
        #                     #     else:
        #                     #         partner_to_update.append(child_ids[0][0])
        #
        #
        #             if column == 6 and isinstance(value, str) and value:
        #                 #Codice Fiscale
        #                 partner_vals['fiscalcode'] = value.replace(' ', '')
        #                 if len(partner_to_update) == 0:
        #                     #Cerco Per codice Fiscale
        #                     partner_id = self.env.cr.execute( "select id from res_partner where fiscalcode = '%s' " % value)
        #                     partner_id = self.env.cr.fetchall()
        #                     if partner_id:
        #                         # Aggiungo La Fatturazione
        #                         partner_to_update.append(partner_id[0][0])
        #
        #                         # if partner_id[0][1]:
        #                         #     # Aggiungo L'Intestazione
        #                         #     partner_to_update.append(partner_id[0][1])
        #                         #     child_ids = self.env.cr.execute("select id from res_partner where parent_id = '%s' " % partner_id[0][1])
        #                         #     child_ids = self.env.cr.fetchall()
        #                         #     if len(child_ids) > 2:
        #                         #         for child in child_ids:
        #                         #             partner_to_update.append(child[0])
        #                         #     else:
        #                         #         partner_to_update.append(child_ids[0][0])
        #             if column == 7 and isinstance(value, str) and value:
        #                 #Indirizzo
        #                 partner_vals['street'] = value.replace("'", ' ')
        #             if column == 8 and value:
        #                 #CAP
        #                 partner_vals['zip'] = value
        #             if column == 9 and value:
        #                 #Codice Destinatario o Pec
        #                 if '@' in value:
        #                     #PEC
        #                     partner_vals['pec_destinatario'] = value
        #                 else:
        #                     #SDI
        #                     partner_vals['codice_destinatario'] = value
        #             if column == 10 and value:
        #                 #EMAIL
        #                 partner_vals['email'] = value
        #
        #
        #
        #         # self.env.cr.execute("INSERT INTO danea_partner (name, city, vat, fiscalcode, street, zip, "
        #         #                     " pec_destinatario, codice_destinatario, email) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s') " %
        #         #                     (partner_vals['name'] if 'name' in partner_vals else '',
        #         #                      partner_vals['city'] if 'city' in partner_vals else '',
        #         #                      partner_vals['vat'] if 'vat' in partner_vals else '',
        #         #                      partner_vals['fiscalcode'] if 'fiscalcode' in partner_vals else '',
        #         #                      partner_vals['street'] if 'street' in partner_vals else '',
        #         #                      partner_vals['zip'] if 'zip' in partner_vals else '',
        #         #                      partner_vals['pec_destinatario'] if 'pec_destinatario' in partner_vals else '',
        #         #                      partner_vals[
        #         #                          'codice_destinatario'] if 'codice_destinatario' in partner_vals else '',
        #         #                      partner_vals['email'] if 'email' in partner_vals else ''))
        #         self.env.cr.commit()
        #
        #         if 'vat' in partner_vals:
        #             self.env.cr.execute("select * from res_partner where vat = '%s'" % (partner_vals['vat'], ))
        #             danea = self.env.cr.fetchall()
        #             if not danea:
        #                 self.env.cr.execute("INSERT INTO res_partner (e_invoice_detail_level, display_name, name, city, vat, fiscalcode, street, zip, "
        #                                     " pec_destinatario, codice_destinatario, email, country_id) VALUES ('%s', '%s', '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') " %
        #                                     (2,
        #                                      partner_vals['name'] if 'name' in partner_vals else '',
        #                                      partner_vals['name'] if 'name' in partner_vals else '',
        #                                      partner_vals['city'] if 'city' in partner_vals else '',
        #                                      partner_vals['vat'] if 'vat' in partner_vals else '',
        #                                      partner_vals['fiscalcode'] if 'fiscalcode' in partner_vals else '',
        #                                      partner_vals['street'] if 'street' in partner_vals else '',
        #                                      partner_vals['zip'] if 'zip' in partner_vals else '',
        #                                      partner_vals['pec_destinatario'] if 'pec_destinatario' in partner_vals else '',
        #                                      partner_vals[
        #                                          'codice_destinatario'] if 'codice_destinatario' in partner_vals else '',
        #                                      partner_vals['email'] if 'email' in partner_vals else '',
        #                                      109))
        #                 self.env.cr.commit()
        #
        #
        #         # #Aggiorno il cliente
        #         # if len(partner_to_update) > 0:
        #         #     for id in partner_to_update:
        #         #         try:
        #         #             self.env.cr.execute(
        #         #                 "UPDATE res_partner SET name = '%s', city = '%s', vat = '%s', fiscalcode = '%s', street = '%s', zip = '%s', "
        #         #                 " pec_destinatario = '%s', codice_destinatario = '%s', email = '%s' WHERE id = %s " %
        #         #                 (partner_vals['name'] if 'name' in partner_vals else '',
        #         #                  partner_vals['city'] if 'city' in partner_vals else '',
        #         #                  partner_vals['vat'] if 'vat' in partner_vals else '',
        #         #                  partner_vals['fiscalcode'] if 'fiscalcode' in partner_vals else '',
        #         #                  partner_vals['street'] if 'street' in partner_vals else '',
        #         #                  partner_vals['zip'] if 'zip' in partner_vals else '',
        #         #                  partner_vals['pec_destinatario'] if 'pec_destinatario' in partner_vals else '',
        #         #                  partner_vals['codice_destinatario'] if 'codice_destinatario' in partner_vals else '',
        #         #                  partner_vals['email'] if 'email' in partner_vals else '', id))
        #         #             self.env.cr.commit()
        #         #         except Exception as e:
        #         #             logging.info('cliente non aggiornato')
        #         #     logging.info('AGGIORNATO CLIENTE')
        #         #     self.env.cr.commit()



