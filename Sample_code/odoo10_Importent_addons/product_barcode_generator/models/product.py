from odoo import api, models, fields, _
from odoo import exceptions
from odoo.exceptions import UserError


def isodd(x):
    return bool(x % 2)


class ProductCategory(models.Model):
    _inherit = 'product.category'

    ean_sequence_id = fields.Many2one('ir.sequence', string='Ean sequence')

class ProductTemplate(models.Model):
    _inherit = "product.template"
    _description = "Product Template"
    
    ean_sequence_id = fields.Many2one('ir.sequence', string='Ean sequence', default=lambda self: self.env['ir.sequence'].search([('name','=','Ean13')]).id)
    
    
    @api.model
    def _get_ean_next_code(self, product):
        sequence_obj = self.env['ir.sequence']
        if product.ean_sequence_id:
            ean = product.ean_sequence_id.next_by_id()
#            ean = sequence_obj.next_by_id(product.ean_sequence_id.id)
        elif product.categ_id.ean_sequence_id:
            ean = product.categ_id.ean_sequence_id.next_by_id()
        elif product.company_id and product.company_id.ean_sequence_id:
            ean = product.company_id.ean_sequence_id.next_by_id()
        elif self.env.context.get('sequence_id', False):
            ean = self.env.context.get('sequence_id').next_by_id()
        else:
            return None
        ean = (len(ean[0:6]) == 6 and ean[0:6] or
               ean[0:6].ljust(6, '0')) + ean[6:].rjust(6, '0')
        if len(ean) > 12:
            raise exceptions.Warning(
                _("Configuration Error!"
                  "The next sequence is longer than 12 characters. "
                  "It is not valid for an EAN13 needing 12 characters, "
                  "the 13 being used as a control digit"
                  "You will have to redefine the sequence or create a new one")
                )

        return ean

    def _get_ean_control_digit(self, code):
        sum = 0
        for i in range(12):
            if isodd(i):
                sum += 3 * int(code[i])
            else:
                sum += int(code[i])
        key = (10 - sum % 10) % 10
        return '%d' % key

    @api.model
    def _generate_ean13_value(self, product):
        ean = self._get_ean_next_code(product)
        if not ean:
            return None
        key = self._get_ean_control_digit(ean)
        ean13 = ean + key
        return ean13
    
#    @api.multi
#    def copy(self, default=None, context=None):
#        if default is None:
#            default = {}
#        if context is None:
#            context = {}
#        default['ean13'] = False
#        return super(ProductTemplate, self.with_context(context)).copy(default=default)

#    @api.one
#    def generate_ean13(self):
#        if self.ean13:
#            return
#        ean13 = self._generate_ean13_value(self)
#        if not ean13:
#            return
#        self.write({'barcode': ean13})
#        return True
    
    @api.model
    def create(self, vals):
        if not vals.get('default_code'):
            vals.update({'default_code': vals.get('name')})
        template = super(ProductTemplate, self).create(vals)
        barcode = self._generate_ean13_value(template)
        template.write({'barcode': barcode})
        return template
    
    @api.multi
    def write(self,vals):
        barcode = ''
        if vals.get('barcode'):
            template =  super(ProductTemplate, self).write(vals)
            if not len(self.barcode) == 13:
                raise UserError(_("Barcode must contains 13 digits."))
        if vals.get('default_code'):
            template =  super(ProductTemplate, self).write(vals)
            barcode = self._generate_ean13_value(self)
            if barcode:
                self.write({'barcode': barcode})
            return template
        else:
            return super(ProductTemplate, self).write(vals)
