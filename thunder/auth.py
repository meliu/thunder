import hashlib
from thunder.model import Query
from thunder.common.models import User, PersonInfo

def verify_user(email, password):
    user = Query(User).filter_by(email=email, password=password).one()
    if user and user.status:
        return user
    else:
        return None

def signup_person(email, password, confirm, gender, lastname, firstname):
    '''
    gender - 0:male , 1:female
    '''
    errors = []
    if  password != confirm:
        errors.append('confirm_failed')
    if Query(User).filter_by(email=email).one():
        errors.append('email_exists')
    if errors:
        return errors
    else:
        User(email, hashlib.md5(password).hexdigest()).add()
        PersonInfo(gender, lastname, firname)
        return None
