odoo.define('addoons_website_theme.analysis_graph', function(require) {

    'use strict';

    var rpc = require('web.rpc');
    var base = require('web_editor.base');
    var session = require('web.session');
    base.ready().then(function(){
        var mesi = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio",
                        "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"];

        rpc.query({
            model: 'res.partner',
            method: 'get_analysis_graph_data',
            args: [{
                'user_id': session.user_id,
                'year': 2020,
            }],
        }).then(function (data) {
            new Chart(document.getElementById("grafico-fatture"), {
                type: 'bar',
                data: {
                    labels: mesi,
                    datasets: [
                        {
                            label: "Fatturato in €",
                            backgroundColor: ["#875A7B", "#875A7B","#875A7B","#875A7B","#875A7B","#875A7B", "#875A7B","#875A7B","#875A7B","#875A7B", "#875A7B", "#875A7B"],
                            data: data['fatturato'],
                        }
                    ]
                },
                options: {
                    legend: { display: false },
                    title: {
                        display: true,
                        text: 'Fatturato 2020'
                    }
                }
            });
            new Chart(document.getElementById("grafico-task"), {
                type: 'line',
                data: {
                    labels: mesi,
                    datasets: [{
                        data: data['task_aperte'],
                        label: "Task aperte",
                        borderColor: "#875A7B",
                        backgroundColor: "#875A7B",

                        fill: false
                    },{
                        data: data['task_completate'],
                        label: "Task chiuse",
                        borderColor: "#00A09D",
                        backgroundColor: "#00A09D",
                        fill: false
                    }]
                },
                options: {
                    title: {
                        display: true,
                        text: 'Task'
                    },
                    tooltips: {
                        mode: 'index',
                        intersect: false,
                    },
                    hover: {
                        mode: 'nearest',
                        intersect: true
                    },
                }
            });
        });
    });
});