import babel.messages.pofile
import base64
import csv
import datetime
import functools
import glob
import hashlib
import imghdr
import itertools
import jinja2
import json
import logging
import operator
import os
import re
import sys
import time
import werkzeug.utils
import werkzeug.wrappers
import zlib
from xml.etree import ElementTree
from cStringIO import StringIO
import jwt

import odoo
import odoo.modules.registry
from odoo.api import call_kw, Environment
from odoo.modules import get_resource_path
from odoo.tools import topological_sort
from odoo.tools.translate import _
from odoo.tools.misc import str2bool, xlwt
from odoo import http
from odoo.http import content_disposition, dispatch_rpc, request, \
                      serialize_exception as _serialize_exception
from odoo.exceptions import AccessError
from odoo.models import check_method_name
from datetime import datetime
import pytz

databases = http.db_list()
db = False
if databases:
    db = databases[0]

req_env = request.httprequest.environ

class UserController(http.Controller):
    
    @http.route('/api/user/get_token', type='json', auth="none", methods=['POST'], csrf=False)
    def get_token(self, debug=False, **kw):
        result = {}
        username = kw.get('username', False)
        password = kw.get('password', False)
        uid = request.session.authenticate(db, username, password)
        tz = request.env['res.users'].search([('id','=',uid)]).tz
        if uid:
            token = jwt.encode({'uid': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}, 'secret', algorithm='HS256', headers={'uid': uid})
            if token:
                result.update({'token': token})
                request.env['res.user.token'].sudo().create({'user_id':uid, 'token':token, 'last_request':datetime.now(pytz.timezone(tz)).strftime("%Y-%m-%d %H:%M:%S") if tz else datetime.now(pytz.utc).strftime("%Y-%m-%d %H:%M:%S")})
                request.env['rest.api.access.history'].sudo().create({'user_id':uid, 'origin':req_env['REMOTE_ADDR'], 'token':token, 'accessed_on':datetime.now(pytz.timezone(tz)).strftime("%Y-%m-%d %H:%M:%S") if tz else datetime.now(pytz.utc).strftime("%Y-%m-%d %H:%M:%S")})
            else:
                result.update({'token': 'Invalid Token'})
        return json.dumps(result)
    
    @http.route('/api/user/delete_token', type='json', auth="none", methods=['POST'], csrf=False)
    def delete_token(self, debug=False, **kw):
        result = {}
        token = False
        header = req_env['HTTP_AUTHORIZATION']
        if header:
            token = header[4:]
        else:
            result.update({'token':'Invalid Token'})
            return json.dumps(result)
        user_id = request.env['res.user.token'].sudo().search([('token','=',token)], limit=1).user_id
        if token:
            record = request.env['res.user.token'].sudo().search([('token', '=', token)], limit=1)
            if record:
                request.env['rest.api.access.history'].sudo().create({'user_id':user_id.id, 'origin':req_env['REMOTE_ADDR'], 'token':token, 'accessed_on':datetime.now(pytz.timezone(user_id.tz)).strftime("%Y-%m-%d %H:%M:%S") if user_id.tz else datetime.now(pytz.utc).strftime("%Y-%m-%d %H:%M:%S")})
                record = record.sudo().unlink()
                result.update({'id':record})
            else:
                result.update({'error':"Record Not Found!"})
        else:
            result.update({'error':"Token Not Found!"})
        return json.dumps(result)

