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
            obj = sae.storage.Ojbect(self.files[0]['body'])
            obj_name = int(time.time()) + random_str(8) + \
                    self.files[0]['format'].lower()
            s.put(self.domain, obj_name, obj)
            return True
        except ImportError:
            obj = self.files[0]['body']
            obj_name = int(time.time()) + random_str(8) + \
                    self.files[0]['format'].lower()
            obj_url = '/static/upload/' + obj_name
            with open(obj_url, 'wb') as f:
                f.write(obj)
        except:
            return False

    def upload_all(self, **kwargs):
        try:
            import sae.storage
            s = sae.storage.Client()
            for file in self.files:
                obj = sae.storage.Object(file['body'])
                obj_name = int(time.time()) + random_str(8) + \
                        file['format'].lower()
                s.put(self.domain, obj_name, obj)
                obj_url = s.url(self.domain, obj_name)
            return True
        except ImportError:
            for file in self.files:
                obj = file['body']
                obj_name = int(time.time()) + random_str(8) + \
                        file['format'].lower()
                obj_url = '/static/upload/' + obj_name
                with open(obj_url, 'wb') as f:
                    f.write(obj)
            return True
        except:
            return False
