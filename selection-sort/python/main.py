#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def selection_sort(list_: list) -> list:
    """Returns a sorted list, by selection sort method

    :param list_: The list to be sorted
    :type list_: list

    :rtype: list
    :return: Sorted list, by selection sort method
    """
    def find_smallest_index(list_: list) -> int:
        """Returns the index of the smallest element

        :param list_: The list to be sorted
        :type list_: list

        :rtype: int
        :return: Index of the smallest element
        """
        smallest = list_[0]
        smallest_index = 0
        for i in range(1, len(list_)):
            if list_[i] < smallest:
                smallest = list_[i]
                smallest_index = i
        return smallest_index

    new_list = []
    for _ in range(len(list_)):
        new_list.append(list_.pop(find_smallest_index(list_)))
    return new_list
