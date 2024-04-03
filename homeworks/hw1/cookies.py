"""
File: cookies.py
Author: Ravindu Gunasekara
Date: 09/11/2023
Section: 44
E-mail: rgunase1@umbc.edu
Description:
  Asks for an input of the nuber of batches of
  cookies, then outputs the required ingredients.
"""
batches = float(input("How many batches of cookies do you want to make? "))

print("You Need: ")
print("    ", batches * 2.25, "cups of flour")
print("    ", batches * 2, "sticks of butter")
print("    ", batches * 0.75, "cups of granulated sugar")
print("    ", batches * 0.75, "cups of brown sugar")
print("    ", batches * 1, "teaspoon of vanilla extract")
print("    ", batches * 1, "teaspoon of baking soda")
print("    ", batches * 1, "teaspoon of salt")
print("    ", batches * 2, "cups of chocolate chips")
