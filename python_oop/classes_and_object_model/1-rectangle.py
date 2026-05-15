#!/usr/bin/env python3
"""Define a class [Square] with a private instance attribute [size]"""


class Square:
    """Definition of [Square]"""
    def __init__(self, size=0):
        """Initialize [Square] with [size], [size] is private

            Arguments:
                size: the size of the square
        """
        self.__size = size
