"""
File: pascal.py
Author: Ravindu Gunasekara
Setion: 44
E-mail: rgunase1@umbc.edu
Date: 10/18/2023
Description:
    Using Pascal's triangle, calculate
    and output the following row of
    numbers from the starting list.
"""


def next_level(level):
    new_level = []
# Using a for loop in order to use the values as needed.
    for i in range(len(level)):
# Makes the starting value always 1.
        if i == 0:
            new_level.append(1)
        else:
            new_level.append(level[i] + level[i - 1])
# Makes the end value always 1.
    new_level.append(1)
    level = new_level

    return level


if __name__ == "__main__":
    level = [1]

    for i in range(10):

        for x in level:
            print(x, end="\t")

        print()
        level = next_level(level)
