# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)
import logging
import os
import zipfile
from datetime import datetime,timedelta
import base64

import paramiko

from odoo import api, models
import pysftp
from ftplib import FTP

PATH = "/tmp/"
#PATH = "C:\\Users\\frani\\AppData\\Local\\Temp"
FTP_PATH = "RX/MM062_WEB/"

SSH_KEY = b"""AAAAB3NzaC1yc2EAAAADAQABAAABgQC2ofSQ5PdJD+9+TTJBY6YNQJ7OSDYlffpaz+q4fmxjQXow+xZvrVUKQjWaoZLRdR38vccpgzE7gYl6wYJtGYrlruyOFv+4ssH54k8LWlRQRQuduv2Kg67ydErj7Yv8sbud6Z37rv/8zyT2rsmJ71K8+1s3h3kzKHr0s77ZyRQ1OP/xHGm6UzYmVhtBQa9JDPpZ8pBs6xxqqjXVcBM58z35bBJpMM9rf9nqiI83axbA972FdpGrk/dljvrcAcV4zeKvkW7qIHa3Rt010srbnYAuXHyRDI11QV2p/i6U94lLb9cVxkwKq3v1dhhMswu9tOKv4jIn/yJ1DDh9FgcX0TmjnjMoZB2PzB6G8Ll9gKQzSOEWlge+4B8j/RTIKJT8rsuChcg+dH4MSjdCeJbBNBVM7JKZPNdqr9dvaTmDLg9NfBz9tlet1GnxhrVCHhXmGBnstYn6ruknTKRVz6HyUhdMUlAhUD/IUXkDYMILdunxydyrFPM/qx0WzWTKntgRbX8="""


class CronDocumentiFiscali(models.Model):
    _name = 'ir.cron.fiscal.documents'



    def export_credemtel_fiscal_documents(self):

        invoice = self.env.ref("l10n_it_account.1").id
        credit_note = self.env.ref("l10n_it_account.2").id
        vat_company = self.env.user.company_id.vat
        adattamento_ora = timedelta(hours=2)
        now = datetime.now() + adattamento_ora
        timestamp = datetime.strftime(now, '%Y%m%d%H%M%S')

        exist_nc = False
        exist_f = False

        nome_zip_f = vat_company + '_F_' + timestamp + '.zip'
        zipf = zipfile.ZipFile(PATH + nome_zip_f, 'w')

        nome_zip_nc = vat_company + '_NC_' + timestamp + '.zip'
        zipnc = zipfile.ZipFile(PATH + nome_zip_nc, 'w')

        ftp_service = self.env['sdi.channel'].search([('channel_type', '=', 'ftp'), ('active_web_server', '=', True)])

        key = paramiko.RSAKey(data=base64.decodebytes(SSH_KEY))
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys.add(ftp_service.url, 'ssh-rsa', key)


        with pysftp.Connection(ftp_service.url, username=ftp_service.username, password=ftp_service.password, cnopts=cnopts) as ftp:


            docs = self.env['fatturapa.attachment.out'].search(['&', ('create_date', '>=', '2020-10-01 00:00:00'), ('exported_zip', '=', False)])
            logging.info(docs)
            for doc in docs:
                if doc.out_invoice_ids[0].fiscal_document_type_id.id == invoice:
                    zipf.writestr(doc.name, base64.b64decode(doc.datas))
                    doc.out_invoice_ids[0].fatturapa_state = 'sent'
                    doc.exported_zip = 1
                    exist_f = True
                if doc.out_invoice_ids[0].fiscal_document_type_id.id == credit_note:
                    zipnc.writestr(doc.name, base64.b64decode(doc.datas))
                    doc.out_invoice_ids[0].fatturapa_state = 'sent'
                    doc.exported_zip = 1
                    exist_nc = True

            zipf.close()
            zipnc.close()

            if exist_f:
                ftp.put(PATH + nome_zip_f, FTP_PATH + nome_zip_f)
                logging.info("File Caricato")
            if exist_nc:
                ftp.put(PATH + nome_zip_nc, FTP_PATH + nome_zip_nc)
                logging.info("File Caricato")

            ftp.close()


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
