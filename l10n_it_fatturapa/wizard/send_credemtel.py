import pysftp
import os
import zipfile
from datetime import datetime,timedelta
import base64
from odoo import api,fields,models
PATH = "/opt/"
FTP_PATH = "RX/MM062_WEB/"


class CronDocumentiFiscali(models.Model):
    _name = 'ir.cron.fiscal.documents'

    def export_fiscal_documents(self):
        invoice = self.env.ref("l10n_it_account.1").id
        credit_note = self.env.ref("l10n_it_account.2").id
        vat_company = self.env.user.company_id.vat
        adattamento_ora = timedelta(hours=2)
        now = datetime.now() + adattamento_ora
        timestamp = datetime.strftime(now,'%d%b%Y%H%M%S')

        exist_nc = False
        exist_f = False

        nome_zip_f = vat_company + '_F_' + timestamp + '.zip'
        zipf = zipfile.ZipFile(PATH + nome_zip_f, 'w')

        nome_zip_nc = vat_company + '_NC_' + timestamp + '.zip'
        zipnc = zipfile.ZipFile(PATH + nome_zip_nc, 'w')

        ftp_service = self.env['sdi.channel'].search([('channel_type', '=', 'ftp'), ('active_web_server', '=', True)])
        with pysftp.Connection(host=ftp_service.url, username=ftp_service.username,
                               password=ftp_service.password) as sftp:


            docs = self.env['fatturapa.attachment.out'].search([('exported_zip', '=', False)])
            for doc in docs:
                if doc.out_invoice_ids[0].fiscal_document_type_id.id == invoice:
                    zipf.writestr(self.name, base64.b64decode(self.datas))
                    doc.out_invoice_ids[0].fatturapa_state = 'sent'
                    self.exported_zip = 'sent'
                    exist_f = True
                if doc.out_invoice_ids[0].fiscal_document_type_id.id == credit_note:
                    zipnc.writestr(self.name, base64.b64decode(self.datas))
                    doc.out_invoice_ids[0].fatturapa_state = 'sent'
                    self.exported_zip = 'sent'
                    exist_nc = True

            zipf.close()
            zipnc.close()

            # if exist_f:
            #     sftp.put(PATH + nome_zip_f, FTP_PATH + nome_zip_f)
            #     os.remove(PATH + nome_zip_f)
            # if exist_nc:
            #     sftp.put(PATH + nome_zip_nc, FTP_PATH + nome_zip_nc)
            #     os.remove(PATH + nome_zip_nc)


class WizardDownloadZip(models.TransientModel):
    _name = 'wizard.send.credemtel'

    @api.multi
    def export_zip_fatture(self):
        self.ensure_one()
        attachments = self.env[self.env.context['active_model']].browse(
            self.env.context['active_ids'])
        invoice = self.env.ref("l10n_it_account.1").id
        credit_note = self.env.ref("l10n_it_account.2").id
        debit_note = self.env.ref("l10n_it_account.3").id
        fiscal_document_types = [invoice, credit_note, debit_note]
        vat_company = self.env.user.company_id.vat
        adattamento_ora = timedelta(hours=2)
        now = datetime.now() + adattamento_ora
        timestamp = datetime.strftime(now, '%d%b%Y%H%M%S')
        print("Connection succesfully stablished ... ")
        zip_summary = zipfile.ZipFile(PATH + 'fatture_' + timestamp + '.zip', 'w')
        for doc_type in fiscal_document_types:
            zip_pieno = False
            if len(attachments) > 0:
                if doc_type == 1:  # fattura
                    nome_zip = vat_company + '_F_' + timestamp + '.zip'
                    zipf = zipfile.ZipFile(PATH + nome_zip, 'w')
                elif doc_type == 4:  # nota credito
                    nome_zip = vat_company + '_NC_' + timestamp + '.zip'
                    zipf = zipfile.ZipFile(PATH + nome_zip, 'w')
                else:  # nota debito
                    nome_zip = vat_company + '_ND_' + timestamp + '.zip'
                    zipf = zipfile.ZipFile(PATH + nome_zip, 'w')
                if zipf:
                    for doc in attachments:
                        if doc.out_invoice_ids:
                            if doc.out_invoice_ids[0].fatturapa_state == 'ready' \
                                    and doc.out_invoice_ids[0].fiscal_document_type_id.id == doc_type:
                                zipf.writestr(doc.name,
                                              base64.b64decode(doc.datas))
                                zip_pieno = True
                    zipf.close()
                    if zip_pieno:
                        zip_summary.write(PATH + nome_zip, arcname=nome_zip)
                    os.remove(PATH + nome_zip)  # cancello lo zip locale

        return {
            'name': 'Report',
            'type': 'ir.actions.act_url',
            'url': "/my/download_files?path="+ PATH + "&name=" + 'fatture_' + timestamp + '.zip',
            'target': 'self',
        }
