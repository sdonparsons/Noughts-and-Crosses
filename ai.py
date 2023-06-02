from numpy import *

# Board values.
EMPTY = 0
CROSS = -1
NOUGHT = 1

class AI():
    """A class to manage the AI."""

    def __init__(self, game):
        # Get access to the turn and board information.
        self.turn = game.turn
        self.board = game.board

        # Set computer nought or cross.
        if self.turn.human == CROSS:
            self.computer = NOUGHT
        else:
            self.computer = CROSS

    def move(self):
        board = self.board.current_board()
        for location, state in board.items():
            if state == 0:
                self.board.move(location, self.computer)
                break


        if not self.turn.is_player_turn():
            self._debug("No valid moves found.")


    def _debug(self, message):
        """System console messaging"""
        print(f"______SYSMSG: '{message}'")

    def set_self(self):
        # Set computer nought or cross.
        if self.turn.human == CROSS:
            self.computer = NOUGHT
        else:
            self.computer = CROSS

    def logic(move):

        # 1) Do I move first? (i.e. Is board empty?)
        if size(board.nonzero()) == 0:
            # → First move in center:
            print("not here?")
            move[1, 1] = 1
            return
        
        # 2) Do I move second?
        if size(board.nonzero()) == 2 and board[1, 1] == 0:
            # And center free:
            print("are we here?")
            print(move[1, 1])
            move[1, 1] = 1 # → move center
            return
        elif size(board.nonzero()) == 2 and board[1, 1] == 1:
            # Center taken:
            move[2, 2] = 1 # Move corner
            return

        # 3) Win condition → win.
        row_sum = sum(array_board, axis=1)  # Sum of each row
        col_sum = sum(array_board, axis=0)  # Sum of each column
        diag_sum = sum(diag(array_board)), sum(diag(fliplr(array_board)))  # Sum of diagonals

        indices = []

        # Find indices where row sum, column sum, or diagonal sum equals 2 and element value is 0
        for i in range(array_board.shape[0]):
            if row_sum[i] == 2:
                row_indices = where(array_board[i, :] == 0)[0]
                for idx in row_indices:
                    indices.append((i, idx))

        for j in range(array_board.shape[1]):
            if col_sum[j] == 2:
                col_indices = where(array_board[:, j] == 0)[0]
                for idx in col_indices:
                    indices.append((idx, j))

        if diag_sum[0] == 2:
            diag_indices = where(diag(array_board) == 0)[0]
            for idx in diag_indices:
                indices.append((idx, idx))

        if diag_sum[1] == 2:
            diag_indices = where(diag(fliplr(array_board)) == 0)[0]
            for idx in diag_indices:
                indices.append((idx, array_board.shape[1] - 1 - idx))

        print(f"indices: {indices}")

        # If list of winning moves is not empty:
        if indices:
            row = indices[0][0] # Row value
            column = indices[0][1] # Column value
            move[row, column] = 1
            return

        # 4) Lose condition → block.
        # Clear the list.
        indices = []

        # Find indices where row sum, column sum, or diagonal sum equals -14 and element value is 0
        for i in range(array_board.shape[0]):
            if row_sum[i] == -14:
                row_indices = where(array_board[i, :] == 0)[0]
                for idx in row_indices:
                    indices.append((i, idx))

        for j in range(array_board.shape[1]):
            if col_sum[j] == -14:
                col_indices = where(array_board[:, j] == 0)[0]
                for idx in col_indices:
                    indices.append((idx, j))

        if diag_sum[0] == -14:
            diag_indices = where(diag(array_board) == 0)[0]
            for idx in diag_indices:
                indices.append((idx, idx))

        if diag_sum[1] == -14:
            diag_indices = where(diag(fliplr(array_board)) == 0)[0]
            for idx in diag_indices:
                indices.append((idx, array_board.shape[1] - 1 - idx))

        print(f"indices: {indices}")

        # If list of losing moves is not empty:
        if indices:
            row = indices[0][0] # Row value
            column = indices[0][1] # Column value
            move[row, column] = 1
            return

        # 5) Move in a corner if there is one, when there is free space.
        # Clear the list.
        indices = []

        # Find indices where row sum, column sum, or diagonal sum equals -14 and element value is 0
        for i in range(array_board.shape[0]):
            if row_sum[i] == 1:
                row_indices = where(array_board[i, :] == 0)[0]
                for idx in row_indices:
                    indices.append((i, idx))

        for j in range(array_board.shape[1]):
            if col_sum[j] == 1:
                col_indices = where(array_board[:, j] == 0)[0]
                for idx in col_indices:
                    indices.append((idx, j))

        # **) Block forks??

