from base import Base

class User(Base):
    __table__ = 'users'

    def __init__(self, email, password):
        Base.__init__(self)
        self['email'] = email
        self['password'] = password
