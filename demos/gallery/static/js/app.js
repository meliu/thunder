define([
    'jquery',
    'underscore',
    'backbone',
    'views/stream',
    'views/sharePhoto'
], function($, _, Backbone, streamView, sharePhotoView) {
    var AppView = Backbone.View.extend({
        events: {
            'click .shareBtn': 'showAlert'
        },
        initialize: function () {
            streamView.render();
        },
        showAlert: function () {
            window.alert("LOL");
        },
        showShareBox: function () {
            sharePhotoView.render();
        }
    });
    return AppView;
});
