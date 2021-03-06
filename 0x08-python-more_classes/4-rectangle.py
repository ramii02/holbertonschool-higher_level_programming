#!/usr/bin/python3
"""defining a class Square"""


class Rectangle:
    """
    Rectangle Class
    Args:
        width (int): Rectangle width.
        heigth (int): Rectangle height
    """

    def __init__(self, width=0, height=0):
        """
        docstring on the __init__ method.
        Note:
            Do not include the `self` parameter in the ``Args`` section.
        Args:
            width (int): Rectangle width.
            heigth (int): Rectangle height
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Area method
        Args:
            width: The first parameter.
            height: The second parameter.
        Returns:
            Area of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * self.__height)

    def perimeter(self):
        """
        Perimeter method
        Args:
            width: The first parameter.
            height: The second parameter.
        Returns:
            Perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """
        String of the Rectangle
        Returns:
            The String of the rectangle.
        """
        r = ""
        if self.__height != 0 and self.__width != 0:
            r += '\n'.join(("#" * self.__width) for j in range(self.__height))
        return r

    def __repr__(self):
        """
        Representation of the Rectangle
        Returns:
            The representation of the rectangle.
        """
        return ('Rectangle({}, {})'.format(self.__width, self.__height))
