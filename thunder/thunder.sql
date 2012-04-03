
DROP TABLE IF EXISTS `images`;
CREATE TABLE `images` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` int(23) NOT NULL,
    `url` varchar(100) NOT NULL,
    `create_time` int(10) NOT NULL DEFAULT '0',
    `user_id` int(11) NOT NULL DEFAULT '0',
    PRIMARY KEY (`id`),
    UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
