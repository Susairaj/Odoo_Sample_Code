from odoo import api, fields, models, _
import odoo.addons.decimal_precision as dp

class SaleOrder(models.Model):
    _inherit = "sale.order"
    _description = "Sales Order"
    
    amount_untaxed = fields.Float(string='Untaxed Amount', store=True, readonly=True, compute='_amount_all', track_visibility='always', digits=dp.get_precision('Product Price'))
    amount_total = fields.Float(string='Total', store=True, readonly=True, compute='_amount_all', track_visibility='always', digits=dp.get_precision('Product Price'))
    
    
class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    _description = 'Sales Order Line'
    
    price_subtotal = fields.Float(compute='_compute_amount', string='Subtotal', readonly=True, store=True, digits=dp.get_precision('Product Price'))
    