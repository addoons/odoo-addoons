# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)

from odoo import models, fields, api,_


class FiscalDocumentType(models.Model):
    _name = 'fiscal.document.type'
    _description = 'Fiscal document type'

    code = fields.Char(string='Code', size=5)
    name = fields.Char(string='Name', size=150)
    out_invoice = fields.Boolean(string='Customer Invoice')
    in_invoice = fields.Boolean(string='Vendor Bill')
    out_refund = fields.Boolean(string='Customer Credit Note')
    in_refund = fields.Boolean(string='Vendor Credit Note')
    priority = fields.Integer(string='Priority', default='3')

    journal_ids = fields.Many2many(
        'account.journal',
        'account_journal_fiscal_doc_type_rel',
        'fiscal_document_type_id',
        'journal_id',
        'Journals'
    )

    _order = 'code, priority asc'

    @api.model
    def create(self, vals):
        res = super(FiscalDocumentType, self).create(vals)
        res.journal_ids.check_doc_type_relation()
        return res

    @api.multi
    def write(self, vals):
        res = super(FiscalDocumentType, self).write(vals)
        for doc in self:
            doc.journal_ids.check_doc_type_relation()
        return res
