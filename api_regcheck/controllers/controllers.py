from odoo import http, _, fields
from odoo.http import request

class RegCheck(http.Controller):
     
     @http.route('/search', type='http', auth='public', website=True)
     def vehicle_search_index(self, **kw):
          return request.render('api_regcheck.vehicle_search')