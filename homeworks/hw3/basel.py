"""
File: basel.py
Author: Ravindu Gunasekara
Date: 09/25/2023
Section: 44
E-mail: rgunase1@umbc.edu
Description:
    Asks user for an integer and uses
    that to solve the Basel problem
    up to the number inputted.
"""
basel = int(input("What is the number of terms you want to sum? "))
total = 0

for i in range(basel):
    total += (1 / ((i + 1) ** 2))
print(f"The approximation for {basel} terms is {total}")
