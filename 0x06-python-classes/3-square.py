#!/usr/bin/python3
""" defining a square """


class Square:
    """ the square with private instance attribute size """

    def __init__(myself, mysize=0):
        """
        the initializes square
        the Args:
            the size: size of side of square
        """

        if type(mysize) is int:
            if mysize < 0:
                raise ValueError('size must be >= 0')
            else:
                myself.__size = mysize
        else:
            raise TypeError('size must be an integer')

    def area(myself):
        """
        finding area of square
        Returns:
            the area of the square
        """

        return myself.__size ** 2
