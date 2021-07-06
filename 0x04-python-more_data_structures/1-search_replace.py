#!/usr/bin/python3
"""
Defining write_file Function
"""


def write_file(filename="", text=""):
    '''
    write_file Function
    '''
    with open(filename, mode="w") as fl:
        return fl.write(text)
