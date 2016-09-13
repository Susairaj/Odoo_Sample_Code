import urllib
from openerp import fields, models, api
import base64
import os


class ImageUrl(models.Model):
    _name = 'image.url'
    
    @api.multi
    def load_image(self):
        image_list = []; image_add_list = []
        for tem_id in self.env['product.template'].search([]):
            thumbnail_image = True
            for file in os.listdir("/opt/cc_product_images"):
                if file.endswith(".jpg"):
                    if file[:file.rfind('_')] == tem_id.default_code:
                        if thumbnail_image == True:
                            with open(("/opt/cc_product_images/%s")%(file), "rb") as image_file:
                                encoded_string = base64.b64encode(image_file.read())
                                print encoded_string
                                tem_id.write({'image_medium':encoded_string})
                                thumbnail_image = False
                        elif thumbnail_image == False:
                            with open(("/opt/cc_product_images/%s")%(file), "rb") as image_file:
                                encoded_string = base64.b64encode(image_file.read())
                                if not tem_id.photo_ids:
                                    image_list.append((0, 0, {'name':tem_id.default_code,'product_template_id':tem_id.id, 'product_image': encoded_string}))
                                else:
                                    image_add_list.append((0, 0, {'name':tem_id.default_code,'product_template_id':tem_id.id, 'product_image': encoded_string}))    
        if image_list:
            tem_id.photo_ids = image_list
#         elif image_add_list:
#             tem_id.write({'photo_ids': image_add_list})
    
#To download the image
    @api.multi
    def save_image(self):
        count = 0;
#         for im in self:
        for im in self.search([]):
            count += 1
            name = im.name +'_'+str(count)
            urllib.urlretrieve(("%s")%(im.url),
                       ("/opt/cc_product_images/%s.jpg")%(name))
    
    @api.multi
    def get_file(self):
        result = []
        with open(("%s")%(self.url), "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            print encoded_string
            self.write({'image': encoded_string})
            self.file = encoded_string
            
            
    name = fields.Char('Sku', required=True)
    url = fields.Char('Image Url')
    file =  fields.Binary(compute='get_file', string="Download File")
    image = fields.Binary('Image')