# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)

{
    'name': 'Contabilità Italiana',
    'version': '12.0.1.0.1',
    'category': 'Hidden',
    "author": "servizi@addoons.it",
    'website': 'www.addoons.it',
    'license': 'AGPL-3',
    "depends": [
        'account',
        'l10n_it',
        'account_fiscal_year',
        'account_tax_balance',
        'web',
        'sale_management',
        'base_vat',
        'addoons_reports',
        'account_cancel',
        'report_xlsx'
    ],
    "data": [
        'data/rc_type.xml',
        'data/ir_config_parameter.xml',
        'data/piano_dei_conti.xml',
        'data/ateco_data.xml',
        'data/iva_annuale.xml',
        'data/alpha_region.xml',
        'data/dogana.xml',
        'views/account_rc_type.xml',
        'views/product_template.xml',
        'views/account_tax_kind.xml',
        'views/account_tax.xml',
        'views/res_bank.xml',
        'views/account_account.xml',
        'views/causali_pagamento.xml',
        'views/account_report.xml',
        'views/sale_order.xml',
        'views/codice_carica.xml',
        'views/account_invoice.xml',
        'views/fiscal_document_type.xml',
        'views/res_partner.xml',
        'views/res_company.xml',
        'views/withholding_tax.xml',
        'views/account_journal.xml',
        'views/account_fiscal_position.xml',
        'views/account_reports.xml',
        'views/check_tools.xml',
        'views/bollette_doganali.xml',
        'wizards/wizard_set_product_tax.xml',
        'reports/account_reports_view.xml',
        'reports/reports.xml',
        'reports/report_invoice_document.xml',
        'reports/report_chart_of_accounts.xml',
        'reports/report_bilancio.xml',
        'data/account.tax.kind.csv',
        'data/codici_carica_data.xml',
        'data/causali_pagamento_data.xml',
        'data/fiscal.document.type.csv',
        #'data/res_city_it_code.xml',
        'data/account_journal_data.xml',
        'security/security.xml',
        'wizards/compute_fc_view.xml',
        'wizards/add_period.xml',
        'wizards/remove_period.xml',
        'wizards/bilancio_di_verifica.xml',
        'views/assets_backend.xml',
        'wizards/compute_fiscal_document_type_view.xml',
        'wizards/export_file_view.xml',
        'wizards/wizard_nota_di_credito.xml',
        'wizards/wizard_cambio_conti.xml',
        'views/ateco_category.xml',
        'data/remove_menu.xml',
        'reports/account_reports_view.xml',
        'reports/report_invoice_document.xml',
        'reports/reports_vat_statement.xml',
        'reports/report_scheda_contabile.xml',
        'wizards/wizard_scheda_contabile.xml',
        'security/ir.model.access.csv',
        'views/print_report_assets.xml',
        'views/accounting_tools.xml',
        'views/account_move_template.xml',
        'views/account_move.xml',
        'views/account_vat_period_end_statement.xml',
        'views/comunicazione_liquidazione.xml',
        'wizards/split_big_communication_view.xml',
        'views/esterometro.xml',
        'wizards/export_liquidazione.xml',
        'data/change_menu.xml',
        'wizards/wizard_invoice_date.xml',
        'wizards/wizard_invoice_due_date.xml',
        'wizards/wizard_annulla_fattura.xml',
        'wizards/wizard_import_partner_xls.xml',
        'wizards/wizard_import_product_xls.xml',
        'wizards/wizard_import_chart_account_xls.xml',
        'wizards/wizard_import_saldi.xml',
        'wizards/wizard_account_partner.xml',
        'wizards/wizard_struttura_piano_conti.xml',
        'wizards/wizard_tipologia_conto.xml',
        'wizards/wizard_fill_invoice_sequence.xml',
        'wizards/wizard_report_corrispettivi.xml',
        'reports/certificazione_rda_report.xml',
        'views/res_config_settings.xml',
    ],
    'installable': True,
}
