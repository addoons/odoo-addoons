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

        if request.env.user.partner_id.parent_id:
            partner = request.env.user.partner_id.parent_id
        else:
            partner = request.env.user.partner_id

        pacchetti_attivi = request.env['pacchetti.ore'].sudo().search([('partner_id', '=', partner.id), ('ore_residue', '>', 0)])

        ore_sv_utilizzate = 0
        ore_fc_utilizzate = 0

        stringa_pacchetti = ""
        for pacchetto in pacchetti_attivi:
            if pacchetto.order_id:
                stringa_pacchetti = stringa_pacchetti + pacchetto.order_id.name + " - "
            else:
                stringa_pacchetti = stringa_pacchetti + pacchetto.name + " - "
            if pacchetto.type == 'developing':
                ore_sv_utilizzate += pacchetto.hours - pacchetto.ore_residue
            if pacchetto.type == 'training':
                ore_fc_utilizzate += pacchetto.hours - pacchetto.ore_residue
        stringa_pacchetti = stringa_pacchetti[:-2]
        values.update({
            'error': {},
            'error_message': [],
            'partner': request.env.user.partner_id,
            'countries': countries,
            'states': states,
            'has_check_vat': hasattr(request.env['res.partner'], 'check_vat'),
            'redirect': '/my/home',
            'page_name': 'my_details',
            'ore_sv_utilizzate': round(ore_sv_utilizzate,2),
            'ore_fc_utilizzate': round(ore_fc_utilizzate,2),
            'pacchetti_attivi': stringa_pacchetti
        })

        return request.render("addoons_website_theme.addoons_customer_portal", values)

    @http.route(['/my/pacchetti-ore', '/my/pacchetti-ore/page/<int:page>'], type='http', auth="user", website=True)
    def pacchetti_ore_portal(self, filterby='all', search_in='content', search=None, page=1, **kw):
        pacchetti_ore = request.env['pacchetti.ore']
        # FILTRI: _filters filtra per campo, _inputs per ricerca testuale in un contesto
        searchbar_filters = {'all': {'label': 'Tutti', 'domain': []},
                             'attivi': {'label': 'Attivi', 'domain': [('ore_residue', '>', 0)]}}
        searchbar_inputs = {
            'content': {'input': 'content', 'label': 'Cerca <span class="nolabel"> (nel contenuto)</span>'},
            'all': {'input': 'all', 'label': 'Cerca ovunque'},
        }
        if request.env.user.partner_id.parent_id:
            cliente = request.env.user.partner_id.parent_id
        else:
            cliente = request.env.user.partner_id

        # costruisce il dominio a seconda del filtro selezionato
        domain = [('partner_id.id', '=', cliente.id)]
        if filterby != 'all':
            domain += searchbar_filters[filterby]['domain']

        if search and search_in:
            search_domain = []
            if search_in in ('content', 'all'):
                search_domain = OR([search_domain, ['|', ('name', 'ilike', search), ('description', 'ilike', search)]])
            domain += search_domain

        # paginazione con _items_per_page elementi per pagina
        pacchetti_ore_list = pacchetti_ore.sudo().search_count(domain)
        pager = portal_pager(
            url="/my/pacchetti-ore/",
            url_args={'filterby': filterby, 'search_in': search_in, 'search': search},
            total=pacchetti_ore_list,
            page=page,
            step=self._items_per_page
        )
        pacchetti_ore_list = pacchetti_ore.sudo().search(domain, limit=self._items_per_page,
                                                         offset=(page - 1) * self._items_per_page)
        return request.render("addoons_website_theme.addoons_pacchetti_ore_portal", {'pacchetti_ore': pacchetti_ore_list,
                                                                                     'searchbar_filters': OrderedDict(sorted(searchbar_filters.items())),
                                                                                     'filterby': filterby,
                                                                                     'searchbar_inputs': searchbar_inputs,
                                                                                     'search_in': search_in,
                                                                                     'default_url': '/my/pacchetti-ore',
                                                                                     'page_name': 'pacchetti',
                                                                                     'pager': pager,})

    @http.route(['/my/pacchetto-ore/<int:pacchetto_id>'], type='http', auth="public", website=True)
    def portal_my_pacchetti_ore(self, pacchetto_id, access_token=None, **kw):

        pacchetto = request.env['pacchetti.ore'].sudo().search([('id', '=', pacchetto_id)])

        return request.render("addoons_website_theme.portal_my_pacchetto", {'pacchetto': pacchetto,
                                                                            'page_name': 'pacchetti'})
