#!/usr/bin/python3
'''JSON string module'''


import json


def to_json_string(my_obj):
    '''converts my_obj to JSON'''
    return json.dumps(my_obj)
