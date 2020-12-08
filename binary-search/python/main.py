#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def binary_search(list_: list, item: int = 0):
    """Returns the index of the number to find in the SORTED list

    :param list_: SORTED list to find the item
    :type list_: list
    :param item: The number to find the index
    :type item: int 

    :rtype: int, else: None
    :return: The index of the number found
    """
    lowest = 0
    highest = len(list_) - 1

    while lowest <= highest:
        middle = int((lowest + highest) / 2)
        guess = list_[middle]
        if guess == item:
            return middle
        if guess > item:
            highest = middle - 1
        else:
            lowest = middle + 1

    return None