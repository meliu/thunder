import StringIO
import time
from thunder.utils import random_str

class Upload:
    def __init__(self, domain, files):
        self.domain = domain
        self.files = files

    def upload(self, **kwargs):
        try:
            import sae.storage
            s = sae.storage.Client()
            for file in files:
                obj = sae.storage.Object(file['body'])
                obj_name = int(time.time()) + random_str(8) + \
                        file['format'].lower()
                s.put(domain, obj_name, obj)
                obj_url = s.url(domain, obj_name)
        except ImportError:
            for file in files:
                obj = file['body']
                obj_name = int(time.time()) + random_str(8) + \
                        file['format'].lower()
                obj_url = '/static/upload/' + obj_name
                with open(obj_url, 'wb') as f:
                    f.write(obj)

        return (domain, obj_name, obj_url)
