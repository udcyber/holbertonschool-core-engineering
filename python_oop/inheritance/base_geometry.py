#!/usr/bin/env python3
"""Create a class [BaseGeometry] with two methods"""
# [BaseGeometry] includes
# area(self) and
# integer_validator(self, name, value)


class BaseGeometry:
    """Definition of [BaseGeometry]"""
    # represents the area of a geometric shape
    def area(self):
        raise Exception("area() is not implemented")

    # validates that a value represents a valid positive integer
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
