"""
File: ab_equality.py
Author: Ravindu Gunasekara
Date: 11/10/2023
Section: 44
E-mail: rgunase1@umbc.edu
Description:
    Uses a recursive function to
    print out all strings of a's
    and b's of length n so that the
    number of a's and b's are equal.
"""

def ab_equal(n, k, current):
    # Print only when equal number of a's and b's, and length is 0.
    if n == 0 and k == 0:
        # Gets rid of the initial ' '.
        print(current[1:])
        return

    # Creates strings of length n and changes k's value.
    # The if statement above filters through all of this using k.
    if n > 0:
        ab_equal(n - 1, k + 1, current + 'a')
        ab_equal(n - 1, k - 1, current + 'b')


if __name__ == "__main__":
    num = int(input("What length do you want to run? "))
    ab_equal(num, 0, ' ')
