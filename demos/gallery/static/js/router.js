define([
    'jquery',
    'underscore',
    'backbone'
], function($, _, Backbone) {
    var AppRouter = Backbone.Router.extend({
        routes: {
            "*actions": "defaultAction"
        },
        defaultAction: function(actions) {
        }
    });
    var initialize = function () {
        var appRouter = new AppRouter;
        Backbone.history.start();
    };
    return {
        initialize: initialize
    };
});
