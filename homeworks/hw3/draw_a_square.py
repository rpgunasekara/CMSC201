"""
File: draw_a_square.py
Author: Ravindu Gunasekara
Date: 09/25/2023
Section: 44
E-mail: rgunase1@umbc.edu
Description:
    Asks for a size, then prints
    a square border using asterisks
    in that size (4 by 4, etc).
"""
size = int(input("What is the size of the square that we want to draw? "))

for i in range(size):
    for j in range(size):
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print(f"*", end = "")
            if j == size - 1:
                print()
        else:
            print(" ", end = "")
