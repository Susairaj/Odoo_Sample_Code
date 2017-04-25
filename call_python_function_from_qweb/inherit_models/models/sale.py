# -*- encoding: utf-8 -*-

from openerp import api, models, fields


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    list_price = fields.Float(string='List Price')

    @api.onchange('product_id')
    def product_id_change(self):
        res = super(SaleOrderLine, self).product_id_change()
        if self.product_id:
            self.list_price = self.product_id.original_list_price

        return res
         