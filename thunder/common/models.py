from thunder.model import Base

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

DROP TABLE IF EXISTS `person_info`;
CREATE TABLE `user_info` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`gender` int(1) NOT NULL,
`lastname` varchar(50) NOT NULL,
`firstname` varchar(50) NOT NULL,
`user_id` int(11) NOT NULL,
PRIMARY KEY (`id`),
KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=ut8;

DROP TABLE IF EXISTS `firm_info`;
CREATE TABLE `firm_info` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`name` varchar(50) NOT NULL,
`user_id` int(11) NOT NULL,
PRIMARY KEY (`id`),
KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=ut8;
'''

class User(Base):
    __table__ = 'users'
    
    def __init__(self, email, password):
        item = dict(
                email = email,
                password = password,
            )
        Base.__init__(self, item)

class PersonInfo(Base):
    __table__ = 'person_info'

    def __init__(self, gender, lastname, firstname):
        item = dict(
                gender = gender,
                lastname = lastname,
                firstname = firstname
            )
        Base.__init__(self, item)

class Picture(Base):
    __table__ = 'pictures'

    def __init__(self, name, ourl, surl):
        item = dict(
                name = name,
                ourl = ourl,
                surl = surl,
            )
        Base.__init__(self, item)
