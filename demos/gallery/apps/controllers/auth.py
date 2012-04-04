from thunder.handler import BaseHandler
from thunder.form import Form, Input, Email, Password

class SignUp(BaseHandler):

    def get(self):
        self.render("auth/signup.html")

    def post(self):
        form = Form(self.request.arguments)
        form.add( Email('email') )
        form.add( Password('password') )
        if form.validate():
            email = form['email']
            password = form['password']
            print email
            print password
        else:
            print "BAD"

urls = [
    ('/auth/signup', SignUp)
]
