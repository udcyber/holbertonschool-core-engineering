#!/usr/bin/env python3
"""Add getters and setters for [size]"""
# the settes must validate input


class Square:
    """Defininition of [Square]"""
    def __init__(self, size=0):
        """Initialize [Square] with [size]

            Arguments:
                size: the size of the square

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

    # getter
    @property
    def size(self):
        """Return the size of the square"""
        return self.__size

    # setter
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
