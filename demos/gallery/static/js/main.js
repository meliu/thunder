require.config({
    paths: {
        jquery: 'libs/jquery/jquery',
        underscore: 'libs/underscore/underscore',
        backbone: 'libs/backbone/backbone',

        // require.js plugins
        order: 'libs/require/order',
        text: 'libs/require/text',

        //  
        templates: '../templates'
    },
    urlArgs: "bust=" + (new Date()).getTime()
});

require([
    'views/app',
], function(AppView) {
    var app = new AppView;
    app.render();
});
