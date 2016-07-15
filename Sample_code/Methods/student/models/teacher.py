from openerp import models, fields, api, _
from openerp.exceptions import Warning
from openerp.addons.payment.models.payment_acquirer import ValidationError
import openerp.addons.decimal_precision as dp
#from openerp.exceptions import except_orm, Warning, RedirectWarning

GENDER = [
		('male', 'Male'),
		('female', 'Female'),
		('other', 'Other')
]
VERIFIED = [
		('yes', 'Yes'),
		('no', 'No'),
]
STATE = [
		('draft', 'Draft'),
		('verify', 'Verify'),
		('done', 'Complete'),
]

class Student_Student(models.Model):
	_name = "student.student"
	_description = "Student Details"
	
	@api.multi
	def get_view(self):
		view_id = self.env.ref('student.standared_standared_view_tree', False)
		return {
		    'name': _('Standared view'),
		    'type': 'ir.actions.act_window',
		    'view_type': 'tree',
		    'view_mode': 'tree',
		    'res_model': 'standared.standared',
		    'views': [(view_id.id, 'tree')],
		   	'view_id': view_id.id,
		    'target': 'new',
		}
	
	@api.multi
	def print_report(self):
		return {
		    'name': _('Student Report'),
		    'type': 'ir.actions.report.xml',
		    'res_model': 'student.student',
		    'report_name':'student.report_student_sample_qweb', 
		}
	
	@api.multi
	def open_url(self):
		url = str(self.url)
		furl = 'http://' + url
		print furl
		return {
 		    "type": "ir.actions.act_url",
		    "url": furl,
		    "target": "new",
		}

	@api.one
	@api.depends('tamil', 'english', 'maths', 'science', 'social')
	def _total(self):
		total = 0
		if self.tamil and self.english and self.maths and self.science and self.social:
			total = self.tamil + self.english + self.maths + self.science + self.social
			self.total = total
			
	@api.onchange('tamil', 'english', 'maths', 'science', 'social')
	def onchange_subject(self):
		if self.tamil > 100:
			raise Warning(_('Error!'),_('Given value %s is more than 100.') %(self.tamil))
		if self.english > 100:
			raise Warning(_('Error!'),_('Given value %s is more than 100.') %(self.english))
		if self.maths > 100:
			raise Warning(_('Error!'),_('Given value %s is more than 100.') %(self.maths))
		if self.science > 100:
			raise Warning(_('Error!'),_('Given value %s is more than 100.') %(self.science))
		if self.social > 100:
			raise Warning(_('Error!'),_('Given value %s is more than 100.') %(self.social))
	
	@api.one
	@api.depends('total')
	def _avg(self):
		avg = 0.00
		if self.total:
			avg = float(self.total) / 5
			self.avg = avg
	
	@api.one
	@api.constrains('name', 'student_id')
	def _check_description(self):
		if self.name == self.student_id:
			raise ValidationError("Name and ID must be different")
	
	@api.one
	def _get_class(self):
		if self.total > 100:
			self.s_class = 'Fourth class'
	
	@api.one
	def _get_number(self):
		for record in self:
			count = 0
			for time_ids in record.time_table_ids:
				if time_ids.id:
					count += 1
			if count:
				self.no_of_hours = count
			
	student_id = fields.Char("Student ID", required=True)
	name = fields.Char("Name", required=True)
	gender = fields.Selection(GENDER, "Gender")
	year_id = fields.Many2one('standared.standared','Standared')
	section_id = fields.Many2one('section.section', 'Section')
	tamil = fields.Float('Tamil',  digits_compute=dp.get_precision('Student'))
	english = fields.Integer('English')
	maths = fields.Integer('Maths')
	science = fields.Integer('Science')
	social = fields.Integer('Social')
	total = fields.Integer(compute='_total', string='Total', readonly=True)
	avg = fields.Float(compute='_avg', string='Avg', readonly=True)
	s_class = fields.Char(compute="_get_class", string='Class')
	syllabus_ids = fields.Many2many('teacher.syllabus','syllabus_rel','student_id','syllabus_id','Syllabus')
	time_table_ids = fields.One2many('time.table', 'student_id', 'Time table')
	no_of_hours = fields.Integer(compute="_get_number", string="Total of Hours")
	url = fields.Char('URL')
	state = fields.Selection(STATE, 'State', default='draft')
	duration = fields.Integer('DUration')
	start_date = fields.Date('Start Date')
	_sql_constraints = [('student_id_uniq', 'unique(student_id)', 'Student ID already exists!')]
	
	@api.model
	def create(self, vals):
		if vals.get('tamil'):
			if vals.get('tamil') > 100:
				raise Warning(_('Error!'),_('Given value is more than 100.'))
		return super(Student_Student, self).create(vals)
	
	@api.multi
	def write(self, vals):
		if not vals.get('gender'):
			vals.update({'gender':'male'})
		return super(Student_Student, self).write(vals)
	
#	@api.model
#	def name_get(self):
#		reads = self.read(['student_id','name'])
#		res = []
#		for record in reads:   
#			name = record['name']
#			if record['student_id']:
#				name = record['student_id']+' - '+ name
#			res.append((record['id'], name))
#		return res
	
class Section_Section(models.Model):
	_name = "section.section"

	name = fields.Char("Section")
	syllabus_code = fields.Integer('Code')
			
class Standared_Standared(models.Model):
	_name = "standared.standared"
	
	name = fields.Char('Standared')
	
class Time_Table(models.Model):
	_name = "time.table"
	
	is_check = fields.Boolean('Check')
	student_id = fields.Many2one('student.student', 'Teacher')
	serial_no = fields.Integer('#')
	standared_id = fields.Many2one('standared.standared', 'Standared')
	subject_id = fields.Many2one('section.section', 'Subject')
	start_time = fields.Datetime('Start Time')
	end_time = fields.Datetime('End Time')
	is_verify = fields.Selection(VERIFIED, 'Verified?', readonly=True)
	
class Student_Studies(models.Model):
	_name = 'student.studies'
	
	
	@api.onchange('student_id')
	def onchange_other(self):
		if self.student_id.id:
			self.gender = self.student_id.gender
			self.year_id = self.student_id.year_id
			self.section_id = self.student_id.section_id
			self.tamil = self.student_id.tamil
			self.english = self.student_id.english
			self.maths = self.student_id.maths
			self.science = self.student_id.science
			self.social = self.student_id.social
			self.total = self.student_id.total
			self.avg = self.student_id.avg
			
	student_id = fields.Many2one('student.student', 'Student')
	gender = fields.Selection(GENDER, "Gender", readonly=True)
	year_id = fields.Many2one('standared.standared','Standared', readonly=True)
	section_id = fields.Many2one('section.section', 'Section', readonly=True)
	tamil = fields.Integer('Tamil', readonly=True)
	english = fields.Integer('English', readonly=True)
	maths = fields.Integer('Maths', readonly=True)
	science = fields.Integer('Science', readonly=True)
	social = fields.Integer('Social', readonly=True)
	total = fields.Integer('Total', readonly=True)
	avg = fields.Float('Avg', readonly=True)
	year = fields.Char('Current Year')
	description = fields.Text('Remarks')
	
	@api.model
	def create(self, vals):
		if vals.get('student_id'):
			student_id = vals.get('student_id')
			vals.update({'gender':self.env['student.student'].browse(student_id).gender})
			vals.update({'english':self.env['student.student'].browse(student_id).english})
		return super(Student_Studies, self).create(vals)