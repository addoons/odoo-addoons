# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)
from odoo import http
from odoo.http import Controller, route, request


class FatturaElettronicaController(Controller):

    @route([
        '/fatturapa/preview/<attachment_id>',
    ], type='http', auth='user', website=True)
    def pdf_preview(self, attachment_id, **data):
        attach = request.env['ir.attachment'].browse(int(attachment_id))
        html = attach.get_fattura_elettronica_preview()
        pdf = request.env['ir.actions.report']._run_wkhtmltopdf(
            [html])

        pdfhttpheaders = [
            ('Content-Type', 'application/pdf'), ('Content-Length', len(pdf)
                                                  )]
        return request.make_response(pdf, headers=pdfhttpheaders)


class DownloadController(Controller):

    @route([
        '/my/download_files',
    ], type='http', auth='public')
    def download_attachment(self, path, name):
        file_to_download = path + '/' + name
        file_name = name

        return http.send_file(file_to_download, filename=file_name, as_attachment=True)