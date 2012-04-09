define([
    'jquery',
    'underscore',
    'backbone',
    'views/stream',
    'views/header/sharePhoto'
], function($, _, Backbone, streamView, sharePhotoView) {
    var AppView = Backbone.View.extend({
        el: $('header'),
        events: {
            'click .share-btn': 'showShareBox'
        },
        initialize: function () {
            streamView.render();
        },
        showShareBox: function () {
            sharePhotoView.render();
        }
    });
    return AppView;
});
