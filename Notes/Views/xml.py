Xpath in tree::
<xpath expr="//tree[@string='Attachments']" position="attributes">
	<attribute name="colors">orange:state=='request_review';green:type == 'binary'; blue:type =='url';</attribute>
</xpath>
#########################
lable and placeholder::

<label for="description" string="Description"/>
<field name="description" nolabel='1' placeholder='Description'/>
#########################

Create write one2many fields:::
(0, 0,  { values })    link to a new record that needs to be created with the given values dictionary
(1, ID, { values })    update the linked record with id = ID (write *values* on it)
(2, ID)                remove and delete the linked record with id = ID (calls unlink on ID, that will delete the object completely, and the link to it as well)
(3, ID)                cut the link to the linked record with id = ID (delete the relationship between the two objects but does not delete the target object itself)
(4, ID)                link to existing record with id = ID (adds a relationship)
(5)                    unlink all (like using (3,ID) for all linked records)
(6, 0, [IDs])          replace the list of linked IDs (like using (5) then (4,ID) for each ID in the list of IDs)
###


Try this Values, If the second.class obj has partner than one2many is created.

obj = self.browse(cr, uid, ids)[0]

if obj.partner_id:
    vals{
    'partner_id': obj.partner_id.id,
    'res_ids': [(0,0, {
                    'partner_id': obj.partner_id.id,   #give id of partner 
                    'first_id': obj.first_id.id   #give id of first
             })]
    }
    self.pool.get('first.class').create(cr, uid, vals)

##########
Create , write many2many fields:::

    For Many2many

    For a many2many field, a list of tuples is expected. Here is the list of tuple that are accepted, with the corresponding semantics

    (0, 0, { values }) link to a new record that needs to be created with the given values dictionary

    (1, ID, { values }) update the linked record with id = ID (write values on it)

    (2, ID) remove and delete the linked record with id = ID (calls unlink on ID, that will delete the object completely, and the link to it as well)

    (3, ID) cut the link to the linked record with id = ID (delete the relationship between the two objects but does not delete the target object itself)

    (4, ID) link to existing record with id = ID (adds a relationship)

    (5) unlink all (like using (3,ID) for all linked records)

    (6, 0, [IDs]) replace the list of linked IDs (like using (5) then (4,ID) for each ID in the list of IDs)

    Example: [(6, 0, [8, 5, 6, 4])] sets the many2many to ids [8, 5, 6, 4]

    And One2many :

    (0, 0, { values }) link to a new record that needs to be created with the given values dictionary

    (1, ID, { values }) update the linked record with id = ID (write values on it)

    (2, ID) remove and delete the linked record with id = ID (calls unlink on ID, that will delete the object completely, and the link to it as well)

    Example: [(0, 0, {'field_name':field_value_record1, ...}), (0, 0, {'field_name':field_value_record2, ...})]
############
Xml attributes important::
<group>
	<field name="material_id" options="{'no_create': True, 'no_open': True , 'always_reload': True}"
		attrs="{'required': [('all_material','=', False)], 'readonly': [('all_material','=', True)]}" context="{'get_name':1}" />
</group>
###########################
Generate total in report::

<td style="border: 1px solid black;text-align:center; width:10px;line-height: 2em;">
	<t t-set="total" t-value="0" />
		<t t-foreach="o.supplier_transaction_ids" t-as="line">
			<t t-set="total" t-value="total+line.quantity_total_receipt" />
				<t t-if="line_last">
					<t t-esc="total" />
			</t>
		</t>
</td>
#####################
To Round the total::
<t t-esc="round(total, 1)" />

 OR

<td style="border: 1px solid black;text-align:right; width:10px;line-height: 2em;">
	<t t-set="total" t-value="0" />
	<t t-foreach="o.supplier_summary_ids" t-as="line">
		<t t-set="total" t-value="total+line.quantity_returned" />
			<t t-if="line_last">
			  <t t-esc="'{0:,.2f}'.format(round(total, 1))" />
		</t>
	</t>
</td>
##############
Attrs Conditions:::

This gives a overview:

List of Domain operators: ! (Not), | (Or), & (And)

List of Term operators: '=', '!=', '<=', '<', '>', '>=', '=?', '=like', '=ilike', 'like', 'not like', 'ilike', 'not ilike', 'in', 'not in', 'child_of'

Usage:

Input records:

Record 1: Openerp

Record 2: openerp

Record 3: Opensource

Record 4: opensource

Record 5: Open

Record 6: open

Record 7: Odoo

Record 8: odoo

Record 9: Odooopenerp

Record 10: OdooOpenerp

'like': [('input', 'like', 'open')] - Returns case sensitive (wildcards - '%open%') search.

O/p: open, opensource, openerp, Odooopenerp

'not like': [('input', 'not like', 'open')] - Returns results not matched with case sensitive (wildcards - '%open%') search.

O/p: Openerp, Opensource, Open, Odoo, odoo, OdooOpenerp

'=like': [('name', '=like', 'open')] - Returns exact (= 'open') case sensitive search.

