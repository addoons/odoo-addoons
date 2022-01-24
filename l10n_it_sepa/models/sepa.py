import base64
import random

from lxml import etree
from pyxb.utils import domutils
from pyxb.binding.datatypes import decimal as pyxb_decimal, ValidationError
import time

from odoo import models, fields, api,_
from odoo.exceptions import UserError
from odoo.tools import float_repr
from odoo.tools import float_round
from ..bindings.binding import (
    CBIPaymentRequest,
    CBIGroupHeader,
    CBIPaymentInstructionInformation,
    CBICreditTransferTransactionInformation,
    CBIPartyIdentification1,
    CBIBranchAndFinancialInstitutionIdentification1,
    CBIOrganisationIdentification1,
    CBIGenericIdentification1,
    CBIIdType1,
    CBIPaymentTypeInformation1, CBIServiceLevel1, CBIPartyIdentification4, CBIPostalAddress6, CBIIdType2,
    CBIOrganisationIdentification3, CBICashAccount1, CBIAccountIdentification1,
    CBIBranchAndFinancialInstitutionIdentification2, CBIFinancialInstitutionIdentification3,
    CBIClearingSystemMemberIdentification1, PaymentIdentification1, CBIAmountType1, CBIPartyIdentification3,
    CBIParty1Choice, CBIPaymentRequest_00_04_00, CBIOrganisationIdentification2, ActiveOrHistoricCurrencyAndAmount,
    CBICashAccount2, RemittanceInformation5, CountryCode, CBIRegulatoryReporting1)


