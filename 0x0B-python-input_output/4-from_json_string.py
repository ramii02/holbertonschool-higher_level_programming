#!/usr/bin/python3
'''append to a file module'''


def append_write(filename="", text=""):
    '''appends text to end of file'''
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
