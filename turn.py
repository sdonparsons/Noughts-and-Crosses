# Board values.
EMPTY = 0
CROSS = -1
NOUGHT = 1


class Turn:
    """A class to keep track of whose turn it is."""


    def __init__(self, player_first):
        """Initialise the turn class."""

        self.NOUGHT = NOUGHT
        self.CROSS = CROSS

        self.num_moves = 0
        
        # Player moves on even turns, starting at 0, including 0 as an 'even' turn.
        if player_first == True:
            self.turn = 0
            self.human = CROSS
        else:
            self.turn = 1
            self.human = NOUGHT

        self.game_active = False


    def set_human_first(self, human_first):
        if human_first == True:
            self.turn = 0
            self.human = self.CROSS
        else:
            self.turn = 1
            self.human = self.NOUGHT


    def is_player_turn(self):
        if self.turn % 2 == 0:
            return True
        else:
            return False
    

    def increment_turn(self):
        self.turn += 1
        self.num_moves += 1
    
    
