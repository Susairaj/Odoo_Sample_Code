from openerp import models, fields, api, _
from datetime import datetime, timedelta, date
from lxml import etree
import re
from cStringIO import StringIO
import xlwt
import base64
from openerp.exceptions import UserError
from mx.DateTime.DateTime import today

class ParishFamilyReport(models.TransientModel):
    _name = 'parish.family.report'
    
    
    @api.model
    def fields_view_get(self,view_id=None, view_type='form',toolbar=False, submenu=False):
        res = super(ParishFamilyReport, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=False)
        doc = etree.XML(res['arch'])
        user = self.env['res.users'].browse(self._uid)
        if view_type=='form':
            for node in doc.xpath("//field[@name='bcc_ids']"):
                domain = "[('parish_id', '=', %s)]" % (user.parish_id.id)
                node.set('domain', domain)
            res['arch'] = etree.tostring(doc)
        return res
    
    report_name = fields.Selection([('entry','Entry'),('exit','Exit')], string='Category', default='entry')
    status = fields.Selection([('active','Active'),('inactive','Inactive')], string='Status', default='active')
    date_range = fields.Selection([('this_year', 'This Year-To Date'), ('last_year', 'Last Year'), ('custom', 'Custom'), ('all', '<All>')], 
                                  string="Date Range", default="all")
    start_date = fields.Date(string='Start date')
    end_date = fields.Date(string='End date')
    bcc_ids = fields.Many2many('res.parish.bcc.scc', string='BCC')
    bcc_all = fields.Boolean('All BCCs', default=True)
    parish_id = fields.Many2one('res.parish')
    
    sort_by = fields.Selection([('date', 'Date'), ('name', 'Family Name'), ('bcc', 'BCC Name')], string="Sort By", default='date')
    sort_rule = fields.Selection([('asc', 'Ascending'), ('desc', 'Descending')], string="Sort Rule", default='asc')
    work_summary = fields.Boolean('Summary', default=False)
    attachment_id = fields.Many2one('ir.attachment', 'Attachment')
    
    @api.onchange('date_range')
    def onchange_date_range(self):
        if self.date_range == 'this_year':
            year = '%s-01-01' % date.today().year
            self.start_date = datetime.strptime(year, '%Y-%m-%d')
            self.end_date = datetime.today().strftime('%Y-%m-%d')
        elif self.date_range == 'last_year':
            y = int(date.today().year)-1
            year1 = '%s-01-01' % y
            year2 = '%s-12-31' % y
            self.start_date = datetime.strptime(year1, '%Y-%m-%d')
            self.end_date = datetime.strptime(year2, '%Y-%m-%d') 
        elif self.date_range == 'custom':
            self.start_date = datetime.today().strftime('%Y-%m-%d') 
            self.end_date = datetime.today().strftime('%Y-%m-%d')
    
    
    @api.onchange('start_date','end_date')
    def onchange_date(self):
        current_year = '%s' % datetime.today().strftime('%Y-%m-%d')
        year = '%s-01-01' % date.today().year
        y = int(date.today().year)-1
        year1 = '%s-01-01' % y
        year2 = '%s-12-31' % y
        if not self.date_range == 'all':
            if self.date_range == 'this_year' and self.start_date == year and self.end_date == current_year:
                self.date_range = 'this_year'
            elif self.date_range == 'last_year' and self.start_date == year1 and self.end_date == year2:
                self.date_range = 'last_year'
            elif self.date_range:
                self.date_range = 'custom'
    
    @api.onchange('start_date','end_date')
    def onchange_date_between(self):
        self.date_validate()
    
    def date_validate(self):
        if self.start_date > self.end_date:
            raise UserError(_('Invalid Date Range !, Please change the Date Range'))
        if self.end_date > date.today().strftime('%Y-%m-%d'):
            raise UserError(_('Invalid Date !, End Date Should not be a Future Date'))

    
    @api.onchange('report_name','status')
    def onchange_report_name(self):
         if self.report_name in 'exit':
            self.status = 'inactive'
        
    @api.onchange('bcc_ids')
    def onchange_bcc_ids(self):
        if self.bcc_ids:
            self.bcc_all = False
        else:
            self.bcc_all = True
            
    @api.onchange('bcc_all')
    def onchange_bcc_all(self):
        if self.bcc_all:
            self.bcc_ids = False
            
    def get_sort_by(self):
        if self.sort_by:
            if self.sort_by == 'name':
                return 'ORDER BY family.name ' +self.sort_rule
            elif self.sort_by == 'bcc':
                return 'ORDER BY bcc.name ' +self.sort_rule
            elif (self.sort_by == 'date' and self.report_name == 'entry') or (self.sort_by == 'date' and self.status == 'active' or 'inactive'):
                return 'ORDER BY family.register_date ' +self.sort_rule
            elif self.sort_by == 'date' and self.report_name == 'exit':
                return 'ORDER BY family.date_of_exit ' +self.sort_rule
            
    def from_data( self, fields, rows ):
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet( 'Sheet 1' )
        header_title = xlwt.easyxf( "font: bold on; pattern: pattern solid, fore_colour gray25;align:horizontal left, indent 1,vertical center" )
        for i, fieldname in enumerate( fields ):
            worksheet.write( 0, i, fieldname, header_title )
            worksheet.col( i ).width = 8000  # around 220 pixels
        base_style = xlwt.easyxf( 'align: horizontal left,wrap yes,indent 1,vertical center' )
        worksheet.row( 0 ).height = 400
        for row_index, row in enumerate( rows ):
            worksheet.row( row_index + 1 ).height = 350 #Row height
            for cell_index, cell_value in enumerate( row ):
                cell_style = base_style
                if isinstance( cell_value, basestring ):
                    cell_value = re.sub( "\r", " ", cell_value )
                worksheet.write( row_index + 1, cell_index, cell_value, cell_style )
        fp = StringIO()
        workbook.save( fp )
        fp.seek( 0 )
        data = fp.read()
        fp.close()
        return data
    
    def get_families(self):
        query = ''
        bcc = ''
        date_range = ''
        user = self.env['res.users'].browse(self._uid)
        if user.parish_id.id:
            if self.bcc_all:
                bcc = 'AND (family.parish_bcc_scc_id is not null OR family.parish_bcc_scc_id is null)'
            elif self.bcc_ids:
                bcc = 'AND family.parish_bcc_scc_id in (%s)' % str(self.bcc_ids.ids).strip('[]')
            
            if self.report_name == 'entry':
                if self.date_range == 'all':
                    date_range = ''
                else:
                    date_range = "AND family.register_date BETWEEN '%s' AND '%s'" % (self.start_date,self.end_date)
            else:
                 if self.date_range == 'all':
                    date_range = ''
                 else:
                    date_range = "AND family.date_of_exit BETWEEN '%s' AND '%s'" % (self.start_date,self.end_date)
                      
                 query = "SELECT family.id FROM res_family AS family " \
                "WHERE family.active_in_parish = '0' "+date_range+" AND "+bcc+" AND family.parish_id="+str(user.parish_id.id)+" "+self.get_sort_by()
            
            if self.status == 'active':
                status = 'active_in_parish = True'
            else:
                status = 'active_in_parish = False'
                
            query = "SELECT family.id FROM res_family AS family JOIN res_parish_bcc_scc bcc ON (family.parish_bcc_scc_id = bcc.id) WHERE "+status+" "+date_range+" "+bcc+" AND family.parish_id= "+str(user.parish_id.id)+" Group by family.id,bcc.name "+self.get_sort_by()
            if query:
                self.env.cr.execute(query)
                member_ids = self.env.cr.fetchall()
                if member_ids:
                    return member_ids
                else:
                    raise UserError(_('No data available!, Please change the filter criteria'))
    @api.multi
    def get_xls(self):
        self.date_validate()
        field_headings = [];
        report_name=''
        if self.report_name == 'exit':
            report_name = 'Date of Exit'
        else:
            report_name = 'Date of Registration'
        
        field_headings =  ['S.No','Family Name', 'BCC', report_name] #headers
        all = []
        s_no = 1
        for member_id in self.get_families():
            for export_record in self.env['res.family'].browse(member_id):
                records = [];
                records.append(s_no)
                records.append(export_record.name or '-')
                records.append(export_record.parish_bcc_scc_id.name or '-')
                if self.report_name == 'exit':
                    records.append(export_record.date_of_exit or '-')
                else:
                    records.append(export_record.register_date or '-')
                all.append(records)
            s_no=s_no+1
        data = base64.encodestring(self.from_data(field_headings, all))
        attach_vals = {
            'name':'%s.xls' % ('Family Statistics'),
            'datas':data,
            'datas_fname':'%s.xls' % ('Family Statistics'),
         }

        doc_id = self.env['ir.attachment'].create(attach_vals)
        if self.attachment_id :
            try :
                self.attachment_id.unlink()
            except :
                pass
        self.write({'attachment_id':doc_id.id})
        return {
            'type': 'ir.actions.act_url',
            'url':'web/content/%s?download=true'%(doc_id.id),
            'target': 'self',
            }
    
    def _build_contexts(self, data):
        result = {}
        result['date_range'] = 'date_range' in data['form'] and data['form']['date_range'] or ''
        result['status'] = 'status' in data['form'] and data['form']['status'] or ''
        result['report_name'] = 'report_name' in data['form'] and data['form']['report_name'] or ''
        result['sort_by'] = 'sort_by' in data['form'] and data['form']['sort_by'] or ''
        result['sort_rule'] = 'sort_rule' in data['form'] and data['form']['sort_rule'] or ''
        result['bcc_ids'] = 'bcc_ids' in data['form'] and data['form']['bcc_ids'] or ''
        result['bcc_all'] = 'bcc_all' in data['form'] and data['form']['bcc_all'] or ''
        result['start_date'] = 'start_date' in data['form'] and data['form']['start_date'] or ''
        result['end_date'] = 'end_date' in data['form'] and data['form']['end_date'] or ''
        result['parish_id'] = 'parish_id' in data['form'] and data['form']['parish_id'] or ''
        result['work_summary'] = data['form']['work_summary'] or False
        return result
    
    @api.multi
    def print_report(self):
        self.ensure_one()
        self.date_validate()
        data = {}
        if self.get_families():
            data['ids'] = self.env.context.get('active_ids', [])
            data['model'] = self.env.context.get('active_model', 'ir.ui.menu')
            data['form'] = self.read(['report_name', 'date_range', 'start_date', 'end_date','status', 'bcc_ids', 'bcc_all', 'work_summary', 'sort_by', 'sort_rule'])[0]
            used_context = self._build_contexts(data)
            data['form']['used_context'] = dict(used_context, lang=self.env.context.get('lang', 'en_US'))                      
            return self.env['report'].get_action(self, 'cristo.report_parish_family_statistics', data=data)

