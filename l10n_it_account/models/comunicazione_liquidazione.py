# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)
import logging

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from lxml import etree
from io import BytesIO
import PyPDF2
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject, NumberObject, createStringObject

from odoo.modules import get_module_resource

NS_IV = 'urn:www.agenziaentrate.gov.it:specificheTecniche:sco:ivp'
NS_XSI = 'http://www.w3.org/2001/XMLSchema-instance'
NS_LOCATION = 'urn:www.agenziaentrate.gov.it:specificheTecniche:sco:ivp'
NS_MAP = {
    'iv': NS_IV,
    'xsi': NS_XSI,
}
etree.register_namespace("vi", NS_IV)


class ComunicazioneLiquidazione(models.Model):
    _inherit = ['mail.thread']
    _name = 'comunicazione.liquidazione'
    _description = 'VAT statement communication'

    @api.model
    def _default_company(self):
        company_id = self._context.get(
            'company_id', self.env.user.company_id.id)
        return company_id

    @api.constrains('identificativo')
    def _check_identificativo(self):
        domain = [('identificativo', '=', self.identificativo)]
        dichiarazioni = self.search(domain)
        if len(dichiarazioni) > 1:
            raise ValidationError(
                _("Communication with identifier {} already exists"
                  ).format(self.identificativo))

    @api.multi
    def _compute_name(self):
        for dich in self:
            name = ""
            for quadro in dich.quadri_vp_ids:
                if not name:
                    period_type = ''
                    if quadro.period_type == 'month':
                        period_type = _('month')
                    else:
                        period_type = _('quarter')
                    name += '{} {}'.format(str(dich.year), period_type)
                if quadro.period_type == 'month':
                    name += ', {}'.format(str(quadro.month))
                else:
                    name += ', {}'.format(str(quadro.quarter))
            dich.name = name

    def _get_identificativo(self):
        dichiarazioni = self.search([])
        if dichiarazioni:
            return len(dichiarazioni) + 1
        else:
            return 1

    company_id = fields.Many2one(
        'res.company', string='Company', required=True,
        default=_default_company)
    identificativo = fields.Integer(string='Identifier',
                                    default=_get_identificativo)
    name = fields.Char(string='Name', compute="_compute_name")
    year = fields.Integer(string='Year', required=True, size=4)
    last_month = fields.Integer(string='Last month')
    liquidazione_del_gruppo = fields.Boolean(string='Group\'s statement')
    taxpayer_vat = fields.Char(string='Vat', required=True)
    controller_vat = fields.Char(string='Controller TIN')
    taxpayer_fiscalcode = fields.Char(string='Taxpayer Fiscalcode')
    declarant_different = fields.Boolean(
        string='Declarant different from taxpayer', default=True)
    declarant_fiscalcode = fields.Char(string='Declarant Fiscalcode')
    natura_giuridica = fields.Char()
    declarant_firstname = fields.Char()
    declarant_lastname = fields.Char()
    declarant_city = fields.Char()
    declarant_date = fields.Date()
    declarant_fiscalcode_company = fields.Char(string='Fiscalcode company')
    codice_carica_id = fields.Many2one('codice.carica', string='Role code')
    declarant_sign = fields.Boolean(string='Declarant sign', default=True)
    codice_ateco_id = fields.Many2one('ateco.category')

    delegate_fiscalcode = fields.Char(string='Delegate Fiscalcode')
    delegate_commitment = fields.Selection(
        [('1', 'Communication prepared by taxpayer'),
         ('2', 'Communication prepared by sender')],
        string='Commitment')
    delegate_sign = fields.Boolean(string='Delegate sign')
    date_commitment = fields.Date(string='Date commitment')
    quadri_vp_ids = fields.One2many(
        'comunicazione.liquidazione.vp', 'comunicazione_id',
        string="VP tables")
    iva_da_versare = fields.Float(
        string='VAT to pay', readonly=True)
    iva_a_credito = fields.Float(
        string='Credit VAT', readonly=True)

    @api.model
    def create(self, vals):
        comunicazione = super(ComunicazioneLiquidazione, self).create(vals)
        comunicazione._validate()
        return comunicazione

    @api.multi
    def write(self, vals):
        super(ComunicazioneLiquidazione, self).write(vals)
        for comunicazione in self:
            comunicazione._validate()
        return True

    @api.onchange('company_id')
    def onchange_company_id(self):
        if self.company_id:
            if self.company_id.partner_id.vat:
                self.taxpayer_vat = self.company_id.partner_id.vat[2:]
            else:
                self.taxpayer_vat = ''
            self.taxpayer_fiscalcode = \
                self.company_id.partner_id.fiscalcode


    def set_need_appearances_writer(self, writer):
        """
        Funzione usata dalla get_export_pdf per generare il report
        precompilato dell'AdE liquidazione periodica IVA
        """
        try:
            catalog = writer._root_object
            # get the AcroForm tree
            if "/AcroForm" not in catalog:
                writer._root_object.update({
                    NameObject("/AcroForm"): IndirectObject(len(writer._objects), 0, writer)})

            need_appearances = NameObject("/NeedAppearances")
            writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)
            return writer

        except Exception as e:
            print('set_need_appearances_writer() catch : ', repr(e))
            return writer

    def pdf_suffix_fields(self, page, sfx):
        for j in range(0, len(page['/Annots'])):
            writer_annot = page['/Annots'][j].getObject()
            writer_annot.update({
                NameObject("/T"): createStringObject(writer_annot.get('/T') + sfx)
            })

    def get_export_iva_annuale_pdf(self):
        """
        Funzione che compila il modulo standard della comunicazione periodica
        IVA dell'AdE, il modulo è presente nella cartella data/moduli_pdf
        """
        pdf_module_path = get_module_resource('l10n_it_account', 'data', 'moduli_pdf', 'iva_2021_modello_editabile.pdf')
        input_stream = open(pdf_module_path, "rb")

        pdf_reader = PyPDF2.PdfFileReader(input_stream, strict=False)

        if "/AcroForm" in pdf_reader.trailer["/Root"]:
            pdf_reader.trailer["/Root"]["/AcroForm"].update(
                {NameObject("/NeedAppearances"): BooleanObject(True)})

        pdf_writer = PyPDF2.PdfFileWriter()

        self.set_need_appearances_writer(pdf_writer)
        if "/AcroForm" in pdf_writer._root_object:
            # Acro form is form field, set needs appearances to fix printing issues
            pdf_writer._root_object["/AcroForm"].update(
                {NameObject("/NeedAppearances"): BooleanObject(True)})

        data_dict_pag1 = {
            'CODICE FISCALE1': self.taxpayer_vat,
            'partita_iva_2': self.taxpayer_vat,
            'denominazione_ragione_sociale': self.company_id.name,
            'codice_fiscale_sottoscrittore': self.declarant_fiscalcode,
            'codice_carica': self.codice_carica_id.code,
            'natura_giuridica': self.natura_giuridica,
            'firma1': 'X',
            'cognome': self.declarant_lastname,
            'nome': self.declarant_firstname,
            'data_nascita_day': self.declarant_date.day,
            'data_nascita_month': self.declarant_date.month,
            'data_nascita_year': self.declarant_date.year,
            'comune_nascita': self.declarant_city,
            'codice_fiscale_incaricato': self.delegate_fiscalcode,
            'firma2': 'X',
            'data_impegno': self.date_commitment,
        }

        data_dict_pag2 = {
            'CODICE FISCALE2': self.taxpayer_vat,
            'codice_ateco': self.codice_ateco_id.code.replace(".",""),
        }

        lipe_annuale = self.quadri_vp_ids[0].liquidazioni_ids[0]

        def get_imponibile_imposta_from_tag(tag):
            """
            Restituisce la somma imponibile e imposta delle aliquote
            con il tag passato
            """
            imponibile = 0
            imposta = 0
            #Verifica TAG righe di Debito
            for tax in lipe_annuale.debit_vat_account_line_ids:
                tax_ids = [tax.tax_id]
                is_gruppo = False
                if tax.tax_id.amount_type == 'group':
                    is_gruppo = True
                    #Imposta di gruppo
                    for child_tax in tax.tax_id.children_tax_ids:
                        tax_ids.append(child_tax)

                for tax in tax_ids:
                    for quadro in tax.dichiarazione_annuale_quadro:
                        if quadro.name == tag:
                            tax_datas = tax._compute_totals_tax({
                                'from_date': lipe_annuale.date_range_ids[0].date_start,
                                'to_date': lipe_annuale.date_range_ids[0].date_end,
                                'registry_type': 'customer'
                            })
                            imponibile += tax_datas[1]
                            imposta += tax_datas[2]

                            # Se la tassa è un gruppo prendo l'imposta dal figlio e l'imponibile dal padre
                            if is_gruppo:
                                tax_datas = tax_ids[0]._compute_totals_tax({
                                    'from_date': lipe_annuale.date_range_ids[0].date_start,
                                    'to_date': lipe_annuale.date_range_ids[0].date_end,
                                    'registry_type': 'customer'
                                })
                                imponibile += tax_datas[1]

            #Verifica TAG righe di Credito
            for tax in lipe_annuale.credit_vat_account_line_ids:
                tax_ids = [tax.tax_id]
                is_gruppo = False
                if tax.tax_id.amount_type == 'group':
                    # Imposta di gruppo
                    is_gruppo = True
                    for child_tax in tax.tax_id.children_tax_ids:
                        tax_ids.append(child_tax)

                for tax in tax_ids:
                    for quadro in tax.dichiarazione_annuale_quadro:
                        if quadro.name == tag:
                            tax_datas = tax._compute_totals_tax({
                                'from_date': lipe_annuale.date_range_ids[0].date_start,
                                'to_date': lipe_annuale.date_range_ids[0].date_end,
                                'registry_type': 'supplier'
                            })
                            imponibile += tax_datas[1]
                            imposta += tax_datas[2]

                            #Se la tassa è un gruppo prendo l'imposta dal figlio e l'imponibile dal padre
                            if is_gruppo:
                                tax_datas = tax_ids[0]._compute_totals_tax({
                                    'from_date': lipe_annuale.date_range_ids[0].date_start,
                                    'to_date': lipe_annuale.date_range_ids[0].date_end,
                                    'registry_type': 'supplier'
                                })
                                imponibile_imposta_principale = tax_datas[1]
                                imposta_totale = 0
                                for children in tax_ids[0].children_tax_ids:
                                    imposta_totale += children.amount

                                peso_imposta = tax.amount / imposta_totale
                                imponibile += imponibile_imposta_principale * peso_imposta


            return {'imponibile': round(imponibile, 2), 'imposta': round(imposta,2) }


        def get_sum_imponibile_imposta_from_tags(tags):
            """
            Restituisce la somma imponibile e la somma imposta
            di tutte le aliquote che hanno i tag passati
            """
            imponibile = 0
            imposta = 0
            for tag in tags:
                datas = get_imponibile_imposta_from_tag(tag)
                imponibile += datas['imponibile']
                imposta += datas['imposta']
            return {'imponibile': round(imponibile, 2) , 'imposta': round(imposta, 2) }


        #TOTALI
        VE24_IMPONIBILE = get_sum_imponibile_imposta_from_tags(['VE1','VE2','VE3','VE4','VE5','VE6','VE7','VE8','VE9','VE10','VE11','VE12','VE20','VE21','VE22','VE23'])['imponibile']
        VE24_IMPOSTA = get_sum_imponibile_imposta_from_tags(['VE1', 'VE2', 'VE3', 'VE4', 'VE5', 'VE6', 'VE7', 'VE8', 'VE9', 'VE10', 'VE11', 'VE12', 'VE20', 'VE21','VE22', 'VE23'])['imposta']
        VE30_VE38_IMPONIBILE = get_sum_imponibile_imposta_from_tags(['VE30','VE31','VE32','VE33','VE34','VE35','VE36','VE37','VE38'])['imponibile']
        VE39_IMPONIBILE = get_imponibile_imposta_from_tag('VE39')['imponibile']
        VE40_IMPONIBILE = get_imponibile_imposta_from_tag('VE40')['imponibile']
        VE50_IMPONIBILE = VE24_IMPONIBILE + VE30_VE38_IMPONIBILE - VE39_IMPONIBILE - VE40_IMPONIBILE

        data_dict_pag3 = {
            'CODICE FISCALE3': self.taxpayer_vat,
        }

        data_dict_pag4 = {
            'CODICE FISCALE4': self.taxpayer_vat,
        }

        data_dict_pag5 = {
            'CODICE FISCALE5': self.taxpayer_vat,
            'VE20': str(get_imponibile_imposta_from_tag('VE20')['imponibile']).replace('.', ','),
            'VE20_IMP': str(get_imponibile_imposta_from_tag('VE20')['imposta']).replace('.', ','),
            'VE21': str(get_imponibile_imposta_from_tag('VE21')['imponibile']).replace('.', ','),
            'VE21_IMP': str(get_imponibile_imposta_from_tag('VE21')['imposta']).replace('.', ','),
            'VE22': str(get_imponibile_imposta_from_tag('VE22')['imponibile']).replace('.', ','),
            'VE22_IMP': str(get_imponibile_imposta_from_tag('VE22')['imposta']).replace('.', ','),
            'VE23': str(get_imponibile_imposta_from_tag('VE23')['imponibile']).replace('.', ','),
            'VE23_IMP': str(get_imponibile_imposta_from_tag('VE23')['imposta']).replace('.', ','),
            'VE24': str(VE24_IMPONIBILE).replace('.', ','),
            'VE24_IMP': str(VE24_IMPOSTA).replace('.', ','),
            'VE26': str(VE24_IMPOSTA).replace('.', ','),
            'VE30/1': str(get_imponibile_imposta_from_tag('VE30/1')['imponibile']).replace('.', ','),
            'VE30/2': str(get_imponibile_imposta_from_tag('VE30/2')['imponibile']).replace('.', ','),
            'VE30/3': str(get_imponibile_imposta_from_tag('VE30/3')['imponibile']).replace('.', ','),
            'VE30/4': str(get_imponibile_imposta_from_tag('VE30/4')['imponibile']).replace('.', ','),
            'VE30/5': str(get_imponibile_imposta_from_tag('VE30/5')['imponibile']).replace('.', ','),
            'VE31': str(get_imponibile_imposta_from_tag('VE31')['imponibile']).replace('.', ','),
            'VE32': str(get_imponibile_imposta_from_tag('VE32')['imponibile']).replace('.', ','),
            'VE33': str(get_imponibile_imposta_from_tag('VE33')['imponibile']).replace('.', ','),
            'VE34': str(get_imponibile_imposta_from_tag('VE34')['imponibile']).replace('.', ','),
            'VE40': str(get_imponibile_imposta_from_tag('VE40')['imponibile']).replace('.', ','),
            'VE50': str(VE50_IMPONIBILE).replace('.', ','),
        }

        # TOTALI
        VE23_IMPONIBILE = get_sum_imponibile_imposta_from_tags(['VF1', 'VF2', 'VF3', 'VF4', 'VF5', 'VF6', 'VF7', 'VF8', 'VF9', 'VF10', 'VF11', 'VF12', 'VF13', 'VF14','VF15', 'VF16/1', 'VF16/2','VF17/1', 'VF18', 'VF19', 'VF20', 'VF21/1', 'VF22'])['imponibile']
        VE23_IMPOSTA = get_sum_imponibile_imposta_from_tags( ['VF1', 'VF2', 'VF3', 'VF4', 'VF5', 'VF6', 'VF7', 'VF8', 'VF9', 'VF10', 'VF11', 'VF12', 'VF13', 'VF14'])['imposta']
        VF25_IMPOSTA = VE23_IMPOSTA

        data_dict_pag6 = {
            'CODICE FISCALE6': self.taxpayer_vat,
            'VF1': str(get_imponibile_imposta_from_tag('VF1')['imponibile']).replace('.', ','),
            'VF1_IMP': str(get_imponibile_imposta_from_tag('VF1')['imposta']).replace('.', ','),
            'VF2': str(get_imponibile_imposta_from_tag('VF2')['imponibile']).replace('.', ','),
            'VF2_IMP': str(get_imponibile_imposta_from_tag('VF2')['imposta']).replace('.', ','),
            'VF3': str(get_imponibile_imposta_from_tag('VF3')['imponibile']).replace('.', ','),
            'VF3_IMP': str(get_imponibile_imposta_from_tag('VF3')['imposta']).replace('.', ','),
            'VF4': str(get_imponibile_imposta_from_tag('VF4')['imponibile']).replace('.', ','),
            'VF4_IMP': str(get_imponibile_imposta_from_tag('VF4')['imposta']).replace('.', ','),
            'VF5': str(get_imponibile_imposta_from_tag('VF5')['imponibile']).replace('.', ','),
            'VF5_IMP': str(get_imponibile_imposta_from_tag('VF5')['imposta']).replace('.', ','),
            'VF6': str(get_imponibile_imposta_from_tag('VF6')['imponibile']).replace('.', ','),
            'VF6_IMP': str(get_imponibile_imposta_from_tag('VF6')['imposta']).replace('.', ','),
            'VF7': str(get_imponibile_imposta_from_tag('VF7')['imponibile']).replace('.', ','),
            'VF7_IMP': str(get_imponibile_imposta_from_tag('VF7')['imposta']).replace('.', ','),
            'VF8': str(get_imponibile_imposta_from_tag('VF8')['imponibile']).replace('.', ','),
            'VF8_IMP': str(get_imponibile_imposta_from_tag('VF8')['imposta']).replace('.', ','),
            'VF9': str(get_imponibile_imposta_from_tag('VF9')['imponibile']).replace('.', ','),
            'VF9_IMP': str(get_imponibile_imposta_from_tag('VF9')['imposta']).replace('.', ','),
            'VF10': str(get_imponibile_imposta_from_tag('VF10')['imponibile']).replace('.', ','),
            'VF10_IMP': str(get_imponibile_imposta_from_tag('VF10')['imposta']).replace('.', ','),
            'VF11': str(get_imponibile_imposta_from_tag('VF11')['imponibile']).replace('.', ','),
            'VF11_IMP': str(get_imponibile_imposta_from_tag('VF11')['imposta']).replace('.', ','),
            'VF12': str(get_imponibile_imposta_from_tag('VF12')['imponibile']).replace('.', ','),
            'VF12_IMP': str(get_imponibile_imposta_from_tag('VF12')['imposta']).replace('.', ','),
            'VF13': str(get_imponibile_imposta_from_tag('VF13')['imponibile']).replace('.', ','),
            'VF13_IMP': str(get_imponibile_imposta_from_tag('VF13')['imposta']).replace('.', ','),
            'VF14': str(get_imponibile_imposta_from_tag('VF14')['imponibile']).replace('.', ','),
            'VF14_IMP': str(get_imponibile_imposta_from_tag('VF14')['imposta']).replace('.', ','),
            'VF15': str(get_imponibile_imposta_from_tag('VF15')['imponibile']).replace('.', ','),
            'VF16/1': str(get_imponibile_imposta_from_tag('VF16/1')['imponibile']).replace('.', ','),
            'VF16/2': str(get_imponibile_imposta_from_tag('VF16/2')['imponibile']).replace('.', ','),
            'VF17/1': str(get_imponibile_imposta_from_tag('VF17/1')['imponibile']).replace('.', ','),
            'VF17/2': str(get_imponibile_imposta_from_tag('VF17/2')['imponibile']).replace('.', ','),
            'VF18': str(get_imponibile_imposta_from_tag('VF18')['imponibile']).replace('.', ','),
            'VF19': str(get_imponibile_imposta_from_tag('VF19')['imponibile']).replace('.', ','),
            'VF20': str(get_imponibile_imposta_from_tag('VF20')['imponibile']).replace('.', ','),
            'VF21/1': str(get_imponibile_imposta_from_tag('VF21/1')['imponibile']).replace('.', ','),
            'VF21/2': str(get_imponibile_imposta_from_tag('VF21/2')['imponibile']).replace('.', ','),
            'VF22': str(get_imponibile_imposta_from_tag('VF22')['imponibile']).replace('.', ','),
            'VF23': str(VE23_IMPONIBILE).replace('.', ','),
            'VF23_IMP': str(VE23_IMPOSTA).replace('.', ','),
            'VF25': str(VF25_IMPOSTA).replace('.', ','),
            'VF26/1': str(get_imponibile_imposta_from_tag('VF26/1')['imponibile']).replace('.', ','),
            'VF26/2': str(get_imponibile_imposta_from_tag('VF26/1')['imposta']).replace('.', ','),
            'VF26/3': str(get_imponibile_imposta_from_tag('VF26/3')['imponibile']).replace('.', ','),
            'VF26/4': str(get_imponibile_imposta_from_tag('VF26/3')['imposta']).replace('.', ','),
            'VF26/5': str(get_imponibile_imposta_from_tag('VF26/5')['imponibile']).replace('.', ','),
            'VF26/6': str(get_imponibile_imposta_from_tag('VF26/5')['imposta']).replace('.', ','),
        }


        data_dict_pag7 = {
            'CODICE FISCALE7': self.taxpayer_vat,
            'VF71': str(VF25_IMPOSTA).replace('.', ','),
        }

        #TOTALI
        VE19_IMPOSTA = get_sum_imponibile_imposta_from_tags( ['VJ1', 'VJ2', 'VJ3', 'VJ4', 'VJ5', 'VJ6', 'VJ7', 'VJ8', 'VJ9', 'VJ10', 'VJ11', 'VJ12', 'VJ13', 'VJ14','VJ15', 'VJ16', 'VJ17', 'VJ18'])['imposta']
        VJ19_IMPOSTA = get_sum_imponibile_imposta_from_tags( ['VJ1', 'VJ2', 'VJ3', 'VJ4', 'VJ5', 'VJ6', 'VJ7', 'VJ8', 'VJ9', 'VJ10', 'VJ11', 'VJ12', 'VJ13', 'VJ14','VJ15', 'VJ16', 'VJ17', 'VJ18'])['imposta']


        data_dict_pag8 = {
            'CODICE FISCALE8': self.taxpayer_vat,
            'VJ1': str(get_imponibile_imposta_from_tag('VJ1')['imponibile']).replace('.', ','),
            'VJ1_IMP': str(get_imponibile_imposta_from_tag('VJ1')['imposta']).replace('.', ','),
            'VJ2': str(get_imponibile_imposta_from_tag('VJ2')['imponibile']).replace('.', ','),
            'VJ2_IMP': str(get_imponibile_imposta_from_tag('VJ2')['imposta']).replace('.', ','),
            'VJ3': str(get_imponibile_imposta_from_tag('VJ3')['imponibile']).replace('.', ','),
            'VJ3_IMP': str(get_imponibile_imposta_from_tag('VJ3')['imposta']).replace('.', ','),
            'VJ4': str(get_imponibile_imposta_from_tag('VJ4')['imponibile']).replace('.', ','),
            'VJ4_IMP': str(get_imponibile_imposta_from_tag('VJ4')['imposta']).replace('.', ','),
            'VJ5': str(get_imponibile_imposta_from_tag('VJ5')['imponibile']).replace('.', ','),
            'VJ5_IMP': str(get_imponibile_imposta_from_tag('VJ5')['imposta']).replace('.', ','),
            'VJ6': str(get_imponibile_imposta_from_tag('VJ6')['imponibile']).replace('.', ','),
            'VJ6_IMP': str(get_imponibile_imposta_from_tag('VJ6')['imposta']).replace('.', ','),
            'VJ7': str(get_imponibile_imposta_from_tag('VJ7')['imponibile']).replace('.', ','),
            'VJ7_IMP': str(get_imponibile_imposta_from_tag('VJ7')['imposta']).replace('.', ','),
            'VJ8': str(get_imponibile_imposta_from_tag('VJ8')['imponibile']).replace('.', ','),
            'VJ8_IMP': str(get_imponibile_imposta_from_tag('VJ8')['imposta']).replace('.', ','),
            'VJ9': str(get_imponibile_imposta_from_tag('VJ9')['imponibile']).replace('.', ','),
            'VJ9_IMP': str(get_imponibile_imposta_from_tag('VJ9')['imposta']).replace('.', ','),
            'VJ10': str(get_imponibile_imposta_from_tag('VJ10')['imponibile']).replace('.', ','),
            'VJ10_IMP': str(get_imponibile_imposta_from_tag('VJ10')['imposta']).replace('.', ','),
            'VJ11': str(get_imponibile_imposta_from_tag('VJ11')['imponibile']).replace('.', ','),
            'VJ11_IMP': str(get_imponibile_imposta_from_tag('VJ11')['imposta']).replace('.', ','),
            'VJ12': str(get_imponibile_imposta_from_tag('VJ12')['imponibile']).replace('.', ','),
            'VJ12_IMP': str(get_imponibile_imposta_from_tag('VJ12')['imposta']).replace('.', ','),
            'VJ13': str(get_imponibile_imposta_from_tag('VJ13')['imponibile']).replace('.', ','),
            'VJ13_IMP': str(get_imponibile_imposta_from_tag('VJ13')['imposta']).replace('.', ','),
            'VJ14': str(get_imponibile_imposta_from_tag('VJ14')['imponibile']).replace('.', ','),
            'VJ14_IMP': str(get_imponibile_imposta_from_tag('VJ14')['imposta']).replace('.', ','),
            'VJ15': str(get_imponibile_imposta_from_tag('VJ15')['imponibile']).replace('.', ','),
            'VJ15_IMP': str(get_imponibile_imposta_from_tag('VJ15')['imposta']).replace('.', ','),
            'VJ16': str(get_imponibile_imposta_from_tag('VJ16')['imponibile']).replace('.', ','),
            'VJ16_IMP': str(get_imponibile_imposta_from_tag('VJ16')['imposta']).replace('.', ','),
            'VJ17': str(get_imponibile_imposta_from_tag('VJ17')['imponibile']).replace('.', ','),
            'VJ17_IMP': str(get_imponibile_imposta_from_tag('VJ17')['imposta']).replace('.', ','),
            'VJ18': str(get_imponibile_imposta_from_tag('VJ18')['imponibile']).replace('.', ','),
            'VJ18_IMP': str(get_imponibile_imposta_from_tag('VJ18')['imposta']).replace('.', ','),
            'VJ19': str(VJ19_IMPOSTA).replace('.', ','),
        }

        from_date = str(self.year) + '-01-01'
        to_date = str(self.year) + '-12-31'
        liquidazioni_anno = self.env['account.vat.period.end.statement'].sudo().search([('date', '>=', from_date), ('date', '<=', to_date), ('state', '!=', 'draft')])

        data_dict_pag9 = {
            'CODICE FISCALE9': self.taxpayer_vat,
            'VH1C':0,
            'VH1D': 0,
            'VH2C': 0,
            'VH2D': 0,
            'VH3C': 0,
            'VH3D': 0,
            'VH4C': 0,
            'VH4D': 0,
            'VH5C': 0,
            'VH5D': 0,
            'VH6C': 0,
            'VH6D': 0,
            'VH7C':0,
            'VH7D': 0,
            'VH8C': 0,
            'VH8D': 0,
            'VH9C': 0,
            'VH9D': 0,
            'VH10C': 0,
            'VH10D': 0,
            'VH11C': 0,
            'VH11D': 0,
            'VH12C': 0,
            'VH12D': 0,
            'VH13C': 0,
            'VH13D': 0,
            'VH14C': 0,
            'VH14D': 0,
            'VH15C': 0,
            'VH15D': 0,
            'VH16C': 0,
            'VH16D': 0,
            'VH17': 0,
            'VH17_M': 1,
        }

        VL8 = 0

        for liquidazione in liquidazioni_anno:
            #debit = self.env['report.l10n_it_account.vat_statement'].sudo()._get_account_vat_amounts('debit', liquidazione.debit_vat_account_line_ids)
            #credit = self.env['report.l10n_it_account.vat_statement'].sudo()._get_account_vat_amounts('credit',liquidazione.credit_vat_account_line_ids)
            #debit_amount = 0
            #credit_amount = 0
            #for account in debit:
             #   debit_amount = debit[account]['amount']
            #for account in credit:
             #   credit_amount = credit[account]['amount']

            if liquidazione.date.month == 1:
                #Gennaio
                somma = liquidazione.authority_vat_amount
                if somma < 0:
                    data_dict_pag9['VH1C'] = abs(somma)
                else:
                    data_dict_pag9['VH1D'] = abs(somma)

                #VL8, VERIFICA SE CI SONO CREDITI ANNO PRECEDENTE
                VL8 = liquidazione.previous_credit_vat_amount

            if liquidazione.date.month == 2:
                #Febbraio
                somma = liquidazione.authority_vat_amount
                if somma < 0:
                    data_dict_pag9['VH2C'] = abs(somma)
                else:
                    data_dict_pag9['VH2D'] = abs(somma)
            if liquidazione.date.month == 3:
                #Marzo
                somma = liquidazione.authority_vat_amount
                if somma < 0:
                    data_dict_pag9['VH3C'] = abs(somma)
                else:
                    data_dict_pag9['VH3D'] = abs(somma)
            if liquidazione.date.month == 4:
                #Aprile
                somma = liquidazione.authority_vat_amount
                if somma < 0:
                    data_dict_pag9['VH5C'] = abs(somma)
                else:
                    data_dict_pag9['VH5D'] = abs(somma)
            if liquidazione.date.month == 5:
                #Maggio
                somma = liquidazione.authority_vat_amount
                if somma < 0:
                    data_dict_pag9['VH6C'] = abs(somma)
                else:
                    data_dict_pag9['VH6D'] = abs(somma)
            if liquidazione.date.month == 6:
                #Giugno
                somma = liquidazione.authority_vat_amount
                if somma < 0:
                    data_dict_pag9['VH7C'] = abs(somma)
                else:
                    data_dict_pag9['VH7D'] = abs(somma)
            if liquidazione.date.month == 7:
                #Luglio
                somma = liquidazione.authority_vat_amount
                if somma < 0:
                    data_dict_pag9['VH9C'] = abs(somma)
                else:
                    data_dict_pag9['VH9D'] = abs(somma)
            if liquidazione.date.month == 8:
                #Agosto
                somma = liquidazione.authority_vat_amount
                if somma < 0:
                    data_dict_pag9['VH10C'] = abs(somma)
                else:
                    data_dict_pag9['VH10D'] = abs(somma)
            if liquidazione.date.month == 9:
                #Settembre
                somma = liquidazione.authority_vat_amount
                if somma < 0:
                    data_dict_pag9['VH11C'] = abs(somma)
                else:
                    data_dict_pag9['VH11D'] = abs(somma)
            if liquidazione.date.month == 10:
                #Ottobre
                somma = liquidazione.authority_vat_amount
                if somma < 0:
                    data_dict_pag9['VH13C'] = abs(somma)
                else:
                    data_dict_pag9['VH13D'] = abs(somma)
            if liquidazione.date.month == 11:
                #Novembre
                somma = liquidazione.authority_vat_amount
                if somma < 0:
                    data_dict_pag9['VH14C'] = abs(somma)
                else:
                    data_dict_pag9['VH14D'] = abs(somma)
            if liquidazione.date.month == 12:
                #Dicembre
                somma = liquidazione.authority_vat_amount
                if somma < 0:
                    data_dict_pag9['VH15C'] = abs(somma)
                else:
                    data_dict_pag9['VH15D'] = abs(somma)

                #VERIFICA ACCONTI PER TAG VH17
                for line in liquidazione.generic_vat_account_line_ids:
                    data_dict_pag9['VH17'] = str(abs(line.amount)).replace(".",  ",")

        #Trimestri, questo blocco solo per i trimestrali
        #aggiugere un flag in LIPE IVA
        #data_dict_pag9['VH4C'] = data_dict_pag9['VH1C'] + data_dict_pag9['VH2C'] + data_dict_pag9['VH3C']
        #data_dict_pag9['VH4D'] = data_dict_pag9['VH1D'] + data_dict_pag9['VH2D'] + data_dict_pag9['VH3D']
        #data_dict_pag9['VH8C'] = data_dict_pag9['VH5C'] + data_dict_pag9['VH6C'] + data_dict_pag9['VH7C']
        #data_dict_pag9['VH8D'] = data_dict_pag9['VH5D'] + data_dict_pag9['VH6D'] + data_dict_pag9['VH7D']
        #data_dict_pag9['VH12C'] = data_dict_pag9['VH9C'] + data_dict_pag9['VH10C'] + data_dict_pag9['VH11C']
        #data_dict_pag9['VH12D'] = data_dict_pag9['VH9D'] + data_dict_pag9['VH10D'] + data_dict_pag9['VH11D']
        #data_dict_pag9['VH16C'] = data_dict_pag9['VH13C'] + data_dict_pag9['VH14C'] + data_dict_pag9['VH15C']
        #data_dict_pag9['VH16D'] = data_dict_pag9['VH13D'] + data_dict_pag9['VH14D'] + data_dict_pag9['VH15D']


        VL3 = (VE19_IMPOSTA + VE24_IMPOSTA) - VF25_IMPOSTA
        VL4 = abs(VF25_IMPOSTA - (VE19_IMPOSTA + VE24_IMPOSTA))
        if VL3 > 0:
            VL4 = 0

        data_dict_pag10 = {
            'CODICE FISCALE10': self.taxpayer_vat,
        }

        data_dict_pag11 = {
            'CODICE FISCALE11': self.taxpayer_vat,
            'VL1': str(VE19_IMPOSTA + VE24_IMPOSTA).replace('.', ','),
            'VL2': str(VF25_IMPOSTA).replace('.', ','),
            'VL3': str(VL3).replace('.', ','),
            'VL4': str(VL4).replace('.', ','),
            'VL8': str(VL8).replace('.', ','),
            'VL30/2': str(VL3).replace('.', ','),
        }

        quadro_vp_id = self.quadri_vp_ids[0]

        data_dict_pag12 = {
            # 'CODICE FISCALE12': self.taxpayer_vat,
            # 'CODICE_FISCALE_LIPE': self.taxpayer_fiscalcode,
            # 'MODULO_N': 1,
            # 'MESE_LIPE': str(quadro_vp_id.month).zfill(2) if quadro_vp_id.period_type == 'month' else '',
            # 'TRIMESTRE': str(quadro_vp_id.quarter).zfill(2) if quadro_vp_id.period_type == 'quarter' else '',
            # 'SUBFORNITURE': quadro_vp_id.subcontracting,
            # 'EVENTI_ECCEZIONALI': quadro_vp_id.exceptional_events,
            # 'OPERAZIONI_STRAORDINARIE': '',
            # 'ACCONTO_DOVUTO': str(quadro_vp_id.metodo_acconto_dovuto),
            # 'VP2': str(quadro_vp_id.imponibile_operazioni_attive).replace('.', ' '),
            # 'VP3': str(quadro_vp_id.imponibile_operazioni_passive).replace('.', ' '),
            # 'VP4': str(quadro_vp_id.iva_esigibile).replace('.', ' '),
            # 'VP5': str(quadro_vp_id.iva_detratta).replace('.', ' '),
            # 'VP6/1': str(quadro_vp_id.iva_dovuta_debito).replace('.', ' '),
            # 'VP6/2': str(quadro_vp_id.iva_dovuta_credito).replace('.', ' '),
            # 'VP7': str(quadro_vp_id.debito_periodo_precedente).replace('.', ' '),
            # 'VP8': str(quadro_vp_id.credito_periodo_precedente).replace('.', ' '),
            # 'VP9': str(quadro_vp_id.credito_anno_precedente).replace('.', ' '),
            # 'VP10': str(quadro_vp_id.versamento_auto_UE).replace('.', ' '),
            # 'VP11': str(quadro_vp_id.crediti_imposta).replace('.', ' '),
            # 'VP12': str(quadro_vp_id.interessi_dovuti).replace('.', ' '),
            # 'VP13': str(quadro_vp_id.accounto_dovuto).replace('.', ' '),
            # 'VP14/1': str(quadro_vp_id.iva_da_versare).replace('.', ' '),
            # 'VP14/2': str(quadro_vp_id.iva_a_credito).replace('.', ' '),
        }

        VT1_1 = 0
        VT1_2 = 0
        VT1_3 = 0
        VT1_4 = 0
        VT1_5 = 0
        VT1_6 = 0



        for tax in lipe_annuale.debit_vat_account_line_ids:
            #somma imponibile vendite e imposta vendite
            tax_datas = tax.tax_id._compute_totals_tax({
                'from_date': lipe_annuale.date_range_ids[0].date_start,
                'to_date': lipe_annuale.date_range_ids[0].date_end,
                'registry_type': 'customer'
            })
            VT1_1 += tax_datas[1]
            VT1_2 += tax_datas[2]

        for tax in lipe_annuale.debit_vat_account_line_ids:
            if tax.tax_id.iva_corr:
                #Imposta vs. soggetti privati
                tax_datas = tax.tax_id._compute_totals_tax({
                    'from_date': lipe_annuale.date_range_ids[0].date_start,
                    'to_date': lipe_annuale.date_range_ids[0].date_end,
                    'registry_type': 'customer'
                })
                VT1_3 += tax_datas[1]
                VT1_4 += tax_datas[2]
            if tax.tax_id.iva_fatt:
                #Imposta vs. soggetti privati
                tax_datas = tax.tax_id._compute_totals_tax({
                    'from_date': lipe_annuale.date_range_ids[0].date_start,
                    'to_date': lipe_annuale.date_range_ids[0].date_end,
                    'registry_type': 'customer'
                })
                VT1_5 += tax_datas[1]
                VT1_6 += tax_datas[2]


        region_private_operation = {
            'Abruzzo': {'imponibile': 0, 'imposta': 0},
            'Basilicata': {'imponibile': 0, 'imposta': 0},
            'Trentino Alto Adige': {'imponibile': 0, 'imposta': 0},
            'Calabria': {'imponibile': 0, 'imposta': 0},
            'Campania': {'imponibile': 0, 'imposta': 0},
            'Emilia Romagna': {'imponibile': 0, 'imposta': 0},
            'Friuli Venezia Giulia': {'imponibile': 0, 'imposta': 0},
            'Lazio': {'imponibile': 0, 'imposta': 0},
            'Liguria': {'imponibile': 0, 'imposta': 0},
            'Lombardia': {'imponibile': 0, 'imposta': 0},
            'Marche': {'imponibile': 0, 'imposta': 0},
            'Molise': {'imponibile': 0, 'imposta': 0},
            'Piemonte': {'imponibile': 0, 'imposta': 0},
            'Puglia': {'imponibile': 0, 'imposta': 0},
            'Sardegna': {'imponibile': 0, 'imposta': 0},
            'Sicilia': {'imponibile': 0, 'imposta': 0},
            'Toscana': {'imponibile': 0, 'imposta': 0},
            'Umbria': {'imponibile': 0, 'imposta': 0},
            "Valle d'Aosta": {'imponibile': 0, 'imposta': 0},
            'Veneto': {'imponibile': 0, 'imposta': 0},
        }



        for tax in lipe_annuale.debit_vat_account_line_ids:
            if tax.tax_id.iva_corr:
                # Imposta vs. soggetti privati
                # 1.Operazioni Imponibili
                account_move_line = self.env['account.move.line'].sudo().search(['&','&',('date', '>=', lipe_annuale.date_range_ids[0].date_start),
                                                                                 ('date', '<=', lipe_annuale.date_range_ids[0].date_end),
                                                                                 ('tax_ids', 'in', [tax.tax_id.id] )])
                for line in account_move_line:
                    imponibile = line.debit - line.credit
                    if not line.partner_id or not line.partner_id.region_id:
                        #Se il cliente non e' impostato oppure non e' presente la regione imposta in quella di Default
                        region_private_operation['Lombardia']['imponibile'] += imponibile


                    if line.partner_id.region_id:
                        region_private_operation[line.partner_id.region_id.name]['imponibile'] += imponibile


                # # 1.Operazioni Imposta
                account_move_line = self.env['account.move.line'].sudo().search(['&', '&', ('date', '>=', lipe_annuale.date_range_ids[0].date_start),
                                                                                 ('date', '<=', lipe_annuale.date_range_ids[0].date_end),
                                                                                 ('tax_line_id', '=', tax.tax_id.id)])
                for line in account_move_line:
                    imposta = line.debit - line.credit
                    if not line.partner_id or not line.partner_id.region_id:
                        #Se il cliente non e' impostato oppure non e' presente la regione imposta in quella di Default
                        region_private_operation['Lombardia']['imposta'] += imposta

                    if line.partner_id.region_id:
                        region_private_operation[line.partner_id.region_id.name]['imposta'] += imposta


        data_dict_pag13 = {
            'CODICE FISCALE13': self.taxpayer_vat,
            'VT1/2':  round(VT1_2,2),
            'VT1/1':  round(VT1_1,2),
            'VT1/5':  round(VT1_5,2),
            'VT1/6':  round(VT1_6,2),
            'VT1/3':  round(VT1_3,2),
            'VT1/4':  round(VT1_4,2),
            'VT2/1': round(abs(region_private_operation['Abruzzo']['imponibile']), 2),
            'VT2/2': round(abs(region_private_operation['Abruzzo']['imposta']), 2),
            'VT3/1': round(abs(region_private_operation['Basilicata']['imponibile']), 2),
            'VT3/2': round(abs(region_private_operation['Basilicata']['imposta']), 2),
            'VT4/1': round(abs(region_private_operation['Trentino Alto Adige']['imponibile']), 2),
            'VT4/2': round(abs(region_private_operation['Trentino Alto Adige']['imposta']), 2),
            'VT5/1': round(abs(region_private_operation['Calabria']['imponibile']), 2),
            'VT5/2': round(abs(region_private_operation['Calabria']['imposta']), 2),
            'VT6/1': round(abs(region_private_operation['Campania']['imponibile']), 2),
            'VT6/2': round(abs(region_private_operation['Campania']['imposta']), 2),
            'VT7/1': round(abs(region_private_operation['Emilia Romagna']['imponibile']), 2),
            'VT7/2': round(abs(region_private_operation['Emilia Romagna']['imposta']), 2),
            'VT8/1': round(abs(region_private_operation['Friuli Venezia Giulia']['imponibile']), 2),
            'VT8/2': round(abs(region_private_operation['Friuli Venezia Giulia']['imposta']), 2),
            'VT9/1': round(abs(region_private_operation['Lazio']['imponibile']), 2),
            'VT9/2': round(abs(region_private_operation['Lazio']['imposta']), 2),
            'VT10/1': round(abs(region_private_operation['Liguria']['imponibile']), 2),
            'VT10/2': round(abs(region_private_operation['Liguria']['imposta']), 2),
            'VT11/1': round(abs(region_private_operation['Lombardia']['imponibile']), 2),
            'VT11/2': round(abs(region_private_operation['Lombardia']['imposta']), 2),
            'VT12/1': round(abs(region_private_operation['Marche']['imponibile']), 2),
            'VT12/2': round(abs(region_private_operation['Marche']['imposta']), 2),
            'VT13/1': round(abs(region_private_operation['Molise']['imponibile']), 2),
            'VT13/2': round(abs(region_private_operation['Molise']['imposta']), 2),
            'VT14/1': round(abs(region_private_operation['Piemonte']['imponibile']), 2),
            'VT14/2': round(abs(region_private_operation['Piemonte']['imposta']), 2),
            'VT15/1': round(abs(region_private_operation['Puglia']['imponibile']), 2),
            'VT15/2': round(abs(region_private_operation['Puglia']['imposta']), 2),
            'VT16/1': round(abs(region_private_operation['Sardegna']['imponibile']), 2),
            'VT16/2': round(abs(region_private_operation['Sardegna']['imposta']), 2),
            'VT17/1': round(abs(region_private_operation['Sicilia']['imponibile']), 2),
            'VT17/2': round(abs(region_private_operation['Sicilia']['imposta']), 2),
            'VT18/1': round(abs(region_private_operation['Toscana']['imponibile']), 2),
            'VT18/2': round(abs(region_private_operation['Toscana']['imposta']), 2),
            'VT20/1': round(abs(region_private_operation['Umbria']['imponibile']), 2),
            'VT20/2': round(abs(region_private_operation['Umbria']['imposta']), 2),
            'VT21/1': round(abs(region_private_operation["Valle d'Aosta"]['imponibile']), 2),
            'VT21/2': round(abs(region_private_operation["Valle d'Aosta"]['imposta']), 2),
            'VT22/1': round(abs(region_private_operation['Veneto']['imponibile']), 2),
            'VT22/2': round(abs(region_private_operation['Veneto']['imposta']), 2)
        }


        data_dict_pag14 = {
            'CODICE FISCALE14': self.taxpayer_vat,
            'VX1': str('').replace('.', ','),
            'VX2/1': str('').replace('.', ','),
            'VX2/2': str('').replace('.', ','),
            'VX3': str('').replace('.', ','),
        }

        data_dict_pag15 = {
            'CODICE FISCALE15': self.taxpayer_vat,
        }
        data_dict_pag16 = {
            'CODICE FISCALE16': self.taxpayer_vat,
        }
        data_dict_pag17 = {
            'CODICE FISCALE17': self.taxpayer_vat,
        }
        data_dict_pag18 = {
            'CODICE FISCALE18': self.taxpayer_vat,
        }
        data_dict_pag19 = {
            'CODICE FISCALE19': self.taxpayer_vat,
        }
        data_dict_pag20 = {
            'CODICE FISCALE20': self.taxpayer_vat,
        }
        data_dict_pag21 = {
            'CODICE FISCALE21': self.taxpayer_vat,
        }
        data_dict_pag22 = {
            'CODICE FISCALE22': self.taxpayer_vat,
        }






        pdf_writer.addPage(pdf_reader.getPage(0))
        pdf_writer.addPage(pdf_reader.getPage(1))
        pdf_writer.addPage(pdf_reader.getPage(2))
        pdf_writer.addPage(pdf_reader.getPage(3))
        pdf_writer.addPage(pdf_reader.getPage(4))
        pdf_writer.addPage(pdf_reader.getPage(5))
        pdf_writer.addPage(pdf_reader.getPage(6))
        pdf_writer.addPage(pdf_reader.getPage(7))
        pdf_writer.addPage(pdf_reader.getPage(8))
        pdf_writer.addPage(pdf_reader.getPage(9))
        pdf_writer.addPage(pdf_reader.getPage(10))
        pdf_writer.addPage(pdf_reader.getPage(11))
        pdf_writer.addPage(pdf_reader.getPage(12))
        pdf_writer.addPage(pdf_reader.getPage(13))
        pdf_writer.addPage(pdf_reader.getPage(14))
        pdf_writer.addPage(pdf_reader.getPage(15))
        pdf_writer.addPage(pdf_reader.getPage(16))
        pdf_writer.addPage(pdf_reader.getPage(17))
        pdf_writer.addPage(pdf_reader.getPage(18))
        pdf_writer.addPage(pdf_reader.getPage(19))
        pdf_writer.addPage(pdf_reader.getPage(20))
        pdf_writer.addPage(pdf_reader.getPage(21))
        page = pdf_writer.getPage(1)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag1)
        page = pdf_writer.getPage(2)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag2)
        page = pdf_writer.getPage(3)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag3)
        page = pdf_writer.getPage(4)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag4)
        page = pdf_writer.getPage(5)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag5)
        page = pdf_writer.getPage(6)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag6)
        page = pdf_writer.getPage(7)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag7)
        page = pdf_writer.getPage(8)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag8)
        page = pdf_writer.getPage(9)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag9)
        page = pdf_writer.getPage(10)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag10)
        page = pdf_writer.getPage(11)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag11)
        page = pdf_writer.getPage(12)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag12)
        page = pdf_writer.getPage(13)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag13)
        page = pdf_writer.getPage(14)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag14)
        page = pdf_writer.getPage(15)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag15)
        page = pdf_writer.getPage(16)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag16)
        page = pdf_writer.getPage(17)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag17)
        page = pdf_writer.getPage(18)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag18)
        page = pdf_writer.getPage(19)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag19)
        page = pdf_writer.getPage(20)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag20)
        page = pdf_writer.getPage(21)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag21)


        output_stream = BytesIO()
        pdf_writer.write(output_stream)
        return output_stream.getvalue()


    def generate_separate_lipe_file(self, count, quadro_vp_id):
        pdf_module_path = get_module_resource('l10n_it_account', 'data', 'moduli_pdf','modulo_liquidazione_periodica_iva_editabile.pdf')
        input_stream = open(pdf_module_path, "rb")
        pdf_reader = PyPDF2.PdfFileReader(input_stream, strict=False)

        if "/AcroForm" in pdf_reader.trailer["/Root"]:
            pdf_reader.trailer["/Root"]["/AcroForm"].update(
                {NameObject("/NeedAppearances"): BooleanObject(True)})

        pdf_writer = PyPDF2.PdfFileWriter()
        self.set_need_appearances_writer(pdf_writer)

        if "/AcroForm" in pdf_writer._root_object:
            # Acro form is form field, set needs appearances to fix printing issues
            pdf_writer._root_object["/AcroForm"].update(
                {NameObject("/NeedAppearances"): BooleanObject(True)})

        data_dict_pag2 = {
            'CODICE FISCALE_2' + str(count): self.taxpayer_fiscalcode,
            'MODULO_N' + str(count): str(count).zfill(2),
            'MESE' + str(count): str(quadro_vp_id.month).zfill(2) if quadro_vp_id.period_type == 'month' else '',
            'TRIMESTRE' + str(count): str(quadro_vp_id.quarter).zfill(2) if quadro_vp_id.period_type == 'quarter' else '',
            'SUBFORNITURE' + str(count): quadro_vp_id.subcontracting,
            'EVENTI_ECCEZIONALI' + str(count): quadro_vp_id.exceptional_events,
            'OPERAZIONI_STRAORDINARIE' + str(count): '',
            'ACCONTO_DOVUTO' + str(count): str(quadro_vp_id.metodo_acconto_dovuto),
            'VP2' + str(count): str(quadro_vp_id.imponibile_operazioni_attive).replace('.', ' '),
            'VP3' + str(count): str(quadro_vp_id.imponibile_operazioni_passive).replace('.', ' '),
            'VP4' + str(count): str(quadro_vp_id.iva_esigibile).replace('.', ' '),
            'VP5' + str(count): str(quadro_vp_id.iva_detratta).replace('.', ' '),
            'VP6_D' + str(count): str(quadro_vp_id.iva_dovuta_debito).replace('.', ' '),
            'VP6_C' + str(count): str(quadro_vp_id.iva_dovuta_credito).replace('.', ' '),
            'VP7' + str(count): str(quadro_vp_id.debito_periodo_precedente).replace('.', ' '),
            'VP8' + str(count): str(quadro_vp_id.credito_periodo_precedente).replace('.', ' '),
            'VP9' + str(count): str(quadro_vp_id.credito_anno_precedente).replace('.', ' '),
            'VP10' + str(count): str(quadro_vp_id.versamento_auto_UE).replace('.', ' '),
            'VP11' + str(count): str(quadro_vp_id.crediti_imposta).replace('.', ' '),
            'VP12' + str(count): str(quadro_vp_id.interessi_dovuti).replace('.', ' '),
            'VP13' + str(count): str(quadro_vp_id.accounto_dovuto).replace('.', ' '),
            'VP14_D' + str(count): str(quadro_vp_id.iva_da_versare).replace('.', ' '),
            'VP14_C' + str(count): str(quadro_vp_id.iva_a_credito).replace('.', ' '),
            'ACCONTO_DOVUTO' + str(count): ''
        }

        page = pdf_reader.getPage(2)
        pdf_writer.addPage(page)
        renamed_page_field = pdf_writer.getPage(0)
        self.pdf_suffix_fields(renamed_page_field, str(count))
        pdf_writer.updatePageFormFieldValues(renamed_page_field, data_dict_pag2)

        output_stream = BytesIO()
        pdf_writer.write(output_stream)
        return output_stream.getvalue()



    def get_export_pdf(self):
        """
        Funzione che compila il modulo standard della comunicazione periodica
        IVA dell'AdE, il modulo è presente nella cartella data/moduli_pdf
        """
        pdfs_list = []

        pdf_module_path = get_module_resource('l10n_it_account', 'data', 'moduli_pdf', 'modulo_liquidazione_periodica_iva_editabile.pdf')
        input_stream = open(pdf_module_path, "rb")

        pdf_reader = PyPDF2.PdfFileReader(input_stream, strict=False)

        if "/AcroForm" in pdf_reader.trailer["/Root"]:
            pdf_reader.trailer["/Root"]["/AcroForm"].update(
                {NameObject("/NeedAppearances"): BooleanObject(True)})

        pdf_writer = PyPDF2.PdfFileWriter()

        self.set_need_appearances_writer(pdf_writer)
        if "/AcroForm" in pdf_writer._root_object:
            # Acro form is form field, set needs appearances to fix printing issues
            pdf_writer._root_object["/AcroForm"].update(
                {NameObject("/NeedAppearances"): BooleanObject(True)})

        data_dict_pag1 = {
            'CODICE_FISCALE': self.taxpayer_fiscalcode,
            'ANNO_IMPOSTA': self.year,
            'CODICE_CARICA': self.codice_carica_id.code,
            'PARTITA_IVA': self.taxpayer_vat,
            'PARTITA_IVA_CONTROLLANTE': self.controller_vat if self.controller_vat else '',
            'ULTIMO_MESE': self.last_month,
            'LIQUIDAZIONE_GRUPPO': '',
            'CODICE_FISCALE_DICHIARANTE': self.declarant_fiscalcode if self.declarant_fiscalcode else '',
            'CODICE_FISCALE_SOCIETA_DICHIARANTE': '',
            'FIRMA': 'X' if self.declarant_sign else '',
            'CODICE_FISCALE_INCARICATO': self.delegate_fiscalcode if self.delegate_fiscalcode else '',
            'IMPEGNO_PRESENTAZIONE': '',
            'IMPEGNO_GIORNO_MESE_ANNO': self.date_commitment if self.date_commitment else '',
            'FIRMA_INCARICATO': 'X' if self.delegate_sign else '',
        }

        pdf_writer.addPage(pdf_reader.getPage(0))
        pdf_writer.addPage(pdf_reader.getPage(1))
        page = pdf_writer.getPage(1)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag1)


        count = 0 #Contatore Modulo

        for quadro_vp_id in self.quadri_vp_ids:
            count += 1
            pdfs_list.append(self.generate_separate_lipe_file(count, quadro_vp_id))




        output_stream = BytesIO()
        pdf_writer.write(output_stream)
        pdfs_list.append(output_stream.getvalue())
        return pdfs_list




    def get_export_xml(self):
        """
        Funzione che compila il tracciato standard xml
        della comunicazione periodica
        IVA dell'AdE
        """
        self._validate()
        x1_Fornitura = self._export_xml_get_fornitura()

        x1_1_Intestazione = self._export_xml_get_intestazione()

        attrs = {
            'identificativo': str(self.identificativo).zfill(5)
        }
        x1_2_Comunicazione = etree.Element(
            etree.QName(NS_IV, "Comunicazione"), attrs)
        x1_2_1_Frontespizio = self._export_xml_get_frontespizio()
        x1_2_Comunicazione.append(x1_2_1_Frontespizio)

        x1_2_2_DatiContabili = etree.Element(
            etree.QName(NS_IV, "DatiContabili"))
        nr_modulo = 0
        for quadro in self.quadri_vp_ids:
            nr_modulo += 1
            modulo = self.with_context(
                nr_modulo=nr_modulo)._export_xml_get_dati_modulo(quadro)
            x1_2_2_DatiContabili.append(modulo)
        x1_2_Comunicazione.append(x1_2_2_DatiContabili)
        # Composizione struttura xml con le varie sezioni generate
        x1_Fornitura.append(x1_1_Intestazione)
        x1_Fornitura.append(x1_2_Comunicazione)

        xml_string = etree.tostring(
            x1_Fornitura, encoding='utf8', method='xml', pretty_print=True)
        return xml_string

    def _validate(self):
        """
        Controllo congruità dati della comunicazione
        """
        # Anno obbligatorio
        if not self.year:
            raise ValidationError(
                _("Year required"))

        # Codice Fiscale
        if not self.taxpayer_fiscalcode \
                or len(self.taxpayer_fiscalcode) not in [11, 16]:
            raise ValidationError(
                _("Taxpayer Fiscalcode is required. It's accepted codes \
                    with lenght 11 or 16 chars"))

        # Codice Fiscale dichiarante Obbligatorio se il codice fiscale
        # del contribuente è di 11 caratteri
        if self.taxpayer_fiscalcode and len(self.taxpayer_fiscalcode) == 11\
                and not self.declarant_fiscalcode:
            raise ValidationError(
                _("Declarant Fiscalcode is required. You can enable the \
                section with different declarant option"))

        # LiquidazioneGruppo: elemento opzionale, di tipo DatoCB_Type.
        # Se presente non deve essere presente l'elemento PIVAControllante.
        # Non può essere presente se l'elemento CodiceFiscale è lungo 16
        # caratteri.
        if self.liquidazione_del_gruppo:
            if self.controller_vat:
                raise ValidationError(
                    _("For group's statement, controller's TIN must be empty"))
            if len(self.taxpayer_fiscalcode) == 16:
                raise ValidationError(
                    _("Group's statement not valid, as fiscal code is 16 "
                      "characters"))
        # CodiceCaricaDichiarante
        if self.declarant_fiscalcode:
            if not self.codice_carica_id:
                raise ValidationError(
                    _("Specify role code of declarant"))
        # CodiceFiscaleSocieta:
        # Obbligatori per codice carica 9
        if self.codice_carica_id and self.codice_carica_id.code == '9':
            if not self.declarant_fiscalcode_company:
                raise ValidationError(
                    _("With this role code, you need to specify fiscal code "
                      "of declarant company"))
        # ImpegnoPresentazione::
        if self.delegate_fiscalcode:
            if not self.delegate_commitment:
                raise ValidationError(
                    _("With intermediary fiscal code, you need to specify "
                      "commitment code"))
            if not self.date_commitment:
                raise ValidationError(
                    _("With intermediary fiscal code, you need to specify "
                      "commitment date"))
        # ImpegnoPresentazione::
        if self.delegate_fiscalcode and not self.delegate_sign:
            raise ValidationError(
                _("With delegate in commitment section, you need to check "
                  "'delegate sign'"))
        return True

    def _export_xml_get_fornitura(self):
        x1_Fornitura = etree.Element(
            etree.QName(NS_IV, "Fornitura"), nsmap=NS_MAP)
        return x1_Fornitura

    def _export_xml_validate(self):
        return True

    def _export_xml_get_intestazione(self):
        x1_1_Intestazione = etree.Element(etree.QName(NS_IV, "Intestazione"))
        # Codice Fornitura
        x1_1_1_CodiceFornitura = etree.SubElement(
            x1_1_Intestazione, etree.QName(NS_IV, "CodiceFornitura"))
        code = self.company_id.vsc_supply_code
        x1_1_1_CodiceFornitura.text = code
        # Codice Fiscale Dichiarante
        if self.declarant_fiscalcode:
            x1_1_2_CodiceFiscaleDichiarante = etree.SubElement(
                x1_1_Intestazione, etree.QName(NS_IV,
                                               "CodiceFiscaleDichiarante"))
            x1_1_2_CodiceFiscaleDichiarante.text = str(
                self.declarant_fiscalcode)
        # Codice Carica
        if self.codice_carica_id:
            x1_1_3_CodiceCarica = etree.SubElement(
                x1_1_Intestazione, etree.QName(NS_IV, "CodiceCarica"))
            x1_1_3_CodiceCarica.text = str(self.codice_carica_id.code)
        return x1_1_Intestazione

    def _export_xml_get_frontespizio(self):
        x1_2_1_Frontespizio = etree.Element(etree.QName(NS_IV, "Frontespizio"))
        # Codice Fiscale
        x1_2_1_1_CodiceFiscale = etree.SubElement(
            x1_2_1_Frontespizio, etree.QName(NS_IV, "CodiceFiscale"))
        x1_2_1_1_CodiceFiscale.text = str(self.taxpayer_fiscalcode) \
            if self.taxpayer_fiscalcode else ''
        # Anno Imposta
        x1_2_1_2_AnnoImposta = etree.SubElement(
            x1_2_1_Frontespizio, etree.QName(NS_IV, "AnnoImposta"))
        x1_2_1_2_AnnoImposta.text = str(self.year)
        # Partita IVA
        x1_2_1_3_PartitaIVA = etree.SubElement(
            x1_2_1_Frontespizio, etree.QName(NS_IV, "PartitaIVA"))
        x1_2_1_3_PartitaIVA.text = self.taxpayer_vat
        # PIVA Controllante
        if self.controller_vat:
            x1_2_1_4_PIVAControllante = etree.SubElement(
                x1_2_1_Frontespizio, etree.QName(NS_IV, "PIVAControllante"))
            x1_2_1_4_PIVAControllante.text = self.controller_vat
        # Ultimo Mese
        if self.last_month:
            x1_2_1_5_UltimoMese = etree.SubElement(
                x1_2_1_Frontespizio, etree.QName(NS_IV, "UltimoMese"))
            x1_2_1_5_UltimoMese.text = self.last_month
        # Liquidazione Gruppo
        x1_2_1_6_LiquidazioneGruppo = etree.SubElement(
            x1_2_1_Frontespizio, etree.QName(NS_IV, "LiquidazioneGruppo"))
        x1_2_1_6_LiquidazioneGruppo.text = \
            '1' if self.liquidazione_del_gruppo else '0'
        # CF Dichiarante
        if self.declarant_fiscalcode:
            x1_2_1_7_CFDichiarante = etree.SubElement(
                x1_2_1_Frontespizio, etree.QName(NS_IV, "CFDichiarante"))
            x1_2_1_7_CFDichiarante.text = self.declarant_fiscalcode
        # CodiceCaricaDichiarante
        if self.codice_carica_id:
            x1_2_1_8_CodiceCaricaDichiarante = etree.SubElement(
                x1_2_1_Frontespizio,
                etree.QName(NS_IV, "CodiceCaricaDichiarante"))
            x1_2_1_8_CodiceCaricaDichiarante.text = self.codice_carica_id.code
        # CodiceFiscaleSocieta
        if self.declarant_fiscalcode_company:
            x1_2_1_9_CodiceFiscaleSocieta = etree.SubElement(
                x1_2_1_Frontespizio,
                etree.QName(NS_IV, "CodiceFiscaleSocieta"))
            x1_2_1_9_CodiceFiscaleSocieta.text =\
                self.declarant_fiscalcode_company.code
        # FirmaDichiarazione
        x1_2_1_10_FirmaDichiarazione = etree.SubElement(
            x1_2_1_Frontespizio, etree.QName(NS_IV, "FirmaDichiarazione"))
        x1_2_1_10_FirmaDichiarazione.text = '1' if self.declarant_sign else '0'
        # CFIntermediario
        if self.delegate_fiscalcode:
            x1_2_1_11_CFIntermediario = etree.SubElement(
                x1_2_1_Frontespizio, etree.QName(NS_IV, "CFIntermediario"))
            x1_2_1_11_CFIntermediario.text = self.delegate_fiscalcode
        # ImpegnoPresentazione
        if self.delegate_commitment:
            x1_2_1_12_ImpegnoPresentazione = etree.SubElement(
                x1_2_1_Frontespizio, etree.QName(
                    NS_IV, "ImpegnoPresentazione"))
            x1_2_1_12_ImpegnoPresentazione.text = self.delegate_commitment
        # DataImpegno
        if self.date_commitment:
            x1_2_1_13_DataImpegno = etree.SubElement(
                x1_2_1_Frontespizio, etree.QName(NS_IV, "DataImpegno"))
            x1_2_1_13_DataImpegno.text = self.date_commitment.strftime(
                '%d%m%Y')
        # FirmaIntermediario
        if self.delegate_fiscalcode:
            x1_2_1_14_FirmaIntermediario = etree.SubElement(
                x1_2_1_Frontespizio, etree.QName(NS_IV, "FirmaIntermediario"))
            x1_2_1_14_FirmaIntermediario.text =\
                '1' if self.delegate_sign else '0'

        return x1_2_1_Frontespizio

    def _export_xml_get_dati_modulo(self, quadro):
        # 1.2.2.1 Modulo
        xModulo = etree.Element(
            etree.QName(NS_IV, "Modulo"))
        # Numero Modulo
        NumeroModulo = etree.SubElement(
            xModulo, etree.QName(NS_IV, "NumeroModulo"))
        NumeroModulo.text = str(self._context.get('nr_modulo', 1))

        if quadro.period_type == 'month':
            # 1.2.2.1.1 Mese
            Mese = etree.SubElement(
                xModulo, etree.QName(NS_IV, "Mese"))
            Mese.text = str(quadro.month)
        else:
            # 1.2.2.1.2 Trimestre
            Trimestre = etree.SubElement(
                xModulo, etree.QName(NS_IV, "Trimestre"))
            Trimestre.text = str(quadro.quarter)
        # Da escludere per liquidazione del gruppo
        if not self.liquidazione_del_gruppo:
            # 1.2.2.1.3 Subfornitura
            if quadro.subcontracting:
                Subfornitura = etree.SubElement(
                    xModulo, etree.QName(NS_IV, "Subfornitura"))
                Subfornitura.text = '1' if quadro.subcontracting \
                    else '0'
            # 1.2.2.1.4 EventiEccezionali
            if quadro.exceptional_events:
                EventiEccezionali = etree.SubElement(
                    xModulo, etree.QName(NS_IV, "EventiEccezionali"))
                EventiEccezionali.text = quadro.exceptional_events
            # 1.2.2.1.5 TotaleOperazioniAttive
            TotaleOperazioniAttive = etree.SubElement(
                xModulo, etree.QName(NS_IV, "TotaleOperazioniAttive"))
            TotaleOperazioniAttive.text = "{:.2f}"\
                .format(quadro.imponibile_operazioni_attive).replace('.', ',')
            # 1.2.2.1.6  TotaleOperazioniPassive
            TotaleOperazioniPassive = etree.SubElement(
                xModulo, etree.QName(NS_IV, "TotaleOperazioniPassive"))
            TotaleOperazioniPassive.text = "{:.2f}"\
                .format(quadro.imponibile_operazioni_passive).replace('.', ',')
        # 1.2.2.1.7  IvaEsigibile
        IvaEsigibile = etree.SubElement(
            xModulo, etree.QName(NS_IV, "IvaEsigibile"))
        IvaEsigibile.text = "{:.2f}".format(quadro.iva_esigibile)\
            .replace('.', ',')
        # 1.2.2.1.8  IvaDetratta
        IvaDetratta = etree.SubElement(
            xModulo, etree.QName(NS_IV, "IvaDetratta"))
        IvaDetratta.text = "{:.2f}".format(quadro.iva_detratta)\
            .replace('.', ',')
        # 1.2.2.1.9  IvaDovuta
        if quadro.iva_dovuta_debito:
            IvaDovuta = etree.SubElement(
                xModulo, etree.QName(NS_IV, "IvaDovuta"))
            IvaDovuta.text = "{:.2f}".format(quadro.iva_dovuta_debito)\
                .replace('.', ',')
        # 1.2.2.1.10  IvaCredito
        if quadro.iva_dovuta_credito:
            IvaCredito = etree.SubElement(
                xModulo, etree.QName(NS_IV, "IvaCredito"))
            IvaCredito.text = "{:.2f}".format(quadro.iva_dovuta_credito)\
                .replace('.', ',')
        # 1.2.2.1.11 DebitoPrecedente
        DebitoPrecedente = etree.SubElement(
            xModulo, etree.QName(NS_IV, "DebitoPrecedente"))
        DebitoPrecedente.text = "{:.2f}".format(
            quadro.debito_periodo_precedente).replace('.', ',')
        # 1.2.2.1.12 CreditoPeriodoPrecedente
        CreditoPeriodoPrecedente = etree.SubElement(
            xModulo, etree.QName(NS_IV, "CreditoPeriodoPrecedente"))
        CreditoPeriodoPrecedente.text = "{:.2f}".format(
            quadro.credito_periodo_precedente).replace('.', ',')
        # 1.2.2.1.13 CreditoAnnoPrecedente
        CreditoAnnoPrecedente = etree.SubElement(
            xModulo, etree.QName(NS_IV, "CreditoAnnoPrecedente"))
        CreditoAnnoPrecedente.text = "{:.2f}".format(
            quadro.credito_anno_precedente).replace('.', ',')
        # 1.2.2.1.14 VersamentiAutoUE
        VersamentiAutoUE = etree.SubElement(
            xModulo, etree.QName(NS_IV, "VersamentiAutoUE"))
        VersamentiAutoUE.text = "{:.2f}".format(
            quadro.versamento_auto_UE).replace('.', ',')
        # 1.2.2.1.15 CreditiImposta
        CreditiImposta = etree.SubElement(
            xModulo, etree.QName(NS_IV, "CreditiImposta"))
        CreditiImposta.text = "{:.2f}".format(
            quadro.crediti_imposta).replace('.', ',')
        # 1.2.2.1.16 InteressiDovuti
        InteressiDovuti = etree.SubElement(
            xModulo, etree.QName(NS_IV, "InteressiDovuti"))
        InteressiDovuti.text = "{:.2f}".format(
            quadro.interessi_dovuti).replace('.', ',')
        # 1.2.2.1.17 Acconto
        Acconto = etree.SubElement(
            xModulo, etree.QName(NS_IV, "Acconto"))
        Acconto.text = "{:.2f}".format(
            quadro.accounto_dovuto).replace('.', ',')
        if quadro.metodo_acconto_dovuto:
            Metodo = etree.SubElement(
                xModulo, etree.QName(NS_IV, "Metodo"))
            Metodo.text = str(quadro.metodo_acconto_dovuto)
        # 1.2.2.1.18 ImportoDaVersare
        ImportoDaVersare = etree.SubElement(
            xModulo, etree.QName(NS_IV, "ImportoDaVersare"))
        ImportoDaVersare.text = "{:.2f}".format(
            quadro.iva_da_versare).replace('.', ',')
        # 1.2.2.1.19 ImportoACredito
        ImportoACredito = etree.SubElement(
            xModulo, etree.QName(NS_IV, "ImportoACredito"))
        ImportoACredito.text = "{:.2f}".format(
            quadro.iva_a_credito).replace('.', ',')

        return xModulo


