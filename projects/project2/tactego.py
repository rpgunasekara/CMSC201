"""
File: tactego.py
Author: Ravindu Gunasekara
Date: 11/18/2023
Section: 44
E-mail: rgunase1@umbc.edu
Description:
    Sets up a game of Tactego using
    a 2D list of strings, various
    functions, and casting.
"""
import random

# Global Variables
P_RED = "R"
P_BLUE = "B"


# Reads a file of pieces and returns a list with the information organized.
def get_pieces(pieces_file):
    pieces = []
    file = open(pieces_file, 'r')
    
    for line in file:
        line = line.strip().split()
        strength = line[0]
        count = int(line[1])

        if strength == 'F':
            pieces.append(['F', count])
        else:
            pieces.append([int(strength), count])
  
    return pieces


# Makes the board and places the players' pieces on it.
def initialize_board(length, width, red_pieces, blue_pieces):
    board = []
    
    for row in range(length):
        board.append([])
        
        for col in range(width):
            board[row].append(' ')

    row_count = 0
    col_count = 0
    
    for piece in red_pieces:
        strength = piece[0]
        count = piece[1]
        
        for num_of_type in range(count):
            board[row_count][col_count] = f'{P_RED}{strength}'
            col_count += 1
            
            if col_count == width:
                col_count = 0
                row_count += 1

    row_count = length - 1
    col_count = 0
    
    for piece in blue_pieces:
        strength = piece[0]
        count = piece[1]
        
        for num_of_type in range(count):
            board[row_count][col_count] = f'{P_BLUE}{strength}'
            col_count += 1
           
            if col_count == width:
                col_count = 0
                row_count -= 1

    return board


# Prints board, row/col indices are printed too.
def draw_board(board):
    col_indices = ''
    
    for i in range(len(board[0])):
        col_indices += str(i).rjust(5) + ' '
    print(f'  {col_indices}')

    row_count = 0
    
    for row in board:
        row_pieces = f'{row_count} '
        col_count = 0
        
        for col in row:
            row_pieces += col.rjust(5) + ' '
            col_count += 1
        print(row_pieces)
        row_count += 1
    print()


# Asks for inital coordinates and final coordinates.
def make_move():
    initial = input('Select Piece to Move by Position: ').split()
    final = input('Select Position to Move Piece: ').split()
   
    return(f'{initial[0]}{initial[1]}{final[0]}{final[1]}')


# Validates inital and final, if invalid goes again.
def valid_move(board, player_move, player):
    if board[int(player_move[0])][int(player_move[1])] == ' ' or board[int(player_move[0])][int(player_move[1])][0] != player or board[int(player_move[0])][int(player_move[1])][1] == 'F':
        return False
    
    if not (0 <= int(player_move[2]) < len(board) and 0 <= int(player_move[3]) < len(board[0])) or board[int(player_move[2])][int(player_move[3])][0] == player:
        return False

    row_diff = int(player_move[2]) - int(player_move[0])
    col_diff = int(player_move[3]) - int(player_move[1])

    if (row_diff == 1 or row_diff == -1) and col_diff == 0:
        return True
    elif row_diff == 0 and (col_diff == 1 or col_diff == -1):
        return True
    elif (row_diff == 1 or row_diff == -1) and (col_diff == 1 or col_diff == -1):
        return True

    return False


# Moves piece from initial, outcome varies depending on final.
def piece_move(board, player_move):
    piece = board[int(player_move[0])][int(player_move[1])]
    board[int(player_move[0])][int(player_move[1])] = ' '
    
    if board[int(player_move[2])][int(player_move[3])] == ' ':
        board[int(player_move[2])][int(player_move[3])] = piece
    else:
        opponent_piece = board[int(player_move[2])][int(player_move[3])]
        
        if pieces_combat(piece, opponent_piece):
            board[int(player_move[2])][int(player_move[3])] = piece
        else: 
            board[int(player_move[2])][int(player_move[3])] = opponent_piece


# Uses strength (or if a flag) to determine outcome.
def pieces_combat(attacker, defender):
    if attacker[1] >= defender[1]:
        return True
    
    if defender[1] == 'F':
        return True
  
    return False


# Determines if there is a winner.
def tactego_winner(board):
    no_red = True
    no_blue = True
    
    for row in board:
        if 'RF' in row:
            no_red = False
        if 'BF' in row:
            no_blue = False
  
    if no_red and not no_blue:
        draw_board(board)
        print('B has won the game.')
      
        return True
    elif no_blue and not no_red:
        draw_board(board)
        print('R has won the game.')
       
        return True
    else:
        return False


# Main function for game.
def tactego(pieces_file, length, width):
    pieces = get_pieces(pieces_file)

    red_pieces = list(pieces)
    blue_pieces = list(pieces)
    random.shuffle(red_pieces)
    random.shuffle(blue_pieces)

    board = initialize_board(length, width, red_pieces, blue_pieces)
    current_turn = 0

    while tactego_winner(board) == False:
        draw_board(board)
        if current_turn == 0:
            move = make_move()

            while not valid_move(board, move, P_RED):
                print('Invalid move.')
                move = make_move()

            piece_move(board, move)  
            current_turn = 1  
        elif current_turn == 1:
            move = make_move()

            while not valid_move(board, move, P_BLUE):
                print('Invalid move.')
                move = make_move()

            piece_move(board, move)
            current_turn = 0


# Main
if __name__ == '__main__':
    random.seed(input('What is the seed? '))
    file_name = input('What is the filename for the pieces? ')
    length = int(input('What is the length? '))
    width = int(input('What is the width? '))
    tactego(file_name, length, width)
