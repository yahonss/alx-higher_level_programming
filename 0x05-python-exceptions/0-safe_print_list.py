#!/usr/bin/python3
# Safa Hmimda
def safe_print_list(my_list=[], x=0):
    """safe_print_list Print x elememts of a list.
    Args:
        my_list
        nubmer
    Return:
        The number of elements printed.
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
