'CustomMeta implementation'


class CustomMeta(type):
    '''
    CustomMeta implements metaclass which adds 'custom_' prefix
    to all fields and methods of the produced class
    (except those which start and end with '__')
    '''

    def __new__(cls, name, bases, dct):
        new_class_dict = {}
        for key, val in dct.items():
            new_class_dict[CustomMeta.customize_name(key)] = val

        def custom_setattr(self, key, val):
            self.__dict__[CustomMeta.customize_name(key)] = val

        new_class_dict['__setattr__'] = custom_setattr
        res = type(name, bases, new_class_dict)
        return res

    @staticmethod
    def customize_name(name):
        '''
        Adds "custom_" prefix for names without "__"
        both at the end and the begining
        '''
        if name.startswith('__') and name.endswith('__'):
            return name
        return f'custom_{name}'
