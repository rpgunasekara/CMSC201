"""
File: tricky_lock.py
Author: Ravindu Gunasekara
Date: 09/18/2023
Section: 44
E-mail: rgunase1@umbc.edu
Description:
    User inputs values to unlock a combination lock.
    Different inputs lead to different results.
"""
first_number = int(input("What is the first number in the combination lock? "))
second_number = int(input("What is the second number in the combination lock? "))
first_switch = input("What is the position of the first switch (up/down)? ").lower()
second_switch = input("What is the position of the second switch (up/down)? ").lower()
third_switch = input("What is the position of the third switch (up/down)? ").lower()

if first_number + second_number == 36:
    if first_switch == "up" and second_switch == "up" and third_switch == "down":
        print("The lock opens, you gain access to the treasure.")
    elif first_switch == "up" and second_switch == "down" and third_switch == "up":
        print("The lock opens, you gain access to the treasure.")
    elif first_switch == "down" and second_switch == "up" and third_switch == "up":
        print("The lock opens, you gain access to the treasure.")
    else:
        print("The lock clanks but does not open.")
elif first_number + second_number != 36:
    if first_switch == "up" and second_switch == "up" and third_switch == "down":
        print("The lock clanks but does not open.")
    elif first_switch == "up" and second_switch == "down" and third_switch == "up":
        print("The lock clanks but does not open.")
    elif first_switch == "down" and second_switch == "up" and third_switch == "up":
        print("The lock clanks but does not open.")
    else:
        print("The lock does not even budge, try again.")
