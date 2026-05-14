#!/usr/bin/env python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x integer elements of a list."""
    # skip elements that are not integers
    # my_list can contain any type
    # Return: the number of integers printed
    int_printed = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (IndexError):
            raise
        except Exception:
            pass
        else:
            int_printed += 1
    print()
    return int_printed
