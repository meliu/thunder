define([
    'underscore',
    'backbone',
    'text!templates/stream.html'
], function(_, Backbone, streamTemplate) {
    var StreamView = Backbone.View.extend({
        el: '.content',
        initialize: function () {
        },
        render: function () {
            console.log("Execute the streamView render");
            $(this.el).html(streamTemplate);
        }
    });
    return new StreamView;
});