O/p: open

'ilike': [('name', 'ilike', 'open')] - Returns exact case insensitive (wildcards - '%open%') search.

O/p: Openerp, openerp, Opensource, opensource, Open, open, Odooopenerp, OdooOpenerp

'not ilike': [('name', 'not ilike', 'open')] - Returns results not matched with exact case insensitive (wildcards - '%open%') search.

O/p: Odoo, odoo

'=ilike': [('name', '=ilike', 'open')] - Returns exact (= 'open' or 'Open') case insensitive search.

O/p: Open, open

'=?':

name = 'odoo' parent_id = False [('name', 'like', name), ('parent_id', '=?', parent_id)] - Returns name domain result & True

name = 'odoo' parent_id = 'openerp' [('name', 'like', name), ('parent_id', '=?', parent_id)] - Returns name domain result & parent_id domain result

'=?' is a short-circuit that makes the term TRUE if right is None or False, '=?' behaves like '=' in other cases

'in': [('value1', 'in', ['value1', 'value2'])] - in operator will check the value1 is present or not in list of right term

'not in': [('value1', 'not in', ['value2'])] - not in operator will check the value1 is not present in list of right term While these 'in' and 'not in' works with list/tuple of values, the latter '=' and '!=' works with string

'=': value = 10 [('value','=',value)] - term left side has 10 in db and term right our value 10 will match

'!=': value = 15 [('value','!=',value)] - term left side has 10 in db and term right our value 10 will not match

'child_of': parent_id = '1' #Agrolait 'child_of': [('partner_id', 'child_of', parent_id)] - return left and right list of partner_id for given parent_id

'<=', '<', '>', '>=': These operators are largely used in openerp for comparing dates - [('date', '>=', date_begin), ('date', '<=', date_end)]. You can use these operators to compare int or float also.

####################################
Scheduler::::

<?xml version="1.0" encoding="utf-8"?>
<openerp>
	<data>
		
		<!-- Scheduler for Updating country STD Code-->
		<record forcecreate="True" id="update_country_std_code_action" model="ir.cron">
			<field name="name">Update Country STD Code</field>
			<field eval="True" name="active" />
			<field name="user_id" ref="base.user_root" />
			<field name="interval_number">1</field>
			<field name="interval_type">minutes</field>
			<field name="numbercall">-1</field>
			<field eval="False" name="doall" />
			<field eval="'bank.bank.details'" name="model" />
			<field eval="'update_phone_number'" name="function" />
			<field eval="'(False,)'" name="args" />
		</record>
		
	</data>
</openerp>
#########################
Hide using xpath attributes condition::
<xpath expr="//header/button[@name='view_picking']" position="attributes">
 <attribute name="attrs">{'invisible': [('dropship','=', True)]}</attribute>
</xpath>
#############
attrs Format:
attrs = "{'invisible':[('field1', '=', condition)]}"
#######################
Remove label using xpath::
<xpath expr="//label[@for='address3']" position="before">
<label for="address2"/>
	<field  name="address2"/>       
</xpath>
css and js path::

<template id="assets_backend_psit_custom_design" inherit_id="web.assets_backend">
	<xpath expr="." position="inside">
		<link rel="stylesheet" href="/real_estate/static/src/css/sp.css"/>
		<script type="text/javascript" src="/real_estate/static/src/js/sp.js"></script>
	</xpath>
</template> 
####################
Total in one2many field:;

<t t-set="colcount" t-value="0" />
	<t t-foreach="hourly_report(data['form'])" t-as="line">
		<t t-set="colcount" t-value="colcount +line['total']" />
	</t>
	<t t-esc="colcount" />
############################	
call another view from button and filter the data::
Button::

<button class="oe_stat_button" name="%(account.action_invoice_tree1)d" type="action" icon="fa-money" context="{'search_default_booking_id': active_id}" >
	<field name="total_invoice_count" widget="statinfo" string="Invoice" />
</button>
###########################
Search required field in other view::

<record id="view_account_invoice_filter_inherited_real_estate" model="ir.ui.view">
	<field name="name">account.invoice.select.inherited.real.estate</field>
	<field name="model">account.invoice</field>
	<field name="inherit_id" ref="account.view_account_invoice_filter" />
	<field name="arch" type="xml">
		<xpath expr="//filter[@name='group_by_partner_id']" position="before">
			<filter string="Project" context="{'group_by':'construction_id'}"/>
			<filter string="Block" context="{'group_by':'block_id'}"/>
			<filter string="Customer" context="{'group_by':'partner_id'}"/>
		</xpath>
		<xpath expr="//field[@name='number']" position="after">
			<field name="booking_id" string="Booking Number"/>
		</xpath>
	</field>
</record>
#################
Pass one2many field value in context::

<xpath expr="//field[@name='purchase_ids']" position="attributes">
	<attribute name="context">{'purchase_ids': line_ids}</attribute>
