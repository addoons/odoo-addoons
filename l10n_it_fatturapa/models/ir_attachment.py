# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)
import datetime
import json
import lxml.etree as ET
import re
import base64
import binascii
import logging
from io import BytesIO
import requests
from lxml import etree
from odoo import models, api, fields
from odoo.addons.base.models.ir_mail_server import MailDeliveryException
from odoo.modules import get_module_resource
from odoo.exceptions import UserError
from odoo.tools.translate import _

_logger = logging.getLogger(__name__)

try:
    from asn1crypto import cms
except (ImportError, IOError) as err:
    _logger.debug(err)


re_base64 = re.compile(
    br'^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$')

_logger = logging.getLogger(__name__)

RESPONSE_MAIL_REGEX = '[A-Z]{2}[a-zA-Z0-9]{11,16}_[a-zA-Z0-9]{,5}_[A-Z]{2}_' \
                      '[a-zA-Z0-9]{,3}'

WS_ENDPOINT_IMPORT_INVOICE = '/services/invoice/in/findByUsername'
WS_ENDPOINT_IMPORT_INVOICE_XML = '/services/invoice/in/getByFilename'

ERROR_CODE = [
    ('0000', 'OK'),
    ('0001', 'Errore Generico'),
    ('0002', 'Errore parametri in input mancanti o non validi'),
    ('0012', 'Errore Autenticazione'),
    ('0013', 'Si è verificato un errore in fase di registrazione della richiesta'),
    ('0018', 'Errore validazione firma fattura elettronica inviata, il file non risulta firmato'),
    ('0033', 'Il file fattura elettronica inviato supera la dimensione massima accettata'),
    ('0071', 'Errore in fase di verifica nome file per utente'),
    ('0072', 'Errore in fase di caricamento lista fatture per utente'),
    ('0082', 'Si è verificato un errore in fase di recupero notifiche'),
    ('0092', 'Errore generico schema xsd'),
    ('0093', 'Errore deleghe non valide'),
    ('0094', 'La fattura che stai inviando contiene ID e/o contatti dei trasmittenti differenti dai dati dell’intermediario Aruba PEC.'),
    ('0095', 'Servizio momentaneamente non disponibile. Il controllo dei permessi è fallito. Si prega di riprovare più tardi.'),
]

SDI_STATE = [
    ('Presa in carico', 'Presa in carico'),
    ('Errore Elaborazione', 'Errore Elaborazione'),
    ('Inviata', 'Inviata'),
    ('Scartata', 'Scartata'),
    ('Non Consegnata', 'Non Consegnata'),
    ('Recapito Impossibile', 'Recapito Impossibile'),
    ('Consegnata', 'Consegnata'),
    ('Accettata', 'Accettata'),
    ('Rifiutata', 'Rifiutata'),
    ('Decorrenza Termini', 'Decorrenza Termini'),
]

#Elenco degli Stati SDI che indicano che la fattura è in stato "Chiusa"
#Questi stati verranno saltati nelle successive richieste di Aggiornamento SDI
SDI_COMPLETED = [
    ('Consegnata', 'Consegnata'),
    ('Non Consegnata', 'Non Consegnata'),
]

WS_ENDPOINT_NOTIFICATION_FILENAME = '/services/invoice/out/getByFilename'
WS_ENDPOINT_UPLOAD_INVOICE = '/services/invoice/upload'

