import odoo
from odoo import http, _
from odoo.addons.web.controllers.main import ensure_db
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
from odoo.tools import groupby as groupbyelem

from odoo.osv.expression import OR



class CustomerPortal(CustomerPortal):

    @http.route(['/my/analysis'], type='http', auth="user", website=True)
    def analysis_portal(self, **kw):
        return request.render("addoons_website_theme.addoons_analysis_portal", {})