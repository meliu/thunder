import StringIO
import time
try:
    import Image
except:
    from PIL import Image
import sae.storage
from str import random_str
from settings import DEBUG, STORAGE_DOMAIN

class Picture:

    default_size = dict(
            small=(80, 80)
            middle=(360, 360)
        )

    def __init__(self, body):
        self.name = name
        self.body = body

    def upload(self, **kwargs):
        '''
        kwargs['forbid_format'] is a tuple that contains format forbidden.
        kwargs['size'] : 'small' for head photo, 'middle' for info stream.

        return r - 'return dictionary'.
        '''
        r = {isSupport: True}

        try:
            forbid_format = kwargs['forbid_format']
        except KeyError:
            forbid_format = ()

        try:
            self.size = self.default_size[kwargs['size']]
        except KeyError:
            if type(kwargs['size']) is type(()):
                self.size = kwargs['size']
            else:
                self.size = self.default_size['middle']

        try:
            pic = Image.open(StringIO.StringIO(self.body))
        except:
            r['isSupport'] = False
        if pic.format not in forbid_format:
            name = str(int(time.time())) + random_str() + '.' + image.format.lower()
            o_pic_name = 'origin' + name
            s_pic_name = 'show' + name
            s_pic = pic.resize(self.size)

            if DEBUG:
                ourl = '/' + self.settings['static_path'] + '/upload/origin/' +\
                        o_pic_name
                surl = '/' + self.settings['static_path'] + '/upload/show/' +\
                        s_pic_name
                pic.save(ourl)
                pic.save(sulr)

            else:
                s = sae.storage.Client()

                o_obj = sae.storage.Object(self.body)
                s.put(STORAGE_DOMAIN, o_pic_name, o_obj)
                ourl = s.url(STORAGE_DOMAIN, o_pic_name)

                s_obj = sae.storage.Object(s_pic.tostring())
                s.put(STORAGE_DOMAIN, s_pic_name, s_obj)
                surl = s.url(STORAGE_DOMAIN, s_pic_name)
            r['url'] = surl
        else:
            r['isSupport'] = False
        return r
