# coding=utf-8
__author__ = 'meliu'

import tornado.database
from MySQLdb import ProgrammingError
try:
    import sae.const
    MYSQL_HOST_M = sae.const.MYSQL_HOST_M
    MYSQL_HOST_S = sae.const.MYSQL_HOST_S
    MYSQL_PORT = sae.const.MYSQL_PORT
    MYSQL_DB = sae.const.MYSQL_DB
    MYSQL_USER = sae.const.MYSQL_USER
    MYSQL_PASS = sae.const.MYSQL_PASS
except:
    MYSQL_HOST_M = 'localhost'
    MYSQL_HOST_S = 'localhost'
    MYSQL_PORT = '3306'
    MYSQL_DB = 'thunder'
    MYSQL_USER = 'thunder'
    MYSQL_PASS = 'thunder'

class Finder:
    _db = None
    
    @staticmethod
    def dbconnect():
        if not Finder._db:
            Finder._db = tornado.database.Connection(
                    host = MYSQL_HOST_S + ':' + MYSQL_PORT,
                    database = MYSQL_DB,
                    user = MYSQL_USER,
                    password = MYSQL_PASS,
                    max_idle_time = 5)

        return Finder._db
    
    def __init__(self, tablename):
        self._where = None
        self._order = None
        self._skip = 0
        self._limit = 1
        self._page = 1
        self._page_size = 20
        self._fields = '*'
        self._join = None
        self.db = Finder.dbconnect()
        self.tablename = tablename

    @staticmethod
    def sql_str(sql):
        sql = sql.replace('[', '`')
        sql = sql.replace(']', '`')
        return sql

    #
    # Basic function
    #
    
    # The query Fields
    def fields(self, sql):
        '''
        example:
            obj.fields('[name], [age], [email]')
            or
            obj.fields('[users].[name], [users].[age], [users].[email]')
        '''

        self._fields = Finder.sql_str(sql)
        return self

    # The query Conditions
    def where(self, sql, *args):
        '''
        example:
            obj.where('[id] < %s AND [age] < %s', '100', '30')
            or
            obj.where('[title] LIKE %s AND [status] = %s', '%'+ find +'%', 'public')
        '''

        self._where = {
                'where': Finder.sql_str(sql),
                'value': args
            }
        return self

    # The order
    def order(self, sql):
        '''
        example:
            obj.order('[id] DESC, [create_time] DESC')
        '''

        self._order = Finder.sql_str(sql)
        return self

    def limit(self, skip, limit):
        '''
        example:
            obj.limit(0, 20) # first 20 items
        '''

        self._skip = int(skip)
        self._limit = int(limit)
        return self

    # Inner Join
    def join(self, sql):
        '''
        example:
            obj.join('[tags] ON [posts].[id] = [tags].[post_id]').\
                join('[category] ON [posts].[id] = [category].[post_id]')
        '''

        if not self._join:
            self._join = []
        self._join.append(' Inner Join ' + Finder.sql_str(sql))
        return self

    # Left Join
    def left_join(self, sql):
        if not self._join:
            self._join = []
        self._join.append(' Left Join ' + Finder.sql_str(sql))

    # Right Join
    def right_join(self, sql):
        if not self._join:
            self._join = []
        self._join.appnd(' Right Join ' + Finder.sql_str(sql))

    # Execute the query, and return the result
    def query(self):
        sql = 'SELECT ' + self._fields + ' FROM `' + self.tablename + '` '

        if self._join:
            for join in self._join:
                sql += join

        parameters = []
        if self._where:
            sql += ' WHERE ' + self._where['where']
            parameters = self._where['value']

        if self._order:
            sql += ' ORDER BY ' + self._order

        sql += ' LIMIT ' + str(self._skip) + ' , ' + str(self._limit)

        self.db._ensure_connected()
        if self._limit == 1:
            return self.db.get(sql, *parameters)
        return self.db.query(sql, *parameters)

    def all(self):
        sql = 'SELECT ' + self._fields + ' FROM `' + self.tablename + '` '

        if self._join:
            for join in self._join:
                sql += join

        parameters = []
        if self._where:
            sql += ' WHERE ' + self._where['where']
            parameters = self._where['args']

        if self._order:
            sql += ' ORDER BY ' + self._order

        self.db._ensure_connected()
        return self.db.query(sql, *parameters)

    def count(self):
        parameters = []
        sql = 'SELECT COUNT(*) AS row_count FROM `' + self.tablename + '`'

        if self._join:
            for join in self._join:
                sql += join

        if self._where:
            sql += ' WHERE ( ' + self._where['where'] + ' ) '
            parameters = self._where['value']

        self.db._ensure_connected()
        result = self.db.get(sql, *parameters)
        return result['row_count']

    #
    # Advanced function
    #

    def limit_page(self, page, page_size):
        self._page = int(page)
        self._page_size = int(page_size)
        if self._page < 0:
            self._page =1
        return self.limit((self._page-1) * self._page_size, self._page_size)

    def pagination(self):
        import math
        total_item = self.count()
        total_page = math.ceil( float(total_item) / float(self._page_size))

        if self._page <= 1:
            prev = 1
        else:
            prev = self._page - 1

        if self._page >= total_page:
            next = total_page
        else:
            next = total_page + 1

        return {
                'prev': int(prev),
                'next': int(next),
                'current': self._page,
                'total_page': int(total_page),
                'total_item': int(total_item),
            }

    def filter_by(self, **kwargs):
        return self

