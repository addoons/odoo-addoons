# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import Warning as UserError


class WizardRegistroIva(models.TransientModel):
    _name = "wizard.registro.iva"
    _description = "Run VAT registry"

    date_range_id = fields.Many2one('date.range', string="Date range")
    from_date = fields.Date('From date', required=True)
    to_date = fields.Date('To date', required=True)
    layout_type = fields.Selection([
        ('customer', 'Customer Invoices'),
        ('supplier', 'Supplier Invoices'),
        ('corrispettivi', 'Sums due'), ],
        'Layout', required=True, default='customer')
    tax_registry_id = fields.Many2one('account.tax.registry', 'VAT registry')
    journal_ids = fields.Many2many(
        'account.journal',
        'registro_iva_journals_rel',
        'journal_id',
        'registro_id',
        string='Journals',
        help='Select journals you want retrieve documents from')
    message = fields.Char(string='Message', size=64, readonly=True)
    only_totals = fields.Boolean(
        string='Prints only totals')
    fiscal_page_base = fields.Integer('Last printed page', required=True)
    year_footer = fields.Char(
        string='Year for Footer',
        help="Value printed near number of page in the footer")

    @api.onchange('tax_registry_id')
    def on_change_tax_registry_id(self):
        self.journal_ids = self.tax_registry_id.journal_ids
        self.layout_type = self.tax_registry_id.layout_type

    @api.onchange('date_range_id')
    def on_change_date_range_id(self):
        if self.date_range_id:
            self.from_date = self.date_range_id.date_start
            self.to_date = self.date_range_id.date_end

    @api.onchange('from_date')
    def get_year_footer(self):
        if self.from_date:
            self.year_footer = self.from_date.year

    def _get_move_ids(self, wizard):
        moves = self.env['account.move'].search([
            ('date', '>=', self.from_date),
            ('date', '<=', self.to_date),
            ('journal_id', 'in', [j.id for j in self.journal_ids]),
            ('state', '=', 'posted'), ], order='date, name')

        if not moves:
            raise UserError(_('No documents found in the current selection'))

        return moves.ids


    def _get_cash_basis_move_ids(self, wizard):
        """
        Questa funzione ritorna la lista di tutti i movimenti di cassa
        in un particolare range di date
        """
        move_cash_move_ids = {}
        move_ids = []
        SQL_MOVES = """
        with moves_cash_moves as (
        -- prendo solo i movimenti di giroconto, che identificano la parte
        -- pagata delle fatture sotto regime di cassa.
        -- tramite la tabella account_partial_reconcile, risalgo al movimento
        -- della fattura relativa (che potrebbe essere in un periodo diverso
        -- dal pagamento.
        SELECT
            i.date,
            i.number as protocollo,
            ml2.move_id move_id,
            array_agg(distinct m.id) as cash_move_ids
        FROM  account_move m
        INNER JOIN account_move_line ml on (ml.move_id = m.id)
        INNER JOIN account_partial_reconcile r on
                (tax_cash_basis_rec_id = r.id),
        account_move_line ml2, account_invoice i
        WHERE
            (
                (ml2.id = r.debit_move_id and ml2.invoice_id is not null
                and i.id = ml2.invoice_id)
            OR
                (ml2.id = r.credit_move_id and ml2.invoice_id is not null
                and i.id = ml2.invoice_id)
        )
        AND ml.tax_exigible is True
        AND m.state = 'posted'
        AND ml.date >= %(from_date)s
        AND ml.date <= %(to_date)s
        AND ml.company_id = %(company_id)s
        AND ml2.journal_id in %(journals)s
        GROUP BY 1, 2, 3
        ),
        moves as (
        -- query che identifica solo i movimenti delle fatture, escludendo
        -- quelle a regime di cassa.
        SELECT m.date, m.name as protocollo, m.id as move_id,
            ARRAY[]::integer[] as cash_move_ids
        FROM account_move m
        INNER JOIN account_move_line ml on (ml.move_id = m.id)
        WHERE
        ml.tax_exigible is True
        AND ml.tax_line_id  is not null
        AND ml.invoice_id is not null
        AND m.state = 'posted'
        AND ml.date >= %(from_date)s
        AND ml.date <= %(to_date)s
        AND ml.company_id = %(company_id)s
        AND ml.journal_id in %(journals)s
        )
        -- Unisco tutti i movimenti delle fatture NON per cassa, con
        -- quelle che ho trovato partendo dai giroconti e ordino
        -- per data, protocollo
        SELECT *
        FROM
         (
          SELECT * FROM moves_cash_moves
            UNION
          SELECT * FROM moves
          ) as moves
        ORDER BY date, protocollo
        """
        params = {'from_date': wizard.from_date,
                  'to_date': wizard.to_date,
                  'journals': tuple([j.id for j in wizard.journal_ids]),
                  'company_id': self.env.user.company_id.id}

        self.env.cr.execute(SQL_MOVES, params)
        res = self.env.cr.fetchall()

        for date, protocollo, move_id, c_move_ids in res:
            move_ids.append(move_id)
            if c_move_ids:
                move_cash_move_ids[move_id] = c_move_ids

        return move_ids, move_cash_move_ids

    @api.multi
    def print_registro(self):
        self.ensure_one()
        wizard = self
        if not wizard.journal_ids:
            raise UserError(_('No journals found in the current selection.\n'
                              'Please load them before to retry!'))
        move_ids = []
        cash_move_ids = {}

        # controllare se la contabilità è in regime di cassa
        if self.env.user.company_id.tax_cash_basis_journal_id:
            move_ids, cash_move_ids = self._get_cash_basis_move_ids(wizard)

        move_ids = self._get_move_ids(wizard)

        if not move_ids:
            raise UserError(_('No documents found in the current selection'))

        datas_form = {}
        datas_form['from_date'] = wizard.from_date
        datas_form['to_date'] = wizard.to_date
        datas_form['journal_ids'] = [j.id for j in wizard.journal_ids]
        datas_form['fiscal_page_base'] = wizard.fiscal_page_base
        datas_form['registry_type'] = wizard.layout_type
        datas_form['cash_move_ids'] = cash_move_ids
        datas_form['move_ids'] = move_ids
        datas_form['year_footer'] = wizard.year_footer

        lang_code = self.env.user.company_id.partner_id.lang
        lang = self.env['res.lang']
        lang_id = lang._lang_get(lang_code)
        date_format = lang_id.date_format
        datas_form['date_format'] = date_format

        if wizard.tax_registry_id:
            datas_form['tax_registry_name'] = wizard.tax_registry_id.name
        else:
            datas_form['tax_registry_name'] = ''
        datas_form['only_totals'] = wizard.only_totals
        report_name = 'l10n_it_vat_registries.action_report_registro_iva'
        datas = {
            'ids': move_ids,
            'model': 'account.move',
            'form': datas_form
        }
        return self.env.ref(report_name).report_action(self, data=datas)
