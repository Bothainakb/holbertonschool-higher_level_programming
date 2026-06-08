#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Return a list of True/False for multiples of 2."""
    new_list = []

    for num in my_list:
        new_list.append(num % 2 == 0)

    return new_list
