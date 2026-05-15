#!/usr/bin/env python3
"""Create a class Square that inherits from Rectangle"""


Rectangle = __import__("2-rectangle").Rectangle


class Square(Rectangle):
    """Definition of Square"""
    def __init__(self, size):
        # call the parent class Rectangle's __init__
        super().__init__(size, size)
