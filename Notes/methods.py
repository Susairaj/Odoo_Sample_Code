Calculate size of direcotry structure recursion method
----------------------------------------------------------------------------

def _get_size(self, cr, uid, dir_id):
        size = 0
        attach_obj = self.pool.get('ir.attachment')
        file_ids = attach_obj.search(cr, uid, [('parent_id', '=', dir_id)])
        for f in attach_obj.browse(cr, uid, file_ids):
            size += f.file_size or 0
        child_ids = self.search(cr, uid, [('parent_id', '=', dir_id)])
        for child_id in child_ids:
            size += self._get_size(cr, uid, child_id)
        return size
    
def _size_calc(self, cr, uid, ids, name, args, context=None):
	""" Finds size of the direcotry.
	@param name: Name of field.
	@param args none:
	@return: Dictionary of values.
	"""
	result = {}
	for dir in self.browse(cr, uid, ids, context=context):
		result[dir.id] = self._get_size(cr, uid, dir.id)
	return result
		
		
'size': fields.function(_size_calc, type='float', string='Total Size'),
###################
Create function one object to another::

@api.model
    def create(self, vals):
        vals.update({'name':self.env['ir.sequence'].get('materials.receiving')})
        accepted_quantities = vals.get('material_ids')
        for accepted_qty in accepted_quantities:
            material_id= accepted_qty[2]['material_id']
            material_obj = self.env['material.material'].search([('id', '=', material_id )])
            material_qty=material_obj.available_units
            total= accepted_qty[2]['accepted_qty'] + material_qty
            self.env['material.material'].browse([material_id]).write({'available_units':total})
        return super(MaterialReceiving, self).create(vals)
		
	def write(self, cr, uid,ids, vals, context=None):
#		vals['num1'] = vals['num1'] + 10
		value = self.pool.get('student').search(cr,uid,[('name','like','susai')])
		for stu in self.pool.get('student').browse(cr, uid, value):
			vals['title'] = stu.name
			return super(test, self).write(cr, uid,ids, vals, context=None)
			
	def create(self, cr, uid, vals, context=None):
        if context is None:
            context = {}
        vals.update({'user_name': vals.get('name', None),'phone_no':vals.get('phone',None),
                     'mobile_no':vals.get('mobile',None),'email_id':vals.get('email',None),'user_role':vals.get('user',None)}),
        vals.update({'customer_name':vals.get('customer',False),'supplier_name':vals.get('supplier',False)})
        return super(res_partner, self).create(cr, uid, vals, context=None)
