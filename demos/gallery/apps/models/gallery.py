from thunder.model import Base

class User(Base):
    def __init__(self):
        Base.__init__(self)
        self.tablename = 'users'

class Image(Base):
    def __init__(self):
        Base.__init__(self)
        self.tablename = 'images'
