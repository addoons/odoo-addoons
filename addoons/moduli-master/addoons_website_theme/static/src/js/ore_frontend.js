odoo.define('addoons_website_theme.ore_frontend', function(require) {

    'use strict';

    var rpc = require('web.rpc');
    var base = require('web_editor.base');
    var session = require('web.session');
    base.ready().then(function(){
        $('.ore_sv').html(0);
        $('.ore_fc').html(0);
        rpc.query({
            model: 'res.partner',
            method: 'get_ore_disponibili',
            args: [{
                'user_id': session.user_id,//china export
            }],
        }).then(function (returned_value) {
            $('.ore_sv').html(returned_value['ore_sviluppo']);
            $('.ore_fc').html(returned_value['ore_formazione']);
        });
    });
});