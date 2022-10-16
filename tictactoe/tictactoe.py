"""
Tic Tac Toe Player
"""
import math
import copy

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
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                action = (i, j)
                possible_actions.add(action)
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row = action[0]
    col = action[1]
    if board[row][col] is not EMPTY:
        raise Exception("Invalid action")

    resultant_board = copy.deepcopy(board)
    resultant_board[row][col] = player(board)

    return resultant_board


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
    # Another way of improving this algorithm besides alpha-beta pruning is by caching AI responses to some boards.
    # For example: if AI starts, minimax will call max_value and min_value 551242 times before returning an actions
    # WHICH is always the same actions. If we cache that anwer (and some more, check test_cache.py) AI will be so fast
    # json.dumps(initial_board) could be the key and the answer would be (0,1) or the resulting board.

    if terminal(board):
        return None

    current_player = player(board)
    if current_player == X:
        return max_value(board)[1]

    else:
        return min_value(board)[1]


def max_value(board):
    if terminal(board):
        return [utility(board), None]

    best_value = -math.inf
    best_action = tuple()
    for action in actions(board):
        partial_best = min_value(result(board, action))[0]
        if best_value < partial_best:
            best_value = partial_best
            best_action = action

    return [best_value, best_action]


def min_value(board):
    if terminal(board):
        return [utility(board), None]

    best_value = math.inf
    best_action = tuple()
    for action in actions(board):
        partial_best = max_value(result(board, action))[0]
        if best_value > partial_best:
            best_value = partial_best
            best_action = action

    return [best_value, best_action]
