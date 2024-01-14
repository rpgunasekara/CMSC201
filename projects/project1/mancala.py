"""
File: mancala.py
Author: Ravindu Gunasekara
Date: 11/01/2023
Section: 44
E-mail: rgunase1@umbc.edu
Description:
    Manipulating lists, creates a playable
    game of mancala.
"""

BLOCK_WIDTH = 6
BLOCK_HEIGHT = 5
BLOCK_SEP = "*"
SPACE = ' '


def draw_board(top_cups, bottom_cups, mancala_a, mancala_b):
    """
    draw_board is the function that you should call in order to draw the board.
        top_cups and bottom_cups are lists of strings. Each string should be length BLOCK_WIDTH and each list should be of length BLOCK_HEIGHT.
        mancala_a and mancala_b should be 2d lists of strings. Each string should be BLOCK_WIDTH in length, and each list should be 2 * BLOCK_HEIGHT + 1

    :param top_cups: This should be a list of strings that represents cups 1 to 6 (Each list should be at least BLOCK_HEIGHT in length, since each string in the list is a line.) 
    :param bottom_cups: This should be a list of strings that represents cups 8 to 13 (Each list should be at least BLOCK_HEIGHT in length, since each string in the list is a line.)
    :param mancala_a: This should be a list of 2 * BLOCK_HEIGHT + 1 in length which represents the mancala at position 7.
    :param mancala_b: This should be a list of 2 * BLOCK_HEIGHT + 1 in length which represents the mancala at position 0.
    """
    board = [[SPACE for _ in range((BLOCK_WIDTH + 1) * (len(top_cups) + 2) + 1)] for _ in range(BLOCK_HEIGHT * 2 + 3)]
    for p in range(len(board)):
        board[p][0] = BLOCK_SEP
        board[p][len(board[0]) - 1] = BLOCK_SEP

    for q in range(len(board[0])):
        board[0][q] = BLOCK_SEP
        board[len(board) - 1][q] = BLOCK_SEP

    # draw midline
    for p in range(BLOCK_WIDTH + 1, (BLOCK_WIDTH + 1) * (len(top_cups) + 1) + 1):
        board[BLOCK_HEIGHT + 1][p] = BLOCK_SEP

    for i in range(len(top_cups)):
        for p in range(len(board)):
            board[p][(1 + i) * (1 + BLOCK_WIDTH)] = BLOCK_SEP

    for p in range(len(board)):
        board[p][1 + BLOCK_WIDTH] = BLOCK_SEP
        board[p][len(board[0]) - BLOCK_WIDTH - 2] = BLOCK_SEP

    for i in range(len(top_cups)):
        draw_block(board, i, 0, top_cups[i])
        draw_block(board, i, 1, bottom_cups[i])

    draw_mancala(0, mancala_a, board)
    draw_mancala(1, mancala_b, board)

    print('\n'.join([''.join(board[i]) for i in range(len(board))]))


def draw_mancala(fore_or_aft, mancala_data, the_board):
    """
    draw_mancala is a helper function for the draw_board function.

    :param fore_or_aft: front or back (0, or 1).
    :param mancala_data: a list of strings of length 2 * BLOCK_HEIGHT + 1 each string of length BLOCK_WIDTH
    :param the_board: a 2d list of characters which we are creating to print the board.
    """
    if fore_or_aft == 0:
        for i in range(len(mancala_data)):
            data = mancala_data[i][0: BLOCK_WIDTH].rjust(BLOCK_WIDTH)
            for j in range(len(mancala_data[0])):
                the_board[1 + i][1 + j] = data[j]
    else:
        for i in range(len(mancala_data)):
            data = mancala_data[i][0: BLOCK_WIDTH].rjust(BLOCK_WIDTH)
            for j in range(len(mancala_data[0])):
                the_board[1 + i][len(the_board[0]) - BLOCK_WIDTH - 1 + j] = data[j]


def draw_block(the_board, pos_x, pos_y, block_data):
    """
    draw_block is a helper function for the draw_board function.

    :param the_board: the_board is the 2d grid of characters we're filling in.
    :param pos_x: which cup it is
    :param pos_y: upper or lower
    :param block_data: the list of strings to put into the block.
    """
    for i in range(BLOCK_HEIGHT):
        data = block_data[i][0:BLOCK_WIDTH].rjust(BLOCK_WIDTH)
        for j in range(BLOCK_WIDTH):
            the_board[1 + pos_y * (BLOCK_HEIGHT + 1) + i][1 + (pos_x + 1) * (BLOCK_WIDTH + 1) + j] = data[j]
            

