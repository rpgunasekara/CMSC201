"""
File: binary.py
Author: Ravindu Gunasekara
Date: 11/10/2023
Section: 44
E-mail: rgunase1@umbc.edu
Description:
    Uses a recursive function to
    determine the binary representation
    of a number, then compares it
    using bin().
"""

def binary(number):
    if number == 0:
        return '0'
    else:
        # Document gave the example of 5, worked that logic into code.
        # First floor division to get 2, then modulus to get 1.
        # Would return ((('0') '1') '0') '1'.
        return binary(number // 2) + str(number % 2)


if __name__ == "__main__":
    x = int(input("Tell me a number: "))
    while x != -1:
        # Sliced the function call because it added an extra 0 in front.
        # Because of base case.
        print('0b' + binary(x)[1:], bin(x))
        x = int(input("Tell me a number: "))
