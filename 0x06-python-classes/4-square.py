#!/usr/bin/python3
"""Defining a class Square"""


class Square:
    """ Representing a square
    the attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """initializing the square
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
    def size(self, thevalue):
        """ setter of __size
        the Args:
            thevalue (int): the size of a size of the square
        Returns:
            None
        """
        if type(thevalue) is not int:
            raise TypeError("size must be an integer")
        else:
            if thevalue < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = thevalue
