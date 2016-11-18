from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class CrmLead(models.Model):
    _inherit = 'crm.lead'
    
    enquiry_no = fields.Char('Enquiry Number')
    vessel_name = fields.Char('Vessel Name', size=50)
    opp_url = fields.Char('URL')
    current_date = fields.Date('Date', default = fields.Date.today())
    department_id = fields.Many2one('lead.department', 'Department')
    
    @api.model
    def create(self, vals):
        context = dict(self._context or {})
        enq_code = str(self.env['ir.sequence'].next_by_code('crm.lead'))
        year = fields.date.today()
        current_year =  str(year)[2:4]
        first = enq_code.split('ENQ')[0]
        second =enq_code.split('ENQ')[1]
        vals['enquiry_no'] = str(first) + 'ENQ' + '-' + str(current_year) + '-' + str(second)
        return super(CrmLead, self.with_context(context, mail_create_nolog=True)).create(vals)
    
    @api.model
    def _cron_send_mail(self):
        self.send_mail()
        return True

    @api.multi
    def send_mail(self):
        try:
            template_id = self.env['ir.model.data'].get_object_reference('new_crm', 'send_stage_mail')[1]
        except ValueError:
            _logger.info('Could not find email template')
        if template_id:
                self.env['mail.template'].browse(template_id).send_mail(self.id, force_send=True)
        return True
        
class LeadDepartment(models.Model):
    _name = 'lead.department'
    
    name = fields.Char('Name', required=True)