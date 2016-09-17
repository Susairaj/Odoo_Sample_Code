'''
Created on Sep 3, 2016

@author: bosco
'''
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
            for file in os.listdir("/home/ranjith/Desktop/cricket_crush_images"):
                if file.endswith(".jpg"):
                    if file[:file.rfind('_')] == tem_id.default_code:
                        if thumbnail_image == True:
                            with open(("/home/ranjith/Desktop/cricket_crush_images/%s")%(file), "rb") as image_file:
                                encoded_string = base64.b64encode(image_file.read())
                                print encoded_string
                                tem_id.write({'image_medium':encoded_string})
                                thumbnail_image = False
#                         elif thumbnail_image == False:
#                             with open(("/home/ranjith/Desktop/cricket_crush_images/%s")%(file), "rb") as image_file:
#                                 encoded_string = base64.b64encode(image_file.read())
#                                 if not tem_id.photo_ids:
#                                     image_list.append((0, 0, {'name':tem_id.default_code,'product_template_id':tem_id.id, 'product_image': encoded_string}))
#                                 else:
#                                     image_add_list.append((0, 0, {'name':tem_id.default_code,'product_template_id':tem_id.id, 'product_image': encoded_string}))    
        if image_list:
            tem_id.photo_ids = image_list
        elif image_add_list:
            tem_id.write({'photo_ids': image_add_list})
    
#To download the image
    @api.multi
    def save_image(self):
        count = 0;
#         for im in self:
        for im in self.search([]):
            count += 1
            name = im.name +'_'+str(count)
            urllib.urlretrieve(("%s")%(im.url),
                       ("/home/ranjith/Desktop/cricket_crush_images/%s.jpg")%(name))
            
    name = fields.Char('Sku', required=True)
    url = fields.Char('Image Url')
    
# class Photos(models.Model):
#     _name = 'photo.photo'
#     
# #     @api.multi
# #     def load_image(self):
# #         count = 0
# #         for tem_id in self.env['product.template'].search([]):
# #             with open("D:/image path/CB-005_253.jpg", "rb") as image_file:
# #                 encoded_string = base64.b64encode(image_file.read())
# #                 print encoded_string
# #                 tem_id.write({'name': 'test', 'image_medium':encoded_string})
# # #         for im in self.search([]):
# # #             count += 1
# # #             name = im.name +'_'+str(count)
# # #             urllib.urlretrieve(("%s")%(im.url), 
# # #                        ("D:/image path/%s.jpg")%(name))
# #             
#     product_template_id = fields.One2many('product.template', ondelete="cascade")
#     upload_template_ids = fields.Many2many('ir.attachment', 'ir_attachment_rel', 'ir_attachment_id', 'photo_id', 'Upload')
#     url = fields.Char('Image')