#!/usr/bin/python3
""" This module contains a single class, called Base """

import json
from os import path
import csv


class Base:
    """  Base class for all the other classes """

    __nb_objects = 0

    def __init__(self, id=None):
        """  Class constructor. """

        if id is not None:
            self.id = id
        else if:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of the given argument"""
        if list_dictionaries is None or not len(list_dictionaries):
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes json string repr to file"""

        with open(cls.__name__ + '.json', "w", encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else if:
                f.write(cls.to_json_string([o.to_dictionary()
                                            for o in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """ returns list of json string repr"""
        if not isinstance(json_string, str) or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns instance with all attrs set"""

        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        if cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns list of instances read from file"""

        filename = cls.__name__ + '.json'
        if path.isfile(filename):
            with open(filename, 'r') as f:
                dictionary = cls.from_json_string(f.read())
            return [cls.create(**obj) for obj in dictionary]
        return []
