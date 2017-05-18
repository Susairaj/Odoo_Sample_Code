# -*- coding: utf-8 -*-
import base64

from openerp import SUPERUSER_ID
from openerp import http
from openerp.tools.translate import _
from openerp.http import request
from wtforms import Form, StringField, TextAreaField, validators
from openerp.http import Controller, route, request

from openerp.addons.website.models.website import slug


class website_freshers(http.Controller):
    @http.route(['/freshers'], type='http', auth="public", website=True)
    def freshers(self, **kwargs):
        env = request.env(context=dict(request.env.context, no_tag_br=True))
        Freshers = env['hr.applicant']
        # List jobs available to current UID
        fresher_ids = Freshers.search([]).ids
        # Browse jobs as superuser, because address is restricted
        freshers = Freshers.sudo().browse(fresher_ids)

        # Deduce departments and offices of those jobs
        name = set(n.name for n in freshers if n.name)

        # Render page
        return request.website.render("website_freshers.index", {
            'freshers': freshers,
            'name':name,
        })

    @http.route('/freshers/create/', type='http', auth="public", website=True)
    def freshers_apply(self, **form_data):
#        cr, uid, context, registry = request.cr, request.uid, request.context, request.registry
        values = {}
        return request.render("website_freshers.create", values)
    
    @http.route('/freshers/save', methods=['POST'], type='http', auth="public", website=True)
    def freshers_thankyou(self, **post):
        error = {}
        for field_name in ["name"]:
            if not post.get(field_name):
                error[field_name] = 'missing'
        if error:
            request.session['website_freshers_error'] = error
            request.session['website_freshers_default'] = post
            return request.redirect('/freshers/create/%s' % post.get("fresher_id"))

        # public user can't create applicants (duh)
        env = request.env(user=SUPERUSER_ID)
        value = {
            'name': '%s\'s Application' % post.get('partner_name'), 
        }
        
        username=post.pop('name', False)
        value['name'] = username
        value['partner_name']= post.pop('partner_name', False)
        value['email_from']=post.pop('email_from', False)
        value['partner_phone']= post.pop('partner_phone', False)
#        file=post['ufile']
        env['hr.applicant'].create(value).id
        
