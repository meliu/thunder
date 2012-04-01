import unittest
import time
import sys
sys.path.append('../..')
import thunder.db 

class User(thunder.db.Base):
    def __init__(self):
        thunder.db.Base.__init__(self)
        self.tablename = 'users'

class Post(thunder.db.Base):
    def __init__(self):
        thunder.db.Base.__init__(self)
        self.tablename = 'posts'

class Tag(thunder.db.Base):
    def __init__(self):
        thunder.db.Base.__init__(self)
        self.tablename = 'tags'

class PostTag(thunder.db.Base):
    def __init__(self):
        thunder.db.Base.__init__(self)
        self.tablename = 'post_tag'

class Category(thunder.db.Base):
    def __init__(self):
        thunder.db.Base.__init__(self)
        self.tablename = 'category'

class DBTest(unittest.TestCase):

    def setUp(self):
        self.user = User()
        self.post = Post()
        self.tag = Tag()
        self.post_tag = PostTag()
        self.category = Category()

    @unittest.skip("OK")
    def test_init_db(self):
        sql = '''
        CREATE DATABASE IF NOT EXISTS `thunder`;
        USE `thunder`;

        DROP TABLE IF EXISTS `users`;
        CREATE TABLE `users` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `email` varchar(32) NOT NULL,
        `password` varchar(32) NOT NULL,
        `age` int(3),
        `create_time` int(10) DEFAULT '0',
        PRIMARY KEY `id` (`id`)
        ) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

        DROP TABLE IF EXISTS `posts`;
        CREATE TABLE `posts` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `title` varchar(100) NOT NULL,
        `content` varchar(255) NOT NULL,
        `create_time` int(10) DEFAULT '0',
        `user_id` int(11) NOT NULL,
        `category_id` int(11) NOT NULL,
        PRIMARY KEY `id` (`id`),
        KEY `user_id` (`user_id`),
        KEY `category_id` (`category_id`)
        ) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

        DROP TABLE IF EXISTS `tags`;
        CREATE TABLE `tags` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `name` varchar(32) NOT NULL,
        PRIMARY KEY `id` (`id`),
        UNIQUE KEY `name` (`name`)
        ) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

        DROP TABLE IF EXISTS `post_tag`;
        CREATE TABLE `post_tag` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `post_id` int(11) NOT NULL,
        `tag_id` int(11) NOT NULL,
        PRIMARY KEY `id` (`id`)
        ) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

        DROP TABLE  IF EXISTS `category`;
        CREATE TABLE `category` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `name` varchar(32) NOT NULL,
        PRIMARY KEY `id` (`id`),
        UNIQUE KEY `name` (`name`)
        ) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
        '''
        self.assertTrue(thunder.db.InitDB.init(sql))
    
    @unittest.skip("OK")
    def test_add(self):
        self.user['email'] = 'wenkai.mel@gmail.com'
        self.user['password'] = 'thunder'
        self.user['age'] = 22
        self.user['create_time'] = int(time.time())
        self.assertTrue(self.user.add())
        self.category['name'] = 'IT'
        self.category.add()
        self.post['title'] = 'thunder is best'
        self.post['content'] = 'I love thunder.'
        self.post['user_id'] = 1
        self.post['category_id'] = 1
        self.post['create_time'] = int(time.time())
        self.post.add()

    def test_finder_all(self):
        self.assertTrue(self.user.find().all())

    def test_finder_count(self):
        self.assertGreater(self.user.find().count(), 0)

    def test_finder_fields(self):
        user = self.user.find().fields('[email], [age]').query()
        self.assertFalse('id' in user)

    def test_finder_where(self):
        user = self.user.find().where('[id] = %s', 1).query()
        self.assertEqual(user.id, 1)

    def test_finder_join(self):
        user = self.user.find().join('[posts] ON [users].[id] = [posts].[user_id]').\
                fields('[users].[id] as [author_id], [posts].[title]').query()
        self.assertIsNotNone(user)

    def test_pagination(self):
        self.user.find().limit_page(1, 20)
        self.assertIsNotNone(self.user.find().pagination())

    @unittest.skip("OK")
    def test_delete(self):
        result = self.user.delete('[id] = %s', 1)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
