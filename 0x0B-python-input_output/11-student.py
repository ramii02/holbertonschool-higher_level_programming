#!/usr/bin/python3
'''Student to disk and reload module'''


class Student:
    '''student class'''
    def __init__(self, first_name, last_name, age):
        '''initialize atributes first_name last_name age'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''retrieves a dictionary representation of instance'''
        new = {}
        if attrs is None:
            return self.__dict__
        else:
            for i in attrs:
                if i in self.__dict__:
                    new[i] = self.__dict__[i]
                else:
                    continue
            return new

    def reload_from_json(self, json):
        '''replaces all attributes of student instance'''
        for key, value in json.items():
            self.__dict__[key] = value