(first the changintg field vals.get(the other object field ,validation)(False is the check box)			
			
	def write(self, cr, uid, ids, values, context = None):
   res = super(MyChildClass, self).write(cr, uid, ids, values, context = context)
   if 'child_field' in values:
      for child_item in self.browse(cr, uid, ids, context = context):
          self.pool.get('my.parent.model').write(cr, uid, [child_item.parent_id.id], {'parent_field': values['child_field'],}, context = context) 

   return res

	def write(self, cr, uid, ids, vals, context=None):
        state1 = self.browse(cr, uid, ids).state
        state2 = vals.get('state',None)
        date_start = self.browse(cr, uid, ids).date_start
        date_end = self.browse(cr, uid, ids).date_end
        res = super(initiative_proposal, self).write(cr, uid,ids, vals, context=None)
        if state1 not in ['approval','decline'] and state2 == 'approval':
            if (not date_start) or (not date_end):
                raise osv.except_osv(_('Validate Error'), _('Start Date or End Date Missing'))
            if date_start > date_end:
                raise osv.except_osv(_('Validate Error'), _('Start Date is Greater than End Date'))    
            for stu in self.pool.get('initiative.proposal').browse(cr, uid, ids, context=None):
                vals['name']=str(stu.name)
                vals['team_lead_id']=stu.team_lead_id.id
                vals['date_start']=stu.date_start
                vals['date_end']=stu.date_end
                vals['caution_day']=stu.caution_day
                vals['department_id']=stu.department_id.id
                vals['initiative_type_id']=stu.initiative_type_id.id
                vals['initiative_category_id']=stu.initiative_category_id.id
                vals.pop('state')
                record=[]
                for objectives in stu.objective_ids:
                    record.append([6,False,[objectives.id]])
                vals['objective_ids']=record    
                self.pool.get('project.project').create(cr, uid, vals, context=None)
        if state1 == 'approval' and state2 == state1:
                vals.update({'name': vals.get('name', None)})
                self.pool.get('project.project').create(cr, uid, vals, context=None)
        return res
			
Create:			
#############		
	def create(self, cr, uid, vals, context=None):
        if context is None:
            context = {}
        vals['join_date'] = datetime.today()       
        return super(student, self).create(cr, uid, vals, context=None)
		
	def create(self, cr, uid, vals, context=None):
        if context is None:
            context = {}
            vals.update({'user_name': str(vals['name']),'phone_no':str(vals['phone']),
                     'mobile_no':str(vals['mobile']),'email_id':str(vals['email']),'user_role':str(vals['user']),
                     'customer_name':str(vals['customer']),'supplier_name':str(vals['supplier'])}),
        return super(res_partner, self).create(cr, uid, vals, context=None)	
###########################
name_get,concatenate:
		
		
	def name_get(self, cr, uid, ids, context=None):
		if not ids:
			return []
			res = []
		for record in self.read(cr, uid, ids, ['student_name','name'], context=context):
			if record['name']:
			print record['name'][1]
			name = "%s (%s)" % (str(record['student_name']), str(record['name'][1]))
			res.append((record['id'],name ))
		return res
#######################		
	witget="radio";
#################
name_get:
	def name_get(self, cr, uid, ids, context=None):
        if not ids:
            return []
        res = []
        for record in self.read(cr, uid, ids, ['student_id'], context=context):
            if record.get('student_id', False):
                studen_id = "%s" % (str(record['student_id'][1]))
                res.append((record['id'],studen_id ))
        return resnote
#######################		
on_change:

	def onchange_activity_stage(self, cr, uid, ids, activity_temp_state_id, context=None):
        val = {}
        if activity_temp_state_id:
            percentage = self.pool.get('activity.template.state').browse(cr, uid, activity_temp_state_id)
            per_completion = percentage.percentage_of_completion
            val = {
                   'per_completion': per_completion,
                   }
        return {'value': val}



	def onchange_student_name(self, cr, uid, ids, stu_id, context=None):
        val = {}
        if stu_id:
            mark_id = self.pool.get('student.course').browse(cr, uid, stu_id)
            val = {
                   'percentage': mark_id.percentage,
                   'grade':mark_id.grade,
                   }
        return {'value': val}
	
	def onchange_dob(self, cr, uid, ids, dob, context=None):
        val = {}
        if dob:
            val = { 'age' : datetime.date.today().year - datetime.datetime.strptime(dob, '%Y-%m-%d').date().year }
        return {'value': val}
		
		
records(0) to name::


  def _get_milestone_name(self, cr, uid, ids, fieldname, args, context=None):
        res = {};milestone_names =''
        for rec in self.browse(cr, uid, ids):
            for mileston_id in rec.mileston_ids:
                if milestone_names:    
                    milestone_names += ', ' + mileston_id.milestone_id.name
                else:
                    milestone_names = mileston_id.milestone_id.name
            res[rec.id] = milestone_names
        return res

	
#####################	
On_change xml:

		on_change="onchange_student_name(student_id)"
		
		options="{'no_create':'1','no_edit':'1'}"
		
	

	
	burnur account:
		tpeac gziei aduld kylcs
		
#######################		
function fields:


   def _get_total(self, cr, uid, ids, name, arg, context=None):
        res = dict.fromkeys(ids, False)
        if name:
            for rec in self.browse(cr, uid, ids):
                m=(rec.anatomy+rec.biochemistry+rec.microbiology+rec.community_medicine+rec.anesthesiology)
                res[rec.id] =m
        return res
    def _get_percentage(self, cr, uid, ids, name, arg, context=None):
        res = dict.fromkeys(ids, False)
        if name:
            for rec in self.browse(cr, uid, ids):
                m=(rec.total)/10
                res[rec.id] =m
        return res
    
    def _get_grade(self, cr, uid, ids, grade, arg, context=None):
        res = dict.fromkeys(ids, False)
        grade = False
        for rec in self.browse(cr, uid, ids):
            if (rec.percentage >= 90) and (rec.percentage <= 100):
                grade = "a_plus"
            elif (rec.percentage >= 60) and (rec.percentage < 90):
                grade = "a"
            elif (rec.percentage >= 40) and (rec.percentage < 60):
                grade = "b"
            elif (rec.percentage < 40):
                grade = "c"
            res[rec.id] = grade
        return res
		
########################		
get age::


    def _get_age(self, cr, uid, ids, dob, arg, context=None):
        res = dict.fromkeys(ids, False)
        today = date.today()
        if dob:
            for rec in self.browse(cr, uid, ids):
                dob = datetime.strptime(rec.dob, '%Y-%m-%d').date()
                delta = today - dob
                days = delta.days
                months = (delta.days/365) * 12
                year = today.year - dob.year
                if days>1:
                    res[rec.id] = "%s Day(s), %s Month(s)  , %s Year(s)" % (days, months, year)
                elif days<=0:
                    res[rec.id] = "You are not yet born"
                else:
                    res[rec.id] = "%s Day, %s Month , %s Year" % (days, months, year)
        return res
    
    def _get_age1(self, cr, uid, ids, dob, arg, context=None):
        res = dict.fromkeys(ids, False)
        today = date.today()
        if dob:
            for rec in self.browse(cr, uid, ids):
                dob = datetime.strptime(rec.dob, '%Y-%m-%d').date()
                res[rec.id] = today.year - dob.year
        return res
############################
Function field take the one class field to other class::

	def _get_total(self, cr, uid, ids, name, args, context=None):
        res = dict.fromkeys(ids, False)
        total=0
        for rec in self.browse(cr, uid, ids):
            for ttl in rec.discount_ids:
                count_ob = ttl.amount
                if count_ob:
                    total=total+(count_ob)
        res[rec.id] = total
        return res
##################		
attrs="{'readonly':[('is_system_admin_group','=',False),('is_executive_group','=',False),('is_lead_active_user','!=',True),('is_assigned_to','!=',True)]}"

    def _is_assigned_to(self, cr, uid, ids, fieldname, args, context=None):
        res = {}
        ''' Checking whether current user is Team Member or not '''            
        is_user_group = False
        user = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'project', 'group_project_user')
        if user:
            val = self.pool.get('res.users').read(cr, uid, [uid], ['groups_id'], context=context)[0]['groups_id']
            for record in self.browse(cr, uid, ids, context=context):
                if record.assigned_to.id == uid:
                        res[record.id] = True
                else:
                    res[record.id] = False
        return res
    
        'is_assigned_to': fields.function(_is_assigned_to, type="boolean", string='Assigned to user'),

