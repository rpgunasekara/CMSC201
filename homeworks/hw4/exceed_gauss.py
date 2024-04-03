"""
File: exceed_gauss.py
Author: Ravindu Gunasekara
Date: 10/02/2023
Section: 44
E-mail: rgunase1@umbc.edu
Description:
    Asks user for input, then performs
    the Gauss sum until the sum passes
    or is equal to the inputted value.
"""
if __name__ == "__main__":
    test_number = int(input("What number do you want to test? "))
    gauss_sum = 0
    iterations = 0
    while gauss_sum < test_number:
        gauss_sum += iterations + 1
        iterations += 1

    print(f"After {iterations} iterations, the gauss sum is {gauss_sum} which exceeds (or is equal to) the number {test_number}.")
