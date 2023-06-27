#!/usr/bin/python3

"""Defining a class Square."""


class Square:
    """the Represent a square."""

    def __init__(self, size=0, pos=(0, 0)):
        """Initializing a new square.
        Args:
            the size (int): The size of the new square.
            the pos (int, int): The position of the new square.
        """
        self.size = size
        self.pos = pos
    @property
    def size(self):
        """Get the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, thevalue):
        if not isinstance(thevalue, int):
            raise TypeError("size must be an integer")
        elif thevalue < 0:
            raise ValueError("size must be >= 0")
        self.__size = thevalue

    @property
    def pos(self):
        """Get/set the current position of the square."""
        return (self.__position)

    @pos.setter
    def pos(self, thevalue):
        if (not isinstance(thevalue, tuple) or
                len(thevalue) != 2 or
                not all(isinstance(num, int) for num in thevalue) or
                not all(num >= 0 for num in thevalue)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = thevalue

    def area(self):
        """Returning the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Printing the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
