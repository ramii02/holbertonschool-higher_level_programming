#!/usr/bin/python3
""" read and prints it to stdout """


def read_file(filename=""):
    """ Write a function that reads a text file """
    with open(filename, 'r') as f:
        print(f.read(), end="
