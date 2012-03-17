from __future__ import absolute_import
from random import randint

def random_str(random_length=8):
    _str = ''
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for i in xrange(random_length):
        _str += chars[randint(0, len(chars)-1)]
    return _str

def to_unicode(arg):
    try:
        x = unicode(arg, 'ascii')
    except:
        x = unicode(arg, 'utf-8')
    else:
        pass
    return
