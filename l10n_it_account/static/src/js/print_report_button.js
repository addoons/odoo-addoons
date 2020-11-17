odoo.define('l10n_it_account.button_piano_dei_conti', function (require) {
"use strict";
var config = require('web.config');
var core = require('web.core');
var session = require('web.session');
var Widget = require('web.Widget');
var list_controller = require('web.ListController');

var QWeb = core.qweb;

list_controller.include({


    renderButtons: function ($node) {
        var self = this;
        if (!this.noLeaf && this.hasButtons) {
            this.$buttons = $(QWeb.render(this.buttons_template, {widget: this}));
            this.$buttons.on('click', '.o_list_button_add', this._onCreateRecord.bind(this));

            this._assignCreateKeyboardBehavior(this.$buttons.find('.o_list_button_add'));
            this.$buttons.find('.o_list_button_add').tooltip({
                delay: {show: 200, hide:0},
                title: function(){
                    return qweb.render('CreateButton.tooltip');
                },
                trigger: 'manual',
            });
            this.$buttons.on('click', '.o_list_button_discard', this._onDiscard.bind(this));

            /// aggiunta del bottone PIANO DEI CONTI durante il render
            if(this.modelName == 'account.account' && this.viewType == 'list'){
                this.$buttons.append('<button id="button_report_piano_conti" class="btn btn-primary btn-sm btn_piano_dei_conti" >stampa piano dei conti</button>');
                this.$buttons.on('click', '.btn_piano_dei_conti', function(){
                    var action = {
                        'type': 'ir.actions.report',
                        'report_type': 'qweb-pdf',
                        'report_name': 'l10n_it_account.report_cof?docids=1&report_type=qweb-pdf',
                        'report_file': 'l10n_it_account.report_cof',

                    };
                    return self.do_action(action);
                });
            }

            this.$buttons.appendTo($node);
        }
    },

});

});