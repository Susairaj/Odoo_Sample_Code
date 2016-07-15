/* -----------------------------------------------------------\ 
 * web functions for web_hide_buttons
 * --------------------------------------------------------- */

/* comments to control jslint */
/*jslint nomen: true, white: true, */
/*global window, openerp, $, _ */

odoo.define('web_hide_buttons', function (require) {
"use strict";

var data = require('web.data');
var FormView = require('web.FormView');

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
});