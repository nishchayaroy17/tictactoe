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
    x=0
    o=0
    for i in range(3):
        for j in range(3):
            if board[i][j]==X:
                x+=1
            elif board[i][j]==O:
                o+=1
    if (x>o):
        return O
    elif (x==o):
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions=set()
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                possible_actions.add((i,j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    move=player(board)
    board[action[0]][action[1]]=move
    return(board)


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if all(cell != EMPTY for row in board for cell in row) or utility(board) != 0:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            if board[i][0]==X:
                return 1
            else:
                return -1
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            if board[0][i]==X:
                return 1
            else:
                return -1
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        if board[1][1]==X:
            return 1
        else:
            return -1
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        if board[1][1]==X:
            return 1
        else:
            return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    raise NotImplementedError
