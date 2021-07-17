#!/usr/bin/python3
import json


def load_from_json_file(filename):
    with open(filename, mode='r') as jfile:
        return json.loads(jfile.read())
