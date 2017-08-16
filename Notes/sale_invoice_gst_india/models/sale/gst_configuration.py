# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class GstConfiguration(models.Model):
    _name = "gst.configuration"
    
    name = fields.Char('GST Name', required=True)
    
class OurGstConfiguration(models.Model):
    _name = "our.gst.configuration"
    
    name = fields.Char('Our GST Name', required=True)