class Attachment(models.Model):
    _inherit = 'ir.attachment'

    ftpa_preview_link = fields.Char(
        "Preview link", readonly=True, compute="_compute_ftpa_preview_link"
    )

    @api.multi
    def _compute_ftpa_preview_link(self):
        for att in self:
            att.ftpa_preview_link = '/fatturapa/preview/%s' % att.id

    def remove_xades_sign(self, xml):
        # Recovering parser is needed for files where strings like
        # xmlns:ds="http://www.w3.org/2000/09/xmldsig#&quot;"
        # are present: even if lxml raises
        # {XMLSyntaxError}xmlns:ds:
        # 'http://www.w3.org/2000/09/xmldsig#"' is not a valid URI
        # such files are accepted by SDI
        recovering_parser = ET.XMLParser(recover=True)
        root = ET.XML(xml, parser=recovering_parser)
        for elem in root.iter('*'):
            if elem.tag.find('Signature') > -1:
                elem.getparent().remove(elem)
                break
        return ET.tostring(root)

    def strip_xml_content(self, xml):
        recovering_parser = ET.XMLParser(recover=True)
        root = ET.XML(xml, parser=recovering_parser)
        for elem in root.iter('*'):
            if elem.text is not None:
                elem.text = elem.text.strip()
        return ET.tostring(root)

    @staticmethod
    def extract_cades(data):
        info = cms.ContentInfo.load(data)
        return info['content']['encap_content_info']['content'].native

    def cleanup_xml(self, xml_string):
        xml_string = self.remove_xades_sign(xml_string)
        xml_string = self.strip_xml_content(xml_string)
        return xml_string

    def get_xml_string(self):
        try:
            data = base64.b64decode(self.datas)
        except binascii.Error as e:
            raise UserError(
                _(
                    'Corrupted attachment %s.'
                ) % e.args
            )

        if re_base64.match(data) is not None:
            try:
                data = base64.b64decode(data)
            except binascii.Error as e:
                raise UserError(
                    _(
                        'Base64 encoded file %s.'
                    ) % e.args
                )

        # Amazon sends xml files without <?xml declaration,
        # so they cannot be easily detected using a pattern.
        # We first try to parse as asn1, if it fails we assume xml

        # asn1crypto parser will raise ValueError
        # if the asn1 cannot be parsed
        # KeyError is raised if one of the needed key is not
        # in the asn1 structure (info->content->encap_content_info->content)
        try:
            data = self.extract_cades(data)
        except (ValueError, KeyError):
            pass

        try:
            return self.cleanup_xml(data)
        # cleanup_xml calls root.iter(), but root is None if the parser fails
        # Invalid xml 'NoneType' object has no attribute 'iter'
        except AttributeError as e:
            raise UserError(
                _(
                    'Invalid xml %s.'
                ) % e.args
            )

    def get_fattura_elettronica_preview(self):
        xsl_path = get_module_resource(
            'l10n_it_fatturapa', 'data', 'fatturaordinaria_v1.2.1.xsl')
        xslt = ET.parse(xsl_path)
        xml_string = self.get_xml_string()
        xml_file = BytesIO(xml_string)
        recovering_parser = ET.XMLParser(recover=True)
        dom = ET.parse(xml_file, parser=recovering_parser)
        transform = ET.XSLT(xslt)
        newdom = transform(dom)
        return ET.tostring(newdom, pretty_print=True)




