from __future__ import absolute_import
from math import ceil
from thunder.settings import ITEMS_PER_PAGE

class Pagination:
    def __init__(self, current_page, total_items):
        self.current_page = current_page
        self.total_items = total_items
        self.total_pages = \
                int(ceil(self.total_items / float(ITEMS_PER_PAGE)))

    def next(self):
        if self.current_page >= self.total_pages:
            return self.total_pages
        return self.current_page + 1

    def pre(self):
        if self.current_page <-1:
            return 1
        return self.current_page - 1 

    def __getattr__(self, attr):
        if attr == 'next_page':
            return self.next()
        if attr == 'pre_page':
            return self.pre()
        if attr == 'current':
            return self.current_page
        if attr == 'total':
            return self.total_pages
        if attr == 'start':
            return 1
        if attr == 'end':
            return self.total_pages
