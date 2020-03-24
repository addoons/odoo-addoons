odoo.define('addoons_website_theme.analysis_graph', function(require) {

    'use strict';
    require('web.dom_ready');

    var rpc = require('web.rpc');
    var base = require('web_editor.base');
    var session = require('web.session');

    base.ready().then(function(){
        var mesi = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio",
                        "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"];

//      Creo i due grafici vuoti assegnandoli a due variabili
        if (document.getElementById("grafico-fatture")){

            var barre = new Chart(document.getElementById("grafico-fatture"), {
                type: 'bar',
                data: {
                    labels: mesi,
                    datasets: [
                        {
                            label: "Fatturato in €",
                            backgroundColor: ["#875A7B", "#875A7B","#875A7B","#875A7B","#875A7B","#875A7B", "#875A7B","#875A7B","#875A7B","#875A7B", "#875A7B", "#875A7B"],
                            data: [0,0,0,0,0,0,0,0,0,0,0,0],
                        }
                    ]
                },

            });
            var linee = new Chart(document.getElementById("grafico-task"), {
                type: 'line',
                data: {
                    labels: mesi,
                    datasets: [{
                        data: [0,0,0,0,0,0,0,0,0,0,0,0],
                        label: "Task aperte",
                        borderColor: "#875A7B",
                        backgroundColor: "#875A7B",

                        fill: false
                    },{
                        data: [0,0,0,0,0,0,0,0,0,0,0,0],
                        label: "Task chiuse",
                        borderColor: "#00A09D",
                        backgroundColor: "#00A09D",
                        fill: false
                    }]
                },
            });
        }

//      Onchange textbox anno
        $('#graph-year').change(function () {

            var self = this;
            if (this.value < 2017 || this.value > 2021){
                this.value = 2020;
            }
            rpc.query({
            model: 'res.partner',
            method: 'get_analysis_graph_data',
            args: [{
                'user_id': session.user_id,
                'year': parseInt(this.value),
            }],
            }).then(function (data) {
//              distruggo i grafici precendenti ogni volta che cambia l'anno
                linee.destroy();
                barre.destroy();

//              popolo i grafici con i nuovi dati
                barre = new Chart(document.getElementById("grafico-fatture"), {
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
                            text: 'Fatturato ' + self.value,
                        }
                    }
                });
                linee = new Chart(document.getElementById("grafico-task"), {
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

//      triggero l'onchange per la prima volta che entro nella pagina
        $('#graph-year').trigger('change');

    });
});