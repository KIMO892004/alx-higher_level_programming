#!/usr/bin/python3
"""Defining a class Square"""


class Square:
    """the Represents a square
    the Attributes:
        __size (int): size of a side of the square
    """
    def __init__(myself, mysize=0):
        """initializes the square
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
    def size(myself):
        """the getter of __size
        Returns:
            The size of the square
        """
        return myself.__size

    @size.setter
    def size(myself, myvalue):
        """the setter of __size
        Args:
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

