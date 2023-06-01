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
                


        