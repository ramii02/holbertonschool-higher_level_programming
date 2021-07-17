#!/usr/bin/python3
""" writes object to text file """


def save_to_json_file(my_obj, filename):
    """ save to json """
    if type(filename) != str:
        raise TypeError("filename must be a string")
    import json
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
