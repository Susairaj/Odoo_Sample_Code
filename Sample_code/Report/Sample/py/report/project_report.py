from openerp import api, fields, models, _
import datetime
import time
from openerp.exceptions import except_orm

class ProjectReport(models.Model):
    _name = "project.report"
    _description = "Project Report Details"
    
    @api.multi
    def print_report(self):
        return self.env['report'].get_action(self, 'receivables.project_report')
    

    date_from = fields.Date(string='Start Date',default=datetime.datetime.today(), required=True)
    date_to = fields.Date(string='End Date',default=datetime.datetime.today(), required=True)
    project_details_ids = fields.One2many('project.details', 'project_report_id', 'Project Details Report')

class ProjectDetailsReport(models.Model):
    _name = "project.details"
    _description = 'Project Details Report'
    
    project_report_id = fields.Many2one('project.report', 'Project Report', ondelet="cascade")
    
    project_id = fields.Many2one('receivable.project', 'Project')
    total_bill = fields.Char('Total Bill')
    total_budget_cost = fields.Char('Total Budget Cost')
    actual_cost = fields.Char('Actual Cost')
    budget_gross_marigin = fields.Char('Budget Gross Margin')
    actual_gross_marigin = fields.Char('Actual Gross Margin')
    
    