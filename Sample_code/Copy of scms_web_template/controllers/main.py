# -*- coding: utf-8 -*-
import time
import json
import openerp

from openerp.addons.web import http
from openerp.addons.web.http import request
from openerp.tools.translate import _
from datetime import timedelta, datetime


class WebsiteScms(http.Controller):
    _name = 'website.scms'
    
    @http.route(['/scms'], type='http', auth="public", website=True)
    def website_scms(self, **kwargs):
        return request.render("scms_web_template.index", {})
    
    @http.route('/scms/about', type='http', auth="public", website=True)
    def freshers_apply(self, **form_data):
#        cr, uid, context, registry = request.cr, request.uid, request.context, request.registry
        values = {}
        return request.render("scms_web_template.about_us", values)
    
    @http.route('/scms/news', type='http', auth="public", website=True)
    def scms_news(self, **form_data):
#        cr, uid, context, registry = request.cr, request.uid, request.context, request.registry
        values = {}
        return request.render("scms_web_template.news", values)
