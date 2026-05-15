#!/usr/bin/env python3
"""Add an instance methode [area(self)] to the [Square] class."""


class Square:
    """Define [Square]."""
    def __init__(self, size=0):
        """Initialize [Square] with [size].

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
    """Return the current square area."""
    return self.__size ** 2
