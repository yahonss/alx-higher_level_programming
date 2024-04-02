#!/usr/bin/python3
# 4-list_division.py


def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element.

    Args:
        my_list_1 (list): list number one.
        my_list_2 (list): list number two.
        list_length (int): The number of elements to be divided.

    Returns:
        A new list of length list_length containing all the divisions.
    """
    list_neu = []
    for i in range(0, list_length):
        try:
            division_result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            division_result = 0
        except ZeroDivisionError:
            print("division by 0")
            division_result = 0
        except IndexError:
            print("out of range")
            division_result = 0
        finally:
            new_list.append(division_result)
    return (list_neu)
