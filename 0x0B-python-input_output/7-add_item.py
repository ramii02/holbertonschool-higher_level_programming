#!/usr/bin/python3
import sys


load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

filename = "add_item.json"
try:
    prevl = load_from_json_file(filename)
except Exception as e:
    prevl = []
i = 0
while i < len(sys.argv) - 1:
    i += 1
    prevl.append(sys.argv[i])
save_to_json_file(prevl, filename)
