"""
File: creature_combat.py
Author: Ravindu Gunasekara
Date: 09/18/2023
Section: 44
E-mail: rgunase1@umbc.edu
Description:
    Uses user inputs to create two creatures,
    then has them fight each other, using math
    to determine the outcome.
"""
creature_one_name = input("What is the name of the first creature? ")
creature_one_power = int(input("What is the power of the first creature? "))
creature_one_toughness = int(input("What is the toughness of the first creature? "))
creature_two_name = input("What is the name of the second creature? ")
creature_two_power = int(input("What is the power of the second creature? "))
creature_two_toughness = int(input("What is the toughness of the second creature? "))

print(f"The first creature now has ({creature_one_power}, {creature_one_toughness-creature_two_power})")
print(f"The second creature now has ({creature_two_power}, {creature_two_toughness-creature_one_power})")

if creature_one_toughness - creature_two_power <= 0 and creature_two_toughness - creature_one_power <= 0:
    print(f"Both creatures die in mutual combat.")
elif creature_one_toughness - creature_two_power > 0 and creature_two_toughness - creature_one_power > 0:
    print(f"Both creatures live to fight another day.")
elif creature_one_toughness - creature_two_power < creature_two_toughness - creature_one_power:
    print(f"{creature_one_name} has died, {creature_two_name} wins.")
elif creature_two_toughness - creature_one_power < creature_one_toughness - creature_two_power:
    print(f"{creature_two_name} has died, {creature_one_name} wins.")
