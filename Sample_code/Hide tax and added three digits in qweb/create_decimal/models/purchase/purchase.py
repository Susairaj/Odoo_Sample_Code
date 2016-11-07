from odoo import api, fields, models, _
import odoo.addons.decimal_precision as dp

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    _description = "Purchase Order"
    
    amount_untaxed = fields.Float(string='Untaxed Amount', store=True, readonly=True, compute='_amount_all', track_visibility='always', digits=dp.get_precision('Product Price'))
    amount_total = fields.Float(string='Total', store=True, readonly=True, compute='_amount_all', track_visibility='always', digits=dp.get_precision('Product Price'))
    
class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    _description = 'Purchase Order Line'
    
    price_subtotal = fields.Float(compute='_compute_amount', string='Subtotal', readonly=True, store=True, digits=dp.get_precision('Product Price'))
    