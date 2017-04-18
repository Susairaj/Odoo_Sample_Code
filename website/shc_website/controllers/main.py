from openerp import http
from openerp.http import request
from openerp.tools.translate import _

class website_knowspace(http.Controller):
    _name = 'website.knowspace'
    
    @http.route('/shop/shoppage/', type='http', auth="public", website=True)
    def createreservation(self, **form_data):
        values = {}
        return request.render("scms_website.create_reservation", values)