class FatturaPAAttachmentIn(models.Model):
    _name = "fatturapa.attachment.in"
    _description = "E-bill import file"
    _inherits = {'ir.attachment': 'ir_attachment_id'}
    _inherit = ['mail.thread']
    _order = 'id desc'

    ir_attachment_id = fields.Many2one(
        'ir.attachment', 'Attachment', required=True, ondelete="cascade")
    in_invoice_ids = fields.One2many(
        'account.invoice', 'fatturapa_attachment_in_id',
        string="In Bills", readonly=True)
    xml_supplier_id = fields.Many2one(
        "res.partner", string="Supplier", compute="_compute_xml_data",
        store=True)
    invoices_number = fields.Integer(
        "Bills Number", compute="_compute_xml_data", store=True)
    invoices_total = fields.Float(
        "Bills Total", compute="_compute_xml_data", store=True,
        help="If specified by supplier, total amount of the document net of "
             "any discount and including tax charged to the buyer/ordered"
    )
    registered = fields.Boolean(
        "Registered", compute="_compute_registered", store=True)
    exported_zip = fields.Many2one(
        'ir.attachment', 'Exported ZIP', readonly=True)

    e_invoice_received_date = fields.Datetime(string='E-Bill Received Date')

    e_invoice_validation_error = fields.Boolean(
        compute='_compute_e_invoice_validation_error')

    e_invoice_validation_message = fields.Text(
        compute='_compute_e_invoice_validation_error')

    aruba_filename = fields.Char()

    def import_aruba_invoice(self):
        """
        Import Aruba Supplier Invoice
        """
        ws_ids = self.env['sdi.channel'].get_default_ws()
        for ws in ws_ids:
            ws.web_auth()
            header = {'Authorization': 'Bearer ' + ws.web_server_token}
            data = {
                'username': ws.web_server_login,
                'countrySender': 'IT',
                'countryReceiver': 'IT'
            }
            r = requests.get(ws.web_server_method_address + WS_ENDPOINT_IMPORT_INVOICE, headers=header,
                             params=data).json()
            for invoice in r['content']:
                filename = invoice['filename']
                invoice_id = self.search([('aruba_filename', '=', filename)])
                if not invoice_id:
                    # LA FATTURA MANCA, IMPORTA
                    invoice_data = {'filename': filename}
                    r = requests.get(ws.web_server_method_address + WS_ENDPOINT_IMPORT_INVOICE_XML, headers=header,
                                     params=invoice_data).json()
                    if r:
                        # CREA LA FATTURA
                        self.create({
                            'aruba_filename': filename,
                            'datas': r['file'],
                        })

    @api.onchange('datas_fname')
    def onchagne_datas_fname(self):
        self.name = self.datas_fname

    def get_xml_string(self):
        return self.ir_attachment_id.get_xml_string()

    @api.multi
    @api.depends('ir_attachment_id.datas')
    def _compute_xml_data(self):
        for att in self:
            fatt = self.env['wizard.import.fatturapa'].get_invoice_obj(att)
            cedentePrestatore = fatt.FatturaElettronicaHeader.CedentePrestatore
            partner_id = self.env['wizard.import.fatturapa'].getCedPrest(
                cedentePrestatore)
            att.xml_supplier_id = partner_id
            att.invoices_number = len(fatt.FatturaElettronicaBody)
            att.invoices_total = 0
            for invoice_body in fatt.FatturaElettronicaBody:
                att.invoices_total += float(
                    invoice_body.DatiGenerali.DatiGeneraliDocumento.
                    ImportoTotaleDocumento or 0
                )

    @api.multi
    @api.depends('in_invoice_ids')
    def _compute_registered(self):
        for att in self:
            if (
                att.in_invoice_ids and
                len(att.in_invoice_ids) == att.invoices_number
            ):
                att.registered = True
            else:
                att.registered = False

    def extract_attachments(self, AttachmentsData, invoice_id):
        AttachModel = self.env['fatturapa.attachments']
        for attach in AttachmentsData:
            if not attach.NomeAttachment:
                name = _("Attachment without name")
            else:
                name = attach.NomeAttachment
            content = attach.Attachment
            _attach_dict = {
                'name': name,
                'datas': base64.b64encode(content),
                'datas_fname': name,
                'description': attach.DescrizioneAttachment or '',
                'compression': attach.AlgoritmoCompressione or '',
                'format': attach.FormatoAttachment or '',
                'invoice_id': invoice_id,
            }
            AttachModel.create(_attach_dict)

class SdiNotification(models.Model):
    _name = 'sdi.notification'

    attachment_out_id = fields.Many2one('fatturapa.attachment_out')
    date = fields.Datetime()
    sdi_state = fields.Selection(SDI_STATE)
    sdi_description = fields.Text()

