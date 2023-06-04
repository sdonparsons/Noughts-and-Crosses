"""
A script file for use in testing ideas and debugging.
"""

from numpy import *
from get_zero import get_zero


board1 = array([
    [1, 0, 0],
    [0, 0, 0],
    [-1, -1, 0]
])

board2 = array([
    [-1, 0, 0],
    [0, -1, 0],
    [0, 0, 1]
])

board3 = array([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
])

# Set where we move, using array:
move = array([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
])

SET_BOARD = board1

""" _______BOARD SETUP ETC_______ """

# 1) TODO: normalise move.
# Check am I negative or positive.
# If negative then convert to positive

SELF = 1
PLAYER = -7
EMPTY = 0

# 2) change -1's to -7s
for element in nditer(SET_BOARD, op_flags=['readwrite']):
    if element == -1:
        element[...] = -7

# Set which board to test the logic:
board = SET_BOARD
print(board)
print((board))

print(range(len(board)))

print("_____________")

""" 1) Do I move first? (i.e. Is board empty?) """
# TODO: Solve this faster in program by testing self.turn.turn value.
# TODO: Could use numpy.nditer as more concise way of solving.
board_sum = 0 # Total board sum.
for row in range(len(board)):
    for pos in range(len(board[row])):
        board_sum += board[row][pos] # Sum board values.

if board_sum == 0:
    # → First move in center:
    move[1, 1] = 1

""" 2) Do I move second? """
if board_sum == PLAYER and board[1, 1] == EMPTY:
    # Is center free?
    move[1, 1] = SELF # → Move center.
elif board_sum == PLAYER and board[1, 1] != EMPTY:
    # Center taken:
    move[2, 2] = SELF # Move corner.

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

# Sum columns.
column_sums = [0, 0 ,0]
for column in range(0, 3):
    for row in range(0, 3):
        column_sums[column] += board[row][column]
    # Check win condition exists:
    if column_sums[column] == 2:
        print("ERROR SAUCE?")
        print(f"Column: {column}")
        # → Move
        position = get_zero(board, 1, column)
        print(f"position: {position}")
        move[position[0], position[1]] = SELF # → Move

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
if diagonal_sums[1] == 2:
    # → Move
    position = get_zero(board, 2, 1)
    move[position[0], position[1]] = SELF # → Move

print("_____DEUBUGGING_____")
print(f"Column sums: {column_sums}")
print(f"Row sums: {row_sums}")
print(f"Diagonal sums: {diagonal_sums}")

""" 4) Will I lose? """
# Check sum of rows, columns, and diagonals are not -14.
for row, sum in enumerate(row_sums):
    if sum == -14:
        # → Move
        position = get_zero(board, 0, row)
        move[position[0], position[1]] = SELF

for column, sum in enumerate(column_sums):
    if sum == -14:
        # → Move
        position = get_zero(board, 1, column)
        move[position[0], position[1]] = SELF # → Move

for diag, sum in enumerate(diagonal_sums):
    if sum == -14:
        # → Move
        position = get_zero(board, 2, diag)
        move[position[0], position[1]] = SELF # → Move

""" 5) I think next best move will always be pick a corner based on the logic so far """
if board[0, 0] == EMPTY:
    move[0, 0] = SELF
if board[0, 2] == EMPTY:
    move[0, 2] = SELF
if board[2, 0] == EMPTY:
    move[2, 0] = SELF
if board[2, 2] == EMPTY:
    move[2, 2] = SELF


""" 6) The next best move is a non-move, simply fill an empty square. This should now always win? """
for row in range(len(board)):
    for pos in range(len(board[row])):
        if board[row][pos] == EMPTY:
            move[row, pos] = SELF

# TODO: Not sure I need move array. Maybe use just position - two numbers?

print("____BOARD:____")
print(board)

print("____MOVE:____")
print(move)



