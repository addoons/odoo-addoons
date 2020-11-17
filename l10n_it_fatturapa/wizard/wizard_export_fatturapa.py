# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)

import io
import zipfile
from datetime import datetime

import base64
import logging
import os
import string
import random

from odoo import api, fields, models
from odoo.tools.translate import _
from odoo.exceptions import UserError
from odoo.tools.float_utils import float_round, float_is_zero

from ..bindings.fatturapa import (
    FatturaElettronica,
    DatiRitenutaType,
    AltriDatiGestionaliType,
    DatiCassaPrevidenzialeType,
    DatiRiepilogoType,
    FatturaElettronicaHeaderType,
    DatiTrasmissioneType,
    IdFiscaleType,
    ContattiTrasmittenteType,
    CedentePrestatoreType,
    AnagraficaType,
    IndirizzoType,
    IscrizioneREAType,
    CessionarioCommittenteType,
    RappresentanteFiscaleType,
    DatiAnagraficiCedenteType,
    DatiAnagraficiCessionarioType,
    DatiAnagraficiRappresentanteType,
    TerzoIntermediarioSoggettoEmittenteType,
    DatiAnagraficiTerzoIntermediarioType,
    FatturaElettronicaBodyType,
    DatiGeneraliType,
    DettaglioLineeType,
    DatiBeniServiziType,
    DatiRiepilogoType,
    DatiGeneraliDocumentoType,
    DatiDocumentiCorrelatiType,
    ContattiType,
    DatiPagamentoType,
    DettaglioPagamentoType,
    AllegatiType,
    ScontoMaggiorazioneType,
    CodiceArticoloType,
    DatiAnagraficiVettoreType, DatiBolloType, DatiTrasportoType, DatiDDTType)


WT_TAX_CODE = {
    'inps': 'RT03',
    'enasarco': 'RT04',
    'enpam': 'RT05',
    'other': 'RT06'
}

TC_CODE = {
    'inps': 'TC22',
    'enasarco': 'TC07',
    'enpam': 'TC09',
}

from ..models.account import (
    RELATED_DOCUMENT_TYPES)

_logger = logging.getLogger(__name__)

try:
    from pyxb.utils import domutils
    from pyxb.binding.datatypes import decimal as pyxb_decimal
    from unidecode import unidecode
    from pyxb.exceptions_ import SimpleFacetValueError, SimpleTypeValueError
except ImportError as err:
    _logger.debug(err)


def id_generator(
        size=5, chars=string.ascii_uppercase + string.digits +
                      string.ascii_lowercase
):
    return ''.join(random.choice(chars) for dummy in range(size))

class FatturapaBDS(domutils.BindingDOMSupport):

    def valueAsText(self, value, enable_default_namespace=True):
        if isinstance(value, pyxb_decimal) and hasattr(value, '_CF_pattern'):
            # PyXB changes the text representation of decimals
            # so that it breaks pattern matching.
            # We have to use directly the string value
            # instead of letting PyXB edit it
            return str(value)
        return super(FatturapaBDS, self) \
            .valueAsText(value, enable_default_namespace)


fatturapaBDS = FatturapaBDS()


class WizardFatturapaZipExport(models.TransientModel):
    _name = 'wizard.fatturapa.export'

    @api.model
    def _default_name(self):
        return "%s_%s" % (
            _("E-invoice-export"), datetime.now().strftime('%Y%m%d%H%M'))

    data = fields.Binary("File", readonly=True)
    name = fields.Char('Filename', default=_default_name, required=True)

    @api.multi
    def export_zip(self):
        self.ensure_one()
        attachments = self.env[self.env.context['active_model']].browse(
            self.env.context['active_ids'])
        for att in attachments:
            if att.exported_zip:
                raise UserError(_(
                    "Attachment %s already exported. Remove ZIP file first"
                ) % att.display_name)
            if not att.datas or not att.datas_fname:
                raise UserError(
                    _("Attachment %s does not have XML file")
                    % att.display_name)

        fp = io.BytesIO()
        with zipfile.ZipFile(fp, mode="w") as zf:
            for att in attachments:
                zf.writestr(att.datas_fname, base64.b64decode(att.datas))
        fp.seek(0)
        data = fp.read()
        attach_vals = {
            'name': self.name + '.zip',
            'datas_fname': self.name + '.zip',
            'datas': base64.encodestring(data),
        }
        zip_att = self.env['ir.attachment'].create(attach_vals)
        for att in attachments:
            att.exported_zip = zip_att
        return {
            'view_type': 'form',
            'name': _("Export E-Invoices"),
            'res_id': zip_att.id,
            'view_mode': 'form',
            'res_model': 'ir.attachment',
            'type': 'ir.actions.act_window',
        }


