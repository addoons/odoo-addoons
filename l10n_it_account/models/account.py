# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from odoo.addons import decimal_precision as dp
from odoo.tools import float_compare


class AccountFullReconcile(models.Model):
    _inherit = "account.full.reconcile"

    def _get_wt_moves(self):
        moves = self.mapped('reconciled_line_ids.move_id')
        wt_moves = self.env['withholding.tax.move'].search([
            ('wt_account_move_id', 'in', moves.ids)])
        return wt_moves

    @api.model
    def create(self, vals):
        res = super(AccountFullReconcile, self).create(vals)
        wt_moves = res._get_wt_moves()
        for wt_move in wt_moves:
            if wt_move.full_reconcile_id:
                wt_move.action_paid()
        return res

    @api.multi
    def unlink(self):
        for rec in self:
            wt_moves = rec._get_wt_moves()
            super(AccountFullReconcile, rec).unlink()
            for wt_move in wt_moves:
                if not wt_move.full_reconcile_id:
                    wt_move.action_set_to_draft()
        return True


class AccountPartialReconcile(models.Model):
    _inherit = "account.partial.reconcile"

    @api.model
    def create(self, vals):
        # In case of WT The amount of reconcile mustn't exceed the tot net
        # amount. The amount residual will be full reconciled with amount net
        # and amount wt created with payment
        invoice = False
        ml_ids = []
        if vals.get('debit_move_id'):
            ml_ids.append(vals.get('debit_move_id'))
        if vals.get('credit_move_id'):
            ml_ids.append(vals.get('credit_move_id'))
        move_lines = self.env['account.move.line'].browse(ml_ids)
        for ml in move_lines:
            domain = [('move_id', '=', ml.move_id.id)]
            invoice = self.env['account.invoice'].search(domain)
            if invoice:
                break
        # Limit value of reconciliation
        if invoice and invoice.withholding_tax and invoice.amount_net_pay:
            # We must consider amount in foreign currency, if present
            # Note that this is always executed, for every reconciliation.
            # Thus, we must not change amount when not in withholding tax case
            amount = vals.get('amount_currency') or vals.get('amount')
            digits_rounding_precision = invoice.company_id.currency_id.rounding
            if float_compare(
                amount,
                invoice.amount_net_pay,
                precision_rounding=digits_rounding_precision
            ) == 1:
                vals.update({'amount': invoice.amount_net_pay})

        # Create reconciliation
        reconcile = super(AccountPartialReconcile, self).create(vals)
        # Avoid re-generate wt moves if the move line is an wt move.
        # It's possible if the user unreconciles a wt move under invoice
        ld = self.env['account.move.line'].browse(vals.get('debit_move_id'))
        lc = self.env['account.move.line'].browse(vals.get('credit_move_id'))

        if lc.withholding_tax_generated_by_move_id \
                or ld.withholding_tax_generated_by_move_id:
            is_wt_move = True
        else:
            is_wt_move = False

        # Wt moves creation
        if invoice.withholding_tax_line_ids \
                and not self._context.get('no_generate_wt_move')\
                and not is_wt_move:
            reconcile.generate_wt_moves()

        return reconcile

    def _prepare_wt_move(self, vals):
        """
        Hook to change values before wt move creation
        """
        return vals

    @api.model
    def generate_wt_moves(self):
        wt_statement_obj = self.env['withholding.tax.statement']
        # Reconcile lines
        line_payment_ids = []
        line_payment_ids.append(self.debit_move_id.id)
        line_payment_ids.append(self.credit_move_id.id)
        domain = [('id', 'in', line_payment_ids)]
        rec_lines = self.env['account.move.line'].search(domain)

        # Search statements of competence
        wt_statements = False
        rec_line_statement = False
        for rec_line in rec_lines:
            domain = [('move_id', '=', rec_line.move_id.id)]
            wt_statements = wt_statement_obj.search(domain)
            if wt_statements:
                rec_line_statement = rec_line
                break
        # Search payment move
        rec_line_payment = False
        for rec_line in rec_lines:
            if rec_line.id != rec_line_statement.id:
                rec_line_payment = rec_line
        # Generate wt moves
        wt_moves = []
        for wt_st in wt_statements:
            amount_wt = wt_st.get_wt_competence(self.amount)
            # Date maturity
            p_date_maturity = False
            payment_lines = wt_st.withholding_tax_id.payment_term.compute(
                amount_wt,
                rec_line_payment.date or False)
            if payment_lines and payment_lines[0]:
                p_date_maturity = payment_lines[0][0][0]
            wt_move_vals = {
                'statement_id': wt_st.id,
                'date': rec_line_payment.date,
                'partner_id': rec_line_statement.partner_id.id,
                'reconcile_partial_id': self.id,
                'payment_line_id': rec_line_payment.id,
                'credit_debit_line_id': rec_line_statement.id,
                'withholding_tax_id': wt_st.withholding_tax_id.id,
                'account_move_id': rec_line_payment.move_id.id or False,
                'date_maturity':
                    p_date_maturity or rec_line_payment.date_maturity,
                'amount': amount_wt
            }
            wt_move_vals = self._prepare_wt_move(wt_move_vals)
            wt_move = self.env['withholding.tax.move'].create(wt_move_vals)
            wt_moves.append(wt_move)
            # Generate account move
            wt_move.generate_account_move()
        return wt_moves

    @api.multi
    def unlink(self):
        statements = []
        for rec in self:
            # To avoid delete if the wt move are paid
            domain = [('reconcile_partial_id', '=', rec.id),
                      ('state', '!=', 'due')]
            wt_moves = self.env['withholding.tax.move'].search(domain)
            if wt_moves:
                raise ValidationError(
                    _('Warning! Only Withholding Tax moves in Due status \
                        can be deleted'))
            # Statement to recompute
            domain = [('reconcile_partial_id', '=', rec.id)]
            wt_moves = self.env['withholding.tax.move'].search(domain)
            for wt_move in wt_moves:
                if wt_move.statement_id not in statements:
                    statements.append(wt_move.statement_id)

        res = super(AccountPartialReconcile, self).unlink()
        # Recompute statement values
        for st in statements:
            st._compute_total()
        return res





