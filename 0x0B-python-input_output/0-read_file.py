#!/usr/bin/python3
""" read and prints it to stdout """


def read_file(filename=""):
    """ read and prints to stdout """
    with open(filename, 'r') as f:
        print(f.read(), end="
