#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def shell_sort(list_: list) -> list:
    """Returns a sorted list, by shell sort method

    :param list_: The list to be sorted
    :type list_: list

    :rtype: list
    :return: Sorted list, by shell sort method
    """
    half = len(list_) // 2
    while half > 0:
        for i in range(half, len(list_)):
            tmp = list_[i]
            j = i
            while j >= half and list_[j - half] > tmp:
                list_[j] = list_[j - half]
                j -= half
            list_[j] = tmp
        half //= 2
    return list_
