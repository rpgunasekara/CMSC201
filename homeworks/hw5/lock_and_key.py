"""
File: lock_and_key.py
Author: Ravindu Gunasekara
Setion: 44
E-mail: rgunase1@umbc.edu
Date: 10/17/2023
Description:
    Given two lists of key cuts and lock pinnings
    and a minimum difference, the function
    determines whether or not the lock will open.
"""


def lock_and_key(key_cuts, lock_pinning, minimum):
    locked_or_unlocked = True
# Checks that the list lengths are the same, key won't work otherwise.
    if len(key_cuts) == len(lock_pinning):

        for i in range(len(key_cuts)):
# This is the equation 6 - m <= c + p <= 6 + m.
            if (key_cuts[i] + lock_pinning[i]) <= (6 + minimum) and (key_cuts[i] + lock_pinning[i]) >= (6 - minimum):
                locked_or_unlocked = True
            else:
                locked_or_unlocked = False
    else:
        locked_or_unlocked = False

    return locked_or_unlocked


if __name__ == "__main__":

    if lock_and_key([2.1, 3.5, 2.7], [4.1, 2.5, 3.2], 0.25):
        print('Unlocked')
    else:
        print('Still Locked')

    if lock_and_key([2.1, 3.5, 2.7, 1.7], [4.1, 2.5, 3.2], 0.25):
        print('Unlocked')
    else:
        print('Still Locked')

    if lock_and_key([2.1, 3.5, 2.7, 1.7], [4.1, 2.5, 3.2, 3.2], 0.25):
        print('Unlocked')
    else:
        print('Still Locked')
