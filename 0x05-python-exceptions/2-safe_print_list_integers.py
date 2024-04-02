#!/usr/bin/python3
# 2-safe_print_list_integers.py


def safe_print_list_integers(my_list=[], x=0):
    """Fonction: Print the first x elements of a list that are integers.

    Args:
        my_list (list)
        x (int): The number of elements of my_list to print.

    Returns:
        The number ofprinted elements.
    """
    zahl = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            zahl += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (zahl)
