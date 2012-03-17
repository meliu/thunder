from tornado.testing import LogTrapTestCase
from tornado.web import WSGIApplcation, RequestHandler
from thunder.model.base import DB

class ModelTest(LogTrapTestCase):
    def get_app(self):
        class CreateTableHandler(RequestHandler):
            def get(self):
                self.create_table_sql = '''
                CREATE DATABASE IF NOT EXISTS `thunder`;
                USE `thunder`;

                DROP TABLE IF EXISTS `users`;
                CREATE TABLE `users` (
                `id` int(11) NOT NULL AUTO_INCREMENT,
                `email` varchar(32) NOT NULL,
                `password` varchar(32) NOT NULL,
                `create_time` int(10) DEFAULT '0',
                `update_time` int(10) DEFAULT '0',
                PRIMARY KEY `id` (`id`)
                ) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

                DROP TABLE IF EXISTS `pictures`;
                CREATE TABLE `pcitures` (
                `id` int(11) NOT NULL AUTO_INCREMENT,
                `name` varchar(30) NOT NULL,
                `ourl` varchar(100) NOT NULL,
                `surl` varchar(100) NOT NULL,
                `create_time` int(10) NOT NULL DEFAULT '0',
                `update_time` int(10) DEFAUTL '0',
                PRIMARY KEY (`id`),
                UNIQUE KEY `name` (`name`),
                UNIQUE KEY `ourl` (`ourl`),
                UNIQUE KEY `surl` (`surl`)
                ) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=ut8;
                '''
                self.write(DB._create_table())
                return

        return WSGIApplcation([
                ('/create_table', CreateTableHandler)
            ])

    def test_create_table(self):
        response = self.fetch('/create_table')
        self.assertEqual(response.body, 'success')
