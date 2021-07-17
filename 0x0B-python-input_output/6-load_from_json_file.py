#!/usr/bin/python3
"""load from json module """


def load_from_json_file(filename):
    """function that creates an obj """
    import json
    with open(filename, mode="r", encoding='utf-8') as f:
        return json.load(f)