###################################		
	def fields_view_get(self, cr, uid, view_id=None, view_type='form', context=None, toolbar=False, submenu=False):
        user_id = []
        member = context.get('members', False)
        res = super(project_task, self).fields_view_get(cr, uid, view_id=view_id, view_type=view_type, context=context, toolbar=toolbar, submenu=submenu)
        if member:
            for record in member[0][2]:
                user_id.append(record)
            doc = etree.XML(res['arch'])
            for field in res['fields']:
                if field == 'assigned_to':
                    res['fields'][field]['domain'] = [('id','in',user_id)]
        return res
    
    
    def _get_total(self, cr, uid, ids, name, args, context=None):
        res = {}; total = 0 ; 
        for rp in self.browse(cr, uid, ids):
            for am in rp.discount_ids:
                total += am.amount
            res[rp.id] = total
        return res
	def default_get(self, cr, uid, fields, context=None):
        data = super(project_issue, self).default_get(cr, uid, fields, context=context)
        task_id = context.get('project_id', None)
        if task_id:
            task = self.pool.get('project.task').browse(cr, uid, task_id)
            project = self.pool.get('project.project').browse(cr, uid, task_id)
            if task.name:
                data['activity'] = task.name
                data['project_id'] = project.id
        return data
##########################
Related method::
			'total_ids':fields.related('total_id','total',relation='discount',type='many2one',string='Total'),
		current class many2one field,the other class field name that you need ,other class object name,type text or char
			then string.

