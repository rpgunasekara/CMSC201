"""
File: how_deep.py
Author: Ravindu Gunasekara
Date: 11/10/2023
Section: 44
E-mail: rgunase1@umbc.edu
Description:
    Given various lists, or using the
    provided function to create one,
    use recursion to find the innermost
    list, or the 'max_depth'.
"""
import random

def how_deep(list_struct):
    # Base case, for empty list [].
    if len(list_struct) == 0:
        return 1
    else:
        max_depth = 0
        # Searches through each index till it hits an empty list.
        # Then adds up all the 1's and compares the sum (sublist_depth) to the current max_depth.
        for sublist in list_struct:
            sublist_depth = how_deep(sublist)
            if sublist_depth > max_depth:
                max_depth = sublist_depth

        return max_depth + 1


def make_list_structure(max_depth, p=.8):
    if max_depth and random.random() < p:
        new_list = []
        for i in range(5):
            sub_list = make_list_structure(max_depth - 1, p * .9)
            if sub_list is not None:
                new_list.append(sub_list)
        return new_list

    return None


if __name__ == '__main__':
    print(how_deep([[[], [], [], [[[]]]], []]))
    print(how_deep([]))
    print(how_deep([[], []]))
    print(how_deep([[[]], [], [[]], [[[]]]]))
    print(how_deep([[[[], [[]], [[[]]], [[[[]]]]]]]))
    print(how_deep([[[], []], [], [[], []]]))
