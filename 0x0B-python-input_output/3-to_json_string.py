#!/usr/bin/python3
'''write string to a file module'''


def write_file(filename="", text=""):
    '''write to file'''
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
