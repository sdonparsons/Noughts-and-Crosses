from numpy import *

def get_zero(board, type, index):
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
    if len(board) != 3:
        print("ERROR: Array not 3x3.")
        return 1
    # Each row should have three columns.
    for row in range(len(board)):
        if len(board[row]) != 3:
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
                

