require.config({
    paths: {
        jquery: 'libs/jquery/jquery',
        underscore: 'libs/underscore/underscore',
        backbone: 'libs/backbone/backbone',

        // require.js plugins
        order: 'libs/require/order',
        text: 'libs/require/text',

        //  
        templates: '../templates',

        //
        router: 'router'
    },
    urlArgs: "bust=" + (new Date()).getTime()
});

require([
    'app',
    'router'
], function(AppView, router) {
    var app = new AppView;
    app.render();
    router.initialize();
});
