from odoo import api, models, _

class ProductTemplate(models.Model):
    _inherit = "product.template"
    _description = "Product Template"
    
    @api.model
    def default_get(self, fields_name):
        data = super(ProductTemplate, self).default_get(fields_name)
        data['taxes_id'] = []
        data['supplier_taxes_id'] = []
        return data
