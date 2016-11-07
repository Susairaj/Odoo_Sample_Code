from odoo import api, fields, models, _
import odoo.addons.decimal_precision as dp

class AccountInvoice(models.Model):
    _inherit = "account.invoice"
    _description = 'Account Invoice Details'
    
    amount_untaxed = fields.Float(string='Untaxed Amount',digits=dp.get_precision('Product Price'),
        store=True, readonly=True, compute='_compute_amount', track_visibility='always')
    amount_total = fields.Float(string='Total',digits=dp.get_precision('Product Price'),
        store=True, readonly=True, compute='_compute_amount')
    residual = fields.Float(string='Amount Due',digits=dp.get_precision('Product Price'),
        compute='_compute_residual', store=True, help="Remaining amount due.")
    residual_signed = fields.Float(string='Amount Due in Invoice Currency', currency_field='currency_id', digits=dp.get_precision('Product Price'),
        compute='_compute_residual', store=True, help="Remaining amount due in the currency of the invoice.")
    amount_total_signed = fields.Float(string='Total in Invoice Currency', currency_field='currency_id', digits=dp.get_precision('Product Price'),
        store=True, readonly=True, compute='_compute_amount',
        help="Total amount in the currency of the invoice, negative for credit notes.")
    
    
class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"
    _description = "Account Invoice Line Details"
    
    price_subtotal = fields.Float(string='Amount',digits=dp.get_precision('Product Price'),
       store=True, readonly=True, compute='_compute_price')
    
class account_payment(models.Model):
    _inherit = "account.payment"
    _description = 'Account Payment Details'
    
    amount = fields.Float(string='Payment Amount', required=True, digits=dp.get_precision('Product Price'))
    
    