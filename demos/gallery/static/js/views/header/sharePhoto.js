define([
    'jquery',
    'underscore',
    'backbone',
    'text!templates/sharePhoto.html'
], function ($, _, Backbone, sharePhotoTemplate) {
    var SharePhoto = Backbone.View.extend({
        el: ".share-box",
        body: $('.wrapper')[0],
        events: {
            'click .share': 'share',
            'click .share-cancel': 'shareCancel'
        },
        render: function () {
            this.$el.html(sharePhotoTemplate);
            this.$el.show();
            this.body.style.opacity = '0.5';
            return this;
        },
        share: function () {
        },
        shareCancel: function () {
            this.$el.hide();
            this.body.style.opacity = '1';
        }
    });

    return new SharePhoto;
});
