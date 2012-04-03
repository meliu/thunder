import StringIO
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

class Image:

    support_format = ('JPEG', 'PNG', 'GIF')
    common_size = dict(
            icon = (80, 80),
        )

    def __init__(self, file):
        slef.file = file
        self.img = Img.open(StringIO.StringIO(self.file['body']))

    def verify(self):
        if self.img.format not Image.support_format:
            return False
        return True

    def set_domain(self, domain):
        self.domain = domain

    def make_icon(self):
        '''
        Must set storage domain using set_domain() before make_icon().
        return a Upload object.
        '''
        if self.verify():
            self.icon = self.img.resize(Image.common_size['icon'])
            icon = {
                'body': self.icon.tostring(),
                'format': self.img.format
            }
            return Upload(self.domain, [icon])
        return None