#        if file and partner_id:
#            attachment_value = {
#                'name': post['ufile'].filename,
#                'res_name': value['partner_name'],
#                'res_model': 'hr.applicant',
#                'res_id': partner_id,
#                'datas': base64.encodestring(post['ufile'].read()),
#                'datas_fname': post['ufile'].filename,
#            }
#            env['ir.attachment'].create(attachment_value)
        value={}
        value['name']= username
        value['active']= True
        value['login'] = post.pop('login', False)
        value['password']= post.pop('password', False)
        value['partner_id']=''
        env['res.users'].create(value).id
        
        return request.render("website_freshers.index", {})

    @http.route('/freshers/create_company/', type='http', auth="public", website=True)
    def company_apply(self, **form_data):
        cr, uid, context, registry = request.cr, request.uid, request.context, request.registry
        companies = request.env['res.partner']
        orm_country = registry.get('res.country')
        state_orm = registry.get('res.country.state')
        district_orm = registry.get('district.district')
        companies = companies.search([])     
        country_ids = orm_country.search(cr, SUPERUSER_ID, [], context=context)
        countries = orm_country.browse(cr, SUPERUSER_ID, country_ids, context)
        states_ids = state_orm.search(cr, SUPERUSER_ID, [], context=context)
        states = state_orm.browse(cr, SUPERUSER_ID, states_ids, context)
        district_ids = district_orm.search(cr, SUPERUSER_ID, [], context=context)
        districts = district_orm.browse(cr, SUPERUSER_ID, district_ids, context)
        
        values = {
            'countries': countries,
            'states': states,
            'districts': districts,
            'error': {},
        }
        
        return request.render("website_freshers.create_company", values)
        
    @http.route('/freshers/company_save', methods=['POST'], type='http', auth="public", website=True)
    def company_save(self, **post):
        error = {}
        for field_name in ["name"]:
            if not post.get(field_name):
                error[field_name] = 'missing'
        if error:
            request.session['website_freshers_error'] = error
            request.session['website_freshers_default'] = post
            return request.redirect('/freshers/create_company/%s' % post.get("fresher_id"))

        # public user can't create applicants (duh)
        env = request.env(user=SUPERUSER_ID)
        value = {
            'name': '%s\'s Application' % post.get('partner_name'), 
        }
        contact_value = {
            'type':'contact',
            'use_parent_address':True,
            'name': post.pop('contact_name'),
            'email': post.pop('contact_email'),
            'mobile': post.pop('contact_mobile'), 
        }
        username=post.pop('name', False)
        value['name'] = username
        value['street'] = post.pop('street', False)
        value['city'] = post.pop('city', False)
        value['phone'] = post.pop('phone', False)
        value['email'] = post.pop('email', False)
        value['district_id'] = post.pop('district_id', False)
        value['state_id'] = post.pop('state_id', False)
        value['country_id'] = post.pop('country_id', False)
        value['is_company'] = True
        value['child_ids'] = [(0,0,contact_value)]
        partner_id=env['res.partner'].create(value).id
        if partner_id:
            value={}
            value['name']= username
            value['active']= True
            value['login'] = post.pop('login', False)
            value['password']= post.pop('password', False)
            value['partner_id']=partner_id
            env['res.users'].create(value).id
        
        return request.render("website_freshers.index", {})

    @http.route('/freshers/create_college/', type='http', auth="public", website=True)
    def college_apply(self, **form_data):
        cr, uid, context, registry = request.cr, request.uid, request.context, request.registry
        colleges = request.env['res.partner']
        orm_country = registry.get('res.country')
        state_orm = registry.get('res.country.state')
        district_orm = registry.get('district.district')
        colleges = colleges.search([])
        country_ids = orm_country.search(cr, SUPERUSER_ID, [], context=context)
        countries = orm_country.browse(cr, SUPERUSER_ID, country_ids, context)
        states_ids = state_orm.search(cr, SUPERUSER_ID, [], context=context)
        states = state_orm.browse(cr, SUPERUSER_ID, states_ids, context)
        district_ids = district_orm.search(cr, SUPERUSER_ID, [], context=context)
        districts = district_orm.browse(cr, SUPERUSER_ID, district_ids, context)
        
        values = {
            'countries': countries,
            'states': states,
            'districts': districts,
        }
        return request.render("website_freshers.create_college", values)

    @http.route('/freshers/college_save', methods=['POST'], type='http', auth="public", website=True)
    def college_save(self, **post):
        error = {}
        for field_name in ["name"]:
            if not post.get(field_name):
                error[field_name] = 'missing'
        if error:
            request.session['website_freshers_error'] = error
            request.session['website_freshers_default'] = post
            return request.redirect('/freshers/create_college/%s' % post.get("fresher_id"))

        # public user can't create applicants (duh)
        env = request.env(user=SUPERUSER_ID)
        value = {
            'name': '%s\'s Application' % post.get('partner_name'),
        }
        username=post.pop('name', False)
        value['name'] = username
        value['email']= post.pop('email', False)
        value['mobile']= post.pop('mobile', False)
        value['country_id']= post.pop('country_id', False)
        value['state_id']= post.pop('state_id', False)
        value['street']= post.pop('street', False)
        value['city']= post.pop('city', False)
        value['accreditation']= post.pop('accreditation', False)
        value['year_of_establishemnt']= post.pop('year_of_establishemnt', False)
        value['avail_courses']= post.pop('avail_courses', False)
        value['college_dec']= post.pop('college_dec', False)
        value['about_management']= post.pop('about_management', False)
        value['is_college']=True
        partner_id=env['res.partner'].create(value).id
        if partner_id:
            value={}
            value['name']= username
            value['active']= True
            value['login'] = post.pop('login', False)
            value['password']= post.pop('password', False)
            value['partner_id']=partner_id
            env['res.users'].create(value).id
        return request.render("website_freshers.index", {})
    
# vim :et:
