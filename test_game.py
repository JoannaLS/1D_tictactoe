import pytest
from unittest.mock import patch
from tictactoe1d import check_winner, tictactoe, pc_move

# Test Evaluate (check_winner)

def test_check_winner_X():
    # Test an "X" win
    board = ["X", "X", "X", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
    assert check_winner(board, "X") is True

def test_check_winner_O():
    # Test an "O" win
    board = ["O", "O", "O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
    assert check_winner(board, "O") is True

def test_check_winner_no_win():
    # Test when the board is not full and there is no win
    board = ["X", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
    assert check_winner(board, "X") is False

def test_check_winner_full_board():
    # Test when the board is full but no win
    board = ["X", "O", "X", "X", "O", "X", "O", "X", "O", "O", "X", "O", "X", "O", "X", "O", "X", "X", "O", "X"]
    assert check_winner(board, "X") is False

# Test move

def test_pc_move_within_range():
    # Test if the random value generated is within range
    result = pc_move()
    assert 0 <= result < 21

def test_pc_move_consistency():
    # Test if the function produces different results 
    result1 = pc_move()
    result2 = pc_move()
    assert result1 != result2

# Had a really tough time going through this homework and I couldn't come up with another test for the evaluate/chech_winner function, so I just submited four. Sorry! 


# What is a Python module and how does it differ from a Python package?
    # A module is basicaly a Python file that contains functions that we may want to use in our program. A package is a group of modules that "make sense" to be together.

# What are side effects and give some examples.
    # A side-effect is when the module is actually giving us the result to the function or altering our program in some manner. The module should give us the function for us to include in our code and not the result of the function itself.
    # For example if in our module we use the "print" statment, when using the module we get that information printed. So we should not use this function.

# What are Exceptions and what to do if third-party code that we use throws them?
    # Exceptions are the error codes we get if something in our code is not right or if we are using the wrong input for example.
    # If a third-party code throws exceptions we could try to catch and handle those exceptions which could help us fix and improve the code or deal with the input in a different way.

# Using which keywords can you create, throw and catch your new custom Exception?
    # To create an exception we can create a new class that derives from the built-in Exception class. We can throw a new exception using the "raise" keywordn and catch exceptions using the "try/except" block. 

# Give examples of some benefits of testing?
    # By testing we can better understand how our code is working or where it is failing and work towards its improvement. So it can help us detect bugs, helps reduce time spent doing repetitive manual testing and helps us assure the quality of the code.