import datetime

from odoo import models, fields, api
import logging

from xlrd import XLRDError

from odoo import api, models, fields
import base64
import xlrd

from odoo.exceptions import UserError


class WizardImportSaldi(models.TransientModel):

    _name = 'wizard.import.saldi'

    excel_import = fields.Binary(string="File Xls")
    conto_dare_id = fields.Many2one('account.account')
    conto_avere_id = fields.Many2one('account.account')
    move_date = fields.Date(default=datetime.date.today())
    riferimento = fields.Char()
    journal_id = fields.Many2one('account.journal')

    def import_saldi(self):
        try:
            wb = xlrd.open_workbook(file_contents=base64.decodebytes(self.excel_import))
            vals_keys = ['data', 'cliente', 'conto_dare', 'conto_avere', 'importo', 'causale']

            move_lines = []
            for sheet in wb.sheets():
                not_first_row = False
                row_counter = 0
                for row in range(sheet.nrows):
                    row_counter += 1
                    if not_first_row:
                        i = 0
                        vals = {}
                        for col in range(sheet.ncols):
                            if i < len(vals_keys):
                                vals[vals_keys[i]] = sheet.cell(row, col).value
                                i += 1
                        if vals['cliente']:
                            partner_name = vals['cliente'].split()
                            partner_name_reversed = ' '.join(reversed(partner_name))
                            partner = self.env['res.partner'].search(['|', ('name', '=ilike', vals['cliente']), ('name', '=ilike', partner_name_reversed)], limit=1)
                            print(partner_name_reversed)
                            if not partner:
                                if len(partner_name) >= 2:
                                    firstname = partner_name[0]
                                    lastname = ' '.join(partner_name[1:])
                                else:
                                    firstname = vals['cliente']
                                    lastname = False
                                partner = self.env['res.partner'].create({
                                    'firstname': firstname,
                                    'lastname': lastname,
                                    'company_type': 'person'
                                })
                                print('crea partner')
                            dare = 0
                            avere = 0
                            conto = False
                            if float(vals['importo']) > 0:
                                dare = abs(float(vals['importo']))
                                conto = self.conto_dare_id.id
                            else:
                                avere = abs(float(vals['importo']))
                                conto = self.conto_avere_id.id
                            move_lines.append((0,0, {
                                'partner_id': partner.id,
                                'account_id': conto,
                                'date_maturity': datetime.datetime.today(),
                                'debit': dare,
                                'credit': avere
                            }))

                    not_first_row = True
            account_move = self.env['account.move'].create({
                'date': self.move_date,
                'ref': self.riferimento,
                'journal_id': self.journal_id.id,
                'line_ids': move_lines
            })
            return {
                'name': account_move.ref,
                'type': 'ir.actions.act_window',
                'res_model': 'account.move',
                'view_mode': 'form',
                'target': 'self',
                'res_id': account_move.id
            }
        except XLRDError as e:
            logging.info(e)
            raise UserError('Il file selezionato non e\' in formato excel')
        except Exception as e:
            logging.info(e)
            raise UserError('Problemi durante l\'esportazione dei dati')

