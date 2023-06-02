from numpy import *
from get_zero import get_zero

board1 = array([
    [1,-1, 0],
    [0, 1, 0],
    [1, -1, 0]
])

board2 = array([
    [-1, 0, 0],
    [0, -1, 0],
    [0, 0, 1]
])

board3 = array([
    [0, 0, 0],
    [0, -7, 0],
    [0, 0, 0]
])

SET_BOARD = board1

""" _______BOARD SETUP ETC_______ """

# 1) TODO: normalise move.
# Check am I negative or positive.
# If negative then convert to positive

# CONSTANTS
SELF = 1
PLAYER = -7
EMPTY = 0

# 2) change -1's to -7s
for element in nditer(SET_BOARD, op_flags=['readwrite']):
    if element == -1:
        element[...] = -7

# Set which board to test the logic:
board = SET_BOARD
array_board = SET_BOARD

""" _______DECISION LOGIC_______ """

# 0) Set where we move, using list:
move = array([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
])

def logic():

    """ 1) Do I move first? (i.e. Is board empty?) """
    # TODO: Solve this faster in program by testing self.turn.turn value?
    board_sum = EMPTY # Total board sum.
    for row in range(len(board)):
        for pos in range(len(board[row])):
            board_sum += board[row][pos] # Sum board values.
    
    if board_sum == 0:
        # → First move in center:
        move[1, 1] = 1
        return
    
    """ 2) Do I move second? """
    if board_sum == PLAYER and board[1, 1] == EMPTY:
        # Is center free?
        move[1, 1] = SELF # → Move center.
        return
    elif board_sum == PLAYER and board[1, 1] != EMPTY:
        # Center taken:
        move[2, 2] = SELF # → Move corner.
        return

    # **) Block forks??

# Run decision logic.
logic()

print(f"__Board__: \n {board}")

#TODO: Convert next move from move to matrix position, i.e. TR, TL, etc..
# Flatten move
# Access a dictionary with move index: position
# {0: TL}, {2: TM}, {3: TR}, etc
print(f"__Move pos__:\n {move}")
# If move empty, error...