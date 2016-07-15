odoo.define('web_psit.backend', function (require) {
'use strict';

var core = require('web.core');
var Model = require('web.DataModel');
var ControlPanel = require('web.ControlPanel');
var _t = core._t;

ControlPanel.include({
	update: function(status, options) {
		var self = this;
		this._super.apply(this, arguments);
		
		if (!status.hidden) {
			new Model("res.users").call("get_store").then(function(data) {
				self.$('h4.oe_store_title').text(data);
			});
		}
    }
});

});