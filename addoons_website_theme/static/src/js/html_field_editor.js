odoo.define('addoons_website_theme.html_field_editor', function(require) {

    'use strict';
    require('web.dom_ready');


    var base = require('web_editor.base');
    var session = require('web.session');

    base.ready().then(function(){
        //      per il text editor
        $('.summernote-html-editor').summernote({
            height:150,
            toolbar: [
              ['style', ['style']],
              ['font', ['bold', 'underline', 'clear']],
              ['fontname', ['fontname']],
              ['color', ['color']],
              ['para', ['ul', 'ol', 'paragraph']],
              ['table', ['table']],
              ['insert', ['link', 'picture', 'video']],
              ['view', ['fullscreen', 'help']],
            ]
        });
    });
});