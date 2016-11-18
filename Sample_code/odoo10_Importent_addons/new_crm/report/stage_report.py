from odoo import api, models, fields

class CrmReport(models.AbstractModel):
    _name = 'report.new_crm.crm_report'

    def _get_data(self):
        self._context
        records = []
        # Get state ids
        waiting_quotation = self.env['crm.stage'].search([('name', '=', 'Waiting for Quotation')])
        waiting_confirmation = self.env['crm.stage'].search([('name', '=', 'Waiting for Confirmation')])
        if waiting_confirmation or waiting_quotation:
            for record in self.env['crm.lead'].search([('stage_id', 'in', (waiting_confirmation.id,waiting_quotation.id)),('current_date', '=', fields.Date.today())]):
                records.append({'name':record.name, 'enquiry_no':record.enquiry_no, 'vessel_name':record.vessel_name, 'url':record.opp_url, 'department_id':record.department_id.name,
                                 'partner_id':record.partner_id.name, 'country_id':record.country_id.name, 'date_action':record.date_action, 'stage_id':record.stage_id.name, 'planned_revenue':record.planned_revenue,
                                'probability':record.probability, 'team_id':record.team_id.name, 'user_id':record.user_id.name})
        return records

    @api.model
    def render_html(self, docids, data=None):
        docargs = {}
        if data:
            docargs = {
                'doc_ids': self.ids,
                'doc_model': 'crm.lead',
                'docs': self.env['crm.lead'].browse(self.ids),
                'get_data': self._get_data(data['form'], doc_ids=None)
            }
        else:
            docargs = {
                'doc_ids': self.ids,
                'doc_model': 'crm.lead',
                'docs': self.env['crm.lead'].browse(self.ids),
                'get_data': self._get_data()
            }
        return self.env['report'].render('new_crm.crm_report', values=docargs)