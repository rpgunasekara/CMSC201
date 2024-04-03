"""
File: leap_year.py
Author: Ravindu Gunasekara
Date: 09/18/2023
Section: 44
E-mail: rgunase1@umbc.edu
Description:
    Asks for an input (a year), then
    goes through a nested if/elif/else
    statement to determine whether or not
    that year is a leap year.
"""
year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        print("It is not a leap year.")
    elif year % 400 == 0:
        print("It is a leap year.")
    else:
        print("It is a leap year.")
elif year % 4 != 0:
    print("It is not a leap year.")
