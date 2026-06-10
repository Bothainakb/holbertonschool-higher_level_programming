#!/usr/bin/python3
def safe_print_integer(value):
    """Prints an integer and returns True, otherwise False."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
