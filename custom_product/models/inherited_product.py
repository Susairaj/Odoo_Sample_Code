from odoo import api, fields, models, tools, _
import odoo.addons.decimal_precision as dp
from docutils.nodes import field
from odoo.exceptions import UserError

class ProductTemplateInherit(models.Model):
    _inherit = "product.template"
    
    @api.onchange('standard_price','vat_id','income_percentage')
    def onchange_standard_price(self):
        if self.standard_price and self.vat_id and not self.income_percentage:
            self.list_price = (self.standard_price * (self.vat_id.amount/100)) + self.standard_price
        if self.standard_price and self.vat_id and self.income_percentage:
            self.list_price = (self.standard_price * ((self.vat_id.amount + self.income_percentage)/100)) + self.standard_price
        
    @api.onchange('mrp')
    def onchange_mrp(self):
        if self.list_price and self.mrp:
            if not self.mrp >= self.list_price:
                raise UserError(_('Sale price should not be greater then the MRP!.'))
        
    options = fields.Selection([('paint','Paint'),('others','Others')],string= 'Options')
    standard_price = fields.Float(
        'Actual Price', compute='_compute_standard_price',
        inverse='_set_standard_price', search='_search_standard_price',
        digits=dp.get_precision('Product Price'), groups="base.group_user",
        help="Cost of the product, in the default unit of measure of the product.")
    vat_id  = fields.Many2one('account.tax', 'VAT')
    income_percentage = fields.Float('Income(%)')
    mrp = fields.Float('MRP')
