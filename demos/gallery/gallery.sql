CREATE DATABASE IF NOT EXISTS `thunder`;
USE `thunder`;

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `email` varchar(32) NOT NULL,
    `password` varchar(32) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `email` (`email`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `images`;
CREATE TABLE `images` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` int(23) NOT NULL,
    `create_time` int(10) NOT NULL DEFAULT '0',
    `user_id` int(11) NOT NULL DEFAULT '0',
    PRIMARY KEY (`id`),
    UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

INSERT INTO `users` (`email`, `password`) values ('admin@gallery.com', 'gallery');
