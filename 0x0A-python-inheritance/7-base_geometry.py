#!/usr/bin/python3
"""Same class or inherit from module"""


class BaseGeometry:
    """Using the class"""
    def area(self):
        """that raises an Exception with the message area()
           is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to check values
        Args: Value and Name
        Return: Raises errors
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
