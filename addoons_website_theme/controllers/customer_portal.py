from collections import OrderedDict
from operator import itemgetter

import odoo
from odoo import http, _
from odoo.addons.web.controllers.main import ensure_db
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
from odoo.tools import groupby as groupbyelem

from odoo.osv.expression import OR



class CustomerPortal(CustomerPortal):

    @http.route(['/my', '/my/home'], type='http', auth="user", website=True)
    def home(self, **kw):
        values = self._prepare_portal_layout_values()
        countries = request.env['res.country'].sudo().search([])
        states = request.env['res.country.state'].sudo().search([])
        partner = request.env.user.partner_id
        tasks = request.env['project.task'].sudo().search([('partner_id', '=', partner.id)])
        ore_sv_utilizzate = 0
        ore_fc_utilizzate = 0
        for task in tasks:
            for line in task.ore_lines:
                if line.type == 'developing':
                    ore_sv_utilizzate += line.requested_hours
                if line.type == 'training':
                    ore_fc_utilizzate += line.requested_hours

        values.update({
            'error': {},
            'error_message': [],
            'partner': partner,
            'countries': countries,
            'states': states,
            'has_check_vat': hasattr(request.env['res.partner'], 'check_vat'),
            'redirect': '/my/home',
            'page_name': 'my_details',
            'ore_sv_utilizzate': round(ore_sv_utilizzate, 2),
            'ore_fc_utilizzate': round(ore_fc_utilizzate, 2),
        })

        return request.render("addoons_website_theme.addoons_customer_portal", values)

