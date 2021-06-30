#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for k in a_dictionary:
        if k is key:
            del a_dictionary[k]
            break
    return a_dictionary
