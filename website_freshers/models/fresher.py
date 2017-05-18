# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

class hr_applicant(osv.osv):
    _name = 'hr.applicant'
    _inherit = ['hr.applicant']

    def _website_url(self, cr, uid, ids, field_name, arg, context=None):
        res = dict.fromkeys(ids, '')
        for job in self.browse(cr, uid, ids, context=context):
            res[job.id] = "/freshers/detail/%s" % job.id
        return res

    def job_open(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, {'website_published': False}, context=context)
        return super(hr_applicant, self).job_open(cr, uid, ids, context)

    _columns = {
        'website_published': fields.boolean('Published', copy=False),
        'website_description': fields.html('Website description'),
        'website_url': fields.function(_website_url, string="Website URL", type="char"),
    }
    _defaults = {
        'website_published': False
    }

class district_district(osv.osv):
    _description = 'District'
    _name = 'district.district'

    _columns = {
        'name': fields.char('Name', copy=False),
    }
    
class res_partner(osv.osv):
    _description = 'Partner'
    _name = 'res.partner'
    _inherit = ['res.partner']

    _columns = {
        'is_college':fields.boolean('Is_college?'),
        'district_id': fields.many2one('district.district','District'),
        'contact_name':fields.char('Contact Person Name'),
        'contact_email':fields.char('Contact Person Email'),
        'contact_mobile':fields.char('Contact Person Mobile'),
        'login':fields.char('AdminUserName'),
        'password':fields.char('AdminPassword'),
        'confirm':fields.char('ConfirmAdminPassword'),
        'dob': fields.date('DOB', required=True),
        'gender':fields.selection([('male', 'Male'),('female', 'Female')],'Gender'),
        
        'accreditation':fields.char('Accreditation Details'),
        'year_of_establishemnt':fields.char('Year of Establishment'),
        'avail_courses':fields.char('Courses Available'),
        'college_dec':fields.char('Description about College'),
        'about_management':fields.char('About Management'),
        
        
    }
    
