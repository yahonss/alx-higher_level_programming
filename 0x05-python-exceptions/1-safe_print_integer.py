#!/usr/bin/python3
# 1-safe_print_integer.py

def safe_print_integer(value):
    """Fonction: Print an integer with "{:d}".format().

    Args:
        value (int): The integer to be printed.

    Returns:
        If a TypeError or ValueError - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
