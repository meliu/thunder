#coding=utf-8
import re
import tornado.escape

class Form:
    def __init__(self, values):
        self.items = []
        self.values = values
        self.msg = ''

    def add(self, item):
        self.items.append(item)
        
    def validate(self):
        for k in self.values:
            for item in self.items:
                if item.name == k:
                    item.set_value(self.values[k])

        for item in self.items:
            result = item.validate()
            if not result['success']:
                self.msg = result['msg']
                return False 
        return True

    def __setitem__(self, key, value):
        if isinstance(value, list):
            self.values[key] = value
        else:
            self.values[key] = [value]

    def __getitem__(self, key):
        if len(self.values[key]) == 1:
            return self.values[key][0]
        else:
            return self.values

class Validators:
    @staticmethod
    def notEmpty(value):
        failure = { 'success': False, 'msg': 'The input should not be empty!' }

        if isinstance(value, unicode):
            if len(value.strip()) == 0:
                return failure
        else:
            if not value:
                return failure
        return { 'success': True }

    @staticmethod
    def isEmail(value):
        pattern = '[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$'
        if re.match(pattern, value):
            return { 'success': True }
        return { 'success': False, 'msg': 'This is not email address!' }

    @staticmethod
    def maxLength(value, length=15):
        if len(value) <= length:
            return { 'success': True }
        return { 'success': False, 'msg': 'The input is too long!' }

    @staticmethod
    def minLength(value, length=6):
        if len(value) >= length:
            return { 'success': True }
        return { 'success': False, 'msg': 'The input is too short!' }

class ItemBase:
    '''
        name, value, validators
    '''
    def __init__(self, name, *validators):
        self.name = name
        self.validators = validators
        self.value = ''

    def set_value(self, value):
        if len(value) == 1:
            self.value = value[0]
        else:
            self.value = value

    def get_value(self):
        return self.value

    def validate(self):
        for v in self.validators:
            if hasattr(Validators, v):
                result = getattr(Validators, v)(self.value)
                if not result['success']:
                    return result
        return {'success': True} 

class Input(ItemBase):
    def __init__(self, name, *validators):
        ItemBase.__init__(self, name, *validators)

class Email(ItemBase):
    def __init__(self, name):
        ItemBase.__init__(self, name, 'isEmail', 'notEmpty')

class Password(ItemBase):
    def __init__(self, name):
        ItemBase.__init__(self, name, 'notEmpty', 'minLength')

class Select(ItemBase):
    def __init__(self, name, *validators):
        ItemBase.__init__(self, name, *validators)
