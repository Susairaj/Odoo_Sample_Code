odoo.define('psit', function (require) {
"use strict";

var data = require('web.data');
var FormView = require('web.FormView');
var ListView = require('web.ListView');
var core = require('web.core');
var _t = core._t;

FormView.include({
	toggle_buttons: function() {
			var view_mode = this.get("actual_mode") === "view";
			var self = this;
			if (this.$buttons) {
				if (self.dataset.context.nosave) {
					this.$buttons.find('.o_form_buttons_view').toggle(view_mode).hide();
					this.$buttons.find('.o_form_buttons_edit').toggle(view_mode).hide();
				}
				if (self.dataset.context.nodiscard) {
					this.$buttons.find('.o_form_buttons_view').toggle(view_mode).hide();
					this.$buttons.find('.o_form_buttons_edit').toggle(view_mode).hide();
				}
				else{
					this.$buttons.find('.o_form_buttons_view').toggle(view_mode);
					this.$buttons.find('.o_form_buttons_edit').toggle(!view_mode);
				}
			}
		}
		
	});
ListView.include({
        //Add multi header
        load_list: function(data) {
            var self = this;
            this._super(data);
            if (self.model == "transaction.summary") {
                if (this.fields_view.arch.attrs.class == 'psit_multi_header') {
					this.$el.find(".oe_list_content > thead:first").after('<tr> \
								<th style="border-left: 1px solid #DFE1E6; background-color:#337AB7; color:#F5F3F3; text-align:center;"> Supplier </th>\
								<th style="border-left: 1px solid #DFE1E6;  background-color:#337AB7; color:#F5F3F3; text-align:center;"> Inter store </th>\
								<th style="border-left: 1px solid #DFE1E6;  background-color:#337AB7; color:#F5F3F3; text-align:center;"> Contractor returns </th>\
								<th style="border-left: 1px solid #DFE1E6; background-color:#337AB7; color:#F5F3F3; text-align:center;"> Total Receipts </th>\
								<th style="border-left: 1px solid #DFE1E6;  background-color:#337AB7; color:#F5F3F3; text-align:center;"> Contractors </th>\
								<th style="border-left: 1px solid #DFE1E6;  background-color:#337AB7; color:#F5F3F3; text-align:center;"> Inter store </th>\
								<th style="border-left: 1px solid #DFE1E6;  background-color:#337AB7; color:#F5F3F3; text-align:center;"> Supply Return </th>\
								<th style="border-left: 1px solid #DFE1E6;  background-color:#337AB7; color:#F5F3F3; text-align:center;"> Total Issues </th>\
								</tr>');
                }
                if (this.fields_view.arch.attrs.class == 'psit_multi_header') {
                   this.$el.find(".oe_list_content > thead:first").replaceWith('<tr class="oe_list_header_columns"> \
								<th rowspan="2" style="border-left: 1px solid #DFE1E6; background-color:#337AB7; color:#F5F3F3; text-align:center;"><div>SL.NO.<div></th> \
								<th rowspan="2" style="border-left: 1px solid #DFE1E6; background-color:#337AB7; color:#F5F3F3; text-align:center;"><div>Material Code<div></th> \
								<th rowspan="2" style="border-left: 1px solid #DFE1E6; background-color:#337AB7; color:#F5F3F3; text-align:center;"><div>Material Name<div></th> \
								<th rowspan="2" style="border-left: 1px solid #DFE1E6; background-color:#337AB7; color:#F5F3F3; text-align:center;"><div>UOM<div></th> \
								<th rowspan="2" style="border-left: 1px solid #DFE1E6; background-color:#337AB7; color:#F5F3F3; text-align:center;"><div>Opening stock<div></th> \
								<th colspan="4" style="border-left: 1px solid #DFE1E6; border-bottom:1pt solid #ffffff; background-color:#337AB7; color:#F5F3F3; text-align:center;"><div>Receipts<div></th> \
								<th colspan="4" style="border-left: 1px solid #DFE1E6; border-bottom:1pt solid #ffffff; background-color:#337AB7; color:#F5F3F3; text-align:center;"><div>Issues<div></th> \
								<th rowspan="2" style="border-left: 1px solid #DFE1E6; background-color:#337AB7; color:#F5F3F3; text-align:center;"><div>Closing Stock<div></th> \
								<th rowspan="2" style="border-left: 1px solid #DFE1E6; background-color:#337AB7; color:#F5F3F3; text-align:center;"><div>Total Cumulative receipt from supplier<div></th> \
								<th rowspan="2" style="border-left: 1px solid #DFE1E6; background-color:#337AB7; color:#F5F3F3; text-align:center;"><div>Total Cumulative issued to contractor<div></th> \
								<th rowspan="2" style="border-left: 1px solid #DFE1E6; background-color:#337AB7; color:#F5F3F3; text-align:center;"><div>Remarks<div></th> \
								</tr>');
                }
            
            }
        },
		configure_pager: function (dataset) {
			this.dataset.ids = dataset.ids;
			// Not exactly clean
			if (dataset._length) {
				this.dataset._length = dataset._length;
			}
			if (this.$pager) {
				if (this.grouped) {
					if (this.dataset.context.noselection == 1) {
							this.$('.oe_list_record_selector').hide();
							this.$('table.oe_list_content th:eq(1)').hide();
						}
					// page count is irrelevant on grouped page, replace by limit
					this.$pager.find('.oe-pager-buttons').hide();
					this.$pager.find('.oe_list_pager_state').text(this._limit || '∞');
				} else {
					if (this.dataset.context.noselection == 1) {
							this.$('.oe_list_record_selector').hide();
							this.$('table.oe_list_content th:eq(1)').hide();
						}
					var total = dataset.size();
					var limit = this._limit || total;
					this.$pager.find('.oe-pager-buttons').toggle(total > limit);
					this.$pager.find('.oe_pager_value').toggle(total !== 0);
					var spager = '-';
					if (total) {
						var range_start = this.page * limit + 1;
						var range_stop = range_start - 1 + limit;
						if (this.records.length) {
							range_stop = range_start - 1 + this.records.length;
						}
						if (range_stop > total) {
							range_stop = total;
						}
						spager = _.str.sprintf(_t("%d-%d of %d"), range_start, range_stop, total);
					}

					this.$pager.find('.oe_list_pager_state').text(spager);
				}
			}
		}
    });
});