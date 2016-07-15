odoo.define('web_debranding.dialog', function(require) {
    var core = require('web.core');
    var QWeb = core.qweb;
    var _t = core._t;

    var CrashManager = require('web.CrashManager')
    CrashManager.include({
    	show_warning: function(error) {
            if (!this.active) {
                return;
            }
            new Dialog(this, {
                size: 'medium',
                title: "CristO " + (_.str.capitalize(error.type) || _t("Warning")),
                subtitle: error.data.title,
                $content: $('<div>').html(QWeb.render('CrashManager.warning', {error: error}))
            }).open();
        },
        show_error: function(error) {
            if (!this.active) {
                return;
            }
            new Dialog(this, {
                title: "CristO " + _.str.capitalize(error.type),
                $content: QWeb.render('CrashManager.error', {session: session, error: error})
            }).open();
        },
    });

    var Dialog = require('web.Dialog')
    Dialog.include({
    	init: function (parent, options) {
            this._super(parent);

            options = _.defaults(options || {}, {
                title: _t('CristO'), subtitle: '',
                size: 'large',
                dialogClass: '',
                $content: false,
                buttons: [{text: _t("Ok"), close: true}]
            });

            this.$content = options.$content;

            this.title = options.title;
            this.subtitle = options.subtitle;
            this.$modal = $(QWeb.render('Dialog', {title: this.title, subtitle: this.subtitle}));

            switch(options.size) {
                case 'large':
                    this.$modal.find('.modal-dialog').addClass('modal-lg');
                    break;
                case 'small':
                    this.$modal.find('.modal-dialog').addClass('modal-sm');
                    break;
            }

            this.dialogClass = options.dialogClass;
            this.$footer = this.$modal.find(".modal-footer");

            this.set_buttons(options.buttons);
            
            this.$modal.on('hidden.bs.modal', _.bind(this.destroy, this));
        },
    }); 
});
