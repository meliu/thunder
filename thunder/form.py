#coding=utf-8
import re
import tornado.escape

class Form:
    def __init__(self, **kwargs):
        self.items = []
        self.values = {}
        self.kwargs = kwargs
        self.msg = ''

    def add(self, item):
        self.items.append(item)
        
    def validate(self):
        for k in self.kwargs:
            for item in self.items:
                if item.name == k:
                    item.set_value(kwargs[k])

        for item in self.items:
            result = item.validate()
            if result['success']:
                self.values[item.name] = item.get_value()
            else:
                self.msg = result['msg']
                return False return True

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
        self.name = self.name
        self.validators = validators

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def validate(self):
        for v in validators:
            if hasattr(Validators, v):
                result = getattr(Validators, v)(self.value)
                if not result['success']:
                    return result
        return {'success': True} 

class Input(ItemBase):
    '''
    Input('email', 'isEmail', 'notEmpty')
    '''
    def __init__(self, name, *validators):
        self.type = 'text'
        ItemBase.__init__(self, name, *validators)

class Select(ItemBase):
    def __init__(self, name, *validators):
        self.type = 'select'
        ItemBase.__init__(self, name, *validators)
