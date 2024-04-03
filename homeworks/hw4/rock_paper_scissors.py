"""
File: rock_paper_scissors.py
Author: Ravindu Gunasekara
Date: 10/02/2023
Section: 44
E-mail: rgunase1@umbc.edu
Description:
    User plays rock, paper, scissors
    with the computer. After inputting
    their choice, computer generates a
    choice at random, prints the result.
"""
import sys
from random import choice, seed

if len(sys.argv) >= 2:
    seed(sys.argv[1])

if __name__ == "__main__":
    user_choice = ""

    while user_choice != "stop":
        the_choice = choice(["rock", "paper", "scissors"])
        user_choice = input("Enter rock, paper, or scissors to play, stop to end. ").lower()
        if user_choice == "rock":
            if the_choice == "rock":
                print("Both rock, there is a tie.")
            if the_choice == "paper":
                print("Paper covers rock, you lose.")
            if the_choice == "scissors":
                print("Rock crushes scissors, you win.")
        elif user_choice == "paper":
            if the_choice == "rock":
                print("Paper covers rock, you win.")
            if the_choice == "paper":
                print("Both paper, there is a tie.")
            if the_choice == "scissors":
                print("Scissors cut paper, you lose.")
        elif user_choice == "scissors":
            if the_choice == "rock":
                print("Rock crushes scissors, you lose.")
            if the_choice == "paper":
                print("Scissors cut paper, you win.")
            if the_choice == "scissors":
                print("Both scissors, there is a tie.")
        else:
            if user_choice != "stop":
                print("You need to select rock, paper, or scissors.")