class AccountAbstractPayment(models.AbstractModel):
    _inherit = "account.abstract.payment"

    @api.model
    def default_get(self, fields):
        """
        Compute amount to pay proportionally to amount total - wt
        """
        rec = super(AccountAbstractPayment, self).default_get(fields)
        invoice_defaults = self.resolve_2many_commands('invoice_ids',
                                                       rec.get('invoice_ids'))
        if invoice_defaults and len(invoice_defaults) == 1:
            invoice = invoice_defaults[0]
            if 'withholding_tax_amount' in invoice \
                    and invoice['withholding_tax_amount']:
                coeff_net = invoice['residual'] / invoice['amount_total']
                rec['amount'] = invoice['amount_net_pay_residual'] * coeff_net
        return rec

    @api.multi
    def _compute_payment_amount(self, invoices=None, currency=None):
        if not invoices:
            invoices = self.invoice_ids
        original_values = {}

        for invoice in original_values:
            invoice.residual_signed = original_values[invoice]

        for invoice in invoices:
            if invoice.withholding_tax:
                original_values[invoice] = invoice.residual_signed
                invoice.residual_signed = invoice.amount_net_pay_residual
        res = super(AccountAbstractPayment, self)._compute_payment_amount(
            invoices, currency)

        return res



class AccountReconciliation(models.AbstractModel):
    _inherit = 'account.reconciliation.widget'

    @api.multi
    def _prepare_move_lines(
        self, move_lines, target_currency=False, target_date=False,
        recs_count=0
    ):
        """
        Net amount for invoices with withholding tax
        """
        res = super(
            AccountReconciliation, self
        )._prepare_move_lines(
            move_lines, target_currency, target_date, recs_count)
        for dline in res:
            if 'id' in dline and dline['id']:
                line = self.env['account.move.line'].browse(dline['id'])
                if line.withholding_tax_amount:
                    dline['debit'] = (
                        line.invoice_id.amount_net_pay_residual if line.debit
                        else 0
                    )
                    dline['credit'] = (
                        line.invoice_id.amount_net_pay_residual
                        if line.credit else 0
                    )
                    dline['name'] += (
                        _(' (Residual Net to pay: %s)')
                        % (dline['debit'] or dline['credit'])
                    )
        return res
