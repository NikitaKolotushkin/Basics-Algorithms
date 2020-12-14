#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def quick_sort(list_: list) -> list:
    """Returns a sorted list, by quick sort method
    
    :param list_: The list to be sorted
    :type list_: list

    :rtype: list
    :return: Sorted list, by quick sort method
    """
    if len(list_) < 2:
        return list_
    else:
        axis = list_[0]
        lower = [el for el in list_[1:] if el <= axis]
        greater = [el for el in list_[1:] if el > axis]
        return quick_sort(lower) + [axis] + quick_sort(greater)