#################################
Create the msg in inbox put in create method::

post_vars = {'subject': "Message subject",
             'body': "Message body",
             'partner_ids': [(4, 3)],} # Where "4" adds the ID to the list 
                                       # of followers and "3" is the partner ID 
thread_pool = self.pool.get('mail.thread')
thread_pool.message_post(
        cr, uid, False,
        type="notification",
        subtype="mt_comment",
        context=context,
        **post_vars)		

##################
Apply domain filter for the many2one field:::

@api.onchange('place')
def onchange_place(self):
    res = {}
    if self.place:
        res['domain'] = {'asset_catg_id': [('place_id', '=', self.place.id)]}
    return res
#################
Load One2many fields value using default_get::

@api.model
    def default_get(self, fields_name):
        receiving_type = [];
        data = super(MaterialReceiving, self).default_get(fields_name)
        for record in self.env['receiving.attachment.type'].search([]):
            if record.id != self.env['receiving.attachment'].search([('id', '=', record.id )]).id:
                receiving_type.append((0, 0,{'receiving_attach_type_id': record.id}))
            else:
                receiving_type.append((0, 0,{'receiving_attach_type_id': record.id}))
            data['receiving_attachment_ids'] = receiving_type
        return data
    
    @api.model
    def default_get(self, fields_name):
        res = super(MaterialReceiving, self).default_get(fields_name)
        attachment_types = self.env['receiving.attachment.type'].search([])
        receiving_attachment = self.env['receiving.attachment']
        data = []
        for attachment_type in attachment_types:
            attachment = receiving_attachment.create({
                'receiving_attach_type_id': attachment_type.id,
            })
            data.append(attachment.id)
        res['receiving_attachment_ids'] = [(6, False, data)]
        return res	
###############################		
Send Notifications::
alert_msg = 'Your message has been sent successfully. Your have overridden '+str(cre_bal_now)+' credits.'
            res = {
            'type': 'ir.actions.client',
            'tag': 'action_warn',
            'name': 'Failure',
            'params': {
               'title': 'Notification',
               'text': alert_msg,
               'sticky': True
                }
            }
####################################
Load Tow value in one place:::

@api.multi
    @api.depends('name', 'branch_name')
    def name_get(self):
        result = []
        for bank in self:
            if bank.name:
                name = '' + str(bank.name) + '-' + str(bank.branch_name)
            result.append((bank.id, name))
        return result
############
Unlink Function::

@api.multi
    def unlink(self):
        bill_confirmation_id = self.env['billing.confirmation'].search([('project_id', '=', self.id),('state', '=', 'request_delivery_confirmation')])
        if bill_confirmation_id:
            bill_confirmation_id.unlink()
        else:
            raise except_orm(_('Invalid Deletion'), _('Can not delete the delivery/bill confirmed record.'))
        return super(BillDetails, self).unlink()
###########
To display currency symbol::
currency_id = fields.Many2one('res.currency', string='Currency', required=True, default=lambda self: self.env.user.company_id.currency_id)
<field name="currency_id" invisible="1"/>
widget='monetary' options="{'currency_field': 'currency_id'}"

###########
Update one2many field value to one2many field::

