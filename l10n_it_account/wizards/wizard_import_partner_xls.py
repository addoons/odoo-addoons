import logging
from base64 import b64decode

import xlrd

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class WizardImportPartnerXls(models.TransientModel):
    _name = 'wizard.import.partner.xls'

    name = fields.Char(default="Importa Clienti/Fornitori")
    file_xls_partners_import = fields.Binary()
    filename_file_xls_partners_import = fields.Char()

    def load_partners_from_xls(self):
        """
        Carica i clienti/fornitori tramite file xls sfruttando il seguente tracciato:
        tipologia, è un cliente/fornitore, codice cliente, ragione sociale, nome, cognome, via, cap, città, provincia,
        nazione, codice fiscale, partita iva, telefono cellulare, email, pec, sdi, termini di pagamento, azienda di appartenenza
        """
        if self.file_xls_partners_import:
            if not (self.filename_file_xls_partners_import.endswith('.xlsx') or self.filename_file_xls_partners_import.endswith('.xls')):
                raise UserError("Formato errato. Inserire un file XLS o XLSX.")
            # apre il foglio excel
            wb = xlrd.open_workbook(file_contents=b64decode(self.file_xls_partners_import))
            sheet = wb.sheet_by_index(0)

            record_non_importati = []
            # cicla righe e colonne in matrice
            data_map = {                        # campi da importare
                1: ['company_type', ""],        # tipologia
                2: ['customer', ""],            # è un cliente?
                3: ['supplier', ""],            # è un fornitore?
                4: ['ref', ""],                 # codice cliente
                5: ['name', ""],                # ragione sociale azienda
                6: ['firstname', ""],           # nome privato
                7: ['lastname', ""],            # cognome privato
                8: ['street', ""],              # Via
                9: ['zip', ""],                 # CAP
                10: ['city', ""],               # Città
                11: ['state_id', ""],           # Provincia
                12: ['country_id', ""],         # Nazione
                13: ['fiscalcode', ""],         # cod. fiscale
                14: ['vat', ""],                # P. IVA
                15: ['phone', ""],              # telefono
                16: ['mobile', ""],             # cellulare
                17: ['email', ""],              # E-Mail
                18: ['pec', ""],                # PEC
                19: ['sdi', ""],                # SDI
                20: ['payment_term_id', ""],    # Termini di Pagamento
                21: ['parent_id', ""],         # Azienda di appartenenza
            }
            for row in range(3, sheet.nrows):
                current_partner = {  # dizionario nuovo cliente
                    'ref': "",
                    'name': "",
                    'fiscalcode': "",
                    'vat': "",
                    'phone': "",
                    'email': "",
                    'mobile': "",
                    'street': "",
                    'zip': "",
                    'city': "",
                    'state_id': 0,
                    'country_id': 0,
                    'category_id': [],
                    'customer': False,
                    'supplier': False,
                    'property_payment_term_id': 0,
                    'property_supplier_payment_term_id': 0,
                    'company_type': "",
                    'parent_id': 0,
                    'firstname': '',
                    'lastname': '',
                    'payment_term_id': '',
                }
                for column in range(0, sheet.ncols):
                    if column + 1 in data_map.keys():
                        data_map[column + 1][1] = sheet.cell(row, column).value
                for key, value in data_map.items():
                    if value[0] in current_partner.keys():
                        if isinstance(value[1], float):
                            value[1] = str(int(value[1]))
                        if value[0] == 'category_id':
                            current_partner[value[0]].append(value[1])
                        else:
                            current_partner[value[0]] = value[1]

                # termini di pagamento
                metodo_pagamento_odoo = current_partner['payment_term_id']
                if metodo_pagamento_odoo:
                    payment_term_id = self.env['account.payment.term'].search(
                        [('name', '=', metodo_pagamento_odoo)])
                    if not payment_term_id:
                        payment_term_id = self.env['account.payment.term'].create({
                            'name': metodo_pagamento_odoo
                        })
                    if current_partner['supplier']:
                        current_partner['property_supplier_payment_term_id'] = payment_term_id.id
                    else:
                        current_partner['property_payment_term_id'] = payment_term_id.id
                del current_partner['payment_term_id']

                # gestione nazione
                country_name = current_partner['country_id']
                country_id = self.env['res.country'].search([('code', '=', current_partner['country_id'])])
                if country_id:
                    current_partner['country_id'] = country_id.id
                else:
                    current_partner['country_id'] = False

                # gestione provincia
                state_id = self.env['res.country.state'].search(
                    [('code', '=', current_partner['state_id']), ('country_id', '=', current_partner['country_id'])])
                if state_id:
                    current_partner['state_id'] = state_id.id
                else:
                    current_partner['state_id'] = False

                # gestione P. IVA e cod. fiscale
                if len(current_partner['vat']) > 0 and (len(current_partner['vat']) != 13 and len(current_partner['vat']) != 11):
                    del current_partner['vat']

                if not current_partner['vat'] and current_partner['fiscalcode'] and country_name == 'Italia':
                    current_partner['vat'] = 'IT' + current_partner['fiscalcode']

                # import come azienda
                if current_partner['company_type'] == 'Azienda':
                    if not current_partner['name']:
                        logging.info("SCARTATO riga numero " + str(row + 1))
                        record_non_importati.append(str(row + 1))
                        continue
                    current_partner['company_type'] = 'company'
                    current_partner['is_company'] = True
                    current_partner['electronic_invoice_subjected'] = True
                    # se azienda deve esserci almeno il firstname, altrimenti va
                    # in eccezione la funzione di partnerfirstname
                    current_partner['firstname'] = current_partner['name']

                # CASO PARTICOLARE: privato con p. iva
                if current_partner['company_type'] == 'Privato':
                    if not current_partner['firstname'] or not current_partner['lastname']:
                        logging.info("SCARTATO riga numero " + str(row + 1))
                        record_non_importati.append(str(row + 1))
                        continue
                    current_partner['company_type'] = 'person'
                    current_partner['name'] = current_partner['firstname'] + ' ' + current_partner['lastname']
                    parent_obj = self.env['res.partner'].search([('ref', '=', current_partner['parent_id'])])
                    if parent_obj:
                        current_partner['parent_id'] = parent_obj.id
                    if current_partner['vat']:
                        current_partner['electronic_invoice_subjected'] = True

                # creazione cliente SOLO se non già presente
                existing_partner = self.env['res.partner'].search([('ref', '=', current_partner['ref'])])
                try:
                    if current_partner['name']:
                        if not existing_partner:
                            self.env['res.partner'].create(current_partner)
                            if 'is_company' not in current_partner.keys():
                                logging.info('Creato: ' + data_map[6][1] + " " + data_map[7][1])
                            else:
                                logging.info('Creato: ' + data_map[5][1])
                        else:
                            existing_partner.write(current_partner)
                            logging.info('Aggiornato: ' + current_partner['name'])

                except ValidationError as e:
                    logging.info("SCARTATO " + current_partner['name'] + ": " + e.args[0])
                    record_non_importati.append(str(row + 1))
                    continue
                except TypeError as e:
                    logging.info("SCARTATO " + current_partner['name'] + ": " + e.args[0])
                    record_non_importati.append(str(row + 1))
                    continue
                except Exception as e:
                    if 'firstname' not in e.args[0]:
                        logging.info("SCARTATO " + data_map[5][1] + ": " + e.args[0])
                        record_non_importati.append(str(row + 1))
                    continue
            logging.info("-----------FINE IMPORT------------")
            logging.info("SCARTATI " + str(len(record_non_importati)) + " record nelle seguenti righe: " + str(record_non_importati))
        else:
            raise UserError("Inserire un file XLS o XLSX da cui importare i dati")

    def download_xls_partner(self):
        """
        Scarica un tracciato da compilare. Per inserire nuovi tracciati scaricabili inserirli in static/src/download
        """
        return {
            'type': 'ir.actions.act_url',
            'url': '/l10n_it_account/static/src/download/tracciato_partners.xlsx',
            'target': 'new',
        }