class Base:
    _db = None

    @staticmethod
    def dbconnect():
        if not Base._db:
            Base._db = tornado.database.Connection(
                    host = MYSQL_HOST_M + ':' + MYSQL_PORT,
                    database = MYSQL_DB,
                    user = MYSQL_USER,
                    password = MYSQL_PASS,
                    max_idle_time = 5)
        return Base._db

    def __init__(self):
        self.db = Base.dbconnect()
        self.attr = {}

    @staticmethod
    def sql_str():
        return Finder.sql_str(sql)

    def table(self, name):
        self.tablename = name
        return self

    def find(self, sql = None, *args):
        finder = Finder(self.tablename)
        if not sql:
            return finder
        else:
            return finder.where(sql, *args)

    def delete(self, sql, *args):
        '''
        example:
            obj.delete('[status] = %s AND ['age'] < %s', '0', '18')
        '''

        sql = Finder.sql_str(sql)
        self.db._ensure_connected()
        return self.db.execute('DELETE FROM `' + self.tablename + '` WHERE ' \
                + sql, *args)

    def __setitem__(self, key, value):
        self.attr[key] = value

    def __getitem__(self, key):
        return self.attr[key]

    def __delitem__(self, key):
        if self.attr.has_key(key):
            del self.attr[key]

    # Delete all attributes.
    def clear_attr(self):
        self.attr = {}

    def add(self):
        if len(self.attr) == 0:
            return False

        parameters = []
        key = []
        value = []
        sql = 'INSERT INTO `' + self.tablename + '` '

        for k in self.attr.keys():
            key.append('`' + k + '`')
            value.append('%s')
            parameters.append(self.attr[k])

        sql = sql + '(' + ','.join(key) + ') VALUES (' + ','.join(value) + ')'
        self.db._ensure_connected()
        return self.db.execute(sql, *parameters)

    def update(self, sql, *args):
        if not self.attr:
            return false

        # confirm the data exists.
        if self.find().where(sql, *args).count() != 0:
            key = []
            parameters = []
            for k in self.attr.keys():
                key.append('`' + k + '` = %s')
                parameters.append(self.attr[k])

            for item in args:
                parameters.append(item)

            where = Base.sql_str(sql)
            sql = 'UPDATE `' + self.tablename + '` SET ' + ','.join(key) + \
                    'WHERE'+ where + 'LIMIT 1'
            self.db._ensure_connected()
            return self.db.execute(sql, *parameters)
        return False

class InitDB:
    @staticmethod
    def init(sql):
        db = Base.dbconnect()
        try:
            db._ensure_connected()
            db.execute(sql)
        except ProgrammingError:
            return True
