#!/usr/bin/env python3


# Output info
def pow(a, b):
    """return the result value of a raised to the power of b"""
    result = 1
    # _ here means "the loop counter is not used"
    for _ in range(b):
        result *= a

    return result
