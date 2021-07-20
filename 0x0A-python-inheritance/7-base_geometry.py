#!/usr/bin/python3
""" basegeometry class """


class BaseGeometry:
    """ calculations """

    def area(self):
        """ area calculations """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates integer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
