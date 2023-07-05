#!/usr/bin/python3
"""
Defining a class Rectangle
"""


class Rectangle:
    """Representation of a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializing the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, myvalue):
        """setter for the private instance attribute width"""
        if type(myvalue) is not int:
            raise TypeError("width must be an integer")
        if myvalue < 0:
            raise ValueError("width must be >= 0")
        self.__width = myvalue

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, myvalue):
        """setter for the private instance attribute height"""
        if type(myvalue) is not int:
            raise TypeError("height must be an integer")
        if myvalue < 0:
            raise ValueError("height must be >= 0")
        self.__height = myvalue

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
