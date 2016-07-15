odoo.define('Receivables', function (require) {
"use strict";

var data = require('web.data');
var ListView = require('web.ListView');

ListView.include({
        //Adding blue background color for tree view including one2many table.
        load_list: function(data) {
            var self = this;
            this._super(data);
            this.$el.find('tr.oe_list_header_columns').css({'background-color': '#337AB7' , 'color': '#F5F3F3'});
        },
		
    });
});