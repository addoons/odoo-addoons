# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)

from odoo import models, api, fields
from odoo.exceptions import Warning as UserError
from odoo.tools.translate import _


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    corrispettivi = fields.Boolean(string='Receipts')

    @api.model
    def get_corr_journal(self, company_id=None):
        if not company_id:
            company_id = self.env.user.company_id
        corr_journal_id = self.search(
            [('type', '=', 'sale'),
             ('corrispettivi', '=', True),
             ('company_id', '=', company_id.id)], limit=1)

        if not corr_journal_id:
            raise UserError(_('No journal found for receipts'))

        return corr_journal_id

    @api.multi
    def check_doc_type_relation(self):
        doc_model = self.env['fiscal.document.type']
        for journal in self:
            docs = doc_model.search(
                [('journal_ids', 'in', [journal.id])])
            if len(docs) > 1:
                raise UserError(
                    _("Journal %s can be linked to only 1 fiscal document "
                      "type (found in %s)")
                    % (journal.name, ', '.join([d.code for d in docs])))
