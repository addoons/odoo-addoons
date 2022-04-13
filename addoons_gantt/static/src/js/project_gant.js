odoo.define('addoons_gantt.project_gant', function (require) {
    "use strict";
    var core = require('web.core');
    var session = require('web.session');
    var ajax = require('web.ajax');
    var AbstractAction = require('web.AbstractAction');
    var ControlPanelMixin = require('web.ControlPanelMixin');
    var data = require('web.data');
    var SearchView = require('web.SearchView');
    var rpc = require('web.rpc');
    var pyUtils = require('web.py_utils');
    var QWeb = core.qweb;


    var _t = core._t;
    var _lt = core._lt;

    var ProjectGant = AbstractAction.extend(ControlPanelMixin, {
        events: {
        },

         init: function (parent, action) {
            this._super.apply(this, arguments);
            this.action = action;
            this.set('title', action.name || _t('Gant view'));
            this.project_ids = [];
            this.initialized = false;
            gantt.eachSuccessor = function(callback, root){
              if(!this.isTaskExists(root))
                return;

              // remember tasks we've already iterated in order to avoid infinite loops
              var traversedTasks = arguments[2] || {};
              if(traversedTasks[root])
                return;
              traversedTasks[root] = true;

              var rootTask = this.getTask(root);
              var links = rootTask.$source;
              if(links){
                for(var i=0; i < links.length; i++){
                  var link = this.getLink(links[i]);
                  if(this.isTaskExists(link.target) && !traversedTasks[link.target]){
                    callback.call(this, this.getTask(link.target));

                    // iterate the whole branch, not only first-level dependencies
                    this.eachSuccessor(callback, link.target, traversedTasks);
                  }
                }
              }
            };

        },
        do_show: function () {
            this._super.apply(this, arguments);
            this.searchview.do_search();
            this.action_manager.do_push_state({
                action: this.action.id,
                active_id: this.action.context.active_id,
            });
        },

        /*
        * carica i fields per la search view
        */
        willStart: function () {
            var self = this;
            var view_id = this.action && this.action.search_view_id && this.action.search_view_id[0];
            var def = this
                .loadViews('project.task', this.action.context || {}, [[view_id, 'search']])
                .then(function (result) {
                    self.fields_view = result.search;
                });
            return $.when(this._super(), def);
        },
        start: function () {
            var self = this;

            // find default search from context
            var search_defaults = {};
            var context = this.action.context || [];
            _.each(context, function (value, key) {
                var match = /^search_default_(.*)$/.exec(key);
                if (match) {
                    search_defaults[match[1]] = value;
                }
            });

            // create searchview
            var options = {
                $buttons: $("<div>"),
                action: this.action,
                disable_groupby: true,
                search_defaults: search_defaults,
            };

            var dataset = new data.DataSetSearch(this, 'project.task');
            this.searchview = new SearchView(this, dataset, this.fields_view, options);
            this.searchview.on('search', this, this._onSearch);

            var def1 = this._super.apply(this, arguments);
            var def2 = this.searchview.appendTo($("<div>")).then(function () {
                self.$searchview_buttons = self.searchview.$buttons.contents();
            });

            return $.when(def1, def2).then(function(){
                self.searchview.do_search();
            });

        },


        /*
        * Funzione per prendere i dati da backend e popolare il grafico gantt
        *
        * @domain: domain della searchview
        */
        loadGanttData: function (domain) {
            var self = this;
            rpc.query({
                model: 'project.project',
                method: 'get_data',
                kwargs: {
                    'domain': domain
                }
            }).then(function(result){
                if(self.initialized === false){
                    // renderizzo il template QWeb e inizializzo il gantt
                    var vista_gantt = QWeb.render( 'addoons_project_gant', {});
                    $(vista_gantt).prependTo(self.$el);
                    if(gantt.config.date_format !== "%Y-%m-%d %H:%i"){
                        self.set_gantt_configurations();
                    }
                    gantt.init("gantt-graph", "2020-01-01", "2022-01-01");
                    self.initialized = true;
                }
                // una volta inizializzato pulisco e ripopolo il gantt con i dati presi da backend
                gantt.clearAll();
                gantt.addMarker({
                    start_date: new Date().setHours(0,0,0,0),
                    css: "today",
                    text: "Oggi",
                    title: "Oggi"
                });
                gantt.parse(result);

                // update del control panel, ovvero della searchview
                self._updateControlPanel([]);
            });
        },


        /*
        * in questa funzione vengono settate tutte le configurazioni e viene fatto il binding
        * tra gli eventi della gant e i suoi handler
        */
        set_gantt_configurations: function(){
            // aggiungo il plugin che permette di mettere il flag al giorno di oggi. e fare il drag sulla timeline
            gantt.plugins({
                marker: true,
                drag_timeline: true
            });
            gantt.config.date_format = "%Y-%m-%d %H:%i";

            // permette di spostare le task in alto o in basso
            gantt.config.order_branch = true;
	        gantt.config.order_branch_free = true;

            // larghezza grid
            gantt.config.grid_width = 800;

            // varie visualizzazioni: ora, giorno, mese, anno, settimana
            var zoomConfig = {
                levels: [
                    {
                        name:"hour",
                        scale_height: 50,
                        min_column_width: 20,
                        scales:[
                            {unit: "day", step: 1, format: "%d %M"},
                            {unit: "hour", step: 1, format: "%G"},
                        ],
                    },
                    {
                        name:"day",
                        scale_height: 27,
                        min_column_width:80,
                        scales:[
                            {unit: "day", step: 1, format: "%d %M"}
                        ]
                    },
                    {
                        name:"week",
                        scale_height: 50,
                        min_column_width:50,
                        scales:[
                            {unit: "week", step: 1, format: function (date) {
                                var dateToStr = gantt.date.date_to_str("%d %M");
                                var endDate = gantt.date.add(date, -6, "day");
                                var weekNum = gantt.date.date_to_str("%W")(date);
                                return "#" + weekNum + ", " + dateToStr(date) + " - " + dateToStr(endDate);
                            }},
                            {unit: "day", step: 1, format: "%j %D"}
                        ]
                    },
                    {
                        name:"month",
                        scale_height: 50,
                        min_column_width:120,
                        scales:[
                            {unit: "month", format: "%F, %Y"},
                            {unit: "week", format: "Week #%W"}
                        ]
                    },
                    {
                        name:"quarter",
                        height: 50,
                        min_column_width:90,
                        scales:[
                            {unit: "month", step: 1, format: "%M"},
                            {
                                unit: "quarter", step: 1, format: function (date) {
                                    var dateToStr = gantt.date.date_to_str("%M");
                                    var endDate = gantt.date.add(gantt.date.add(date, 3, "month"), -1, "day");
                                    return dateToStr(date) + " - " + dateToStr(endDate);
                                }
                            }
                        ]
                    },
                    {
                        name:"year",
                        scale_height: 50,
                        min_column_width: 30,
                        scales:[
                            {unit: "year", step: 1, format: "%Y"}
                        ]
                    }
                ]
            };

            // il default è visualizzazione giorno
            gantt.ext.zoom.init(zoomConfig);
            gantt.ext.zoom.setLevel("day");
//            gantt.ext.zoom.attachEvent("onAfterZoom", function(level, config){
//                document.querySelector(".gantt_radio[value='" +config.name+ "']").checked = true;
//            })

            // visualizza progetti in questi giorni
            gantt.templates.task_class = function (st, end, item) {
                return item.$level == 0 ? "gantt_project" : ""
            };
            gantt.config.wide_form = 1;

            // resize del della visualizzazione temporale: mese, settiman, giono, anno
            var radios = document.getElementsByName("scale");
            for (var i = 0; i < radios.length; i++) {
                radios[i].onclick = function (event) {
                    gantt.ext.zoom.setLevel(event.target.value);
                };
            }

            // handler eventi gantt
            gantt.attachEvent("onAfterTaskUpdate", this.updateTask);
            gantt.attachEvent("onAfterTaskDelete", this.deleteTask);
            gantt.attachEvent("onAfterTaskAdd", this.createTask);
            gantt.attachEvent("onAfterLinkAdd", this.createLink);
            gantt.attachEvent("onAfterLinkUpdate", this.updateLink);
            gantt.attachEvent("onAfterLinkDelete", this.deleteLink);


            gantt.attachEvent("onTaskDrag", function(id, mode, task, original){
              var modes = gantt.config.drag_mode;
              if(mode == modes.move){
                var diff = task.start_date - original.start_date;
                console.log(task.start_date);
                console.log(original.start_date);
                gantt.eachSuccessor(function(child){
                  child.start_date = new Date(+child.start_date + diff);
                  child.end_date = new Date(+child.end_date + diff);
                  gantt.refreshTask(child.id, true);
                },id );
              }
              return true;
            });
            gantt.attachEvent("onAfterTaskDrag", function(id, mode, e){
              var modes = gantt.config.drag_mode;
              if(mode == modes.move ){
                gantt.eachSuccessor(function(child){
                  child.start_date = gantt.roundDate(child.start_date);
                  child.end_date = gantt.calculateEndDate(child.start_date, child.duration);
                  gantt.updateTask(child.id);
                },id );
              }
            });
            gantt.attachEvent("onRowDragEnd", function(id, mode, e){
                gantt.updateTask(id);
            });
            // testo da mostrare per il progress della task
            gantt.templates.progress_text=function(start, end, task){ return "<span style='text-align:left;'>" + Math.round(task.progress * 100) + "% </span>";};
        },

        /*--------------------------------------*\
        |         GANT VIEW HANDLERS             |
        \*======================================*/
        updateTask: function(id, item){
            rpc.query({
                model: 'project.project',
                method: 'update_task',
                kwargs: {
                    'task': item
                }
            }).then(function (result) {
                if(result){
//                    gantt.message({text: "Task Aggiornata con successo", expire: 10});
                }
            });
        },
        createTask: function(id, item){
            rpc.query({
                model: 'project.project',
                method: 'create_task',
                kwargs: {
                    'task': item
                }
            }).then(function (result) {
                if(result){
                    gantt.deleteTask(item['id']);
                    gantt.message({text: "Task creata con successo", expire: 10});
                    rpc.query({
                        model: 'project.project',
                        method: 'get_data',
                    }).then(function(res){
                        gantt.parse(res)
                    });
                }
            });
            return false
        },
        deleteTask: function(id){
            rpc.query({
                model: 'project.project',
                method: 'delete_task',
                kwargs: {
                    'task_id': id
                }
            }).then(function (result) {

            });
        },
        createLink: function(id, item){
            rpc.query({
                model: 'project.project',
                method: 'create_link',
                kwargs: {
                    'link': item
                }
            }).then(function (result) {
//                gantt.message({text: "Link creato con successo", expire: 10});
            });
            return false
        },
        updateLink: function(id, item){
            rpc.query({
                model: 'project.project',
                method: 'update_link',
                kwargs: {
                    'link': item
                }
            }).then(function (result) {
//                gantt.message({text: "Link Aggiornato con successo", expire: 1000});
            });
            return false
        },
        deleteLink: function(id){
            rpc.query({
                model: 'project.project',
                method: 'delete_link',
                kwargs: {
                    'link_id': id
                }
            }).then(function (result) {

            });
            return false
        },


        /*
        *    Funzione che aggiorna il control panel e quindi va ad aggiornare e renderizzare la search view.
        *    Ll control panel è tutta la parte che si trova in alto e solitamente comprende:
        *    azione, stampa, bottoni di creazione, import e modifica e la searchview.
        */
        _updateControlPanel: function (buttons) {

            this.update_control_panel({
                cp_content: {
                    $searchview: this.searchview.$el,
                    $searchview_buttons: this.$searchview_buttons,
                },
                searchview: this.searchview,
            });
        },


        /**
        * funzione che prende il domain e il context attualmente utilizzato. entra in questa funzione quando si fa una
        * ricerca dalla searchview e quando si carica la pagina.
        * @private
        * @param {OdooEvent} event
        */
        _onSearch: function (event) {
            event.stopPropagation();
            var session = this.getSession();
            var result = pyUtils.eval_domains_and_contexts({
                domains: event.data.domains,
                contexts: [session.user_context].concat(event.data.contexts)
            });

            // una volta ottenuto il domain si va chiamare odoo per ottenere i dati per la gant filtrati con il domain che
            // è stato creato dalla searchview
            this.loadGanttData(result.domain);
        },
    });

    core.action_registry.add('project.gant.view', ProjectGant);
    return ProjectGant;
});
