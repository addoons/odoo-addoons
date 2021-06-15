
import base64
import io
from io import BytesIO

import PyPDF2
from PyPDF2 import PdfFileMerger, PdfFileReader
from PyPDF2.generic import NameObject, BooleanObject

from odoo import api, fields, models, exceptions, _


class ComunicazioneLiquidazioneExportFile(models.TransientModel):
    _name = "comunicazione.liquidazione.export.file"
    _description = "Export VAT statement communication XML file"

    file_export = fields.Binary('File', readonly=True)
    file_pdf_export = fields.Binary('File PDF', readonly=True)
    name = fields.Char('File Name', readonly=True, default='liquidazione.xml')
    name_pdf = fields.Char('File Name', readonly=True, default='liquidazione.pdf')
    pdf_list = fields.Many2many('ir.attachment')

    def download_pdf(self):
        pdf_writer = PyPDF2.PdfFileWriter()
        self.env['comunicazione.liquidazione'].set_need_appearances_writer(pdf_writer)
        if "/AcroForm" in pdf_writer._root_object:
            # Acro form is form field, set needs appearances to fix printing issues
            pdf_writer._root_object["/AcroForm"].update(
                {NameObject("/NeedAppearances"): BooleanObject(True)})

        for file in self.pdf_list:
            pdf_reader = PyPDF2.PdfFileReader(io.BytesIO(base64.decodebytes(file.datas)), strict=False)

            if "/AcroForm" in pdf_reader.trailer["/Root"]:
                pdf_reader.trailer["/Root"]["/AcroForm"].update(
                    {NameObject("/NeedAppearances"): BooleanObject(True)})

            pageCount = pdf_reader.getNumPages()
            for iPage in range(0, pageCount):
                pdf_writer.addPage(pdf_reader.getPage(iPage))


        output_stream = BytesIO()
        pdf_writer.write(output_stream)
        self.file_pdf_export = base64.encodestring(output_stream.getvalue())



    @api.multi
    def export(self):

        comunicazione_ids = self._context.get('active_ids')
        if not comunicazione_ids:
            raise exceptions.Warning(_(
                "No communication selected"
            ))
        if len(comunicazione_ids) > 1:
            raise exceptions.Warning(_(
                'You can export only 1 communication at a time'
            ))

        for wizard in self:
            for comunicazione in self.env['comunicazione.liquidazione'].sudo().\
                    browse(comunicazione_ids):
                #Comunicazione Tracciato XML
                out = base64.encodestring(comunicazione.sudo().get_export_xml())
                wizard.sudo().write({'file_export': out})

                #Comunicazione Modulo PDF AdE LIPE
                pdf_lists = comunicazione.get_export_pdf()

                pdf_list_add = []
                for pdf in pdf_lists:
                    pdf_list_add.append((0,0,{
                        'name': 'filename',
                        'datas': base64.encodestring(pdf),
                        'mimetype': 'application/pdf'
                    }))

                wizard.sudo().write({'pdf_list': pdf_list_add})

            model_data_obj = self.env['ir.model.data']
            view_rec = model_data_obj.sudo().get_object_reference(
                'l10n_it_account',
                'wizard_liquidazione_export_file_exit'
            )
            view_id = view_rec and view_rec[1] or False

            self.download_pdf()

            return {
                'view_type': 'form',
                'view_id': [view_id],
                'view_mode': 'form',
                'res_model': 'comunicazione.liquidazione.export.file',
                'res_id': wizard.id,
                'type': 'ir.actions.act_window',
                'target': 'new',
            }

class ComunicazioneLiquidazioneAnnualeFile(models.TransientModel):
    _name = "comunicazione.liquidazione.annuale.file"
    _description = "Esporta dichiarazione IVA Annuale"

    file_pdf_iva_annuale_export = fields.Binary('File PDF (Annuale)', readonly=True)
    name_pdf = fields.Char('File Name', readonly=True, default='dichiarazione_iva_annuale.pdf')
    pdf_list = fields.Many2many('ir.attachment')



    def download_iva_annuale_pdf(self):
        pdf_writer = PyPDF2.PdfFileWriter()
        self.env['comunicazione.liquidazione'].set_need_appearances_writer(pdf_writer)
        if "/AcroForm" in pdf_writer._root_object:
            # Acro form is form field, set needs appearances to fix printing issues
            pdf_writer._root_object["/AcroForm"].update(
                {NameObject("/NeedAppearances"): BooleanObject(True)})

        for file in self.pdf_list_iva_annuale:
            pdf_reader = PyPDF2.PdfFileReader(io.BytesIO(base64.decodebytes(file.datas)), strict=False)

            if "/AcroForm" in pdf_reader.trailer["/Root"]:
                pdf_reader.trailer["/Root"]["/AcroForm"].update(
                    {NameObject("/NeedAppearances"): BooleanObject(True)})

            pageCount = pdf_reader.getNumPages()
            for iPage in range(0, pageCount):
                pdf_writer.addPage(pdf_reader.getPage(iPage))


        output_stream = BytesIO()
        pdf_writer.write(output_stream)
        self.file_pdf_iva_annuale_export = base64.encodestring(output_stream.getvalue())


    @api.multi
    def export(self):

        comunicazione_ids = self._context.get('active_ids')
        if not comunicazione_ids:
            raise exceptions.Warning(_(
                "No communication selected"
            ))
        if len(comunicazione_ids) > 1:
            raise exceptions.Warning(_(
                'You can export only 1 communication at a time'
            ))

        for wizard in self:
            for comunicazione in self.env['comunicazione.liquidazione'].sudo().browse(comunicazione_ids):
                # Comunicazione Modulo PDF AdE IVA ANNUALE
                pdf_lists_iva_annuale = comunicazione.get_export_iva_annuale_pdf()
                self.file_pdf_iva_annuale_export = base64.encodestring(pdf_lists_iva_annuale)


            model_data_obj = self.env['ir.model.data']
            view_rec = model_data_obj.sudo().get_object_reference(
                'l10n_it_account',
                'wizard_liquidazione_annuale_file_exit'
            )
            view_id = view_rec and view_rec[1] or False

            return {
                'view_type': 'form',
                'view_id': [view_id],
                'view_mode': 'form',
                'res_model': 'comunicazione.liquidazione.annuale.file',
                'res_id': wizard.id,
                'type': 'ir.actions.act_window',
                'target': 'new',
            }
