# -*- encoding: utf-8 -*-

from openerp import api, models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    original_list_price = fields.Float(string='List Price')