class WizardExportFatturapa(models.TransientModel):
    _name = "wizard.export.fatturapa"
    _description = "Export E-invoice"

    def getTipoRitenuta(self, wt_types, partner):
        if wt_types == 'ritenuta':
            if partner.is_company:
                tipoRitenuta = 'RT02'
            else:
                tipoRitenuta = 'RT01'
        else:
            tipoRitenuta = WT_TAX_CODE[wt_types]
        return tipoRitenuta

    @api.model
    def _domain_ir_values(self):
        model_name = self.env.context.get('active_model', False)
        # Get all print actions for current model
        return [('binding_model_id', '=', model_name),
                ('type', '=', 'ir.actions.report')]


    report_print_menu = fields.Many2one(
        comodel_name='ir.actions.actions',
        domain=_domain_ir_values,
        help='This report will be automatically included in the created XML')

    def saveAttachment(self, fatturapa, number):
        attach_obj = self.env['fatturapa.attachment.out']
        vat = attach_obj.get_file_vat()

        attach_str = fatturapa.toxml(
            encoding="UTF-8",
            bds=fatturapaBDS,
        )
        fatturapaBDS.reset()
        attach_vals = {
            'name': '%s_%s.xml' % (vat, number),
            'datas_fname': '%s_%s.xml' % (vat, number),
            'datas': base64.encodestring(attach_str),
        }
        return attach_obj.create(attach_vals)

    def setProgressivoInvio(self, fatturapa):

        company = self.env.user.company_id
        fatturapa_sequence = company.fatturapa_sequence_id
        if not fatturapa_sequence:
            raise UserError(
                _('E-invoice sequence not configured.'))
        number = fatturapa_sequence.next_by_id()
        try:
            fatturapa.FatturaElettronicaHeader.DatiTrasmissione. \
                ProgressivoInvio = number
        except (SimpleFacetValueError, SimpleTypeValueError) as e:
            msg = _(
                'FatturaElettronicaHeader.DatiTrasmissione.'
                'ProgressivoInvio:\n%s'
            ) % str(e)
            raise UserError(msg)
        return number

    def _setIdTrasmittente(self, company, fatturapa):

        if not company.country_id:
            raise UserError(
                _('Company Country not set.'))
        IdPaese = company.country_id.code

        IdCodice = company.partner_id.fiscalcode
        if not IdCodice:
            if company.vat:
                IdCodice = company.vat[2:]
        if not IdCodice:
            raise UserError(
                _('Company does not have fiscal code or VAT number.'))

        #Ogni connettore, ARUBA, Credemtel ... Necessita di inserire
        #Proprie informazioni come ID Trasmittente e Contatti Trasmittente
        #Prendiamo il canale SDI di default e mettiamo questi.from
        canale_sdi_id = self.env['sdi.channel'].search([('active_web_server', '=', True)])
        if canale_sdi_id:
            if canale_sdi_id.provider == 'aruba':
                IdPaese = 'IT'
                IdCodice = '01879020517'


        fatturapa.FatturaElettronicaHeader.DatiTrasmissione. \
            IdTrasmittente = IdFiscaleType(
            IdPaese=IdPaese, IdCodice=IdCodice)

        return True

    def _setFormatoTrasmissione(self, partner, fatturapa):
        if partner.is_pa:
            fatturapa.FatturaElettronicaHeader.DatiTrasmissione. \
                FormatoTrasmissione = 'FPA12'
        else:
            fatturapa.FatturaElettronicaHeader.DatiTrasmissione. \
                FormatoTrasmissione = 'FPR12'

        return True

    def _setCodiceDestinatario(self, partner, fatturapa):
        pec_destinatario = None
        if partner.is_pa:
            if not partner.ipa_code:
                raise UserError(_(
                    "Partner %s is PA but does not have IPA code."
                ) % partner.name)
            code = partner.ipa_code
        else:
            if not partner.codice_destinatario:
                partner.codice_destinatario = '0000000'
                # raise UserError(_(
                #     "Partner %s is not PA but does not have Addressee "
                #     "Code."
                # ) % partner.name)
            code = partner.codice_destinatario
            if code == '0000000':
                pec_destinatario = partner.pec_destinatario
        fatturapa.FatturaElettronicaHeader.DatiTrasmissione. \
            CodiceDestinatario = code.upper()
        if pec_destinatario:
            fatturapa.FatturaElettronicaHeader.DatiTrasmissione. \
                PECDestinatario = pec_destinatario

        return True

    def _setContattiTrasmittente(self, company, fatturapa):
        Telefono = company.phone
        Email = company.email

        # Ogni connettore, ARUBA, Credemtel ... Necessita di inserire
        # Proprie informazioni come ID Trasmittente e Contatti Trasmittente
        # Prendiamo il canale SDI di default e mettiamo questi.from
        canale_sdi_id = self.env['sdi.channel'].search([('active_web_server', '=', True)])
        if canale_sdi_id:
            if canale_sdi_id.provider == 'aruba':
                Telefono = '05750505'
                Email = 'info@arubapec.it'

        fatturapa.FatturaElettronicaHeader.DatiTrasmissione. \
            ContattiTrasmittente = ContattiTrasmittenteType(
            Telefono=Telefono or None, Email=Email or None)

        return True

    def setDatiTrasmissione(self, company, partner, fatturapa):
        fatturapa.FatturaElettronicaHeader.DatiTrasmissione = (
            DatiTrasmissioneType())
        self._setIdTrasmittente(company, fatturapa)
        self._setFormatoTrasmissione(partner.commercial_partner_id, fatturapa)
        self._setCodiceDestinatario(partner.commercial_partner_id, fatturapa)
        self._setContattiTrasmittente(company, fatturapa)

    def _setDatiAnagraficiCedente(self, CedentePrestatore, company):

        if not company.vat:
            raise UserError(
                _('TIN not set.'))
        CedentePrestatore.DatiAnagrafici = DatiAnagraficiCedenteType()
        fatturapa_fp = company.fatturapa_fiscal_position_id
        if not fatturapa_fp:
            raise UserError(_(
                'Fiscal position for electronic invoice not set '
                'for company %s. '
                '(Go to Accounting / Configuration / Settings / '
                'Electronic Invoice)' % company.name
            ))
        CedentePrestatore.DatiAnagrafici.IdFiscaleIVA = IdFiscaleType(
            IdPaese=company.country_id.code, IdCodice=company.vat[2:])
        CedentePrestatore.DatiAnagrafici.Anagrafica = AnagraficaType(
            Denominazione=company.name)

        if company.partner_id.fiscalcode:
            CedentePrestatore.DatiAnagrafici.CodiceFiscale = (
                company.partner_id.fiscalcode.upper())
        CedentePrestatore.DatiAnagrafici.RegimeFiscale = fatturapa_fp.code
        return True

    def _setAlboProfessionaleCedente(self, CedentePrestatore, company):
        # TODO Albo professionale, for now the main company is considered
        # to be a legal entity and not a single person
        # 1.2.1.4   <AlboProfessionale>
        # 1.2.1.5   <ProvinciaAlbo>
        # 1.2.1.6   <NumeroIscrizioneAlbo>
        # 1.2.1.7   <DataIscrizioneAlbo>
        return True

    def _setSedeCedente(self, CedentePrestatore, company):

        if not company.street:
            raise UserError(
                _('Your company Street is not set.'))
        if not company.zip:
            raise UserError(
                _('Your company ZIP is not set.'))
        if not company.city:
            raise UserError(
                _('Your company City is not set.'))
        if not company.country_id:
            raise UserError(
                _('Your company Country is not set.'))
        # TODO: manage address number in <NumeroCivico>
        # see https://github.com/OCA/partner-contact/pull/96
        CedentePrestatore.Sede = IndirizzoType(
            Indirizzo=company.street,
            CAP=company.zip,
            Comune=company.city,
            Nazione=company.country_id.code)
        if company.partner_id.state_id:
            CedentePrestatore.Sede.Provincia = company.partner_id.state_id.code

        return True

    def _setStabileOrganizzazione(self, CedentePrestatore, company):
        if company.fatturapa_stabile_organizzazione:
            stabile_organizzazione = company.fatturapa_stabile_organizzazione
            if not stabile_organizzazione.street:
                raise UserError(
                    _('Street is not set for %s.') %
                    stabile_organizzazione.name)
            if not stabile_organizzazione.zip:
                raise UserError(
                    _('ZIP is not set for %s.') %
                    stabile_organizzazione.name)
            if not stabile_organizzazione.city:
                raise UserError(
                    _('City is not set for %s.') %
                    stabile_organizzazione.name)
            if not stabile_organizzazione.country_id:
                raise UserError(
                    _('Country is not set for %s.') %
                    stabile_organizzazione.name)
            CedentePrestatore.StabileOrganizzazione = IndirizzoType(
                Indirizzo=stabile_organizzazione.street,
                CAP=stabile_organizzazione.zip,
                Comune=stabile_organizzazione.city,
                Nazione=stabile_organizzazione.country_id.code)
            if stabile_organizzazione.state_id:
                CedentePrestatore.StabileOrganizzazione.Provincia = (
                    stabile_organizzazione.state_id.code)
        return True

    def _setRea(self, CedentePrestatore, company):

        if (
                company.rea_office and company.rea_code and
                company.rea_liquidation_state
        ):
            # The required fields for IscrizioneREA (not required) are
            # Ufficio, NumeroREA and StatoLiquidazione
            CedentePrestatore.IscrizioneREA = IscrizioneREAType(
                Ufficio=(company.rea_office.code or None),
                NumeroREA=company.rea_code,
                CapitaleSociale=(
                        company.rea_capital and
                        '%.2f' % company.rea_capital or None),
                SocioUnico=(company.rea_member_type or None),
                StatoLiquidazione=company.rea_liquidation_state
            )

    def _setContatti(self, CedentePrestatore, company):
        CedentePrestatore.Contatti = ContattiType(
            Telefono=company.partner_id.phone or None,
            Email=company.partner_id.email or None
        )

    def _setPubAdministrationRef(self, CedentePrestatore, company):
        if company.fatturapa_pub_administration_ref:
            CedentePrestatore.RiferimentoAmministrazione = (
                company.fatturapa_pub_administration_ref)

    def setCedentePrestatore(self, company, fatturapa):
        fatturapa.FatturaElettronicaHeader.CedentePrestatore = (
            CedentePrestatoreType())
        self._setDatiAnagraficiCedente(
            fatturapa.FatturaElettronicaHeader.CedentePrestatore,
            company)
        self._setSedeCedente(
            fatturapa.FatturaElettronicaHeader.CedentePrestatore,
            company)
        self._setAlboProfessionaleCedente(
            fatturapa.FatturaElettronicaHeader.CedentePrestatore,
            company)
        self._setStabileOrganizzazione(
            fatturapa.FatturaElettronicaHeader.CedentePrestatore,
            company)
        # TODO: add Contacts
        self._setRea(
            fatturapa.FatturaElettronicaHeader.CedentePrestatore,
            company)
        self._setContatti(
            fatturapa.FatturaElettronicaHeader.CedentePrestatore,
            company)
        self._setPubAdministrationRef(
            fatturapa.FatturaElettronicaHeader.CedentePrestatore,
            company)

    def _setDatiAnagraficiCessionario(self, partner, fatturapa):
        fatturapa.FatturaElettronicaHeader.CessionarioCommittente. \
            DatiAnagrafici = DatiAnagraficiCessionarioType()
        if not partner.vat and not partner.fiscalcode:
            if (
                    partner.codice_destinatario == 'XXXXXXX'
                    and partner.country_id.code
                    and partner.country_id.code != 'IT'
            ):
                # SDI accepts missing VAT# for foreign customers by setting a
                # fake IdCodice and a valid IdPaese
                # Otherwise raise error if we have no VAT# and no Fiscal code
                fatturapa.FatturaElettronicaHeader.CessionarioCommittente. \
                    DatiAnagrafici.IdFiscaleIVA = IdFiscaleType(
                    IdPaese=partner.country_id.code,
                    IdCodice='99999999999')
            else:
                raise UserError(
                    _('VAT number and fiscal code are not set for %s.') %
                    partner.name)
        if partner.fiscalcode:
            fatturapa.FatturaElettronicaHeader.CessionarioCommittente. \
                DatiAnagrafici.CodiceFiscale = partner.fiscalcode.upper()
        if partner.vat and partner.company_type == 'company':
            if 'IT' not in partner.vat and partner.country_id.code == 'IT' :
                partner.vat = 'IT' + partner.vat
            fatturapa.FatturaElettronicaHeader.CessionarioCommittente. \
                DatiAnagrafici.IdFiscaleIVA = IdFiscaleType(
                IdPaese=partner.vat[0:2], IdCodice=partner.vat[2:])
        if partner.company_name:
            # This is valorized by e-commerce orders typically
            fatturapa.FatturaElettronicaHeader.CessionarioCommittente. \
                DatiAnagrafici.Anagrafica = AnagraficaType(
                Denominazione=partner.company_name)
        elif partner.company_type == 'company':
            fatturapa.FatturaElettronicaHeader.CessionarioCommittente. \
                DatiAnagrafici.Anagrafica = AnagraficaType(
                Denominazione=partner.name)
        elif partner.company_type == 'person':
            firstname = False
            lastname = False
            if (not partner.lastname or not partner.firstname) and partner.name:
                #Se il cliente ha il NAME provo a calcolare il nome e cognome
                partner._inverse_name()
                self.env.cr.commit()
                self.env.cr.execute('SELECT lastname, firstname from res_partner WHERE id = %s', (partner.id, ))
                result_query = self.env.cr.fetchall()
                if result_query:
                    firstname = result_query[0][1]
                    lastname = result_query[0][0]
            if (not partner.lastname or not partner.firstname) and (not firstname or not lastname):
                raise UserError(
                    _("Partner %s must have name and surname.") %
                    partner.name)

            if partner.lastname:
                lastname = partner.lastname
            if partner.firstname:
                firstname = partner.firstname
            fatturapa.FatturaElettronicaHeader.CessionarioCommittente. \
                DatiAnagrafici.Anagrafica = AnagraficaType(
                Cognome=lastname,
                Nome=firstname
            )

        if partner.eori_code:
            fatturapa.FatturaElettronicaHeader.CessionarioCommittente. \
                DatiAnagrafici.Anagrafica.CodEORI = partner.eori_code

        return True

    def _setDatiAnagraficiRappresentanteFiscale(self, partner, fatturapa):
        fatturapa.FatturaElettronicaHeader.RappresentanteFiscale = (
            RappresentanteFiscaleType())
        fatturapa.FatturaElettronicaHeader.RappresentanteFiscale. \
            DatiAnagrafici = DatiAnagraficiRappresentanteType()
        if not partner.vat and not partner.fiscalcode:
            raise UserError(
                _('VAT number and fiscal code are not set for %s.') %
                partner.name)
        if partner.fiscalcode:
            fatturapa.FatturaElettronicaHeader.RappresentanteFiscale. \
                DatiAnagrafici.CodiceFiscale = partner.fiscalcode.upper()
        if partner.vat:
            if 'IT' not in partner.vat and partner.country_id.code == 'IT':
                partner.vat = 'IT' + partner.vat
            fatturapa.FatturaElettronicaHeader.RappresentanteFiscale. \
                DatiAnagrafici.IdFiscaleIVA = IdFiscaleType(
                IdPaese=partner.vat[0:2], IdCodice=partner.vat[2:])
        fatturapa.FatturaElettronicaHeader.RappresentanteFiscale. \
            DatiAnagrafici.Anagrafica = AnagraficaType(
            Denominazione=partner.name)
        if partner.eori_code:
            fatturapa.FatturaElettronicaHeader.RappresentanteFiscale. \
                DatiAnagrafici.Anagrafica.CodEORI = partner.eori_code

        return True

    def _setTerzoIntermediarioOSoggettoEmittente(self, partner, fatturapa):
        fatturapa.FatturaElettronicaHeader. \
            TerzoIntermediarioOSoggettoEmittente = (
            TerzoIntermediarioSoggettoEmittenteType()
        )
        fatturapa.FatturaElettronicaHeader. \
            TerzoIntermediarioOSoggettoEmittente. \
            DatiAnagrafici = DatiAnagraficiTerzoIntermediarioType()
        if not partner.vat and not partner.fiscalcode:
            raise UserError(
                _('Partner VAT number and fiscal code are not set.'))
        if partner.fiscalcode:
            fatturapa.FatturaElettronicaHeader. \
                TerzoIntermediarioOSoggettoEmittente. \
                DatiAnagrafici.CodiceFiscale = partner.fiscalcode.upper()
        if partner.vat:
            if 'IT' not in partner.vat and partner.country_id.code == 'IT':
                partner.vat = 'IT' + partner.vat
            fatturapa.FatturaElettronicaHeader. \
                TerzoIntermediarioOSoggettoEmittente. \
                DatiAnagrafici.IdFiscaleIVA = IdFiscaleType(
                IdPaese=partner.vat[0:2], IdCodice=partner.vat[2:])
        fatturapa.FatturaElettronicaHeader. \
            TerzoIntermediarioOSoggettoEmittente. \
            DatiAnagrafici.Anagrafica = AnagraficaType(
            Denominazione=partner.name)
        if partner.eori_code:
            fatturapa.FatturaElettronicaHeader. \
                TerzoIntermediarioOSoggettoEmittente. \
                DatiAnagrafici.Anagrafica.CodEORI = partner.eori_code
        fatturapa.FatturaElettronicaHeader.SoggettoEmittente = 'TZ'
        return True

    def _setSedeCessionario(self, partner, fatturapa):

        if not partner.street:
            raise UserError(
                _('Customer street is not set.'))
        if not partner.city:
            raise UserError(
                _('Customer city is not set.'))
        if not partner.country_id:
            raise UserError(
                _('Customer country is not set.'))

        # TODO: manage address number in <NumeroCivico>
        if partner.codice_destinatario == 'XXXXXXX':
            fatturapa.FatturaElettronicaHeader.CessionarioCommittente.Sede = (
                IndirizzoType(
                    Indirizzo=partner.street,
                    CAP='00000',
                    Comune=partner.city,
                    Provincia='EE',
                    Nazione=partner.country_id.code))
        else:
            if not partner.zip:
                raise UserError(
                    _('Customer ZIP not set.'))
            fatturapa.FatturaElettronicaHeader.CessionarioCommittente.Sede = (
                IndirizzoType(
                    Indirizzo=partner.street,
                    CAP=partner.zip,
                    Comune=partner.city,
                    Nazione=partner.country_id.code))
            if partner.state_id:
                fatturapa.FatturaElettronicaHeader.CessionarioCommittente. \
                    Sede.Provincia = partner.state_id.code

        return True

    def setRappresentanteFiscale(self, company, fatturapa):
        if company.fatturapa_tax_representative:
            self._setDatiAnagraficiRappresentanteFiscale(
                company.fatturapa_tax_representative, fatturapa)
        return True

    def setCessionarioCommittente(self, partner, fatturapa):
        fatturapa.FatturaElettronicaHeader.CessionarioCommittente = (
            CessionarioCommittenteType())
        self._setDatiAnagraficiCessionario(
            partner, fatturapa)
        self._setSedeCessionario(partner, fatturapa)

    def setTerzoIntermediarioOSoggettoEmittente(self, company, fatturapa):
        if company.fatturapa_sender_partner:
            self._setTerzoIntermediarioOSoggettoEmittente(
                company.fatturapa_sender_partner, fatturapa)
        return True

    def setDatiGeneraliDocumento(self, invoice, body):

        # TODO DatiSAL

        body.DatiGenerali = DatiGeneraliType()
        if not invoice.number:
            raise UserError(
                _('Invoice does not have a number.'))

        TipoDocumento = invoice.fiscal_document_type_id.code
        ImportoTotaleDocumento = invoice.amount_total
        if invoice.split_payment:
            ImportoTotaleDocumento += invoice.amount_sp
        body.DatiGenerali.DatiGeneraliDocumento = DatiGeneraliDocumentoType(
            TipoDocumento=TipoDocumento,
            Divisa=invoice.currency_id.name,
            Data=invoice.date_invoice,
            Numero=invoice.number,
            ImportoTotaleDocumento='%.2f' % float_round(ImportoTotaleDocumento, 2))

        # ScontoMaggiorazione, Arrotondamento,

        if invoice.tax_stamp:
            body.DatiGenerali.DatiGeneraliDocumento.DatiBollo = DatiBolloType(
                BolloVirtuale="SI",
            )
            if invoice.company_id.tax_stamp_product_id:
                stamp_price = invoice.company_id.tax_stamp_product_id.list_price
                if not float_is_zero(stamp_price, precision_digits=2):
                    body.DatiGenerali.DatiGeneraliDocumento.DatiBollo. \
                        ImportoBollo = '%.2f' % float_round(stamp_price, 2)

        if invoice.comment:
            # max length of Causale is 200
            caus_list = invoice.comment.split('\n')
            for causale in caus_list:
                if not causale:
                    continue
                causale_list_200 = \
                    [causale[i:i+200] for i in range(0, len(causale), 200)]
                for causale200 in causale_list_200:
                    # Remove non latin chars, but go back to unicode string,
                    # as expected by String200LatinType
                    causale = causale200.encode(
                        'latin', 'ignore').decode('latin')
                    body.DatiGenerali.DatiGeneraliDocumento.Causale \
                        .append(causale)

        if invoice.company_id.fatturapa_art73:
            body.DatiGenerali.DatiGeneraliDocumento.Art73 = 'SI'

        #RITENUTA

        ritenuta_lines = invoice.withholding_tax_line_ids

        for wt_line in ritenuta_lines:
            if not wt_line.withholding_tax_id.causale_pagamento_id.code:
                raise UserError(_('Missing payment reason for '
                                  'withholding tax %s!')
                                % wt_line.withholding_tax_id.name)

            tipoRitenuta = self.getTipoRitenuta(
                wt_line.withholding_tax_id.wt_types,
                invoice.partner_id
            )
            body.DatiGenerali.DatiGeneraliDocumento.DatiRitenuta.append(
                DatiRitenutaType(
                    TipoRitenuta=tipoRitenuta,
                    ImportoRitenuta='%.2f' % float_round(wt_line.tax, 2),
                    AliquotaRitenuta='%.2f' % float_round(
                        wt_line.withholding_tax_id.tax, 2),
                    CausalePagamento=wt_line.withholding_tax_id.
                        causale_pagamento_id.code
            ))

            if wt_line.withholding_tax_id.use_daticassaprev:
                tax_id = wt_line.withholding_tax_id.daticassprev_tax_id
                tax_kind = tax_id.kind_id.code

                body.DatiGenerali.DatiGeneraliDocumento. \
                    DatiCassaPrevidenziale.append(
                    DatiCassaPrevidenzialeType(
                        TipoCassa=TC_CODE[wt_line.withholding_tax_id.wt_types],
                        AlCassa='%.2f' % float_round(
                            wt_line.withholding_tax_id.tax, 2),
                        ImportoContributoCassa='%.2f' % float_round(
                            wt_line.tax, 2),
                        AliquotaIVA='0.00',
                        Natura=tax_kind,
                    )
                )
        # FINE RITENUTA

        return True

    def get_tax_riepilogo(self, body, tax_id):
        for riepilogo in body.DatiBeniServizi.DatiRiepilogo:
            if float(riepilogo.AliquotaIVA) == 0.0 and riepilogo.Natura == tax_id.kind_id.code:
                return riepilogo

    def setRelatedDocumentTypes(self, invoice, body):
        for line in invoice.invoice_line_ids:
            for related_document in line.related_documents:
                doc_type = RELATED_DOCUMENT_TYPES[related_document.type]
                documento = DatiDocumentiCorrelatiType()
                if related_document.name:
                    documento.IdDocumento = related_document.name
                if related_document.lineRef:
                    documento.RiferimentoNumeroLinea.append(
                        line.ftpa_line_number)
                if related_document.date:
                    documento.Data = related_document.date
                if related_document.numitem:
                    documento.NumItem = related_document.numitem
                if related_document.code:
                    documento.CodiceCommessaConvenzione = related_document.code
                if related_document.cup:
                    documento.CodiceCUP = related_document.cup
                if related_document.cig:
                    documento.CodiceCIG = related_document.cig
                getattr(body.DatiGenerali, doc_type).append(documento)
        for related_document in invoice.related_documents:
            doc_type = RELATED_DOCUMENT_TYPES[related_document.type]
            documento = DatiDocumentiCorrelatiType()
            if related_document.name:
                documento.IdDocumento = related_document.name
            if related_document.date:
                documento.Data = related_document.date
            if related_document.numitem:
                documento.NumItem = related_document.numitem
            if related_document.code:
                documento.CodiceCommessaConvenzione = related_document.code
            if related_document.cup:
                documento.CodiceCUP = related_document.cup
            if related_document.cig:
                documento.CodiceCIG = related_document.cig
            getattr(body.DatiGenerali, doc_type).append(documento)
        return True

    def setDatiTrasporto(self, invoice, body):
        return True

    def setDatiDDT(self, invoice, body):
        if self.include_ddt_data == 'dati_ddt':
            inv_lines_by_ddt = {}
            for line in invoice.invoice_line_ids:
                if (
                        line.ddt_line_id and
                        line.ddt_line_id.package_preparation_id.ddt_number and
                        line.ddt_line_id.package_preparation_id.date
                ):
                    key = (
                        line.ddt_line_id.package_preparation_id.ddt_number,
                        line.ddt_line_id.package_preparation_id.date
                    )
                    if key not in inv_lines_by_ddt:
                        inv_lines_by_ddt[key] = []
                    inv_lines_by_ddt[key].append(line.ftpa_line_number)
            for key in sorted(inv_lines_by_ddt.keys()):
                DatiDDT = DatiDDTType(
                    NumeroDDT=key[0],
                    DataDDT=key[1]
                )
                for line_number in inv_lines_by_ddt[key]:
                    DatiDDT.RiferimentoNumeroLinea.append(line_number)
                body.DatiGenerali.DatiDDT.append(DatiDDT)
        elif self.include_ddt_data == 'dati_trasporto':
            body.DatiGenerali.DatiTrasporto = DatiTrasportoType(
                MezzoTrasporto=invoice.transportation_method_id.name or None,
                CausaleTrasporto=invoice.transportation_reason_id.name or None,
                NumeroColli=invoice.parcels or None,
                Descrizione=invoice.goods_description_id.name or None,
                PesoLordo='%.2f' % invoice.gross_weight,
                PesoNetto='%.2f' % invoice.weight,
                TipoResa=invoice.incoterms_id.code or None
            )
            if invoice.carrier_id:
                if not invoice.carrier_id.vat:
                    raise UserError(
                        _('TIN not set for %s.') % invoice.carrier_id.name)
                body.DatiGenerali.DatiTrasporto.DatiAnagraficiVettore = (
                    DatiAnagraficiVettoreType())
                if invoice.carrier_id.fiscalcode:
                    body.DatiGenerali.DatiTrasporto.DatiAnagraficiVettore. \
                        CodiceFiscale = invoice.carrier_id.fiscalcode.upper()
                body.DatiGenerali.DatiTrasporto.DatiAnagraficiVettore. \
                    IdFiscaleIVA = IdFiscaleType(
                    IdPaese=invoice.carrier_id.vat[0:2],
                    IdCodice=invoice.carrier_id.vat[2:]
                )
                body.DatiGenerali.DatiTrasporto.DatiAnagraficiVettore. \
                    Anagrafica = AnagraficaType(
                    Denominazione=invoice.carrier_id.name)

    def _get_prezzo_unitario(self, line):
        res = line.price_unit
        if (
                line.invoice_line_tax_ids and
                line.invoice_line_tax_ids[0].price_include
        ):
            res = line.price_unit / (
                    1 + (line.invoice_line_tax_ids[0].amount / 100))
        return res

    def setDettaglioLinee(self, invoice, body):

        body.DatiBeniServizi = DatiBeniServiziType()
        # TipoCessionePrestazione not handled

        line_no = 1
        price_precision = self.env['decimal.precision'].precision_get(
            'Product Price')
        if price_precision < 2:
            # XML wants at least 2 decimals always
            price_precision = 2
        uom_precision = self.env['decimal.precision'].precision_get(
            'Product Unit of Measure')
        if uom_precision < 2:
            uom_precision = 2
        for line in invoice.invoice_line_ids:
            if not line.display_type:
                if not line.invoice_line_tax_ids:
                    raise UserError(
                        _("Invoice line %s does not have tax.") % line.name)
                if len(line.invoice_line_tax_ids) > 1:
                    raise UserError(
                        _("Too many taxes for invoice line %s.") % line.name)
                aliquota = line.invoice_line_tax_ids[0].amount
                AliquotaIVA = '%.2f' % (aliquota)
                line.ftpa_line_number = line_no
                prezzo_unitario = self._get_prezzo_unitario(line)
                DettaglioLinea = DettaglioLineeType(
                    NumeroLinea=str(line_no),
                    # can't insert newline with pyxb
                    # see https://tinyurl.com/ycem923t
                    # and '&#10;' would not be correctly visualized anyway
                    # (for example firefox replaces '&#10;' with space)
                    Descrizione=line.name.replace('\n', ' ').encode(
                        'latin', 'ignore').decode('latin'),
                    PrezzoUnitario='{prezzo:.{precision}f}'.format(
                        prezzo=prezzo_unitario, precision=price_precision),
                    Quantita='{qta:.{precision}f}'.format(
                        qta=line.quantity, precision=uom_precision),
                    UnitaMisura=line.uom_id and (
                        unidecode(line.uom_id.name)) or None,
                    PrezzoTotale='%.2f' % line.price_subtotal,
                    AliquotaIVA=AliquotaIVA)
                DettaglioLinea.ScontoMaggiorazione.extend(
                    self.setScontoMaggiorazione(line))
                if aliquota == 0.0:
                    if not line.invoice_line_tax_ids[0].kind_id:
                        raise UserError(
                            _("No 'nature' field for tax %s.") %
                            line.invoice_line_tax_ids[0].name)
                    DettaglioLinea.Natura = line.invoice_line_tax_ids[
                        0
                    ].kind_id.code
                if line.admin_ref:
                    DettaglioLinea.RiferimentoAmministrazione = line.admin_ref


                if line.product_id:
                    product_code = line.product_id.default_code

                    if line.product_id.default_code:
                        CodiceArticolo = CodiceArticoloType(
                            CodiceTipo='ODOO',
                            CodiceValore=product_code[:35]
                        )
                        DettaglioLinea.CodiceArticolo.append(CodiceArticolo)

                    product_barcode = line.product_id.barcode
                    if product_barcode:
                        CodiceArticolo = CodiceArticoloType(
                            CodiceTipo='EAN',
                            CodiceValore=product_barcode[:35]
                        )
                        DettaglioLinea.CodiceArticolo.append(CodiceArticolo)

                #Ritenuta
                if any([wt for wt in line.invoice_line_tax_wt_ids]):
                    DettaglioLinea.Ritenuta = 'SI'

                line_no += 1

                body.DatiBeniServizi.DettaglioLinee.append(DettaglioLinea)

        return True

    def setScontoMaggiorazione(self, line):
        res = []
        if line.discount:
            res.append(ScontoMaggiorazioneType(
                Tipo='SC',
                Percentuale='%.2f' % float_round(line.discount, 2)
            ))
        return res

    def setDatiRiepilogo(self, invoice, body):
        for tax_line in invoice.tax_line_ids:
            tax = tax_line.tax_id

            riepilogo = DatiRiepilogoType(
                AliquotaIVA='%.2f' % float_round(tax.amount,2),
                ImponibileImporto='%.2f' % float_round(tax_line.base,2),
                Imposta='%.2f' % float_round(tax_line.amount,2)
            )

            if tax.amount == 0.0:
                if not tax.kind_id:
                    raise UserError(
                        _("No 'nature' field for tax %s.") % tax.name)
                riepilogo.Natura = tax.kind_id.code
                if not tax.law_reference:
                    raise UserError(
                        _("No 'law reference' field for tax %s.") % tax.name)
                riepilogo.RiferimentoNormativo = tax.law_reference.encode(
                    'latin', 'ignore').decode('latin')
            if tax.payability:
                riepilogo.EsigibilitaIVA = tax.payability
            # TODO

            # el.remove(el.find('SpeseAccessorie'))
            # el.remove(el.find('Arrotondamento'))

            body.DatiBeniServizi.DatiRiepilogo.append(riepilogo)

        # RITENUTA
        wt_lines_to_write = invoice.withholding_tax_line_ids.filtered(
            lambda x: x.withholding_tax_id.wt_types not in ('ritenuta', 'other')
                      and x.withholding_tax_id.use_daticassaprev
        )
        for wt_line in wt_lines_to_write:
            tax_id = wt_line.withholding_tax_id.daticassprev_tax_id
            tax_riepilogo = self.get_tax_riepilogo(body, tax_id)
            if tax_riepilogo:
                base_amount = float(tax_riepilogo.ImponibileImporto)
                base_amount += wt_line.tax
                tax_riepilogo.ImponibileImporto = '%.2f' % float_round(
                    base_amount, 2)
            else:
                riepilogo = DatiRiepilogoType(
                    AliquotaIVA='0.00',
                    ImponibileImporto='%.2f' % float_round(wt_line.tax, 2),
                    Imposta='0.00',
                    Natura=tax_id.kind_id.code,
                    RiferimentoNormativo=tax_id.law_reference,
                )
                body.DatiBeniServizi.DatiRiepilogo.append(riepilogo)
        # FINE RITENUTA

        return True



    def setDatiPagamento(self, invoice, body):
        if invoice.payment_term_id:
            payment_line_ids = invoice.get_receivable_line_ids()
            if not payment_line_ids:
                return True
            DatiPagamento = DatiPagamentoType()
            if not invoice.payment_term_id.fatturapa_pt_id:
                raise UserError(
                    _('Payment term %s does not have a linked e-invoice '
                      'payment term.') % invoice.payment_term_id.name)
            if not invoice.payment_term_id.fatturapa_pm_id:
                raise UserError(
                    _('Payment term %s does not have a linked e-invoice '
                      'payment method.') % invoice.payment_term_id.name)
            DatiPagamento.CondizioniPagamento = (
                invoice.payment_term_id.fatturapa_pt_id.code)
            move_line_pool = self.env['account.move.line']
            for move_line_id in payment_line_ids:
                move_line = move_line_pool.browse(move_line_id)
                ImportoPagamento = '%.2f' % (
                        move_line.amount_currency or move_line.debit)
                DettaglioPagamento = DettaglioPagamentoType(
                    ModalitaPagamento=(
                        invoice.payment_term_id.fatturapa_pm_id.code),
                    DataScadenzaPagamento=move_line.date_maturity,
                    ImportoPagamento=ImportoPagamento
                )
                if invoice.partner_bank_id:
                    DettaglioPagamento.IstitutoFinanziario = (
                        invoice.partner_bank_id.bank_name)
                    if invoice.partner_bank_id.acc_number:
                        DettaglioPagamento.IBAN = (
                            ''.join(invoice.partner_bank_id.acc_number.split())
                        )
                    # if invoice.partner_bank_id.bank_bic:
                    #     DettaglioPagamento.BIC = (
                    #         invoice.partner_bank_id.bank_bic)
                DatiPagamento.DettaglioPagamento.append(DettaglioPagamento)
            body.DatiPagamento.append(DatiPagamento)

        # RITENUTA
        if invoice.withholding_tax_line_ids and invoice.payment_term_id:
            payment_line_ids = invoice.get_receivable_line_ids()
            index = 0
            rate = invoice.amount_net_pay / invoice.amount_total
            move_line_pool = self.env['account.move.line']
            for move_line_id in payment_line_ids:
                move_line = move_line_pool.browse(move_line_id)
                body.DatiPagamento[0].DettaglioPagamento[index]. \
                    ImportoPagamento = '%.2f' % float_round(
                    (move_line.amount_currency or move_line.debit) * rate, 2)
                index += 1
        # FINE RITENUTA

        return True

    def setAttachments(self, invoice, body):
        if invoice.fatturapa_doc_attachments:
            for doc_id in invoice.fatturapa_doc_attachments:
                file_name, file_extension = os.path.splitext(doc_id.name)
                attachment_name = doc_id.datas_fname if len(
                    doc_id.datas_fname) <= 60 else ''.join([
                    file_name[:(60-len(file_extension))], file_extension])
                AttachDoc = AllegatiType(
                    NomeAttachment=attachment_name,
                    Attachment=base64.decodestring(doc_id.datas)
                )
                body.Allegati.append(AttachDoc)
        return True

    def setFatturaElettronicaHeader(self, company, partner, fatturapa):
        fatturapa.FatturaElettronicaHeader = (
            FatturaElettronicaHeaderType())
        self.setDatiTrasmissione(company, partner, fatturapa)
        self.setCedentePrestatore(company, fatturapa)
        self.setRappresentanteFiscale(company, fatturapa)
        self.setCessionarioCommittente(partner, fatturapa)
        self.setTerzoIntermediarioOSoggettoEmittente(company, fatturapa)

    def setFatturaElettronicaBody(self, inv, FatturaElettronicaBody):

        self.setDatiGeneraliDocumento(inv, FatturaElettronicaBody)
        self.setDettaglioLinee(inv, FatturaElettronicaBody)
        self.setDatiDDT(inv, FatturaElettronicaBody)
        self.setDatiTrasporto(inv, FatturaElettronicaBody)
        self.setRelatedDocumentTypes(inv, FatturaElettronicaBody)
        self.setDatiRiepilogo(inv, FatturaElettronicaBody)
        self.setDatiPagamento(inv, FatturaElettronicaBody)
        self.setAttachments(inv, FatturaElettronicaBody)

    def getPartnerId(self, invoice_ids):

        invoice_model = self.env['account.invoice']
        partner = False

        invoices = invoice_model.browse(invoice_ids)

        for invoice in invoices:
            if not partner:
                partner = invoice.partner_id
            if invoice.partner_id != partner:
                raise UserError(
                    _('Invoices must belong to the same partner.'))

        return partner

    # def group_invoices_by_partner(self):
    #     invoice_ids = self.env.context.get('active_ids', False)
    #     res = {}
    #     for invoice in self.env['account.invoice'].browse(invoice_ids):
    #         if invoice.partner_id.id not in res:
    #             res[invoice.partner_id.id] = []
    #         res[invoice.partner_id.id].append(invoice.id)
    #     return res


    def exportFatturaPA(self):
        invoice_obj = self.env['account.invoice']
        invoice_ids = self.env.context.get('active_ids', False)
        invoice_ids = self.env['account.invoice'].browse(invoice_ids)
        attachments = self.env['fatturapa.attachment.out']
        for invoice in invoice_ids:
            partner = invoice.partner_id

            partner._compute_commercial_partner()
            partner._compute_commercial_company_name()

            if partner.is_pa:
                fatturapa = FatturaElettronica(versione='FPA12')
            else:
                fatturapa = FatturaElettronica(versione='FPR12')

            company = self.env.user.company_id
            context_partner = self.env.context.copy()
            context_partner.update({'lang': partner.lang})
            try:
                self.with_context(context_partner).setFatturaElettronicaHeader(
                    company, partner, fatturapa)

                inv = invoice_obj.with_context(context_partner).browse(invoice.id)
                if inv.fatturapa_attachment_out_id:
                    raise UserError(
                        _("Invoice %s has e-invoice export file yet.") % (
                            inv.number))
                if self.report_print_menu:
                    self.generate_attach_report(inv)
                invoice_body = FatturaElettronicaBodyType()
                inv.preventive_checks()
                self.with_context(
                    context_partner
                ).setFatturaElettronicaBody(
                    inv, invoice_body)
                fatturapa.FatturaElettronicaBody.append(invoice_body)
                # TODO DatiVeicoli

                number = self.setProgressivoInvio(fatturapa)
            except (SimpleFacetValueError, SimpleTypeValueError) as e:
                raise UserError(str(e))

            attach = self.saveAttachment(fatturapa, number)
            attachments |= attach

            inv = invoice_obj.browse(invoice.id)
            inv.write({'fatturapa_attachment_out_id': attach.id})

        action = {
            'view_type': 'form',
            'name': "Export Electronic Invoice",
            'res_model': 'fatturapa.attachment.out',
            'type': 'ir.actions.act_window',
        }
        if len(attachments) == 1:
            action['view_mode'] = 'form'
            action['res_id'] = attachments[0].id
        else:
            action['view_mode'] = 'tree,form'
            action['domain'] = [('id', 'in', attachments.ids)]
        return action

    def generate_attach_report(self, inv):
        binding_model_id = self.with_context(
            lang=None).report_print_menu.binding_model_id.id
        name = self.report_print_menu.name
        report_model = self.env['ir.actions.report'].with_context(
            lang=None
        ).search(
            [('binding_model_id', '=', binding_model_id),
             ('name', '=', name)]
        )
        attachment, attachment_type = report_model.render_qweb_pdf(inv.ids)
        att_id = self.env['ir.attachment'].create({
            'name': inv.number,
            'type': 'binary',
            'datas': base64.encodebytes(attachment),
            'datas_fname': '{}.pdf'.format(inv.number),
            'res_model': 'account.invoice',
            'res_id': inv.id,
            'mimetype': 'application/x-pdf'
        })
        inv.write({
            'fatturapa_doc_attachments': [(0, 0, {
                'is_pdf_invoice_print': True,
                'ir_attachment_id': att_id.id,
                'description': _("Attachment generated by "
                                 "electronic invoice export")})]
        })

    @api.model
    def default_get(self, fields):
        res = super(WizardExportFatturapa, self).default_get(fields)
        invoice_ids = self.env.context.get('active_ids', False)
        invoices = self.env['account.invoice'].browse(invoice_ids)
        for invoice in invoices:
            for line in invoice.invoice_line_ids:
                #Aggiunto questo IF per verificare se l'app DDT e' installata sull'istanza
                #Altrimenti non vengono inseriti i dati DDT nella fattura elettronica
                if 'ddt_line_id' in self.env['account.invoice.line']._fields:
                    if line.ddt_line_id:
                        res['include_ddt_data'] = 'dati_ddt'
                        return res
        return res

    include_ddt_data = fields.Selection([
        ('dati_ddt', 'Include DDT Data'),
        ('dati_trasporto', 'Include transport data'),
    ],
        string="DDT Data",
        help="Include DDT data: The field must be entered when a transport "
             "document associated with a deferred invoice is present\n"
             "Include transport data: The field must be entered when a "
             "shipping invoice to be filled with transport data is present"
    )


