"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # if there is an odd number of EMPTY slots, it's X turn
    # if there is an even number of EMPTY slots, it's O turn
    empty_count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                empty_count += 1
    return O if empty_count % 2 == 0 else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]

    return None


def board_filled(board):
    """
    Returns True if some slot is empty, False otherwise.
    """
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                return False
    return True


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or board_filled(board):
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if winner_player is None:
        return 0
    if winner_player == X:
        return 1
    if winner_player == O:
        return -1


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
