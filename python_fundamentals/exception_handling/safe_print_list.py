#!/usr/bin/env python3

def safe_print_list(my_list=[], x=0):
    """Print x elements of a list."""
    count = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
        except Exception:
            break
        else:
            count += 1
    print()
    return count
