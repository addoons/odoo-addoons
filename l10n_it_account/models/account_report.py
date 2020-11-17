from odoo import models, fields, api

# class AccountReport(models.AbstractModel):
#     _inherit = 'account.report'
#
#     @api.multi
#     def payment_document(self, options, params=None):
#         if not params:
#             params = {}
#
#         ctx = self.env.context.copy()
#         ctx.pop('id', '')
#
#         # Decode params
#         model = params.get('model', 'account.move.line')
#         res_id = params.get('id')
#         document = params.get('object', 'account.move')
#
#         # Redirection data
#         target = self._resolve_caret_option_document(model, res_id, document)
#         view_name = self._resolve_caret_option_view(target)
#         module = 'account'
#         if '.' in view_name:
#             module, view_name = view_name.split('.')
#
#
#         ctx.update({'default_invoice_ids': [(4, target.id, None)]})
#         # Redirect
#         view_id = self.env['ir.model.data'].get_object_reference(module, 'view_account_payment_invoice_form')[1]
#         return {
#             'type': 'ir.actions.act_window',
#             'view_type': 'form',
#             'view_mode': 'form',
#             'views': [(view_id, 'form')],
#             'res_model': 'account.payment',
#             'view_id': view_id,
#             'context': ctx,
#             'target': 'new'
#         }