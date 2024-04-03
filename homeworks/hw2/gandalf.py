"""
File: gandalf.py
Author: Ravindu Gunasekara
Date: 09/18/2023
Section: 44
E-mail: rgunase1@umbc.edu
Description:
    Uses if/elif/else as well as nested if/elif/else statements
    to create a Lord of the Rings quiz.
"""
race = input("Which race are you? (human/dwarf/elf/maiar/hobbit) ").lower()

if race == "human":
    king = input("Are you the King of Gondor? ").lower()
    if king == "yes":
        print("You are Aragorn, son of Arathorn.")
    elif king == "no":
        ring = input("Did you try to take the ring from Frodo? ").lower()
        if ring == "yes":
            print("You are Boromir.")
        elif ring == "no":
            print("You are Theoden, probably.")
elif race == "dwarf":
    print("You are Gimli, son of Gloin.")
elif race == "elf":
    matrix = input("Were you in The Matrix? ").lower()
    if matrix == "yes":
        print("You are Elrond.")
    elif matrix == "no":
        print("You are Legolas.")
elif race == "maiar":
    good_or_evil = input("Are you good or evil? ").lower()
    if good_or_evil == "good":
        print("You are Gandalf.")
    elif good_or_evil == "evil":
        forge = input("Did you forge the One Ring? ").lower()
        if forge == "yes":
            print("You are Sauron.")
        elif forge == "no":
            print("You are Saruman.")
elif race == "hobbit":
    carry = input("Do you carry the One Ring? ").lower()
    if carry == "yes":
        print("You are Frodo Baggins")
    elif carry == "no":
        gardener = input("Are you a gardener? ").lower()
        if gardener == "yes":
            print("You are Samwise.")
        elif gardener == "no":
            print("You are either Merry or Pippin.")
else:
    print("You are an Orc.")
