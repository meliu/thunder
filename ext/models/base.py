from datetime import datetime
from time import time
from __init__ import mdb, sdb

class DBOper:
    '''
    Basic operation of database.
    '''

    def __init__(self, table):
        self.table = table

    def get_limit_item(self, *args, **kwargs):
        sql = 'select * from ' + self.table
        condition = []
        if args:
            start = args[0]
            limit = args[1]
        else:
            start = 0
            limit = 1
        if kwargs:
            sql += ' where '
            for key, value in kwargs.items():
                if type(value) == type(u"") or value == ''\
                        or type(value) == type(""):
                    condition.append(key + ' = ' + "'" + value + "'")
                else:
                    condition.append(key + ' = ' + str(value))
            sql += ' and '.join(condition)
        sql += ' order by id desc limit %s,%s'
        sdb._ensure_connected()
        return sdb.query(sql, start, limit) # args indicate start and limit

    def get_item(self, **kwargs):
        sql = 'select * from ' + self.table
        condition = []
        if kwargs:
            sql += ' where '
            for key, value in kwargs.items():
                if type(value) == type(u"") or value == ''\
                        or type(value) == type(""):
                    condition.append(key + ' = ' + "'" + value + "'")
                else:
                    condition.append(key + ' = ' + str(value))
            sql += ' and '.join(condition)

        sql += ' order by id desc'
        sdb._ensure_connected()
        return sdb.query(sql)

    def update_item_by_id(self, id, **kwargs):
        sql = 'update ' + self.table + ' set '
        condition = []
        values = []
        if kwargs:
            for key, value in kwargs.items():
                condition.append(key + ' = ' + '%s')
                values.append(value)
            condition.append('update_time' + ' = ' + '%s')
            values.append(int(time()))
            sql += ' , '.join(condition) + ' where id = %s'
            values.append(id)
            mdb._ensure_connected()
            return mdb.execute(sql, *tuple(values))

    def add_item(self, **kwargs):
        sql = 'insert into ' + self.table + ' ('
        if kwargs:
            keys = kwargs.keys()
            keys.append('create_time')
            values = kwargs.values()
            values.append(int(time()))
            sql += ','.join(keys) + ') values (' + ','.join(['%s']*len(keys)) + ')'
            mdb._ensure_connected()
            return mdb.execute(sql, *tuple(values))

    def del_item_by_id(self, id):
        sql = 'delete from ' + self.table + ' where id = %s'
        mdb._ensure_connected()
        return mdb.execute(sql, id)

    def del_item(self, **kwargs):
        sql = 'delete from ' + self.table + ' where '
        condition = []
        if kwargs:
            for key, value in kwargs.items():
                if type(value) is type('') or type(value) is type(u'') or \
                        value == '':
                    condition.append(key + ' = ' + "'" + value + "'")
                else:
                    condition.append(key + ' = ' + str(value))
            sql += ' and '.join(condition)
            mdb._ensure_connected()
            return mdb.execute(sql)

class Base(dict):
    '''
    __table__  # Table name.
    __createtable__ # The sql statement to create table.
    '''

    def __init__(self):
        self.db = DBOper(self.__table__)

    # ADD
    def add(self):
        self.db.add_item(**self)

class Query:
    '''
    The class to get the QuerySet.
    '''

    def __init__(self, Class):
        self.__table__ = Class.__table__

    # SELECT
    def filter_by(self, **kwargs):
        '''
        args[0] : start, args[1] : limit. 
        kwargs indicate the conditions.
        kwargs is blank means get all elements.
        '''
        return QuerySet(self.__table__, **kwargs)

class QuerySet:
    '''
    The class to store the items from database.
    '''

    def __init__(self, table, *args, **kwargs):
        '''
        self.items store all the data.
        '''
        self.condition = kwargs or None
        self.table = table
        self.db = DBOper(self.table)
        if not kwargs:
            self.items = self.db.get_item()
        else:
            self.items = self.db.get_item(**kwargs)
        self.index = len(self.items)
    
    # Get first element of query set.
    def one(self):
        try:
            return QueryItem(self.items[0], self.table)
        except IndexError:
            return "IndexError"

    # DELETE
    def delete(self): 
        if self.condition:
            self.db.del_item(**self.condition)

    def __iter__(self):
        return self

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return QueryItem(self.items[self.index], self.table)

    def __len__(self):
        if self.condition:
            return len(self.i.get_item(**self.condition))
        else:
            return len(self.i.get_item())

class QueryItem(dict):
    def __init__(self, item, table):
        dict.__init__(self, item)
        self.db = DBOper(table)

    def update(self):
        self.db.update_item_by_id(**self)