# Basic True/False validation.
def get_player(player_1):
    if player_1 == True:
        player = input("Player 1 please tell me your name: ")
    else:
        player = input("Player 2 please tell me your name: ")
    
    return player


def take_turn(player, player_1, cups, top_cups, bottom_cups, mancala_b, mancala_a):
    cup = 0
    # Validate chosen cup to move.
    while cup < 1 or cup > 13 or cup == 7 or int(cups[cup]) == 0:
        cup = int(input(f"{player[3]}, what cup do you want to move? "))
        if cup < 1 or cup > 13 or cup == 7 or int(cups[cup]) == 0:
            print("Please move a valid cup.")

    # Setup for moving the stones around.
    current_cup = cup
    stones_in_hand = int(cups[cup])
    cups[cup] = 0

    # Moves stones till none left.
    while stones_in_hand > 0:
        current_cup = (current_cup + 1) % 14
        # Avoids putting stones in other player's mancala.
        if (player_1 == True and current_cup == 0) or (player_1 == False and current_cup == 7):
            current_cup = (current_cup + 1) % 14
        cups[current_cup] = int(cups[current_cup]) + 1
        stones_in_hand -= 1
        
    # If the last stone lands in current player's mancala.
    while (player_1 == True and current_cup == 7) or (player_1 == False and current_cup == 0):
        print("Your last stone landed in a mancala. \nGo again please...")
        
        # Update values.
        mancala_b[8] = str(cups[0])
        for row in range(BLOCK_WIDTH):
            top_cups[row][3] = str(cups[row + 1])

        mancala_a[8] = str(cups[7])
        bottom_cups[5][3] = str(cups[8])
        bottom_cups[4][3] = str(cups[9])
        bottom_cups[3][3] = str(cups[10])
        bottom_cups[2][3] = str(cups[11])
        bottom_cups[1][3] = str(cups[12])
        bottom_cups[0][3] = str(cups[13])
        
        # .rjust() the lists and draw_board()
        top_cups = fix_2d(top_cups)
        bottom_cups = fix_2d(bottom_cups)
        mancala_a = fix_1d(mancala_a)
        mancala_b = fix_1d(mancala_b)
        draw_board(top_cups, bottom_cups, mancala_b, mancala_a)
        
        # Makes sure player hasn't won already before asking for a move.
        if check_cups_1d(cups) == False:
            cup = 0
            # Validate chosen cup to move.
            while cup < 1 or cup > 13 or cup == 7 or int(cups[cup]) == 0:
                cup = int(input(f"{player[3]}, what cup do you want to move? "))
                if cup < 1 or cup > 13 or cup == 7 or int(cups[cup]) == 0:
                    print("Please move a valid cup.")
            
            # Setup for moving the stones around.
            current_cup = cup
            stones_in_hand = int(cups[cup])
            cups[cup] = 0
            
            # Move stones till none left.
            while stones_in_hand > 0:
                current_cup = (current_cup + 1) % 14
                # Avoids putting stones in other player's mancala.
                if (player_1 == True and current_cup == 0) or (player_1 == False and current_cup == 7):
                    current_cup = (current_cup + 1) % 14
                cups[current_cup] = int(cups[current_cup]) + 1
                stones_in_hand -= 1
    
    # Convert to str to not mess with draw_board()
    for i in range(len(cups)):
        cups[i] = str(cups[i])

    return cups


# Checks if the row has no more stones. Meant for 2D lists.
def check_cups_2d(cups):
    count = 0
    for row in range(BLOCK_WIDTH):
        if int(cups[row][3]) == 0:
            count += 1
    if count == 6:
        return True
    else:
        return False

# Checks if the row has no more stones. Meant for 1D lists.
# (Solves problem of player winning and current_cup == their mancala.)
def check_cups_1d(cups):
    top_count = 0
    bottom_count = 0
    if int(cups[1]) == 0:
        top_count += 1
    elif int(cups[2]) == 0:
        top_count += 1
    elif int(cups[3]) == 0:
        top_count += 1
    elif int(cups[4]) == 0:
        top_count += 1
    elif int(cups[5]) == 0:
        top_count += 1
    elif int(cups[6]) == 0:
        top_count += 1
    elif int(cups[8]) == 0:
        bottom_count += 1
    elif int(cups[9]) == 0:
        bottom_count += 1
    elif int(cups[10]) == 0:
        bottom_count += 1
    elif int(cups[11]) == 0:
        bottom_count += 1
    elif int(cups[12]) == 0:
        bottom_count += 1
    elif int(cups[13]) == 0:
        bottom_count += 1
    
    if top_count == 6:
        return True
    elif bottom_count == 6:
        return True
    else:
        return False


