import tornado.web

class BaseHandler(tornado.web.RequestHandler):

    def get_current_user(self):
        user = self.get_secure_cookie("user")
        if not user:
            return None
        return tornado.escape.json_decode(user)

    @property
    def mdb(self):
        return self.application.mdb

    @property
    def sdb(self):
        return self.application.sdb
