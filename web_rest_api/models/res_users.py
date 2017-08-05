# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import pytz
import datetime
import logging

from collections import defaultdict
from itertools import chain, repeat
from lxml import etree
from lxml.builder import E

from odoo import api, fields, models, tools, SUPERUSER_ID, _
from odoo.exceptions import AccessDenied, AccessError, UserError, ValidationError
from odoo.osv import expression
from odoo.service.db import check_super
from odoo.tools import partition
from datetime import datetime, timedelta

class UserToken(models.Model):
    _name = "res.user.token"
    _rec_name = "token"
    
    user_id = fields.Many2one('res.users', string='User', required=True)
    token = fields.Text(string='Token', required=True)
    last_request = fields.Datetime(string='Last Request On')
    
    _sql_constraints = [
        ('token_key', 'UNIQUE (token)',  'Token Already Exists!')
    ]
    
    @api.model
    def expire_token(self):
        date = datetime.now()-timedelta(minutes=10)
        token_ids = self.search([('last_request','<=',date.strftime("%Y-%m-%d %H:%M:%S"))])
        if token_ids:
            token_ids.unlink()
