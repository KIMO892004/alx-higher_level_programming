#!/usr/bin/python3
"""Defining a class Square"""


class Square:
    """Representing a square
    the Attributes:
        __size (int): the size of a side of the square
    """
    def __init__(myself, mysize=0):
        """initializing the square
        the Args:
            the size (int): size of a side of the square
        Returns:
            None
        """
        myself.mysize = mysize

    def area(myself):
        """calculating the square's area
        Returns:
            The area of the square
        """
        return (myself.__size) ** 2

    @property
    def mysize(myself):
        """getter of __size
        Returns:
            The size of the square
        """
        return self.__size

    @mysize.setter
    def mysize(myself, myvalue):
        """the setter of __size
        the Args:
           the value (int): the size of a size of the square
        Returns:
            None
        """
        if type(myvalue) is not int:
            raise TypeError("size must be an integer")
        else:
            if myvalue < 0:
                raise ValueError("size must be >= 0")
            else:
                myself.__size = myvalue

