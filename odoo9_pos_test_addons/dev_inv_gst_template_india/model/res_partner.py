# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 Devintelle Software Solutions (<http://devintelle.com>).
#
##############################################################################
from openerp import models, fields, api, _

			

class res_partner(models.Model):
    """ Add gst Number """
    _inherit = 'res.partner'
    _description = 'Add gst Number'

    partner_gst_number = fields.Char('GST Number')
    
    
    
    
    
    
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