class FatturaPAAttachmentOut(models.Model):
    _name = "fatturapa.attachment.out"
    _description = "E-invoice Export File"
    _inherits = {'ir.attachment': 'ir_attachment_id'}
    _inherit = ['mail.thread']
    _order = 'id desc'

    ir_attachment_id = fields.Many2one(
        'ir.attachment', 'Attachment', required=True, ondelete="cascade")
    out_invoice_ids = fields.One2many(
        'account.invoice', 'fatturapa_attachment_out_id',
        string="Out Invoices", readonly=True)
    has_pdf_invoice_print = fields.Boolean(
        help="True if all the invoices have a printed "
             "report attached in the XML, False otherwise.",
        compute='_compute_has_pdf_invoice_print', store=True)
    invoice_partner_id = fields.Many2one(
        'res.partner', string='Customer', store=True,
        compute='_compute_invoice_partner_id')
    exported_zip = fields.Many2one(
        'ir.attachment', 'Exported ZIP', readonly=True)
    sdi_notification_ids = fields.One2many('sdi.notification', 'attachment_out_id')

    aruba_upload_filename = fields.Char()
    aruba_error_code = fields.Selection(selection=ERROR_CODE)
    aruba_sdi_state = fields.Selection(selection=SDI_STATE)
    aruba_error_description = fields.Text()
    aruba_sent = fields.Boolean()


    def get_sdi_notification(self):
        """
        Aggiorna lo stato notifica SDI
        """
        ws_ids = self.env['sdi.channel'].get_default_ws()
        for ws in ws_ids:
            if ws.provider == 'aruba':
                #Ora gestiamo solo le notifiche di Aruba
                ws.web_auth()
                last_week = datetime.datetime.now() - datetime.timedelta(days=7)
                #12 è il limite massimo ogni 1 minuto ARUBA
                for attachment in self.search([('create_date', '>=', last_week), ('aruba_sdi_state', 'not in', SDI_COMPLETED)], limit=12):
                    if attachment.aruba_upload_filename:
                        header = {
                            'Authorization': 'Bearer ' + ws.web_server_token,
                        }
                        data = {
                            'filename': str(attachment.aruba_upload_filename),
                            'includePdf': False,
                        }
                        r = requests.get(ws.web_server_method_address + WS_ENDPOINT_NOTIFICATION_FILENAME,
                                         headers=header, params=data)

                        if r.status_code == 200:
                            r = r.json()
                            invoices = r['invoices']
                            notification = [(5, )]
                            for inv in invoices:
                                # Cicla tutte le notifiche relative alla fattura
                                # Salva l'ultimo stato
                                attachment.aruba_sdi_state = inv['status']
                                notification_date = re.sub(r'([-+]\d{2}):(\d{2})(?:(\d{2}))?$', r'\1\2\3', inv['invoiceDate'])
                                date = datetime.datetime.strptime(notification_date, '%Y-%m-%dT%H:%M:%S.%f%z')
                                notification.append((0, 0, {
                                    'sdi_state': inv['status'],
                                    'date': date.strftime('%Y-%m-%d %H:%M:%S'),
                                    'sdi_description': inv['statusDescription']
                                }))
                            attachment.sdi_notification_ids = notification
                        else:
                            attachment.aruba_sdi_state = 'Errore Elaborazione' #Errore Elaborazione
                    else:
                        attachment.aruba_sdi_state = 'Errore Elaborazione' #Errore Elaborazione


    def send_to_aruba(self):
        """
        Invia il documento XML al ws di ARUBA
        """
        ws_ids = self.env['sdi.channel'].get_default_ws()
        if not ws_ids:
            raise UserWarning("Non e' stata trovata la configurazione Default di Aruba")
        for ws in ws_ids:
            ws.web_auth()
            header = {
                'Content-Type': 'application/json;charset=UTF-8',
                'Authorization': 'Bearer ' + ws.web_server_token,
            }
            data = {
                'dataFile': self.datas.decode('utf-8'),
                'credential': None,
                'domain': None,
            }
            try:
                r = requests.post(ws.web_server_method_address + WS_ENDPOINT_UPLOAD_INVOICE, headers=header, data=json.dumps(data))
                if r.status_code == 200:
                    r = r.json()
                    self.aruba_upload_filename = r['uploadFileName']
                    self.aruba_error_code = r['errorCode']
                    self.aruba_error_description = r['errorDescription']
                    if self.aruba_error_code == '0000':
                        self.aruba_sent = True
                        for invoice in self.out_invoice_ids:
                            invoice.fatturapa_state = 'sent'
                else:
                    raise UserWarning(r)
            except Exception as e:
                raise UserWarning(e)

    @api.model
    def get_file_vat(self):
        company = self.env.user.company_id
        if company.fatturapa_sender_partner:
            if not company.fatturapa_sender_partner.vat:
                raise UserError(
                    _('Partner %s TIN not set.')
                    % company.fatturapa_sender_partner.display_name
                )
            vat = company.fatturapa_sender_partner.vat
        else:
            if not company.vat:
                raise UserError(
                    _('Company %s TIN not set.') % company.display_name)
            vat = company.vat
        vat = vat.replace(' ', '').replace('.', '').replace('-', '')
        return vat

    def file_name_exists(self, file_id):
        vat = self.get_file_vat()
        partial_fname = r'%s\_%s.' % (vat, file_id)  # escaping _ SQL
        # Not trying to perfect match file extension, because user could have
        # downloaded, signed and uploaded again the file, thus having changed
        # file extension
        return bool(self.search(
            [('datas_fname', '=like', '%s%%' % partial_fname)]))

    @api.multi
    @api.depends('out_invoice_ids')
    def _compute_invoice_partner_id(self):
        for att in self:
            partners = att.mapped('out_invoice_ids.partner_id')
            if len(partners) == 1:
                att.invoice_partner_id = partners.id

    @api.multi
    @api.constrains('datas_fname')
    def _check_datas_fname(self):
        for att in self:
            res = self.search([('datas_fname', '=', att.datas_fname)])
            if len(res) > 1:
                raise UserError(
                    _("File %s already present.") %
                    att.datas_fname)

    @api.multi
    @api.depends(
        'out_invoice_ids.fatturapa_doc_attachments.is_pdf_invoice_print')
    def _compute_has_pdf_invoice_print(self):
        """Check if all the invoices related to this attachment
        have at least one attachment containing
        the PDF report of the invoice"""
        for attachment_out in self:
            for invoice in attachment_out.out_invoice_ids:
                invoice_attachments = invoice.fatturapa_doc_attachments
                if any([ia.is_pdf_invoice_print
                        for ia in invoice_attachments]):
                    continue
                else:
                    attachment_out.has_pdf_invoice_print = False
                    break
            else:
                # We have examined all the invoices and none of them
                # has caused a break, this means all the invoices have at least
                # one attachment having is_pdf_invoice_print = True
                attachment_out.has_pdf_invoice_print = True

    @api.multi
    def write(self, vals):
        res = super(FatturaPAAttachmentOut, self).write(vals)
        if 'datas' in vals and 'message_ids' not in vals:
            for attachment in self:
                attachment.message_post(
                    subject=_("E-invoice attachment changed"),
                    body=_("User %s uploaded a new e-invoice file"
                           ) % self.env.user.login
                )
        return res

    state = fields.Selection([('ready', 'Da Inviare'),
                              ('sent', 'Inviato'),
                              ('sender_error', 'Errore Invio'),
                              ('recipient_error', 'Non Consegnato'),
                              ('rejected', 'Rifiutato (PA)'),
                              ('validated', 'Consegnato'),
                              ('accepted', 'Accettato'),
                              ],
                             string='State',
                             default='ready', track_visibility='onchange')

    last_sdi_response = fields.Text(
        string='Last Response from Exchange System', default='No response yet',
        readonly=True)
    sending_date = fields.Datetime("Sent Date", readonly=True)
    delivered_date = fields.Datetime("Delivered Date", readonly=True)
    sending_user = fields.Many2one("res.users", "Sending User", readonly=True)

    @api.multi
    def reset_to_ready(self):
        for att in self:
            if att.state != 'sender_error':
                raise UserError(
                    _("You can only reset files in 'Sender Error' state.")
                )
            att.state = 'ready'

    @api.model
    def _check_fetchmail(self):
        server = self.env['fetchmail.server'].search([
            ('is_fatturapa_pec', '=', True),
            ('state', '=', 'done')
        ])
        if not server:
            raise UserError(_(
                "No incoming PEC server found. Please configure it."))

    @api.multi
    def send_via_pec(self):
        self._check_fetchmail()
        self.env.user.company_id.sdi_channel_id.check_first_pec_sending()
        states = self.mapped('state')
        if set(states) != set(['ready']):
            raise UserError(
                _("You can only send files in 'Ready to Send' state.")
            )
        for att in self:
            if not att.datas or not att.datas_fname:
                raise UserError(_("File content and file name are mandatory"))
            mail_message = self.env['mail.message'].create({
                'model': self._name,
                'res_id': att.id,
                'subject': att.name,
                'body': 'XML file for FatturaPA {} sent to Exchange System to '
                        'the email address {}.'
                    .format(
                    att.name,
                    self.env.user.company_id.email_exchange_system),
                'attachment_ids': [(6, 0, att.ir_attachment_id.ids)],
                'email_from': (
                    self.env.user.company_id.email_from_for_fatturaPA),
                'reply_to': (
                    self.env.user.company_id.email_from_for_fatturaPA),
                'mail_server_id': self.env.user.company_id.sdi_channel_id.
                    pec_server_id.id,
            })

            mail = self.env['mail.mail'].create({
                'mail_message_id': mail_message.id,
                'body_html': mail_message.body,
                'email_to': self.env.user.company_id.email_exchange_system,
                'headers': {
                    'Return-Path':
                        self.env.user.company_id.email_from_for_fatturaPA
                }
            })

            if mail:
                try:
                    mail.send(raise_exception=True)
                    att.state = 'sent'
                    att.sending_date = fields.Datetime.now()
                    att.sending_user = self.env.user.id
                    self.env.user.company_id.sdi_channel_id. \
                        update_after_first_pec_sending()
                except MailDeliveryException as e:
                    att.state = 'sender_error'
                    mail.body = str(e)

    @api.multi
    def parse_pec_response(self, message_dict):
        message_dict['model'] = self._name
        message_dict['res_id'] = 0

        regex = re.compile(RESPONSE_MAIL_REGEX)
        attachments = [x for x in message_dict['attachments']
                       if regex.match(x.fname)]

        for attachment in attachments:
            response_name = attachment.fname
            message_type = response_name.split('_')[2]
            if attachment.fname.lower().endswith('.zip'):
                # not implemented, case of AT, todo
                continue
            root = etree.fromstring(attachment.content)
            file_name = root.find('NomeFile')
            fatturapa_attachment_out = False

            if file_name is not None:
                file_name = file_name.text
                fatturapa_attachment_out = self.search(
                    ['|',
                     ('datas_fname', '=', file_name),
                     ('datas_fname', '=', file_name.replace('.p7m', ''))])
                if len(fatturapa_attachment_out) > 1:
                    _logger.info('More than 1 out invoice found for incoming'
                                 'message')
                    fatturapa_attachment_out = fatturapa_attachment_out[0]
                if not fatturapa_attachment_out:
                    if message_type == 'MT':  # Metadati
                        # out invoice not found, so it is an incoming invoice
                        return message_dict
                    else:
                        _logger.info('Error: FatturaPA {} not found.'.format(
                            file_name))
                        # TODO Send a mail warning
                        return message_dict

            if fatturapa_attachment_out:
                id_sdi = root.find('IdentificativoSdI')
                receipt_dt = root.find('DataOraRicezione')
                message_id = root.find('MessageId')
                id_sdi = id_sdi.text if id_sdi is not None else False
                receipt_dt = receipt_dt.text if receipt_dt is not None \
                    else False
                message_id = message_id.text if message_id is not None \
                    else False
                if message_type == 'NS':  # 2A. Notifica di Scarto
                    error_list = root.find('ListaErrori')
                    error_str = ''
                    for error in error_list:
                        error_str += "\n[%s] %s %s" % (
                            error.find('Codice').text if error.find(
                                'Codice') is not None else '',
                            error.find('Descrizione').text if error.find(
                                'Descrizione') is not None else '',
                            error.find('Suggerimento').text if error.find(
                                'Suggerimento') is not None else ''
                        )
                    fatturapa_attachment_out.write({
                        'state': 'sender_error',
                        'last_sdi_response': 'SdI ID: {}; '
                                             'Message ID: {}; Receipt date: {}; '
                                             'Error: {}'.format(
                            id_sdi, message_id, receipt_dt, error_str)
                    })
                elif message_type == 'MC':  # 3A. Mancata consegna
                    missed_delivery_note = root.find('Descrizione').text
                    fatturapa_attachment_out.write({
                        'state': 'recipient_error',
                        'last_sdi_response': 'SdI ID: {}; '
                                             'Message ID: {}; Receipt date: {}; '
                                             'Missed delivery note: {}'.format(
                            id_sdi, message_id, receipt_dt,
                            missed_delivery_note)
                    })
                elif message_type == 'RC':  # 3B. Ricevuta di Consegna
                    delivery_dt = root.find('DataOraConsegna').text
                    fatturapa_attachment_out.write({
                        'state': 'validated',
                        'delivered_date': fields.Datetime.now(),
                        'last_sdi_response': 'SdI ID: {}; '
                                             'Message ID: {}; Receipt date: {}; '
                                             'Delivery date: {}'.format(
                            id_sdi, message_id, receipt_dt, delivery_dt)
                    })
                elif message_type == 'NE':  # 4A. Notifica Esito per PA
                    esito_committente = root.find('EsitoCommittente')
                    if esito_committente is not None:
                        # more than one esito?
                        esito = esito_committente.find('Esito')
                        if esito is not None:
                            if esito.text == 'EC01':
                                state = 'validated'
                            elif esito.text == 'EC02':
                                state = 'rejected'
                            fatturapa_attachment_out.write({
                                'state': state,
                                'last_sdi_response': 'SdI ID: {}; '
                                                     'Message ID: {}; Response: {}; '.format(
                                    id_sdi, message_id, esito.text)
                            })
                elif message_type == 'DT':  # 5. Decorrenza Termini per PA
                    description = root.find('Descrizione')
                    if description is not None:
                        fatturapa_attachment_out.write({
                            'state': 'validated',
                            'last_sdi_response': 'SdI ID: {}; '
                                                 'Message ID: {}; Receipt date: {}; '
                                                 'Description: {}'.format(
                                id_sdi, message_id, receipt_dt,
                                description.text)
                        })
                # not implemented - todo
                elif message_type == 'AT':  # 6. Avvenuta Trasmissione per PA
                    description = root.find('Descrizione')
                    if description is not None:
                        fatturapa_attachment_out.write({
                            'state': 'accepted',
                            'last_sdi_response': (
                                'SdI ID: {}; Message ID: {}; Receipt date: {};'
                                ' Description: {}'
                            ).format(
                                id_sdi, message_id, receipt_dt,
                                description.text)
                        })

                message_dict['res_id'] = fatturapa_attachment_out.id
        return message_dict

    @api.multi
    def unlink(self):
        for att in self:
            if att.state != 'ready':
                raise UserError(_(
                    "You can only delete files in 'Ready to Send' state."
                ))
        return super(FatturaPAAttachmentOut, self).unlink()


class FatturaAttachments(models.Model):
    _inherit = "fatturapa.attachments"

    is_pdf_invoice_print = fields.Boolean(
        help="This attachment contains the PDF report of the linked invoice")
