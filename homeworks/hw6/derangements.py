"""
File: derangements.py
Author: Ravindu Gunasekara
Date: 11/10/2023
Section: 44
E-mail: rgunase1@umbc.edu
Description:
    Uses a recursive function to find the
    number of derangements in a set of elements
    given a recursive formula.
"""

def derangement(element):
    if element == 0:
        return 1
    else:
        # Translated the formula into code.
        # Dn = n       * Dn-1                     + (-1)^n
        return element * derangement(element - 1) + (-1) ** element


if __name__ == "__main__":
    for i in range(20):
        print(i, derangement(i))
