import logging

from odoo import models, fields, api,_

class CheckTools(models.Model):
    _name = 'check.tools'

    #Date
    from_date = fields.Date()
    to_date = fields.Date()

    #Corrispettivi
    conti_corrispettivi_ids = fields.Many2many('account.account', 'conti_corrispettivi_rel')
    imposte_corrispettivi_ids = fields.Many2many('account.tax', 'imposte_corrispettivi_rel')

    #Fatture
    conti_fatture_ids = fields.Many2many('account.account', 'conti_fatture_rel')
    imposte_fatture_ids = fields.Many2many('account.tax', 'imposte_fatture_rel')

    #Conti Merce/Servizi
    conti_merce_servizi_ids = fields.Many2many('account.account', 'conti_merce_servizi_rel')

    #Check GENERALI
    sbilanciate = fields.Integer()
    sbilanciate_ids = fields.Many2many('account.move', 'sbilanciate_move_rel')
    conti_errati = fields.Integer()
    conti_errati_ids = fields.Many2many('account.move', 'conti_errati_move_rel')

    #Check IMPONIBILE
    imposte_imponibile_errate = fields.Integer()
    imposte_imponibile_errate_ids = fields.Many2many('account.move', 'imposte_imp_errate_move_rel')
    imposte_imponibile_mancanti = fields.Integer()
    imposte_imponibile_mancanti_ids = fields.Many2many('account.move', 'imposte_imp_mancanti_move_rel')
    imposte_imponibili_su_iva = fields.Integer()
    imposte_imponibili_su_iva_ids = fields.Many2many('account.move', 'imposte_imp_iva_move_rel')

    #Check IVA
    iva_mancante = fields.Integer()
    iva_mancante_ids = fields.Many2many('account.move', 'iva_mancante_move_rel')
    iva_errata = fields.Integer()
    iva_errata_ids = fields.Many2many('account.move', 'iva_errata_move_rel')
    senza_iva = fields.Integer()
    senza_iva_ids = fields.Many2many('account.move', 'senza_iva_move_rel')
    iva_su_merci_servizi = fields.Integer()
    iva_merci_servizi_ids = fields.Many2many('account.move', 'iva_merci_servizi_move_rel')
    iva_calcolata_errata = fields.Integer()
    iva_calcolata_errata_ids = fields.Many2many('account.move', 'iva_calcolata_errata_rel')

    #Check Analitica
    analitica_mancante = fields.Integer()
    analitica_mancante_ids = fields.Many2many('account.move', 'analitica_mancante_move_rel')

    #Check Conti Uguali Registrazione
    conti_uguali = fields.Integer()
    conti_uguali_ids = fields.Many2many('account.move', 'conti_uguali_move_rel')

    # Check Conti Uguali Registrazione
    crediti_sbagliati = fields.Integer()
    crediti_sbagliati_ids = fields.Many2many('account.move', 'crediti_sbagliati_rel')

    @api.multi
    def open_sbilanciate(self):
        context = self._context.copy()
        return {
            'name': 'SBILANCIATE',
            'view_mode': 'list,form',
            'view_type': 'list',
            'view_id': False,
            'res_model': 'account.move',
            'type': 'ir.actions.act_window',
            'target': 'current',
            'domain': [('id', 'in', self.sbilanciate_ids.ids)],
            'context': context
        }

    @api.multi
    def open_crediti_sbagliati(self):
        context = self._context.copy()
        return {
            'name': 'CREDITI SBAGLIATI',
            'view_mode': 'list,form',
            'view_type': 'list',
            'view_id': False,
            'res_model': 'account.move',
            'type': 'ir.actions.act_window',
            'target': 'current',
            'domain': [('id', 'in', self.crediti_sbagliati_ids.ids)],
            'context': context
        }

    @api.multi
    def open_conti_errati(self):
        context = self._context.copy()
        return {
            'name': 'CONTI ERRATI',
            'view_mode': 'list,form',
            'view_type': 'list',
            'view_id': False,
            'res_model': 'account.move',
            'type': 'ir.actions.act_window',
            'target': 'current',
            'domain': [('id', 'in', self.conti_errati_ids.ids)],
            'context': context
        }

    @api.multi
    def open_imponibile_errato(self):
        context = self._context.copy()
        return {
            'name': 'IMPONIBILE ERRATO',
            'view_mode': 'list,form',
            'view_type': 'list',
            'view_id': False,
            'res_model': 'account.move',
            'type': 'ir.actions.act_window',
            'target': 'current',
            'domain': [('id', 'in', self.imposte_imponibile_errate_ids.ids)],
            'context': context
        }

    @api.multi
    def open_imponibile_mancante(self):
        context = self._context.copy()
        return {
            'name': 'IMPONIBILE MANCANTE',
            'view_mode': 'list,form',
            'view_type': 'list',
            'view_id': False,
            'res_model': 'account.move',
            'type': 'ir.actions.act_window',
            'target': 'current',
            'domain': [('id', 'in', self.imposte_imponibile_mancanti_ids.ids)],
            'context': context
        }

    @api.multi
    def open_imponibile_su_iva(self):
        context = self._context.copy()
        return {
            'name': 'IMPONIBILE SU IVA',
            'view_mode': 'list,form',
            'view_type': 'list',
            'view_id': False,
            'res_model': 'account.move',
            'type': 'ir.actions.act_window',
            'target': 'current',
            'domain': [('id', 'in', self.imposte_imponibili_su_iva_ids.ids)],
            'context': context
        }

    @api.multi
    def open_iva_mancante(self):
        context = self._context.copy()
        return {
            'name': 'IVA MANCANTE',
            'view_mode': 'list,form',
            'view_type': 'list',
            'view_id': False,
            'res_model': 'account.move',
            'type': 'ir.actions.act_window',
            'target': 'current',
            'domain': [('id', 'in', self.iva_mancante_ids.ids)],
            'context': context
        }

    @api.multi
    def open_iva_errata(self):
        context = self._context.copy()
        return {
            'name': 'IVA ERRATA',
            'view_mode': 'list,form',
            'view_type': 'list',
            'view_id': False,
            'res_model': 'account.move',
            'type': 'ir.actions.act_window',
            'target': 'current',
            'domain': [('id', 'in', self.iva_errata_ids.ids)],
            'context': context
        }

    @api.multi
    def open_conti_uguali(self):
        context = self._context.copy()
        return {
            'name': 'CONTI UGUALI',
            'view_mode': 'list,form',
            'view_type': 'list',
            'view_id': False,
            'res_model': 'account.move',
            'type': 'ir.actions.act_window',
            'target': 'current',
            'domain': [('id', 'in', self.conti_uguali_ids.ids)],
            'context': context
        }

    @api.multi
    def open_iva_su_merci_servizi(self):
        context = self._context.copy()
        return {
            'name': 'IVA SU MERCI E SERVIZI',
            'view_mode': 'list,form',
            'view_type': 'list',
            'view_id': False,
            'res_model': 'account.move',
            'type': 'ir.actions.act_window',
            'target': 'current',
            'domain': [('id', 'in', self.iva_merci_servizi_ids.ids)],
            'context': context
        }

    @api.multi
    def open_senza_iva(self):
        context = self._context.copy()
        return {
            'name': 'MOVIMENTAZIONE SENZA IVA',
            'view_mode': 'list,form',
            'view_type': 'list',
            'view_id': False,
            'res_model': 'account.move',
            'type': 'ir.actions.act_window',
            'target': 'current',
            'domain': [('id', 'in', self.senza_iva_ids.ids)],
            'context': context
        }

    @api.multi
    def open_analitica(self):
        context = self._context.copy()
        return {
            'name': 'MANCA ANALITICA',
            'view_mode': 'list,form',
            'view_type': 'list',
            'view_id': False,
            'res_model': 'account.move',
            'type': 'ir.actions.act_window',
            'target': 'current',
            'domain': [('id', 'in', self.analitica_mancante_ids.ids)],
            'context': context
        }

    @api.multi
    def open_iva_calcolata_errata(self):
        context = self._context.copy()
        return {
            'name': 'IVA CALCOLATA ERRATA',
            'view_mode': 'list,form',
            'view_type': 'list',
            'view_id': False,
            'res_model': 'account.move',
            'type': 'ir.actions.act_window',
            'target': 'current',
            'domain': [('id', 'in', self.iva_calcolata_errata_ids.ids)],
            'context': context
        }

    def check(self):
        conti_fatture_ids = self.conti_fatture_ids.ids
        conti_corrispettivi_ids = self.conti_corrispettivi_ids.ids
        imposte_fatture_ids = self.imposte_fatture_ids.ids
        imposte_corrispettivi_ids = self.imposte_corrispettivi_ids.ids
        conti_merci_servizi_ids = self.conti_merce_servizi_ids.ids
        conti_iva_fatture_ids = []
        conti_iva_corrispettivi_ids = []

        for c in self.imposte_corrispettivi_ids:
            conti_iva_corrispettivi_ids.append(c.account_id.id)
        for c in self.imposte_fatture_ids:
            conti_iva_fatture_ids.append(c.account_id.id)

        move_ids = self.env['account.move'].search([('date', '>=', self.from_date), ('date', '<=', self.to_date)])

        ######1 - Sbilanciate###########
        self.env.cr.execute(" select distinct move_id as move from account_move_line "
                            " where date between '%s' and '%s'"
                            " group by move_id "
                            " having (sum(credit) - sum(debit)) >= 0.01" % (self.from_date, self.to_date))

        self.sbilanciate_ids = [(5,)]
        self.sbilanciate_ids = self.env.cr.fetchall()
        self.sbilanciate = len(self.sbilanciate_ids)

        ######2 - Conti Errati#########
        conti_errati = []
        for move in move_ids:
            trovato_corrispettivo = False
            trovato_fattura = False
            for line in move.line_ids:
                if line.account_id.id in conti_corrispettivi_ids:
                    trovato_corrispettivo = True
                if line.account_id.id in conti_fatture_ids:
                    trovato_fattura = True
            if trovato_corrispettivo and trovato_fattura:
                conti_errati.append(move.id)
            logging.info('2 - Verifica Conti')
        self.conti_errati = len(conti_errati)
        self.conti_errati_ids = [(5,)]
        self.conti_errati_ids = conti_errati

        #####3 - Imposte Imponibile su Conti Errati#####
        imposta_errata = []
        for move in move_ids:
            for line in move.line_ids:
                if line.account_id.id in conti_corrispettivi_ids:
                    # Linea Corrispettivo
                    for imposta_fattura in imposte_fatture_ids:
                        if imposta_fattura in line.tax_ids.ids:
                            if move.id not in imposta_errata:
                                imposta_errata.append(move.id)
                if line.account_id.id in conti_fatture_ids:
                    # Linea Fattura
                    for imposta_corrispettivo in imposte_corrispettivi_ids:
                        if imposta_corrispettivo in line.tax_ids.ids:
                            if move.id not in imposta_errata:
                                imposta_errata.append(move.id)
            logging.info('3 - Imposte Imponibili su conti Errati')
        self.imposte_imponibile_errate = len(imposta_errata)
        self.imposte_imponibile_errate_ids = [(5,)]
        self.imposte_imponibile_errate_ids = imposta_errata

        #####4 - Imposte Imponibile Mancanti#####
        imposte_mancanti = []
        for move in move_ids:
            for line in move.line_ids:
                if line.account_id.id in conti_merci_servizi_ids:
                    # Riga di Merce o Servizio
                    if not line.tax_ids or line.tax_ids == []:
                        if move.id not in imposte_mancanti:
                            imposte_mancanti.append(move.id)
            logging.info('4 - Imposte Imponibili Mancanti')
        self.imposte_imponibile_mancanti = len(imposte_mancanti)
        self.imposte_imponibile_mancanti_ids = [(5,)]
        self.imposte_imponibile_mancanti_ids = imposte_mancanti

        #####5 - IVA Mancante#####
        iva_mancante = []
        for move in move_ids:
            for line in move.line_ids:
                if line.account_id.id in conti_iva_corrispettivi_ids or line.account_id.id in conti_iva_fatture_ids:
                    if not line.tax_line_id:
                        if move.id not in iva_mancante:
                            iva_mancante.append(move.id)
            logging.info('5 - IVA Mancante')
        self.iva_mancante = len(iva_mancante)
        self.iva_mancante_ids = [(5,)]
        self.iva_mancante_ids = iva_mancante

        #####6 - IVA Errata#####
        iva_errata = []
        for move in move_ids:
            for line in move.line_ids:
                if line.account_id.id in conti_corrispettivi_ids:
                    # Conti Corrispettivi
                    if line.tax_line_id.id in imposte_fatture_ids:
                        if move.id not in iva_errata:
                            iva_errata.append(move.id)
                if line.account_id.id in conti_fatture_ids:
                    # Conti Fatture
                    if line.tax_line_id.id in imposte_corrispettivi_ids:
                        if move.id not in iva_errata:
                            iva_errata.append(move.id)
            logging.info('6 - IVA Errata')
        self.iva_errata = len(iva_errata)
        self.iva_errata_ids = [(5,)]
        self.iva_errata_ids = iva_errata

        #####7 - IVA Non presente move line#####
        iva_senza_move_line = []
        for move in move_ids:
            for line in move.line_ids:
                if line.account_id.id in conti_iva_fatture_ids or line.account_id.id in conti_iva_corrispettivi_ids:
                    if not line.tax_line_id:
                        if move.id not in iva_senza_move_line:
                            iva_senza_move_line.append(move.id)

            logging.info('7 - IVA Senza Move Line')
        self.senza_iva = len(iva_senza_move_line)
        self.senza_iva_ids = [(5,)]
        self.senza_iva_ids = iva_senza_move_line

        #####8 - Analitica Mancante#####
        analitica_mancante = []
        for move in move_ids:
            for line in move.line_ids:
                if line.account_id.id in conti_merci_servizi_ids:
                    # Conti Merce/Servizi
                    if not line.analytic_account_id:
                        if move.id not in analitica_mancante:
                            analitica_mancante.append(move.id)
            logging.info('8 - Analitica Mancante')
        self.analitica_mancante = len(analitica_mancante)
        self.analitica_mancante_ids = [(5,)]
        self.analitica_mancante_ids = analitica_mancante

        #####9 - Imposte Imponibili su IVA ####
        imposte_imponibili_su_iva = []
        for move in move_ids:
            for line in move.line_ids:
                if line.account_id.id in conti_iva_corrispettivi_ids or line.account_id.id in conti_iva_fatture_ids:
                    if line.tax_ids:
                        if move.id not in imposte_imponibili_su_iva:
                            imposte_imponibili_su_iva.append(move.id)
            logging.info('9 - Imposte Imponibili Su IVA')

        self.imposte_imponibili_su_iva = len(imposte_imponibili_su_iva)
        self.imposte_imponibili_su_iva_ids = [(5,)]
        self.imposte_imponibili_su_iva_ids = imposte_imponibili_su_iva

        #####10 - Iva su Merci e Servizi ####
        iva_su_merci_servizi = []
        for move in move_ids:
            for line in move.line_ids:
                if line.account_id.id in conti_merci_servizi_ids:
                    if line.tax_line_id:
                        if move.id not in iva_su_merci_servizi:
                            iva_su_merci_servizi.append(move.id)
            logging.info('10 - IVA Su Merci e Servizi')

        self.iva_su_merci_servizi = len(iva_su_merci_servizi)
        self.iva_merci_servizi_ids = [(5,)]
        self.iva_merci_servizi_ids = iva_su_merci_servizi

        #####11 - Iva Calcolata Errata ####
        iva_calcolata_errata = []
        for move in move_ids:
            imponibile = 0
            iva = 0
            imposta = 1
            for line in move.line_ids:
                if line.account_id.id in conti_merci_servizi_ids:
                    imponibile += line.credit
                    if imposta == 1 and line.tax_ids:
                        if line.tax_ids:
                            tax = line.tax_ids[0]
                            imposta = tax.amount
                if line.account_id.id in conti_iva_fatture_ids or line.account_id.id in conti_iva_corrispettivi_ids:
                    iva += line.credit

            iva_corretta = imponibile * (imposta / 100)
            differenza = abs(iva_corretta - iva)
            if differenza >= 0.04:
                if move.id not in iva_calcolata_errata:
                    iva_calcolata_errata.append(move.id)
            logging.info('11 - IVA Calolata Errata')

        self.iva_calcolata_errata = len(iva_calcolata_errata)
        self.iva_calcolata_errata_ids = [(5,)]
        self.iva_calcolata_errata_ids = iva_calcolata_errata

        #####12 - Conti Uguali ###########
        conti_uguali = []
        for move in move_ids:
            uguale = True
            last_conto = False
            if len(move.line_ids) == 2:
                for line in move.line_ids:
                    if not last_conto:
                        last_conto = line.account_id.id
                    else:
                        if last_conto != line.account_id.id:
                            uguale = False
                if uguale:
                    conti_uguali.append(move.id)

        self.conti_uguali = len(conti_uguali)
        self.conti_uguali_ids = [(5,)]
        self.conti_uguali_ids = conti_uguali

        #####13 - Crediti Sbagliati ###########
        crediti_sbagliati = []
        for move in move_ids:
            reg_crediti = False
            error = False
            for line in move.line_ids:
                if line.account_id.name == 'CREDITI V/CLIENTI' and line.debit > 0:
                    reg_crediti = True
                if line.debit > 0 and line.account_id.name != 'CREDITI V/CLIENTI':
                    error = True
                if line.account_id.name == 'CREDITI V/CLIENTI' and line.debit == 0 and line.credit == 0:
                    reg_crediti = True
                    error = True

            if reg_crediti and error:
                crediti_sbagliati.append(move.id)


        self.crediti_sbagliati = len(crediti_sbagliati)
        self.crediti_sbagliati_ids = [(5,)]
        self.crediti_sbagliati_ids = crediti_sbagliati

