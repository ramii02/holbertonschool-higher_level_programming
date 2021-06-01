#!/usr/bin/python3
""" Write a function that returns True """


def is_kind_of_class(obj, a_class):
    """  the object is an instance of, or if the object is an instance of a class """
    if isinstance(obj, a_class):
        return True
    return False
