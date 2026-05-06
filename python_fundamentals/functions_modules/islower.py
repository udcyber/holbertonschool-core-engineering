#!/usr/bin/env python3

# Check if c is a lowercase letter
# Return: True if c is a lowercase letter
# Return: False otherwise

# Given Function
def islower(c):
    """Check if c is a lowercase letter"""
    if c >= 97 and c <= 122:
        return True
    else:
        return False
