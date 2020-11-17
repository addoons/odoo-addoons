# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)

from odoo import models, fields, api,_


class AccountMovetemplate(models.Model):
    _name = "account.move.template"

    account_journal_id = fields.Many2one('account.journal')
    move_line_ids = fields.One2many('account.move.template.line', 'account_template_id')
    name = fields.Char(required=True)


class AccountMoveTemplateLine(models.Model):
    _name = "account.move.template.line"

    account_id = fields.Many2one('account.account')
    account_template_id = fields.Many2one('account.move.template')
    line_description = fields.Char()
    is_debit = fields.Boolean()
    is_credit = fields.Boolean()

    @api.onchange('is_debit')
    def mutual_exclusion_is_debit(self):
        if self.is_debit:
            self.is_credit = False

    @api.onchange('is_credit')
    def mutual_exclusion_is_credit(self):
        if self.is_credit:
            self.is_debit = False

