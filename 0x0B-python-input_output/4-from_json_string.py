#!/usr/bin/python3
""" returns an object repped by JSON """


import json


def from_json_string(my_str):
    """ returns object """
    return json.loads(my_str)
