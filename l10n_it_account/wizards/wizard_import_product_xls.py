import logging
from base64 import b64decode

import xlrd

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class WizardImportProductXls(models.TransientModel):
    _name = 'wizard.import.product.xls'

    name = fields.Char(default="Importa Prodotti")
    file_xls_products_import = fields.Binary()
    filename_file_xls_products_import = fields.Char()

    def load_products_from_xls(self):
        """
        Carica i prodotti tramite file xls sfruttando il seguente tracciato:
        rif interno, nome, venduto/acquistato, categoria, unità di misura, peso, volume, iva vendite, iva acquisti,
        conto di costo/ricavo
        """

        if self.file_xls_products_import:
            if not (self.filename_file_xls_products_import.endswith('.xlsx') or self.filename_file_xls_products_import.endswith('.xls')):
                raise UserError("Formato errato. Inserire un file XLS o XLSX.")
            # apre il foglio excel
            wb = xlrd.open_workbook(file_contents=b64decode(self.file_xls_products_import))
            sheet = wb.sheet_by_index(0)
            record_non_importati = []
            # cicla righe e colonne in matrice
            for row in range(3, sheet.nrows):
                data_map = {                                    # campi da importare
                    1: ['default_code', ""],                    # rif. interno
                    2: ['name', ""],                            # nome
                    3: ['type', ""],                            # tipo
                    4: ['sale_ok', ""],                         # vendibile
                    5: ['purchase_ok', ""],                     # acquistabile
                    6: ['categ_id', ""],                        # categoria figlia
                    7: ['parent_categ_id', ""],                 # categoria madre
                    8: ['uom_id', ""],                          # unità di misura
                    9: ['weight', ""],                          # Peso
                    10: ['volume', ""],                         # Volume
                    11: ['taxes_id', ""],                       # IVA vendite
                    12: ['supplier_taxes_id', ""],              # IVA acquisti
                    13: ['property_account_income_id', ""],     # Conto ricavo
                    14: ['property_account_expense_id', ""],    # Conto costo
                }
                current_product = {  # dizionario nuovo prodotto
                    'default_code': "",
                    'name': "",
                    'sale_ok': False,
                    'purchase_ok': False,
                    'categ_id': 0,
                    'parent_categ_id': 0,
                    'uom_id': "",
                    'uom_po_id': "",
                    'weight': 0,
                    'volume': 0,
                    'taxes_id': 0,
                    'supplier_taxes_id': 0,
                    'type': "",
                    'property_account_income_id': '',
                    'property_account_expense_id': '',
                }
                for column in range(0, sheet.ncols):
                    if column + 1 in data_map.keys():
                        data_map[column + 1][1] = sheet.cell(row, column).value
                for key, value in data_map.items():
                    if value[0] in current_product.keys():
                        current_product[value[0]] = value[1]

                # gestione conti
                # COSTO
                if current_product['property_account_expense_id']:
                    account_expense_id = self.env['account.account'].search(
                        [('code', '=', str(int(current_product['property_account_expense_id'])))])
                    if account_expense_id:
                        current_product['property_account_expense_id'] = account_expense_id.id
                # RICAVO
                if current_product['property_account_income_id']:
                    account_income_id = self.env['account.account'].search(
                        [('code', '=', str(int(current_product['property_account_income_id'])))])
                    if account_income_id:
                        current_product['property_account_income_id'] = account_income_id.id

                # gestione tipologia
                if current_product['type'] == 'Consumabile':
                    current_product['type'] = 'consu'
                if current_product['type'] == 'Servizio':
                    current_product['type'] = 'service'
                if current_product['type'] == 'Immagazzinabile':
                    current_product['type'] = 'product'

                # converte valore sale_ok per Odoo
                if current_product['sale_ok'] and current_product['sale_ok'].lower() == 'x':
                    current_product['sale_ok'] = True
                else:
                    current_product['sale_ok'] = False
                # converte valore purchase_ok per Odoo
                if current_product['purchase_ok'] and current_product['purchase_ok'].lower() == 'x':
                    current_product['purchase_ok'] = True
                else:
                    current_product['purchase_ok'] = False

                # ricerca unità di misura
                if current_product['uom_id']:
                    uom_id = self.env['uom.uom'].search([('name', 'ilike', current_product['uom_id'])])
                    if uom_id:
                        current_product['uom_id'] = uom_id.id
                        current_product['uom_po_id'] = uom_id.id
                else:
                    del current_product['uom_id']
                    del current_product['uom_po_id']

                # gestione categoria madre
                if current_product['parent_categ_id']:
                    categ_id = self.env['product.category'].search([('name', '=', current_product['parent_categ_id'])])
                    if not categ_id:
                        categ_id = self.env['product.category'].create({'name': current_product['parent_categ_id']})

                    current_product['parent_categ_id'] = categ_id.id

                # gestione categoria figlia
                if current_product['categ_id']:
                    categ_id = self.env['product.category'].search([('name', '=', current_product['categ_id'])])

                    if not categ_id:
                        categ_id = self.env['product.category'].create({'name': current_product['categ_id'],
                                                                        'parent_id': current_product[
                                                                            'parent_categ_id']})
                    else:
                        categ_id.write({'name': current_product['categ_id'],
                                        'parent_id': current_product['parent_categ_id']})

                    current_product['categ_id'] = categ_id.id
                    del current_product['parent_categ_id']
                else:
                    current_product['categ_id'] = 1

                # gestione IVA
                if current_product['taxes_id']:
                    iva_vendite = self.env['account.tax'].search([('amount', '=', current_product['taxes_id']),
                                                                  ('type_tax_use', '=', 'sale')], limit=1)
                    if iva_vendite:
                        current_product['taxes_id'] = [(4, iva_vendite.id)]
                    else:
                        current_product['taxes_id'] = []

                if current_product['supplier_taxes_id']:
                    iva_acquisti = self.env['account.tax'].search([('amount', '=', current_product['supplier_taxes_id']),
                                                                   ('type_tax_use', '=', 'purchase')], limit=1)
                    if iva_acquisti:
                        current_product['supplier_taxes_id'] = [(4, iva_acquisti.id)]
                    else:
                        current_product['supplier_taxes_id'] = []

                # creazione prodotto SOLO se non già presente
                if current_product['default_code'] and isinstance(current_product['default_code'], float):
                    current_product['default_code'] = str(int(current_product['default_code']))
                if len(current_product['default_code']) > 0:
                    domain = [('default_code', '=', current_product['default_code'])]
                elif len(current_product['name']) > 0:
                    domain = [('name', '=', current_product['name'])]
                else:
                    logging.info('SCARTATO: riga numero ' + str(row + 1))
                    record_non_importati.append(str(row + 1))
                    continue
                existing_product = self.env['product.template'].search(domain)
                try:
                    if not existing_product:
                        self.env['product.template'].create(current_product)
                        logging.info('Prodotto Creato: ' + current_product['name'])
                    else:
                        existing_product.write(current_product)
                        logging.info('Prodotto Aggiornato: ' + current_product['name'])
                except ValidationError as e:
                    logging.info("SCARTATO " + current_product['name'] + ": " + e.args[0])
                    continue
                except TypeError as e:
                    logging.info("SCARTATO " + current_product['name'] + ": " + e.args[0])
                    continue
                except Exception as e:
                    logging.info("SCARTATO " + current_product['name'] + ": " + e.args[0])
                    continue
            logging.info("-----------FINE IMPORT------------")
            logging.info("SCARTATI " + str(len(record_non_importati)) + " record nelle seguenti righe: " + str(
                record_non_importati))
        else:
            raise UserError("Inserire un file XLS o XLSX da cui importare i dati")

    def download_xls_product(self):
        """
        Scarica un tracciato da compilare. Per inserire nuovi tracciati scaricabili inserirli in static/src/download
        """
        return {
            'type': 'ir.actions.act_url',
            'url': '/l10n_it_account/static/src/download/tracciato_prodotti.xlsx',
            'target': 'new',
        }
