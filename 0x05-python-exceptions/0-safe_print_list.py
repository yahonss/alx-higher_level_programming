#!/usr/bin/python3
# Safa Hmimda
def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to be printed.

    Returns:
        The number of printed elements.
    """
    zahl = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            zahl += 1
        except IndexError:
            break
    print("")
    return(zahl)
