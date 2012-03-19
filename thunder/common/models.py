import sys
sys.path.append('../..')
from thunder.model import Base, DB

tables = '''
CREATE DATABASE IF NOT EXISTS `thunder`;
USE `thunder`;

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`email` varchar(32) NOT NULL,
`password` varchar(32) NOT NULL,
`status` int(1) NOT NULL DEFAULT '0',
`cid` int(1) NOT NULL DEFAULT '1',
`create_time` int(10) DEFAULT '0',
`update_time` int(10) DEFAULT '0',
PRIMARY KEY `id` (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `pictures`;
CREATE TABLE `pictures` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`name` varchar(30) NOT NULL,
`ourl` varchar(100) NOT NULL,
`surl` varchar(100) NOT NULL,
`create_time` int(10) DEFAULT '0',
`update_time` int(10) DEFAULT '0',
PRIMARY KEY (`id`),
UNIQUE KEY (`name`),
UNIQUE KEY (`ourl`),
UNIQUE KEY (`surl`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `person_info`;
CREATE TABLE `person_info` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`gender` int(1) NOT NULL,
`lastname` varchar(50) NOT NULL,
`firstname` varchar(50) NOT NULL,
`user_id` int(11) NOT NULL,
`create_time` int(10) DEFAULT '0',
`update_time` int(10) DEFAULT '0',
PRIMARY KEY (`id`),
KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `firm_info`;
CREATE TABLE `firm_info` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`name` varchar(50) NOT NULL,
`user_id` int(11) NOT NULL,
`create_time` int(10) DEFAULT '0',
`update_time` int(10) DEFAULT '0',
PRIMARY KEY (`id`),
KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `person_vip';
CREATE TABLE `person_vip` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`right` int(3) DEFAULT '0',
`create_time` int(10) DEFAULT '0',
`update_time` int(10) DEFAULT '0',
PRIMARY KEY (`id`)
)

DROP TABLE IF EXISTS `firm_vip';
CREATE TABLE `firm_vip` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`right` int(3) DEFAULT '0',
`create_time` int(10) DEFAULT '0',
`update_time` int(10) DEFAULT '0',
PRIMARY KEY (`id`)
)
'''

class User(Base):
    '''
    cid 1: common person, 2: vip person, 3: firm, 4: vip firm
    '''
    __table__ = 'users'
    
    def __init__(self, email, password, cid):
        item = dict(
                email = email,
                password = password,
                cid = cid
            )
        Base.__init__(self, item)

class PersonInfo(Base):
    __table__ = 'person_info'

    def __init__(self, gender, lastname, firstname, user_id):
        item = dict(
                gender = gender,
                lastname = lastname,
                firstname = firstname,
                user_id = user_id
            )
        Base.__init__(self, item)

class FirmInfo(Base):
    __table__ = 'firm_info'

    def __init__(self, name):
        item = dict(
                name = name,
            )
        Base.__init__(self, item)

class PersonVIP(Base):
    __table__ = 'person_vip'

    def __init__(self, right):
        Base.__init__(self, dict(right=right))

class FirmVIP(Base):
    __table__ = 'firm_vip'

    def __init__(self, right):
        Base.__init__(self, dict(right=right))

class Picture(Base):
    __table__ = 'pictures'

    def __init__(self, name, ourl, surl):
        item = dict(
                name = name,
                ourl = ourl,
                surl = surl,
            )
        Base.__init__(self, item)

if __name__ == '__main__':
    DB._create_table(tables)

