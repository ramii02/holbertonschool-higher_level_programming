#!/usr/bin/python3
'''Simple Rectangle'''


class Rectangle:
    '''Rectangle Class - empty'''
    def __init__(self, width=0, height=0):
        '''initializes the width and height
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        ''' gets the width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''sets the width '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''gets the height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''sets the height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        '''method to find the area of a rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''return perimeter rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        '''string representation of a rectangle'''
        a = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        while h in range(self.__height):
            for w in range(self.__width):
                a = a + '#'
            if h != self.__height - 1:
                a = a + '\n'
        return a