class AccountBatchPayment(models.Model):
    _inherit = 'account.batch.payment'

    iso_type = fields.Selection([('00.04.00', 'CBI PaymentRequest 00.04.00'),
                                 ('001.001.03', 'Pain.001.001.03'),
                                 ('001.003.03', 'Pain.001.003.03'),
                                 ('001.003.03.ch', 'Pain.001.001.03.ch.02')], default='00.04.00')



    def _generate_export_file(self):
        """
        Funzione che viene chiamata per generare il file XML del pagamento raggruppato
        Verifica il tipo ISO da esportare
        """
        if self.payment_method_code == 'sepa_ct':
            payments = self.payment_ids.sorted(key=lambda r: r.id)

            if self.iso_type == '001.003.03.ch':
                xml_doc = self._create_pain_001_001_03_ch_document(payments)
            elif self.iso_type == '001.003.03':
                xml_doc = self._create_pain_001_003_03_document(payments)
            elif self.iso_type == '001.001.03':
                xml_doc = self._create_pain_001_001_03_document(payments)
            else:
                #Per tutti i restanti metodi di Pagamento 00.04.00
                xml_doc = self._create_00_04_00_document(payments)

            return {
                'file': base64.encodestring(xml_doc),
                'filename': "SCT-" + self.journal_id.code + "-" + str(fields.Date.today()) + ".xml",
                'warning': self.sct_warning,
            }

        return super(AccountBatchPayment, self)._generate_export_file()



    def _create_00_04_00_document(self, doc_payments):
        """
        Crea il Documento di Tipo ISO 00_04_00
        """
        sepa_payment = CBIPaymentRequest()
        company = self.journal_id.company_id
        name_length = self.sct_generic and 35 or 70
        val_MsgId = str(int(time.time() * 100))[-10:]
        val_MsgId = self._sanitize_communication(self.journal_id.company_id.name[-15:]) + val_MsgId
        val_MsgId = str(random.random()) + val_MsgId
        val_MsgId = val_MsgId[-30:]

        val_NbOfTxs = str(len(doc_payments))
        if len(val_NbOfTxs) > 15:
            raise ValidationError(_("Too many transactions for a single file."))
        if not self.journal_id.bank_account_id.bank_bic:
            raise UserError(_("There is no Bank Identifier Code recorded for bank account '%s' of journal '%s'") % (
                self.journal_id.bank_account_id.acc_number, self.journal_id.name))

        #HEADER
        sepa_payment.GrpHdr = CBIGroupHeader(
            MsgId=val_MsgId,
            CreDtTm=time.strftime("%Y-%m-%dT%H:%M:%S"),
            NbOfTxs=val_NbOfTxs,
            CtrlSum=self._get_CtrlSum(doc_payments),
        )

        sepa_payment.GrpHdr.InitgPty = CBIPartyIdentification1(
            Nm=self._sanitize_communication(company.sepa_initiating_party_name[:name_length]),
            Id=CBIIdType1()
        )
        sepa_payment.GrpHdr.InitgPty.Id.OrgId = CBIOrganisationIdentification1()
        sepa_payment.GrpHdr.InitgPty.Id.OrgId.append(
            CBIGenericIdentification1(
                Id='0799996F',
                Issr='CBI'
            )
        )

        #PAYMENT
        sepa_payment.PmtInf = CBIPaymentInstructionInformation(
            PmtInfId=(val_MsgId + str(self.journal_id.id))[-30:],
            PmtMtd='TRA',
            PmtTpInf=CBIPaymentTypeInformation1(),
            ReqdExctnDt=fields.Date.to_string(self.date),
            Dbtr=CBIPartyIdentification4(),
            DbtrAcct=CBICashAccount1(),
            DbtrAgt=CBIBranchAndFinancialInstitutionIdentification2(),
            ChrgBr='SLEV',
            CdtTrfTxInf=[]
        )

        sepa_payment.PmtInf.Dbtr = CBIPartyIdentification4(
            Nm=self._sanitize_communication(company.sepa_initiating_party_name[:name_length]),
            PstlAdr=CBIPostalAddress6(
                Ctry=company.partner_id.country_id.code,
            ),
        )

        sepa_payment.PmtInf.DbtrAcct.Id = CBIAccountIdentification1(
            IBAN=self.journal_id.bank_account_id.sanitized_acc_number
        )

        sepa_payment.PmtInf.DbtrAgt = CBIBranchAndFinancialInstitutionIdentification2(
            FinInstnId=CBIFinancialInstitutionIdentification3(
                ClrSysMmbId=CBIClearingSystemMemberIdentification1(
                    MmbId='02008'
                )
            )
        )


        for payment in doc_payments:
            sepa_payment.PmtInf.CdtTrfTxInf.append(
                CBICreditTransferTransactionInformation(
                    PmtId=PaymentIdentification1(
                        InstrId=self._sanitize_communication(payment.name),
                        EndToEndId=((val_MsgId + str(self.journal_id.id))[-30:] + str(payment.id))[-30:]
                    ),
                    Amt=CBIAmountType1(
                        InstdAmt=ActiveOrHistoricCurrencyAndAmount(
                            float_repr(float_round(payment.amount, 2), 2),
                            Ccy=payment.currency_id and payment.currency_id.name or payment.journal_id.company_id.currency_id.name,
                        )
                    ),
                    Cdtr=CBIPartyIdentification3(
                        Nm=self._sanitize_communication((payment.partner_bank_account_id.acc_holder_name or payment.partner_id.name)[:70]),
                        PstlAdr=CBIPostalAddress6(
                            Ctry=payment.partner_id.country_id.code,
                            TwnNm=payment.partner_id.city
                        ),
                        CtryOfRes=payment.partner_id.country_id.code
                    ),
                    CdtrAcct=CBICashAccount2(
                        Id=CBIAccountIdentification1(
                            IBAN=self._sanitize_communication(payment.partner_bank_account_id.acc_number.replace(' ', ''))
                        )
                    ),
                    # RgltryRptg=CBIRegulatoryReporting1(
                    #     DbtCdtRptgInd='DEBT',
                    #     Dtls='INVOICE'
                    # ),
                    RmtInf=RemittanceInformation5(
                        Ustrd=[self._sanitize_communication(str(payment.communication))]
                    )
                )
            )




        attach_str = sepa_payment.toxml(
            encoding="UTF-8",
        )

        return attach_str



