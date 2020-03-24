import datetime
from collections import OrderedDict
from operator import itemgetter

from odoo import http, _
from odoo.exceptions import AccessError, MissingError

from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.tools import groupby as groupbyelem, base64





class CustomerPortal(CustomerPortal):

    @http.route(['/my/tickets/create_ticket'], type='http', auth="user", website=True)
    def crea_ticket(self, redirect=None, **post):

        ticket = request.env['helpdesk.ticket'].sudo().create({
            'name': post['name'],
            'description': post['description'],
            'partner_id': request.env.user.partner_id.id,

        })

        for data in request.httprequest.files.getlist('attachments'):

            file = base64.b64encode(data.read())
            if (data.filename and data.filename != ''):
                request.env['ir.attachment'].sudo().create({
                    'name': data.filename,
                    'type': 'binary',
                    'datas': file,
                    'datas_fname': data.filename,
                    'store_fname': data.filename,
                    'res_model': 'helpdesk.ticket',
                    'res_id': ticket.id,
                })
        # ticket.sudo().write({'partner_id': request.env.user.partner_id.id})
        return request.redirect('/my/tickets')

    @http.route(['/my/tickets/edit_ticket'], type='http', auth="user", website=True)
    def edit_ticket(self, redirect=None, **post):

        ticket = request.env['helpdesk.ticket'].sudo().browse(int(post['id_ticket']))
        if ticket:
            ticket.sudo().write({
                'name': post['name'],
                'description': post['description'],
            })

            for data in request.httprequest.files.getlist('attachments'):

                file = base64.b64encode(data.read())
                if(data.filename and data.filename != ''):
                    request.env['ir.attachment'].sudo().create({
                        'name': data.filename,
                        'type': 'binary',
                        'datas': file,
                        'datas_fname': data.filename,
                        'store_fname': data.filename,
                        'res_model': 'helpdesk.ticket',
                        'res_id': ticket.id,
                    })

        return request.redirect('/my/ticket/' + str(ticket.id))

    @http.route([
        "/helpdesk/ticket/<int:ticket_id>",
        "/helpdesk/ticket/<int:ticket_id>/<token>",
        '/my/ticket/<int:ticket_id>'
    ], type='http', auth="public", website=True)
    def tickets_followup(self, ticket_id=None, access_token=None, **kw):
        try:
            ticket_sudo = self._document_check_access('helpdesk.ticket', ticket_id, access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        values = self._ticket_get_page_view_values(ticket_sudo, access_token, **kw)

        attachments = request.env['ir.attachment'].sudo().search([('res_model', '=', 'helpdesk.ticket'), ('res_id', '=', ticket_id)])
        values.update({'attachment_ids': attachments})
        return request.render("helpdesk.tickets_followup", values)
