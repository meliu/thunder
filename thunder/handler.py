import hashlib
import tornado
from thunder.model import Query
from thunder.common.models import User, PersonInfo, FirmInfo, PersonVIP, FirmVIP

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        user = self.get_secure_cookie("user")
        if not user:
            return None
        return tornado.escape.json_decode(user)

class SignHandler(tornado.web.RequestHandler):
    def verify_user(self, email, password):
        r = {}
        errors = []
        if not email:
            errors.append('email_blank')
        if not password:
            errors.append('password_blank')

        if email and password:
            user = Query(User).filter_by(email=email, password=password).one()
            print "***", user
            if user:
                if not user['status']:
                    errors.append('pending')
                else:
                    r['user'] = user
            else:
                errors.append('info_wrong')
        r['errors'] = errors
        return r

    def verify_vip(self, user):
        vip = Query

    def signup_person(self, email, password, confirm, gender,\
            lastname, firstname):
        '''
        gender - 0:male , 1:female
        if success return None, failed return errors.
        '''
        errors = []
        if not email:
            errors.append('email_blank')
        if not password:
            errors.append('password_blank')
        if not confirm:
            errors.append('confirm_blank')
        if not gender in '01':
            errors.append('gender_blank')
        if not lastname:
            errors.append('lastname_blank')
        if not firstname:
            errors.append('firstname_blank')

        if email and password and confirm:
            if password != confirm:
                errors.append('confirm_failed')
            if Query(User).filter_by(email=email).one():
                errors.append('email_exists')
        if errors:
            return errors
        else:
            cid = 1
            user_id = User(email, hashlib.md5(password).hexdigest(), cid).add()
            PersonInfo(gender, lastname, firstname, user_id).add()
            return None

