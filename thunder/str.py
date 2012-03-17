from random import randint

def random_str(random_length=8):
    _str = ''
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for i in xrange(randomlength):
        _str += chars[randint(0, len(chars)-1)]
    return _str