</xpath>
#############
OPTIONS::
Place Radio button in horizontal::
options="{'horizontal': true}"
options="{'no_create': True, 'no_open': True}"
options="{'reload_whole_on_button': true}"
options='{"always_reload": True}'
options='{"preview_image": "image_medium"}'
options='{"terminology": "active"}'
options="{'tz_offset_field': 'tz_offset'}"
options="{'model_field': 'model'}"
options="{'currency_field': 'company_currency'}"
options="{'style-inline': true}"
options='{"thread_level": 1}'
<field name="user_domain" widget="char_domain" options="{'model': 'res.users'}" />
options="{&quot;no_open&quot;: True}"
<button name="toggle_payslip_status" field_name="payslip_status" type="object"
                        widget="toggle_button" options='{"active": "Reported in last payslips", "inactive": "To Report in Payslip"}'/>
options="{'preview_image': 'image_medium', 'size': [90, 90]}"
options='{"safe": True}'
##########
Call action view through button::
<button name="%(action name)d" type="action" string="string Name" class="oe_highlight"/>
#########
Call Python method through button::
<button name="method_name" type="object"  string="string Name" class="oe_highlight"/>
############
Attribute Conditions::
attrs condition for one2many field:
attrs="{'invisible':[('interstore_details_ids', '=', [])]}"
for many2many::
attrs="{'invisible': [('pony_ids', '=', [(6, False, [])])]}"
For many2one::
attrs="{'invisible': [(' autre_id ', '=', 'False')]}"
other for one2many::
[('pony_ids', '=', False)]
[('pony_ids', '=', None)]
[('pony_ids', '=', [])]
############
Open paticular view for 
<field name="client_id" context="{'form_view_ref':'scms.sands_view_partner_form'}"/>
#########
Apply Style in xpath::
<xpath expr="//group" position="attributes">
	<attribute name="style">background-color: red</attribute>
</xpath>
#################
<!-- Scheduler for calculating foder size -->
		<record forcecreate="True" id="ir_knowspace_calculatesize_action" model="ir.cron">
			<field name="name">Knowspace Folder size Scheduler</field>
			<field eval="True" name="active" />
			<field name="user_id" ref="base.user_root" />
			<field name="interval_number">30</field>
			<field name="interval_type">minutes</field>
			<field name="numbercall">-1</field>
			<field eval="False" name="doall" />
			<field eval="'ir.attachment'" name="model" />
			<field eval="'update_idle_days'" name="function" />
			<field eval="'(False,)'" name="args" />
		</record>
@api.multi
def update_idle_days(self):
	emp_ids = self.env['hr.employee'].search([('current_pro_to_date', '!=', False)])
	for emp_id in emp_ids:
		current_date = date.today()
		d1 = datetime.strptime(emp_id.current_pro_to_date, "%Y-%m-%d")
		d2 = datetime.strptime(str(current_date), "%Y-%m-%d") 
		days_count = str((d2 - d1).days)
		emp_id.write({'idle_days': days_count})
##############
Visible button only edit mode::
class="oe_edit_only"
##################33
Move the button to the corner::
<div class="oe_right oe_button_box">
     <!-- Buttons -->
</div>
#############
Pass value through context in act window:

<field name="context">{'nosave': '1', 'nodiscard': '1'}</field>

Search Default via button::
<button class="oe_stat_button"
	name="%(real_estate.product_product_unit_action)d" context="{'search_default_product_tmpl_id': active_id}"
	type="action" icon="fa-money">
	<field name="sm_total_cost" widget="statinfo" string="Cost" />
</button>

<record id="cleaning_industry_project_team_view_search"
	model="ir.ui.view">
	<field name="name">project.employee.allocate.search</field>
	<field name="model">project.employee.allocate</field>
	<field name="arch" type="xml">
		<search>
			<field name="employee_id" string="Employee" />
			<field name="clean_project_line_id" string="Task"/>
			<group expand="0" string="Group By">
				<filter string="Team" domain="[]" context="{'group_by':'clean_project_line_id'}" />
			</group>
		</search>
	</field>
</record>

<record id="cleaning_industry_project_team_action" model="ir.actions.act_window">
	<field name="name">Project Team</field>
	<field name="res_model">project.employee.allocate</field>
	<field name="view_type">form</field>
	<field name="view_mode">tree,form</field>
	<field name="search_view_id" ref="cleaning_industry_project_team_view_search" />
	<field name="context">{}</field>
	<field name="view_ids"
		eval="[(5, 0, 0),
				  (0, 0, {'view_mode': 'tree', 'view_id': ref('cleaning_industry_project_team_view_tree')}),
				  (0, 0, {'view_mode': 'form', 'view_id': ref('cleaning_industry_project_team_view_form')})]" />
</record>
###########
Domain in many2many field::]
<field name="employee_ids" domain="[('project_id', '=', False)]"/>
#########################
Format date in Odoo 8 QWeb:::

<span t-field="o.date_order" t-field-options='{"format": "d MMMM y"}'/>

also use this code

<span t-field="o.date_order" t-field-options="{&quot;format&quot;: &quot;yyyy-MM-dd&quot;}" />
