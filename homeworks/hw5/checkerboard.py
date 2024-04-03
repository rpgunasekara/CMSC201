"""
File: checkerboard.py
Author: Ravindu Gunasekara
Setion: 44
E-mail: rgunase1@umbc.edu
Date: 10/18/2023
Description:
    Asks user for a board size and symbols,
    then generates a checkerboard according
    to the inputs.
"""


def checkerboard(size, symbol_1, symbol_2):
    symbol_used = True

    for i in range(size):

        for j in range(size):

            if symbol_used == True:

                if j % 2 == 0:
                    print(symbol_1, end="")
                else:
                    print(symbol_2, end="")
            else:

                if j % 2 == 0:
                    print(symbol_2, end="")
                else:
                    print(symbol_1, end="")
# Works like a switch to determine what symbol starts the next row.
        if symbol_used == True:
            symbol_used = False
        else:
            symbol_used = True
        print()


if __name__ == "__main__":
    board_size = int(input("What size do you want? "))
    board_symbols = input("What symbols do you want? ")
    board_symbol_1 = ""
    board_symbol_2 = ""

    for i in board_symbols:

        if i != " ":
# If board_symbol_1 already has a value, then assign to board_symbol_2.
            if board_symbol_1 != "":
                board_symbol_2 = i
            else:
                board_symbol_1 = i
    checkerboard(board_size, board_symbol_1, board_symbol_2)
