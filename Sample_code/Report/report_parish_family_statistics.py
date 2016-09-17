from openerp import models, fields, api, _
from datetime import datetime,date

class ReportParishFamilyStatistics(models.AbstractModel):
    _name = 'report.cristo.report_parish_family_statistics'
        
    def get_sort_by(self, form):
        if form['sort_by']:
            if form['sort_by'] == 'name':
                return 'ORDER BY family.name ' +form['sort_rule']
            elif form['sort_by'] == 'bcc':
                return 'ORDER BY bcc.name ' +form['sort_rule']
            elif (form['sort_by'] == 'date' and form['report_name'] == 'entry') or (form['sort_by'] == 'date' and form['status'] == 'active' or 'inactive'):
                return 'ORDER BY family.register_date ' +form['sort_rule']
            elif form['sort_by'] == 'date' and form['report_name'] == 'exit':
                return 'ORDER BY family.date_of_exit ' +form['sort_rule']
        
    def get_family_details(self, form):
        result = []
        query = ''
        bcc = ''
        date_range = ''
        user = self.env['res.users'].browse(self._uid)
        if user.parish_id.id:
            if form['bcc_all']:
                bcc = 'AND (family.parish_bcc_scc_id is not null OR family.parish_bcc_scc_id is null)'
            elif form['bcc_ids']:
                bcc = 'AND family.parish_bcc_scc_id in (%s)' % str(form['bcc_ids']).strip('[]')
            
            if form['report_name'] == 'entry':
                if form['date_range'] == 'all':
                    date_range = ''
                else:
                    date_range = "AND family.register_date BETWEEN '%s' AND '%s'" % (form['start_date'],form['end_date'])
            else:
                 if form['date_range'] == 'all':
                    date_range = ''
                 else:
                    date_range = "AND family.date_of_exit BETWEEN '%s' AND '%s'" % (form['start_date'],form['end_date'])
                      
                 query = "SELECT family.id FROM res_family AS family " \
                "WHERE family.active_in_parish = '0' "+date_range+" AND "+bcc+" AND family.parish_id="+str(user.parish_id.id)+" "+self.get_sort_by(form)
            
            if form['status'] == 'active':
                status = 'active_in_parish = True'
            else:
                status = 'active_in_parish = False'
                
            query = "SELECT family.id FROM res_family AS family JOIN res_parish_bcc_scc bcc ON (family.parish_bcc_scc_id = bcc.id) WHERE "+status+" "+date_range+" "+bcc+" AND family.parish_id= "+str(user.parish_id.id)+" Group by family.id,bcc.name "+self.get_sort_by(form)
            
            if query:
                self.env.cr.execute(query)
                member_ids = self.env.cr.fetchall()
                for member_id in member_ids:
                    val = self.env['res.family'].browse(member_id)
                    result.append(val)
                   
        return result
    
    @api.multi
    def render_html(self, data):
        self.model = self.env.context.get('active_model')
        docs = self.env[self.model].browse(self.env.context.get('active_id'))
        report_lines = self.get_family_details(data.get('form'))
        docargs = {
            'doc_ids': self.ids,
            'doc_model': self.model,
            'data': data['form'],
            'docs': docs,
            'get_family_details': report_lines,
        }
        return self.env['report'].render('cristo.report_parish_family_statistics', docargs)
