"""
File: mad_py_lib.py
Author: Ravindu Gunasekara
Date: 09/11/2023
Section: 44
E-mail: rgunase1@umbc.edu
Description:
  Ask for inputs, then creates a poem
  using those inputs and outputs it.
"""
place = input("What is a place name? ")
noun1 = input("Give an example of a noun. ")
noun2 = input("Give an example of another noun. ")
family_relation = input("Give an example of a familial relation. ")
name = input("Give an example of a perrson's name. ")
noun3 = input("Give yet another noun. ")

print(f"There once was a man from {place}\nWho kept all his {noun1} in a {noun2}.\n    But his {family_relation}, named {name},\n    Ran away with a {noun3}\nAnd as for the {noun2}, {place}.")
