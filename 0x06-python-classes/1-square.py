#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(myself, mysize):
        """Initializes a square
        Args:
            size (int): size of a side of the square
        Returns: None
        """
        myself.__size = mysize
