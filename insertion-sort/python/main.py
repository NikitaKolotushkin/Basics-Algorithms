#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def insertion_sort(list_: list) -> list:
    """Returns a sorted list, by insertion sort method

    :param list_: The list to be sorted
    :type list_: list

    :rtype: list
    :return: Sorted list, by insertion sort method
    """
    for i in range(1, len(list_)):
        selected_element = list_[i]
        j = i - 1
        while j >= 0 and selected_element < list_[j]:
            list_[j + 1] = list_[j]
            j -= 1
        list_[j + 1] = selected_element
    return list_
