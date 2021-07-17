#!/usr/bin/python3
""" function that appends a string at the end of a text """


def append_write(filename="", text=""):
    """ appends string to end of text file """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
