import StringIO
import time
try:
    import Image as Img
except:
    from PIL import Image as Img
from thunder.upload import Upload
from thunder.db import Base

class ImageModel(Base):

    def __init__(self):
        Base.__init__(self)
        self.tablename = 'images'

    def add_image(self, name, url, user_id):
        self['name'] = name
        self['create_time'] = int(time.time())
        self['user_id'] = int(user_id)
        self.add()

class Image:
    '''
    example:
        file = self.request.files[0]
        img = Image(file, user_id)
        img.set_domain('thunder')
        img.make_icon()
        img.save()
    '''

    support_format = ('JPEG', 'PNG', 'GIF')
    common_size = dict(
            icon = (80, 80),
        )

    def __init__(self, file, user_id):
        self.file = file
        self.user_id = user_id
        self.img = Img.open(StringIO.StringIO(self.file['body']))

    def verify(self):
        if self.img.format not Image.support_format:
            return False
        return True

    def set_domain(self, domain):
        self.domain = domain

    def make(self):
        '''
        Must set storage domain using set_domain() before maken().
        So do make_icon().
        return a Upload object.
        '''
        if self.verify():
            self.img = {
                'body': self.img.tostring(),
                'format': self.img.format
            }
            self.up =  Upload(self.domain, [img])
        return None

    def make_icon(self):
        if self.verify():
            self.icon = self.img.resize(Image.common_size['icon'])
            self.img = {
                'body': self.icon.tostring(),
                'format': self.img.format
            }
            self.up = Upload(self.domain, [icon])
        return None

    def save(self):
        '''
        Must set user_id by set_user_id().
        '''
        img = ImageModel()
        self.name, self.url = self.up.upload() # Get the name and url.
        img.add_image(self.name, self.url, self.user_id)
