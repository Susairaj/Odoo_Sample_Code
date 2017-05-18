from odoo import api, fields, models, _
import base64
import os

class ShowCharts(models.Model):
    _name = "show.charts"
    
    image1 = fields.Char('Image 1')
    image2 = fields.Char('Image 2')
    image3 = fields.Char('Image 3')
    image4 = fields.Char('Image 4')
    categ_id = fields.Many2one('product.category', 'Category')
    
    @api.model
    def default_get(self, fields):
        res = super(ShowCharts, self).default_get(fields)
        for file in os.listdir("D:/Development/IFS-SRC/Odoo17032017/addons/show_charts/src/img"):
                if file.endswith(".png"):
                    with open(("D:/Development/IFS-SRC/Odoo17032017/addons/show_charts/src/img/%s")%(file), "rb") as image_file:
                        encoded_string = base64.b64encode(image_file.read())
                        res['image1'] = encoded_string
                        res['image2'] = encoded_string
                        res['image3'] = encoded_string
                        res['image4'] = encoded_string
        return res
    