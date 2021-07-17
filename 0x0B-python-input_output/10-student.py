#!/usr/bin/python3
'''Student to JSON with filter module'''


class Student:
    '''class student'''
    def __init__(self, first_name, last_name, age):
        '''initialize attributes first_name, last_name, age'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''retrieves a dictionary'''
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
