#!/usr/bin/python3
""" read from a file and prints it to stdout """


def read_file(filename=""):
    with open(filename, 'r') as f:
        print(f.read(), end="")
