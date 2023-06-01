import pygame

from pygame.sprite import Sprite

REPLAY_POS = (100, 100)
REPLAY_SIZE = (626, 111)

WINNER_POS = (100, 300)
WINNER_SIZE = (500, 200)

class Endgame():
    """A class to manage the end game menu."""

    def __init__(self, game):
        """Initialise the menu object."""

        # Assign the screen to an element of board, 
        # so that we can access it easily in the methods of this class.
        self.screen = game.screen
        self.game = game

        # Access screens rect attribute using get_rect() method.
        # Doing so allows us to place the board in the correct location on the screen.
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        self.turn = game.turn

        # Image for replay game button.
        self.replay = pygame.image.load('images/replay.png')
        self.replay_rect = pygame.Rect(REPLAY_POS, REPLAY_SIZE)

        # Load the images to display winner/draw.
        self.ai_win = pygame.image.load('images/ai_win.png')
        self.human_win = pygame.image.load('images/human_win.png')
        self.draw_game = pygame.image.load('images/draw.png')

    def draw(self):
        # Draw menu buttons.
        self.screen.blit(self.replay, REPLAY_POS)
        if self.turn.winvalue == 0:
            self.screen.blit(self.draw_game, WINNER_POS)
        elif self.have_same_sign(self.turn.winvalue, self.turn.human):
            self.screen.blit(self.human_win, WINNER_POS)
        else:
            self.screen.blit(self.ai_win, WINNER_POS)

    
    def update(self, mouse_pos):
        if self.replay_rect.collidepoint(mouse_pos):
            # Reset turn counter.
            self.game.turn.set_human_first(True)
            # Reset board state.
            self.game.board.reset()
            # Reset game states.
            self.turn.game_active = False
            self.turn.game_end = False 
            self.turn.winvalue = 0

    def have_same_sign(self, num1, num2):
        return (num1 >= 0 and num2 >= 0) or (num1 < 0 and num2 < 0)
            

