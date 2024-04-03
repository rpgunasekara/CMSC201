"""
File: distance.py
Author: Ravindu Gunasekara
Date: 09/11/2023
Section: 44
E-mail: rgunase1@umbc.edu
Description:
  Asks the user for two points, then
  calculates the distance between the
  two points and outputs the result.
"""
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is {((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1/2))}.")
