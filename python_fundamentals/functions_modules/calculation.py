#!/usr/bin/env python3

if __name__ == "__main__":
    """print the result of:

    The 4 Rules of Number:
    - addition
    - subtraction
    - multiplication
    - division

    Arguments:
    a = 1st integer
    b = 2nd integer

    Return:
    the result value
    """
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
