import pygame

from pygame.sprite import Sprite

# Board values.
EMPTY = 0
CROSS = -1
NOUGHT = 1

TOP_LEFT = "TL" 
TOP_MIDDLE = "TM" 
TOP_RIGHT ="TR"
MIDDLE_LEFT = "ML" 
MIDDLE_MIDDLE = "MM" 
MIDDLE_RIGHT = "MR"
BOTTOM_LEFT = "BL"
BOTTOM_MIDDLE = "BM"
BOTTOM_RIGHT = "BR"

SQUARE_SIZE = (200, 200)

EMPTY_BOARD = {TOP_LEFT: EMPTY, 
                TOP_MIDDLE: EMPTY, 
                TOP_RIGHT: EMPTY,
                MIDDLE_LEFT: EMPTY, 
                MIDDLE_MIDDLE: EMPTY, 
                MIDDLE_RIGHT: EMPTY,
                BOTTOM_LEFT: EMPTY, 
                BOTTOM_MIDDLE: EMPTY, 
                BOTTOM_RIGHT: EMPTY}

BOARD_COORDINATES = {TOP_LEFT: (50, 50), 
                    TOP_MIDDLE: (300, 50), 
                    TOP_RIGHT: (550, 50),
                    MIDDLE_LEFT: (50, 300), 
                    MIDDLE_MIDDLE: (300, 300), 
                    MIDDLE_RIGHT: (550, 300),
                    BOTTOM_LEFT: (50, 550), 
                    BOTTOM_MIDDLE: (300, 550), 
                    BOTTOM_RIGHT: (550, 550)}

class Board():
    """A class to manage the Board Object."""


    def __init__(self, game):
        """Initialise the board."""

        # Assign the screen to an element of board, 
        # so that we can access it easily in the methods of this class.
        self.screen = game.screen

        # Access screens rect attribute using get_rect() method.
        # Doing so allows us to place the board in the correct location on the screen.
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        self.turn = game.turn

        self.square0 = pygame.Rect((50, 50), SQUARE_SIZE)
        self.square1 = pygame.Rect((300, 50), SQUARE_SIZE)
        self.square2 = pygame.Rect((550, 50), SQUARE_SIZE)

        self.square3 = pygame.Rect((50, 300), SQUARE_SIZE)
        self.square4 = pygame.Rect((300, 300), SQUARE_SIZE)
        self.square5 = pygame.Rect((550, 300), SQUARE_SIZE)

        self.square6 = pygame.Rect((50, 550), SQUARE_SIZE)
        self.square7 = pygame.Rect((300, 550), SQUARE_SIZE)
        self.square8 = pygame.Rect((550, 550), SQUARE_SIZE)

        self.squares = {TOP_LEFT: self.square0, 
                        TOP_MIDDLE: self.square1, 
                        TOP_RIGHT: self.square2,
                        MIDDLE_LEFT: self.square3, 
                        MIDDLE_MIDDLE: self.square4, 
                        MIDDLE_RIGHT: self.square5,
                        BOTTOM_LEFT: self.square6, 
                        BOTTOM_MIDDLE: self.square7, 
                        BOTTOM_RIGHT: self.square8}
        
        # Initialise an empty board.
        self.board = EMPTY_BOARD
        
        # Images for noughts and crosses to draw to screen.
        self.X = pygame.image.load('images/x.png')
        self.O = pygame.image.load('images/o.png')
    

    def draw(self):
        # Iterate through every board location.
        for square in self.squares.values():
            # Draw square: for display and hit detection.
            pygame.draw.rect(self.screen, (0, 0, 0), square, 4)

        for location, move in self.board.items():
            # Draw X or O dependent on state of game board.
            if move == CROSS:
                self.screen.blit(self.X, BOARD_COORDINATES[location])
            elif move == NOUGHT:
                self.screen.blit(self.O, BOARD_COORDINATES[location])


    def update(self, mouse_pos):
        # Iterate through every board location.
        for location, square in self.squares.items():
            # Check for collision.
            if square.collidepoint(mouse_pos):
                self._debug(f"Clicked {location}.")
                # Update board state -> HUMAN MOVE
                self.move(location, self.turn.human)          

        self._debug(f"Board: \n {self.board}")


    def move(self, location, player):
        if self.board[location] != EMPTY:
            self._debug("Invalid move.")
        else:
            self.board[location] = player
        # Increment turn counter.
        self.turn.increment_turn()

        # Check for winning condition
        if self.turn.num_moves == 9:
            self._debug("Board full.")



    """ Return the current board-state."""
    def current_board(self):
        return self.board
        

    def _debug(self, message):
        """System console messaging"""
        print(f"______SYSMSG: '{message}'")
                
