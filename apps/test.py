
from ext.models import DB
from ext.models.base import Query
from ext.models.test import User
from utils import BaseHandler

class Test1(BaseHandler):
    def get(self):
        DB._create_table()
        return

class Test2(BaseHandler):
    def get(self):
        user = User('wenkai.mel@gmail.com', '123456')
        user.add()

class Test3(BaseHandler):
    def get(self):
        users = Query(User).filter_by(email='wenkai.mel@gmail.com')
        user =  users.one()
        print user, type(user)
        user['email'] = 'moosvelf@gmail.com'
        print user, type(user)

class Test4(BaseHandler):
    def get(self):
        users = Query(User).filter_by()
        for user in users:
            print user

class Test5(BaseHandler):
    def get(self):
        users = Query(User).filter_by(email='wenkai.mel@gmail.com')
        users.delete()
        print len(users)

class Test6(BaseHandler):
    def get(self):
        user = Query(User).filter_by(email='wenkai.mel@gmail.com').one()
        user['email'] = 'moosvelf@gmail.com'
        user.update()

urls = [
    ('/test/1', Test1),
    ('/test/2', Test2),
    ('/test/3', Test3),
    ('/test/4', Test4),
    ('/test/5', Test5),
    ('/test/6', Test6),
]
