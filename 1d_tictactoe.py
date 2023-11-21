import random

from random import randrange

def print_board(board):
    print("".join(board))

def check_winner(board, mark):
    for i in range(len(board) - 2):
        if board[i:i+3] == [mark] * 3:
            return True
    return False

def tictactoe():
    board = ["-"] * 20
    mark = "X" or "O"

    print("This is the game board:")
    print_board(board)

    for play in range(20):  
        try:
            player_move = int(input("Please enter your move (1-20): ")) - 1
            if player_move not in range(21):
                print("That is not a valid number. Try again.")
            elif board[player_move] == "-":
                board[player_move] = mark
                print_board(board)

                if check_winner(board, mark):
                    print(f"Player {mark} wins!")
                    break

                pc_move = randrange(21)
                while board[pc_move] != "-":
                    pc_move = randrange(21)

                board[pc_move] = "O"
                print(f"Computer chose {pc_move + 1}")
                print_board(board)

                if check_winner(board, "O"):
                    print("Computer wins!")
                    break
            else:
                print("That position is already taken! Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 20.")
    

    else:
        print("It's a draw!")

tictactoe()