#!/usr/bin/python3
'''Student to JSON module'''


class Student:
    '''class student'''
    def __init__(self, first_name, last_name, age):
        '''itialize atribute first_name, last_name, age'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''return a private dictionary'''
        return self.__dict__
