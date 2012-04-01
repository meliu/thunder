import os.path
import sys
import tornado.wsgi
import sae

class Application(tornado.wsgi.WSGIApplication):
    def __init__(self):
        handlers = []

        settings = dict(
            debug = True,
            gzip = True,
            root_path = os.path.dirname(__file__),
            template_path = os.path.join(os.path.dirname(__file__), "apps/templates/"),
            static_path = os.path.join(os.path.dirname(__file__), "static"),
            cookie_secret = "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            xsrf_cookies = True,
            login_url = "/auth/signin",
            autoescape = None,
        ) 
        
        tornado.wsgi.WSGIApplication.__init__(self, handlers, **settings)

app = Application()
application = sae.create_wsgi_app(app)
