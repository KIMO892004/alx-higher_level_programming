#!/usr/bin/python3
"""Defining a class Square"""


class Square:
    """the Represents a square
    the Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """initializes the square
       the Args:
            the size (int): size of a side of the square
        Returns:
            None
        """
       self.size = size

    def area(self):
        """calculating the square's area
        Returns:
            The area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """ getter of __size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, myvalue):
        """ setter of __size
        the Args:
            the myvalue (int): the size of a size of the square
        Returns:
            None
        """
        if type(myvalue) is not int:
            raise TypeError("size must be an integer")
        else:
            if myvalue < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = myvalue