@api.multi
    def request_for_delivery_approval(self):
        deliverable_ids = []
        from_mail = self.project_manager.email
        to_mail =self.assignment_in_charge.email
        name = self.name
        for deliver_id in self.deliverable_ids:
            deliverable_ids.append((0, 0, {'deliverable_id': deliver_id.deliverable_id.id,
                                           'due_date':deliver_id.due_date,
                                           'measurement':deliver_id.measurement,
                                           'attachment_need':deliver_id.attachment_need}))
        if self.bill_type == 'occurrence_with_fixed_cost' or self.bill_type == 'occurrence_with_fixed_cost':
            for record in self.billing_detail_ids:
               self.env['billing.confirmation'].create({'bill_date': record.bill_date,'project_id':self.id,
                                                        'total_bill_amount':record.total_bill_amount ,'current_bill_amount':record.current_bill_amount ,
                                                        'reference':record.reference ,'month':record.month ,
                                                        'contact_phone':record.contact_phone, 'contact_email':record.contact_email,
                                                        'service_tax_id':record.service_tax_id.id,'swach_bharat':record.swach_bharat,
                                                        'total':record.total, 'description':record.description,'state': 'request_delivery_confirmation',
                                                        'deliverable_ids': deliverable_ids})
        elif self.bill_type ==  'one_time_occurrence':
            self.env['billing.confirmation'].create({'bill_date': self.bill_date,'project_id':self.id,
                                                        'total_bill_amount':self.total_bill_amount ,'current_bill_amount':self.current_bill_amount ,
                                                        'reference':self.reference ,'month':self.month ,
                                                        'contact_phone':self.contact_phone, 'contact_email':self.contact_email,
                                                        'service_tax_id':self.service_tax_id.id,'swach_bharat':self.swach_bharat,
                                                        'total':self.total, 'description':self.description,'state': 'request_delivery_confirmation',
                                                        'deliverable_ids': deliverable_ids})
														
########################
Create many2many field value::
'skil_set_ids': [(6, 0, [record_id.id for record_id in resource_id.skil_set_ids])]
###################
Name Validation from the function::

@api.model
def create(self, vals):
	name = vals.get('name')
	validations.validate_title_name(self,name)
	return super(RegionRegion, self).create(vals)
		
def validate_title_name(self,name):
    if name:
        trimed_name = name.strip() 
        for record in self.search([]):
            if record.name == trimed_name:
                raise except_orm(_('Invalid Name'), _('Entered name is already exist.'))

####################################				
Get the value and replace the value in create method::

@api.model
	def create(self, vals):
		state_lower =  vals.get('state').lower()
		vals.update({'state':state_lower.title()})
		if vals.get('state') == 'Tamil Nadu':
			vals.update({'state':'Tamilnadu'})
		return super(HospitalHospital, self).create(vals)
				
####################################
Odoo iframe::
<iframe src="/google_map/?width=898&amp;height=485&amp;partner_ids=22839,304331,115647,339246,319987,694954,1118,17692,105287,809497,156060,817411,130275,759167,459457,198697,729921,404547,653869,737166,73881,743758,759086,460789,512662,596235,20017,735815,160703,703068,725074,626268,20225,52665,705447,795149&amp;partner_url=/partners/" style="width:898px; height:485px; border:0; padding:0; margin:0;"></iframe>

############
Export data through button::

from openerp import api, fields, models, _
from datetime import datetime
import time
import datetime
from openerp.exceptions import except_orm 
import base64
try:
    import xlwt
except ImportError:
    xlwt = None
import re
from cStringIO import StringIO
from lxml import etree


