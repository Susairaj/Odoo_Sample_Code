import json
import werkzeug
import itertools
import pytz
import babel.dates
from collections import OrderedDict

from odoo import http, fields, _
from odoo.addons.website.controllers.main import QueryURL
from odoo.addons.website.models.website import slug, unslug
from odoo.exceptions import UserError
from odoo.http import request
from odoo.tools import html2plaintext
from datetime import datetime

req_env = request.httprequest.environ

class RestApi(http.Controller):
    
    @http.route([
        '/api/<string:model>/<string:method>',
        '/api/<string:model>/<string:method>/<string:id>'
        ], type='json', auth="none", csrf=False)
    def odoo_rest_api(self, model=None, method=None, id=None, **kw):
        token = False
        domain = kw.get('domain', [])
        offset = kw.get('offset', 0)
        limit = kw.get('limit', 0)
        fields = kw.get('fields', [])
        vals = kw.get('vals', {})
        args = kw.get('args', [])
        result = {}
        user_id = False
        header = req_env['HTTP_AUTHORIZATION']
        if header:
            token = header[4:]
        else:
            result.update({'token':'Invalid Token'})
            return json.dumps(result)
        if token:
            user_token_id = request.env['res.user.token'].sudo().search([('token','=',token)], limit=1)
            if user_token_id:
                user_id = user_token_id.user_id
                user_token_id.write({'last_request':datetime.now(pytz.timezone(user_id.tz)).strftime("%Y-%m-%d %H:%M:%S") if user_id.tz else datetime.now(pytz.utc).strftime("%Y-%m-%d %H:%M:%S")})
                request.env['rest.api.access.history'].sudo().create({'user_id':user_id.id, 'origin':req_env['REMOTE_ADDR'], 'token':token, 'accessed_on':datetime.now(pytz.timezone(user_id.tz)).strftime("%Y-%m-%d %H:%M:%S") if user_id.tz else datetime.now(pytz.utc).strftime("%Y-%m-%d %H:%M:%S")})
            else:
                result.update({'token':'Invalid Token'})
                return json.dumps(result)
        else:
            result.update({'token':'Invalid Token'})
            return json.dumps(result)
        if model and method:
            if method == 'search' and id:
                domain += [('id','=',id)]
                result = request.env[model].sudo(user_id).search_read(domain, fields)
            elif method == 'search' and limit:
                result = request.env[model].sudo(user_id).search_read(domain, fields, offset=offset, limit=limit)
            elif method == 'search':
                result = request.env[model].sudo(user_id).search_read(domain, fields)
            elif method == 'create' and vals:
                record = request.env[model].sudo(user_id).create(vals)
                result.update({'id':record.id})
            elif method == 'write' and vals and id:
                domain += [('id','=',id)]
                record = request.env[model].sudo(user_id).search(domain)
                if record:
                    record = record.sudo(user_id).write(vals)
                    result.update({'status':record})
                else:
                    result.update({'error':"Record Not Found!"})
            elif method == 'unlink' and id:
                domain += [('id','=',id)]
                record = request.env[model].sudo(user_id).search(domain)
                if record:
                    record = record.sudo(user_id).unlink()
                    result.update({'status':record})
                else:
                    result.update({'error':"Record Not Found!"})
            elif method and args:
                custom_method = "request.env[model].sudo(user_id).%s(args[0])" % (method)
                print custom_method
                result = eval(custom_method)
            else:
                custom_method = "request.env[model].sudo(user_id).%s()" % (method)
                result = eval(custom_method)
        return json.dumps(result)