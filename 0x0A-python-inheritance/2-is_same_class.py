#!/usr/bin/python3
""" Write a function that returns True """


def is_same_class(obj, a_class):
    """  the object is exactly an instance of the specified class """
    if type(obj) is a_class:
        return True
    return False
