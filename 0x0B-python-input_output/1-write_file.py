#!/usr/bin/python3
""" writes string to a text file """


def write_file(filename="", text=""):
    """ write to file """
    with open(filename, mode='w', encoding='utf-8') as f:
        a = f.write(text)
    return a
