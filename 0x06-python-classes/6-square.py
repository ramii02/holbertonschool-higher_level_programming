#!/usr/bin/python3
'''Define class Square '''


class Square():
    '''create square object'''
    def __init__(self, size=0, position=(0, 0)):
        ''' initialize size'''
        self.size = size
        self.position = position

    def area(self):
        '''calculate the area of square '''
        return self.__size * self.__size

    def my_print(self):
        ''' print out the square in #'''
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    @property
    def size(self):
        ''' retrieve the size'''
        return self.__size

    @size.setter
    def size(self, value):
        ''' set the value to size '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        ''' position of the square'''
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
