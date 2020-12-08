#!/usr/bin/env python
# -*- coding: utf-8 -*-

def bubble_sort(list_: list) -> list:
    """Returns a sorted list, by bubble sort method
    
    :param list_: The list to be sorted
    :type list_: list

    :rtype: list
    :return: Sorted list, by bubble sort method
    """
    for i in range(len(list_)):
        for j in range(len(list_) - i - 1):
            if list_[j] > list_[j + 1]:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]

    return list_
