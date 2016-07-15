openerp.web_left_panel = function(instance) {
	instance.web.WebClient.include({
		show_application: function() {
			var self = this;
			self.$(".show_panel_nav").hide();
			self.$(".hide_panel_nav").hide();
			self.$(".show_left_panel_nav").hide();
			self.$(".hide_left_panel_nav").show();
			
			this.$('.hide_left_panel_nav').mouseover(function(ev) {
				self.$(".show_left_panel_nav").hide();
				self.$(".hide_left_panel_nav").hide();
				self.$(".hide_panel_nav").show();
			});
			
			this.$('.show_left_panel_nav').mouseover(function(ev) {
				self.$(".hide_left_panel_nav").hide();
				self.$(".show_left_panel_nav").hide();
				self.$(".show_panel_nav").show();
			});

			this.$('.hide_panel_nav').click(function(ev) {
				self.$(".oe_leftbar").hide();
				self.$('.hide_left_panel_nav').hide();
				self.$('.show_left_panel_nav').show();
				self.$(".hide_panel_nav").hide();
			});
			
			this.$('.show_panel_nav').click(function(ev) {
				self.$(".oe_leftbar").show();
				self.$('.show_left_panel_nav').hide();
				self.$('.hide_left_panel_nav').show();
				self.$(".show_panel_nav").hide();
			});
			
			this._super.apply(this, arguments);
		},
	});
	
}
	
