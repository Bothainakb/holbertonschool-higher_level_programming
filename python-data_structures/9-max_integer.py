#!/usr/bin/python3
def max_integer(my_list=[]):
    """Find the biggest integer in a list."""
    if len(my_list) == 0:
        return None

    maximum = my_list[0]

    for num in my_list:
        if num > maximum:
            maximum = num

    return maximum