# .rjust() each index. Meant for 2D lists.
def fix_2d(list_2d):
    for row in range(BLOCK_WIDTH):
        for col in range(BLOCK_HEIGHT):
            list_2d[row][col] = list_2d[row][col].rjust(BLOCK_WIDTH)

    return list_2d


# .rjust() each index. Meant for 1D lists.
def fix_1d(list_1d):
    for row in range(2 * BLOCK_HEIGHT + 1):
        list_1d[row] = list_1d[row].rjust(BLOCK_WIDTH)

    return list_1d


# Makes a list to hold stone values of each cup in order.
def stones_list(top_cups, bottom_cups, mancala_b, mancala_a):
    cups = []
    
    cups.append(mancala_b[8])
    for row in range(BLOCK_WIDTH):
        cups.append(top_cups[row][3])
    
    cups.append(mancala_a[8])
    cups.append(bottom_cups[5][3])
    cups.append(bottom_cups[4][3])
    cups.append(bottom_cups[3][3])
    cups.append(bottom_cups[2][3])
    cups.append(bottom_cups[1][3])
    cups.append(bottom_cups[0][3])

    return cups


def run_game():
    # True/False to determine what prompt for get_player()
    is_player_a = True
    player_a = get_player(is_player_a)
    is_player_a = False
    player_b = get_player(is_player_a)
    
    # Made lists then called some functions to not mess with starter code.
    top_pits = [["Cup", "1", "Stones", "4", ""], 
                ["Cup", "2", "Stones", "4", ""], 
                ["Cup", "3", "Stones", "4", ""], 
                ["Cup", "4", "Stones", "4", ""], 
                ["Cup", "5", "Stones", "4", ""], 
                ["Cup", "6", "Stones", "4", ""]]
    bottom_pits = [["Cup", "13", "Stones", "4", ""], 
                   ["Cup", "12", "Stones", "4", ""], 
                   ["Cup", "11", "Stones", "4", ""], 
                   ["Cup", "10", "Stones", "4", ""], 
                   ["Cup", "9", "Stones", "4", ""], 
                   ["Cup", "8", "Stones", "4", ""]]
    bank_a = ["", "", "", player_a, "", "", "", "Stones", "0", "", ""]
    bank_b = ["", "", "", player_b, "", "", "", "Stones", "0", "", ""]
    top_pits = fix_2d(top_pits)
    bottom_pits = fix_2d(bottom_pits)
    bank_a = fix_1d(bank_a)
    bank_b = fix_1d(bank_b)
    draw_board(top_pits, bottom_pits, bank_b, bank_a)

    # Makes list to use in take_turn()
    pits = stones_list(top_pits, bottom_pits, bank_b, bank_a)

    # Loops until one row has no more stones.
    player_a_turn = True
    while check_cups_2d(top_pits) == False and check_cups_2d(bottom_pits) == False:
        if player_a_turn == True:
            player_bank = bank_a
            pits = take_turn(player_bank, player_a_turn, pits, top_pits, bottom_pits, bank_b, bank_a)
            player_a_turn = False
            
            # Update values.
            bank_a[8] = pits[7]
            for row in range(BLOCK_WIDTH):
                top_pits[row][3] = pits[row + 1]
            
            bank_b[8] = pits[0]
            bottom_pits[5][3] = pits[8]
            bottom_pits[4][3] = pits[9]
            bottom_pits[3][3] = pits[10]
            bottom_pits[2][3] = pits[11]
            bottom_pits[1][3] = pits[12]
            bottom_pits[0][3] = pits[13]
        else:
            player_bank = bank_b
            pits = take_turn(player_bank, player_a_turn, pits, top_pits, bottom_pits, bank_b, bank_a)
            player_a_turn = True
            
            # Update values.
            bank_a[8] = pits[7]
            for row in range(BLOCK_WIDTH):
                top_pits[row][3] = pits[row + 1]

            bank_b[8] = pits[0]
            bottom_pits[5][3] = pits[8]
            bottom_pits[4][3] = pits[9]
            bottom_pits[3][3] = pits[10]
            bottom_pits[2][3] = pits[11]
            bottom_pits[1][3] = pits[12]
            bottom_pits[0][3] = pits[13]
        
        # Fix lists before printing board.
        top_pits = fix_2d(top_pits)
        bottom_pits = fix_2d(bottom_pits)
        bank_a = fix_1d(bank_a)
        bank_b = fix_1d(bank_b)
        draw_board(top_pits, bottom_pits, bank_b, bank_a)
    
    # Determines the winner.
    if int(bank_a[8]) > int(bank_b[8]):
        print(f"{player_a} is the winner!")
    else:
        print(f"{player_b} is the winner!")

if __name__ == "__main__":
    run_game()
