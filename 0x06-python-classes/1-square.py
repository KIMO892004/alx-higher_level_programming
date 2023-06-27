#!/usr/bin/python3
"""the square class definition"""


class Square:
    """Representing a square
    the attributes:
        __size (int): the size of a side of the square
    """
    def __init__(myself, mysize):
        """Initializing a square
        the Args:
            the size (int): size of a side of the square
        Returns: None
        """
        myself.__size = mysize
