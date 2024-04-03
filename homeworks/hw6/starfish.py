"""
File: starfish.py
Author: Ravindu Gunasekara
Date: 11/10/2023
Section: 44
E-mail: rgunase1@umbc.edu
Description:
    Prints a dictionary containing
    the number of starfish over a
    number of generations, where
    5-legged starfish get split into
    5 1-legged starfish and others
    grow a leg.
"""

def starfish(leg_list, generations):
    # Base case, sends the leg_list after iterations to count_starfish.
    if generations == 0:
        return leg_list

    # List to hold updated values.
    temp_leg_list = []

    for i in range(len(leg_list)):
        if leg_list[i] == 5:
            temp_leg_list.append(1)
            temp_leg_list.append(1)
            temp_leg_list.append(1)
            temp_leg_list.append(1)
            temp_leg_list.append(1)
        else:
            temp_leg_list.append(leg_list[i] + 1)

    # Calls starfish() with new leg_list.
    return starfish(temp_leg_list, generations - 1)


def count_starfish(leg_list):
    leg_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

    for x in leg_list:
        leg_counts[x] += 1

    return leg_counts


if __name__ == "__main__":
    print(count_starfish(starfish([1, 2, 3, 4, 5], 3)))
    print(count_starfish(starfish([2, 4, 5], 10)))
    print(count_starfish(starfish([5, 5, 5], 1)))
    print(count_starfish(starfish([1], 20)))
    print(count_starfish(starfish([5, 5, 5, 5, 5], 5)))
