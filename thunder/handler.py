import time
import tornado
import thunder

class BaseHandler(tornado.web.RequestHandler):

    def __init__(self, application, request, **kwargs):
        self._start_time = time.time()
        tornado.web.RequestHandler.__init__(self, application, request, **kwargs)

    def error(self, **kwargs):
        kwargs['url'] = kwargs.has_key('url') and kwargs['url'] or \
                self.request.path
        self.render("error.html", **kwargs)
        self._finished = True
        return

    def db(self):
        return thunder.db.Base()

    def get_current_user(self):
        pass
