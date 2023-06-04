"""
A script file for use in testing ideas and debugging.
"""

from numpy import *
from get_zero import get_zero

def flattened_move(move):
    """
    Accepts move matrix, returns position of move in format "TL", "BR", etc.
    """
    # Flatten move
    flattened_move = [element for sublist in move for element in sublist]
    # Access a dictionary with move index: position
    # Note: A bit hacky and not utilising constants defined in board.py. Works for now.
    move_indexed = {0: "TL", 1: "TM", 2: "TR", 3: "ML", 4: "MM", 5: "MR", 6: "BL", 7: "BM", 8: "BR"}
    for index, value in enumerate(flattened_move):
        if value == 1:
            return move_indexed[index]


board1 = array([
    [1,-1, 0],
    [1, 0, 0],
    [-1, -1, 0]
])

board2 = array([
    [-1, 0, 0],
    [0, -1, 0],
    [0, 0, 1]
])

board3 = array([
    [0, 0, 0],
    [0, -1, 0],
    [0, 0, 0]
])

SET_BOARD = board3

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
        return flattened_move(move)
    
    """ 2) Do I move second? """
    if board_sum == PLAYER and board[1, 1] == EMPTY:
        # Is center free?
        move[1, 1] = SELF # → Move center.
        return flattened_move(move)
    elif board_sum == PLAYER and board[1, 1] != EMPTY:
        # Center taken:
        move[2, 2] = SELF # → Move corner.
        return flattened_move(move)

    """ 3) Can I win? """
    # Sum rows.
    row_sums = [0, 0, 0]
    for row in range(0, 3):
        for column in range(0, 3):
            row_sums[row] += board[row][column]
        # Check win condition exists:
        if row_sums[row] == 2:
            # → Move
            position = get_zero(board, 0, row)
            move[position[0], position[1]] = SELF
            return flattened_move(move)

    # Sum columns.
    column_sums = [0, 0 ,0]
    for column in range(0, 3):
        for row in range(0, 3):
            column_sums[column] += board[row][column]
        # Check win condition exists:
        if column_sums[column] == 2:
            # → Move
            position = get_zero(board, 1, column)
            print(f"position: {position}")
            move[position[0], position[1]] = SELF # → Move
            return flattened_move(move)

    # Sum diagonals.
    # Top left diagonal = 0 index, bottom left diagonal = 1 index.
    diagonal_sums = [0, 0]
    # Top left diagonal:
    for i in range(0, 3):
        diagonal_sums[0] += board[i, i]
    # Bottom left diagonal:
    for i in range(0, 3):
        diagonal_sums[1] += board[2 - i, i]
    # Check win condition exists:
    if diagonal_sums[0] == 2:
        # → Move
        position = get_zero(board, 2, 0)
        move[position[0], position[1]] = SELF # → Move
        return flattened_move(move)
    if diagonal_sums[1] == 2:
        # → Move
        position = get_zero(board, 2, 1)
        move[position[0], position[1]] = SELF # → Move
        return flattened_move(move)

    """ 4) Will I lose? """
    # Check sum of rows, columns, and diagonals are not -14.
    for row, sum in enumerate(row_sums):
        if sum == -14:
            # → Move
            position = get_zero(board, 0, row)
            move[position[0], position[1]] = SELF
            return flattened_move(move)

    for column, sum in enumerate(column_sums):
        if sum == -14:
            # → Move
            position = get_zero(board, 1, column)
            move[position[0], position[1]] = SELF # → Move
            return flattened_move(move)

    for diag, sum in enumerate(diagonal_sums):
        if sum == -14:
            # → Move
            position = get_zero(board, 2, diag)
            move[position[0], position[1]] = SELF # → Move
            return flattened_move(move)
            
    """ 5) I think next best move will always be pick a corner based on the logic so far """
    if board[0, 0] == EMPTY:
        move[0, 0] = SELF
        return flattened_move(move)
    if board[0, 2] == EMPTY:
        move[0, 2] = SELF
        return flattened_move(move)
    if board[2, 0] == EMPTY:
        move[2, 0] = SELF
        return flattened_move(move)
    if board[2, 2] == EMPTY:
        move[2, 2] = SELF
        return flattened_move(move)


    """ 6) The next best move is a non-move, simply fill an empty square. This should now always win? """
    for row in range(len(board)):
        for pos in range(len(board[row])):
            if board[row][pos] == EMPTY:
                move[row, pos] = SELF
                return flattened_move(move)


# Run decision logic.
position = logic()

print(f"__Board__: \n {board}")
print(f"__Move pos__:\n {move}")
print(f"Position: {position}")