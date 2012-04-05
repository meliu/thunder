import hashlib
from tornado.escape import json_encode
from thunder.handler import BaseHandler
from thunder.form import Form
from apps.models.gallery import User

class Index(BaseHandler):
    def get(self):
        self.render('gallery.html')

class SignIn(BaseHandler):
    def post(self):
        form = Form(self.request.arguments)
        if form.validate():
            email = form['email']
            password = form['password']
            remember = form['remember']
            user = self.db.table('users').\
                    find('[email] = %s AND [password] = %s', email, password).\
                    fields('[id], [email]').\
                    query()
            if user:
                user_cookie = dict(
                        id = str(user['id']),
                        email = user['email']
                    )
                if remember:
                    self.set_secure_cookie("user", json_encode(user_cookie))
                else:
                    self.set_secure_cookie("user", json_encode(user_cookie),\
                            expires_days=None)
                self.redirect('/')
            else:
                self.write("lol")

class SignOut(BaseHandler):
    def get(self):
        self.clear_cookie('user')
        self.redirect('/')

class UploadPhoto(BaseHandler):
    def get(self):
        pass

urls = [
    ('/', Index),
    ('/signin', SignIn),
    ('/signout', SignOut),
    ('/gallery/upload', UploadPhoto),
]
