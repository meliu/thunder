import sys
sys.path.append('../..')
from time import time
from datetime import datetime

from tornado import database

from settings import MYSQL_DB, MYSQL_USER, MYSQL_PASS,\
        MYSQL_HOST_M, MYSQL_HOST_S, MYSQL_PORT
from settings import MAX_IDLE_TIME

mdb = database.Connection("%s:%s" % (MYSQL_HOST_M, str(MYSQL_PORT)), 
        MYSQL_DB, MYSQL_USER, MYSQL_PASS, max_idle_time = MAX_IDLE_TIME)
sdb = database.Connection("%s:%s" % (MYSQL_HOST_S, str(MYSQL_PORT)),
        MYSQL_DB, MYSQL_USER, MYSQL_PASS, max_idle_time = MAX_IDLE_TIME)

class DB():
    def _create_table(self):
        sql = """
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
        """
        mdb._ensure_connected()
        mdb.execute(sql)
DB = DB()
