#!/usr/bin/python3
""" defines a square """


class Square:
    """ square with private instance attribute size """

    def __init__(myself, mysize=0):
        """
        Args:
            size: size of square
        """

        if type(mysize) is int:
            if mysize < 0:
                raise ValueError('size must be >= 0')
            else:
                myself.__size = mysize
        else:
            raise TypeError('size must be an integer')
