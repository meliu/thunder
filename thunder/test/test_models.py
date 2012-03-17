
from tornado.testing import LogTrapTestCase

class TestModels(LogTrapTestCase):
    def get_app(self):
        pass

    def setUp(self):
        self.email = 'wenkai.mel@gmail.com'
        self.password = hashlib('123456').hexdigest()

    def test_create_table(self):
        self.assertEqual()
