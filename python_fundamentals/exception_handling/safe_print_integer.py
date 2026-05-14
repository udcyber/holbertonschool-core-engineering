#!/usr/bin/env python3

def safe_print_integer(value):
    """Print an integer with \"{:d}\".format() followed by a new line."""
    """Return:  True if value is an integer"""
    """         False otherwise"""
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False


print()
