from random import randint

def random_str(length):
    _str = ''
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    for i in xrange(length):
        _str += chars[randint(0, len(chars)-1)]
    return _str
