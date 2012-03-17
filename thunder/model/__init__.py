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
