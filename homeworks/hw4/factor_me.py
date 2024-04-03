"""
File: factor_me.py
Author: Ravindu Gunasekara
Date: 10/04/2023
Section: 44
E-mail: rgunase1@umbc.edu
Description:
    Using only prime numbers under
    50, takes the user input and
    finds it's factors, printing
    out the factors as well as
    value that couldn't be factored.
"""
if __name__ == "__main__":
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    factors = []

    factor_this = int(input("Enter a number to factor: "))

    for i in primes:
        while factor_this % i == 0:
            factors.append(str(i))
            factor_this /= i

    factors_string = "*".join(factors)

    if len(factors) > 0:
        print(f"The factors are: {factors_string}")
    else:
        print(f"We didn't find any factors.")

    if factor_this != 1:
        print(f"This part of the number couldn't be factored with primes less than 50: {int(factor_this)}")
