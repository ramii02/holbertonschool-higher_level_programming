#!/usr/bin/python3
""" Write a function that returns True """


def inherits_from(obj, a_class):
    """  the object is an instance of a class that inherited """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
