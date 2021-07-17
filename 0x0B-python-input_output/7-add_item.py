#!/usr/bin/python3
'''Load, add, save module'''

import sys
import json


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


filename = 'add_item.json'
try:
    new = load_from_json_file(filename)
except:
    new = []
finally:
    for i in range(1, len(sys.argv)):
        new.append(sys.argv[i])
    save_to_json_file(new, filename)
