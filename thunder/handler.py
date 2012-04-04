import time
import tornado
import thunder

class BaseHandler(tornado.web.RequestHandler):

    def __init__(self, application, request, **kwargs):
        tornado.web.RequestHandler.__init__(self, application, request, **kwargs)

    def get_current_user(self):
        user = self.get_secure_cookie("user")
        if not user:
            return None
        return tornado.escape.json_decode(user)

    def error(self, **kwargs):
        kwargs['url'] = kwargs.has_key('url') and kwargs['url'] or \
                self.request.path
        self.render("error.html", **kwargs)
        self._finished = True
        return

    @property
    def db(self):
        return thunder.model.Base()
