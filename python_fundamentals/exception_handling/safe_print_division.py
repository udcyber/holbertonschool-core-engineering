#!/usr/bin/env python3

def safe_print_division(a, b):
    """Divide two integers."""
    # Return:   the result
    #           or None
    try:
        div_result = a / b
    except Exception:
        div_result = None
    finally:
        print("Inside result: {}".format(div_result))
    return div_result
