#!/usr/bin/env python3
"""Print the square according to position parameters"""


class Square:
    """Defininition of [Square]"""
    def __init__(self, size=0):
        """Initialize [Square] with [size]

            Arguments:
                sizea: the size of the square

            Raises:
                Typerror: size is not an integer
                ValueError: size is negative
        """
        # raise exceptions
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        # size is private
        self.__size = size

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size

    # getter for size
    @property
    def size(self):
        """Return the size of the square"""
        return self.__size

    # setter for size
    @size.setter
    def size(self, value):
        """Set a value for the size of the square

        Arguments:
            value: the value set for the size of the square
        """
        # raise same exceptions as for [size]
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    # print the square
    def my_print(self):
        """"Print the square with #"""
        if self.__size == 0:
            print()
            return
        print("{}".format("\n" * self.__position[1]), end="")
        print("{}".format("\n".join(
            [" " * self.__position[0] + "#" * self.__size] * self.__size)))

    # getter for position
    @property
    def position(self):
        """Return the position of the square"""
        return self.__position

    # setter for position
    @position.setter
    def position(self, value):
        """Set a value for the position of the square

        Arguments:
            value: the value set for the position of the square
        """
        if isinstance(value, tuple) and \
                len(value) == 2 and \
                isinstance(value[0], int) and \
                isinstance(value[1], int) and \
                value[0] >= 0 and \
                value[1] >= 0:

            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integer")
