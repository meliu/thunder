from os.path import join, dirname
import tornado.wsgi
import tornado.web
import sae

from settings import DEBUG

class Application(tornado.wsgi.WSGIApplication):
    def __init__(self):
        handlers = []

        if DEBUG:
            from apps.test import urls as test_urls
            handlers += test_urls

        settings = dict(
            template_path=join(dirname(__file__), "templates"),
            static_path=join(dirname(__file__), "static"),
            cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            xsrf_cookies=True,
            login_url="/auth/signin",
            debug=True,
        ) 
        
        tornado.wsgi.WSGIApplication.__init__(self, handlers, **settings)

app = Application()
application = sae.create_wsgi_app(app)
