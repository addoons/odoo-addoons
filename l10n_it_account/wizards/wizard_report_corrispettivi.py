from odoo import api, models, fields
from itertools import groupby


class GenerateReportCorrispettivi(models.AbstractModel):
    """
    REPORT CORRISPETTIVI RAGGRUPPATI PER IMPOSTA
    """
    _name = 'report.report_corrispettivi_imposte'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, receipts):
        sheet = workbook.add_worksheet('Corrispettivi')
        header = workbook.add_format({'bold': True, 'text_wrap': True, 'border': True, 'border_color': 'black'})

        # imposta l'header
        columns = ['Nr. Documento', 'Data', 'Cliente', 'Tipo Documento', 'Origine', 'Totale Lordo €', 'Totale Imponibile €', 'Totale IVA €']
        counter = 0
        for l in columns:
            sheet.set_column(0, counter, 30)
            sheet.write(0, counter, l, header)
            counter += 1

        # cerca le imposte da visualizzare
        # per ogni imposta aggiunge le colonne Imponibile e IVA
        tax_ids = self.env['account.tax'].search([('show_in_receipt_report', '=', True)], order='name desc')
        tax_totals = []
        for tax in tax_ids:
            label_imponibile = 'Imponibile ' + tax.name
            label_iva = 'Imposta ' + tax.name
            sheet.set_column(0, counter, 30)
            sheet.write(0, counter, label_imponibile, header)
            columns.append(label_imponibile)
            counter += 1
            sheet.set_column(0, counter, 30)
            sheet.write(0, counter, label_iva, header)
            columns.append(label_iva)
            counter += 1
            tax_totals.append({label_imponibile: 0.0, label_iva: 0.0})

        # cerca i corrispettivi all'interno del range di date, non bozza o cancellati
        domain = [('number', '!=', False), ('date_invoice', '>=', data['form']['from_date']),
                  ('date_invoice', '<=', data['form']['to_date']), ('corrispettivo', '=', True),
                  ('state', 'not in', ('draft', 'cancel'))]
        docs = self.env['account.invoice'].search(domain)
        receipts = sorted(docs, key=lambda i: i['date_invoice'])

        row = 1
        for receipt in receipts:
            counter = 0
            # gestione note di credito
            if not receipt.fiscal_document_type_id.code in ('TD04', 'TD08'):
                imponibile = receipt.amount_untaxed
                imposte = receipt.amount_tax
                lordo = receipt.amount_total
                documento = 'Corrispettivo'
            else:
                imponibile = receipt.amount_untaxed * (-1)
                imposte = receipt.amount_tax * (-1)
                lordo = receipt.amount_total * (-1)
                documento = 'Nota di credito'
            # per ogni corrispettivo aggiunge i dati della testata
            sheet.write(row, counter, receipt.number)
            sheet.write(row, counter + 1, receipt.date_invoice.strftime("%d/%m/%Y"))
            sheet.write(row, counter + 2, receipt.partner_id.name)
            sheet.write(row, counter + 3, documento)
            sheet.write(row, counter + 4, receipt.origin)
            sheet.write(row, counter + 5, lordo)
            sheet.write(row, counter + 6, imponibile)
            sheet.write(row, counter + 7, imposte)

            # per ogni imposta utilizzata nel corrispettivo
            # si aggiunge l'importo dell'imponibile e dell'imposta nelle colonne dell'imposta
            # Esempio: per l'imposta al 4% vengono inseriti i valori sotto le colonne del 4%
            for tax_line in receipt.tax_line_ids:
                tax_id = self.env['account.tax'].search([('name', '=', tax_line.name)])
                if tax_id and tax_id.show_in_receipt_report:
                    index_tax = counter + 8
                    for tax in tax_ids:
                        if tax.amount == tax_id.amount:
                            if columns[index_tax] == 'Imponibile ' + tax_id.name:
                                if documento != 'Corrispettivo':
                                    imponibile = tax_line.base * (-1)
                                    imposte = tax_line.amount_total * (-1)
                                else:
                                    imponibile = tax_line.base
                                    imposte = tax_line.amount_total
                                sheet.write(row, index_tax, imponibile)
                                sheet.write(row, index_tax + 1, imposte)
                                for total_list in tax_totals:
                                    if 'Imponibile ' + tax_id.name in total_list.keys():
                                        total_list['Imponibile ' + tax_id.name] += imponibile
                                        total_list['Imposta ' + tax_id.name] += imposte
                        index_tax += 2
            row += 1

        # TOTALI IMPOSTE
        counter = 7
        sheet.write(row, counter, 'TOTALE', header)
        for element in tax_totals:
            sheet.write(row, counter + 1, round(list(element.values())[0], 2), header)
            sheet.write(row, counter + 2, round(list(element.values())[1], 2), header)
            counter += 2


class WizardReportCorrispettivi(models.Model):
    _name = 'wizard.report.corrispettivi'

    # range di date
    date_start = fields.Date()
    date_end = fields.Date()

    @api.multi
    def generate_xls_report_corrispettivi(self):
        datas = {
            'model': 'account.invoice',
            'form': {'from_date': self.date_start,
                     'to_date': self.date_end},
        }

        return self.env.ref('l10n_it_account.report_corrispettivi_imposte').report_action(self, data=datas)