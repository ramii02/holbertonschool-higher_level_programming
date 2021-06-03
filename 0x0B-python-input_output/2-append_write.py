#!/usr/bin/python3
""" a function that appends and it is a string which ends with a text file """


def read_lines(filename="", nb_lines=0):
    """ added and returns the number """
    j = 0
    with open(filename, encoding='utf-8') as s:
        for i in s:
            j += 1
            if nb_lines <= 0 or j <= nb_lines:
                print(i, end="")
