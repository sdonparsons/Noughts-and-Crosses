from numpy import *

def get_zero(array, type, index):
    """
    Will return one-dimensional list size two: containing the co-ordinates of element zero in a 3x3 array.

    This will work for row, column, or diagonal, where there is only one element that equals zero.
    
    :param matrix: The 3x3 array.
    :param type: 0 = row, 1 = column, 2 = diagonal. 
    :param index: 0, 1, 2 for row or column index. 0, 1 for diagonal index.
    :return: One dimensional list size two. Return 1 if error.
    """

    # Check valid array.
    # Should have three rows:
    if len(array) != 3:
        print("ERROR: Array not 3x3.")
        return 1
    # Each row should have three columns.
    for row in range(len(array)):
        if len(array[row]) != 3:
            print("ERROR: Array not 3x3.")
            return 1
        
    # Check valid usage.
    if type not in range(0,3) or index not in range(0,3):
        print("ERROR: Type or index usage undefined: 0-2 only.")
        return 1

    # Find empty position in a row.
    if type == 0:
        for i in range(0, 3):
            if board[index, i] == 0:
                return [index, i]
    
    # Find empty position in a column.
    if type == 1:
        print(f"get_zero: COLUMN\nColumn index: {index}")
        for i in range(0, 3):
            if board[i, index] == 0:
                return [i, index]

    # Find empty position in diagonal.
    if type == 2:
        # Check usage.
        if index == 2:
            print("ERROR: Diagonal index usage undefined: 0 or 2 only.")
            return 1
        # If starting top left diagonal:
        if index == 0:
            for i in range(0, 3):
                if board[i, i] == 0:
                    return [i, i]
        # If starting bottom left diagonal:
        if index == 1:
            for i in range(0, 3):
                if board[2 - i, i] == 0:
                    return [2 - i, i]



board1 = array([
    [1,-1, 0],
    [0,-1, 0],
    [1, 0, 0]
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


print("_____FUNCTION OUTPUT______")
print(get_zero(board, 1, 0))






