#!/usr/bin/env python3
"""Contains [Square]."""

class Square:
    """Define a class with a private instance attribute [size]"""
    # the size must be set when the object is created
    def __init__(self, size=0):
        """Initialize [size], [size] is private
        
            Arguments:
                size: the size of the square
        """
        self.__size = size
