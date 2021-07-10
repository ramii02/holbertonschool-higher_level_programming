#!/usr/bin/python3
""" Write a class """


class MyInt(int):
    """
    Initialize MyInt object
    """
    def __init__(self, num):
        if type(num) is super():
            self.__num = num

    """
    Override eq() and return not equal
    """
    def __eq__(self, obj):
        return False

    """
    Override ne() and return equal
    """
    def __ne__(self, obj):
        return True
