#!/usr/bin/env python3

def best_score(a_dictionary):
    "return the key with the biggest integer value"
    value = 0
    key = ""
    if a_dictionary is None:
        return (None)
    else:
        for x, y in a_dictionary.items():
            if y > value:
                value = y
                key = x
    if value == 0:
        return (None)
    return (key)
