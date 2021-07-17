#!/usr/bin/python3
""" funct that returns the JSON representation of an object string """


import json


def to_json_string(my_obj):
    """ returns the JSON """
    return (json.dumps(my_obj))
