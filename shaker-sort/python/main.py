#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def cocktail_shaker_sort(list_: list) -> list:
    """Returns a sorted list, by cocktail shaker sort method

    :param list_: The list to be sorted
    :type list_: list

    :rtype: list
    :return: Sorted list, by cocktail shaker sort method
    """
    higher = len(list_) - 1
    lower = 0

    Flag = False
    while not Flag and higher - lower > 1:
        Flag = True
        for j in range(lower, higher):
            if list_[j + 1] < list_[j]:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]
                Flag = False
        higher -= 1

        for j in range(higher, lower, -1):
            if list_[j - 1] > list_[j]:
                list_[j], list_[j - 1] = list_[j - 1], list_[j]
                Flag = False
        lower += 1

    return list_