class ComunicazioneLiquidazioneVp(models.Model):
    _name = 'comunicazione.liquidazione.vp'
    _description = 'VAT statement communication - VP table'

    @api.multi
    @api.depends('iva_esigibile', 'iva_detratta')
    def _compute_VP6_iva_dovuta_credito(self):
        for quadro in self:
            quadro.iva_dovuta_debito = 0
            quadro.iva_dovuta_credito = 0
            if quadro.iva_esigibile >= quadro.iva_detratta:
                quadro.iva_dovuta_debito = quadro.iva_esigibile - \
                    quadro.iva_detratta
            else:
                quadro.iva_dovuta_credito = quadro.iva_detratta - \
                    quadro.iva_esigibile

    @api.multi
    @api.depends('iva_dovuta_debito', 'iva_dovuta_credito',
                 'debito_periodo_precedente', 'credito_periodo_precedente',
                 'credito_anno_precedente', 'versamento_auto_UE',
                 'crediti_imposta', 'interessi_dovuti', 'accounto_dovuto')
    def _compute_VP14_iva_da_versare_credito(self):
        """
        Tot Iva a debito = (VP6, col.1 + VP7 + VP12)
        Tot Iva a credito = (VP6, col.2 + VP8 + VP9 + VP10 + VP11 + VP13)
        """
        for quadro in self:
            quadro.iva_da_versare = 0
            quadro.iva_a_credito = 0
            debito = (
                quadro.iva_dovuta_debito + quadro.debito_periodo_precedente +
                quadro.interessi_dovuti
            )
            credito = quadro.iva_dovuta_credito \
                + quadro.credito_periodo_precedente\
                + quadro.credito_anno_precedente \
                + quadro.versamento_auto_UE + quadro.crediti_imposta \
                + quadro.accounto_dovuto
            if debito >= credito:
                quadro.iva_da_versare = debito - credito
            else:
                quadro.iva_a_credito = credito - debito

    comunicazione_id = fields.Many2one('comunicazione.liquidazione',
                                       string='Communication', readonly=True)
    period_type = fields.Selection(
        [('month', 'Monthly'),
         ('quarter', 'Quarterly')],
        string='Period type', default='month')
    month = fields.Integer(string='Month', default=False)
    quarter = fields.Integer(string='Quarter', default=False)
    subcontracting = fields.Boolean(string='Subcontracting')
    exceptional_events = fields.Selection(
        [('1', 'Code 1'), ('9', 'Code 9')], string='Exceptional events')

    imponibile_operazioni_attive = fields.Float(
        string='Profitable operations total (without VAT)')
    imponibile_operazioni_passive = fields.Float(
        string='Unprofitable operations total (without VAT)')
    iva_esigibile = fields.Float(string='Due VAT')
    iva_detratta = fields.Float(string='Deducted VAT')
    iva_dovuta_debito = fields.Float(
        string='Debit VAT',
        compute="_compute_VP6_iva_dovuta_credito", store=True)
    iva_dovuta_credito = fields.Float(
        string='Credit due VAT',
        compute="_compute_VP6_iva_dovuta_credito", store=True)
    debito_periodo_precedente = fields.Float(
        string='Previous period debit')
    credito_periodo_precedente = fields.Float(
        string='Previous period credit')
    credito_anno_precedente = fields.Float(string='Previous year credit')
    versamento_auto_UE = fields.Float(string='Auto UE payment')
    crediti_imposta = fields.Float(string='Tax credits')
    interessi_dovuti = fields.Float(
        string='Due interests for quarterly statements')
    accounto_dovuto = fields.Float(string='Due down payment')
    metodo_acconto_dovuto = fields.Integer()
    iva_da_versare = fields.Float(
        string='VAT to pay',
        compute="_compute_VP14_iva_da_versare_credito", store=True)
    iva_a_credito = fields.Float(
        string='Credit VAT',
        compute="_compute_VP14_iva_da_versare_credito", store=True)
    liquidazioni_ids = fields.Many2many(
        'account.vat.period.end.statement',
        'comunicazione_iva_liquidazioni_rel',
        'comunicazione_id',
        'liquidazione_id',
        string='VAT statements')

    def _reset_values(self):
        for quadro in self:
            quadro.imponibile_operazioni_attive = 0
            quadro.imponibile_operazioni_passive = 0
            quadro.iva_esigibile = 0
            quadro.iva_detratta = 0
            quadro.debito_periodo_precedente = 0
            quadro.credito_periodo_precedente = 0
            quadro.credito_anno_precedente = 0
            quadro.versamento_auto_UE = 0
            quadro.crediti_imposta = 0
            quadro.interessi_dovuti = 0
            quadro.accounto_dovuto = 0
            quadro.metodo_acconto_dovuto = 0

    def _get_tax_context(self, period):
        return {
            'from_date': period.date_start,
            'to_date': period.date_end,
        }

    def _compute_imponibile_operazioni_attive(self, liq, period):
        self.ensure_one()
        debit_taxes = self.env['account.tax']
        for debit in liq.debit_vat_account_line_ids:
            debit_taxes |= debit.tax_id
        for debit_tax in debit_taxes:
            if debit_tax.vsc_exclude_operation:
                continue
            tax = debit_taxes.with_context(
                self._get_tax_context(period)).browse(debit_tax.id)
            self.imponibile_operazioni_attive += (
                tax.base_balance)

    def _compute_imponibile_operazioni_passive(self, liq, period):
        self.ensure_one()
        credit_taxes = self.env['account.tax']
        for credit in liq.credit_vat_account_line_ids:
            credit_taxes |= credit.tax_id
        for credit_tax in credit_taxes:
            if credit_tax.vsc_exclude_operation:
                continue
            tax = credit_taxes.with_context(
                self._get_tax_context(period)).browse(credit_tax.id)
            if (tax.base_balance > 0):
                self.imponibile_operazioni_passive += (tax.base_balance)
            else:
                self.imponibile_operazioni_passive -= (tax.base_balance)
            logging.info(credit_tax.name + " - " + str(abs(tax.base_balance)))

    @api.multi
    @api.onchange('liquidazioni_ids')
    def compute_from_liquidazioni(self):

        for quadro in self:
            # Reset valori
            quadro._reset_values()

            interests_account_id = quadro.comunicazione_id.company_id.\
                of_account_end_vat_statement_interest_account_id.id or False

            for liq in quadro.liquidazioni_ids:

                for period in liq.date_range_ids:
                    quadro._compute_imponibile_operazioni_attive(liq, period)
                    quadro._compute_imponibile_operazioni_passive(liq, period)

                # Iva esigibile
                for vat_amount in liq.debit_vat_account_line_ids:
                    if vat_amount.tax_id.vsc_exclude_vat:
                        continue
                    quadro.iva_esigibile += vat_amount.amount
                # Iva detratta
                for vat_amount in liq.credit_vat_account_line_ids:
                    if vat_amount.tax_id.vsc_exclude_vat:
                        continue
                    quadro.iva_detratta += vat_amount.amount
                # credito/debito periodo precedente
                quadro.debito_periodo_precedente =\
                    liq.previous_debit_vat_amount
                quadro.credito_periodo_precedente =\
                    liq.previous_credit_vat_amount
                # Credito anno precedente (NON GESTITO)
                # Versamenti auto UE (NON GESTITO)
                # Crediti d’imposta (NON GESTITO)
                # Da altri crediti e debiti calcolo:
                # 1 - Interessi dovuti per liquidazioni trimestrali
                # 2 - Decremento iva esigibile con righe positive
                # 3 - Decremento iva detratta con righe negative
                for line in liq.generic_vat_account_line_ids:
                    if interests_account_id and \
                            (line.account_id.id == interests_account_id):
                        quadro.interessi_dovuti += (-1 * line.amount)
                    elif line.amount > 0:
                        quadro.iva_esigibile -= line.amount
                    else:
                        quadro.iva_detratta += line.amount