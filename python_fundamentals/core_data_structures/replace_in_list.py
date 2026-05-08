#!/usr/bin/ev python3

def replace_in_list(my_list, idx, element):
    """replace an element of a list at a specific position"""
    if 0 <= idx < len(my_list):
        my_list[idx] = element
        return (my_list)