def from_data( self, fields, rows ):
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet( 'Sheet 1' )
        header_title = xlwt.easyxf( "font: bold on; pattern: pattern solid, fore_colour gray25;align:horizontal left, indent 1,vertical center" )
        for i, fieldname in enumerate( fields ):
            worksheet.write( 0, i, fieldname, header_title )
            worksheet.col( i ).width = 8000  # around 220 pixels
        base_style = xlwt.easyxf( 'align: horizontal left,wrap yes,indent 1,vertical center' )
        date_style = xlwt.easyxf( 'align: horizontal left,wrap yes, indent 1,vertical center', num_format_str='YYYY-MM-DD' )
        datetime_style = xlwt.easyxf( 'align: horizontal left,wrap yes,indent 1,vertical center', num_format_str='YYYY-MM-DD HH:mm:SS' )
        worksheet.row( 0 ).height = 400
        for row_index, row in enumerate( rows ):
            worksheet.row( row_index + 1 ).height = 350
            for cell_index, cell_value in enumerate( row ):
                cell_style = base_style
                if isinstance( cell_value, basestring ):
                    cell_value = re.sub( "\r", " ", cell_value )
                elif isinstance( cell_value, datetime.datetime ):
                    cell_style = datetime_style
                elif isinstance( cell_value, datetime.date ):
                    cell_style = date_style
                worksheet.write( row_index + 1, cell_index, cell_value, cell_style )
        fp = StringIO()
        workbook.save( fp )
        fp.seek( 0 )
        data = fp.read()
        fp.close()
        return data

    @api.multi
    def export_in_excel(self):
        field_headings = []; 
        context=dict(self._context) or {}
        if context and context.get('active_id',False):
            active_id = context.get('active_id',False)
            field_headings =  ['SL.No', 'Supplier', 'Material Code', 'Material Name', 'UOM', 'Supplier Challan No', 
                               'Receipt Date', 'Total Accepted Quantity','Total Return Quantity', 'Remarks']
        if active_id :
            all=[];
            for export_record in self.env['supplier.detailed_transaction.report'].browse(active_id):
                for mat in export_record.supplier_transaction_ids:
                    records = [];
                    records.append(mat.sl_number)
                    records.append(mat.supplier_id.supplier_id.name)
                    records.append(mat.material_id.name)
                    records.append(mat.material_id.unique_id)
                    records.append(mat.material_id.unit_id.name)
                    records.append(mat.challan_numbrer)
                    records.append(mat.receipt_date)
                    records.append(mat.quantity_total_receipt)
                    records.append(mat.quantity_total_return)
                    records.append(mat.remarks if mat.remarks else '')
                    all.append(records)
            data = base64.encodestring(self.from_data(field_headings, all))
            attach_vals = {
                'name':'%s.xls' % ('Supplier Detailed Transaction'),
                'datas':data,
                'datas_fname':'%s.xls' % ('Supplier Detailed Transaction'),
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
#########################
Open xml view through python code::
for particular views:
 @api.multi
    def get_client_tickets(self):
        context = dict(self._context or {})
        context['client_id'] = self.id
        tree_id = self.env.ref('scms.ticket_ticket_view_tree', False)
        form_id = self.env.ref('scms.ticket_ticket_view_form', False) 
        return {
            'name': _('Total Tickets'),
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'ticket.ticket',
            'views': [(tree_id.id, 'tree'),(form_id.id, 'form')],
            'type': 'ir.actions.act_window',
            'domain': [('client_id', 'in', [self.id])],
            'context': context,
        }
For the object:
	@api.multi
    def get_client_tickets(self):
        context = dict(self._context or {})
        context['client_id'] = self.id
        return {
            'name': _('Total Tickets'),
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'ticket.ticket',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'domain': [('client_id', 'in', [self.id])],
            'context': context,
        }
For paticulat view::
@api.multi
    def employee_allocation(self):
        context = dict(self._context or {})
        active_id =self.browse(self._context.get('active_id'))
        return {
            'name': _('Employee Allocation'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'cleaning.indursty.project',
            'view_id': self.env.ref('cleaning_industry.cleaning_industry_employee_allotment_view_form', False).id,
            'type': 'ir.actions.act_window',
            'context': context,
#             'domain':[('cleaning_industry_project_id', '=',active_id.id)],
#             'target': 'new',
            'res_id':self.id
        }
#####################		
Get days count from two days::
api.one
@api.depends('end_date')
def date_days_count(self):
	if self.end_date:
		str_date = self.start_date
		end_dat = self.end_date
		d1 = datetime.strptime(str_date, "%Y-%m-%d")
		d2 = datetime.strptime(end_dat, "%Y-%m-%d") 
		days_count = str((d2 - d1).days)
		self.date_days_counts = days_count
###########################
Query Execution::

receive_query = 'select count(*) maximum , max(supplier_id) from materials_receiving  where store_id= %s and receive_date >= %s::date AND receive_date <= %s ::date  group by supplier_id   ORDER BY maximum DESC limit 5;'
#         receive_query = 'select count(*) maximum , max(supplier_id), store_id  from materials_receiving where store_id = %s  group by supplier_id , store_id ORDER BY maximum DESC limit 5;'
receive_records = self._cr.execute(receive_query, (active_store, from_date, to_date))
receive_records = self._cr.fetchall()

Refresh the page::
return {
         'type': 'ir.actions.client',
         'tag': 'reload',
         }
		 
##########################
Find in between the date range::
@api.onchange('date_from', 'date_to')
    def onchange_work_slot(self):
        if self.date_from and self.date_to:
            active_id = self.env['cleaning.industry.project'].browse(self._context.get('project_id', False))
            if active_id:
                for record in active_id.project_line_ids:
                    if record.start_date <= self.date_from <= self.date_to <= record.end_date:
                        break
                    else:
                        raise except_orm(_('Validation Warning'), _('Out of date.'))
###################################
Write vlue in many2many field::
self.write({'employee_allot_ids': [6, 0 , employee_list_ids]})
##########333
Name Search::

@api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        recs = self.browse()
        project_id = self._context.get('project_id', False)
        if project_id:
            members = self.env['project.project'].browse(project_id).members.ids or []
            recs = self.search([('name', operator, name),('id', 'in', members)] + args, limit=limit)
        else:
            recs = self.search([('name', operator, name)] + args, limit=limit)
        return recs.name_get()

#########################
Inherit Controller Class:::

import openerp
from openerp.addons.auth_signup.controllers.main import AuthSignupHome
class my_class(AuthSignupHome):
    <custom code>	

##############################
Empty whole form when action is done:

@api.multi
def reset(self):
	empty_obj = self.env[self._name]

	for key, value in self._fields.iteritems():
		if value.name not in models.MAGIC_COLUMNS:
			if value.name == 'name':
				setattr(self, key, getattr(empty_obj, key))	
########################################
Date manipulation:::
string date into datetime::
date_end = datetime.strptime(record.end_date, '%Y-%m-%d')
datetime into date:
date_end = datetime.strptime(record.end_date, '%Y-%m-%d').date()
string datetime into datetime:
dt = datetime.strptime(record.confirmation_date, "%Y-%m-%d %H:%M:%S").date()
date into datetime::
dt1 = datetime.strftime(date, "%Y-%m-%d %H:%M:%S")

Create Customer Invoice::
current_date = datetime.datetime.now().date()
            product_id = self.env['product.product'].search([('type','=','service')],limit=1)
            if not product_id:
                raise UserError(_('Please create at   least one service product in order to crate an Invoice'))
            account_type_id = self.env['account.account.type'].sudo().search([('name', '=', 'Receivable')], limit=1)
            journal_id = self.env['account.journal'].sudo().search([('company_id', '=', self.company_id.id), ('type', '=', 'sale')], limit=1)
            account_id = None
            for account in self.env['account.account'].sudo().search([('company_id', '=', self.company_id.id), ('user_type_id', '=', account_type_id.id)]):
                account_id = account.id
                break;
            if not account_id:
                raise UserError(_('Please create payable account for.' + str(self.company_id.name)))
            account_list = []
            account_list.append((0, 0, {'product_id':product_id.id,'quantity':1 , 'name':product_id.name,
                                               'account_id':account_id,'price_unit': self.service_amount, 'uom_id':product_id.uom_id.id}))
            if journal_id:
                if account_list:
                    self.env['account.invoice'].sudo().create({'partner_id':self.partner_id.id, 'date_invoice':current_date, 'currency_id': self.env.user.company_id.currency_id.id,'journal_id':journal_id.id, 'account_id':account_id, 
                                                    'company_id':self.company_id.id,'invoice_line_ids':account_list, 'type':'out_invoice', 'state':'draft'})