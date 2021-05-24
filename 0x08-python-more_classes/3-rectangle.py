#!/usr/bin/python3
""" Rectangle that defines a rectangle by: (based on 2-rectangle.py) """

class Rectangle:
    """ Write a class Rectangle that defines a rectangle """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        return 2 * self.__height + 2 * self.__width

    def __str__(self):
        if self.__height <= 0 or self.__width <= 0:
            return ""
        str_h = ""
        for i in range(self.__height):
            str_h += "#" * self.__width
            str_h += '\n'
        return str_h[:-1]
