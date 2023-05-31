import pygame

from pygame.sprite import Sprite

START_POS = (100, 100)
START_SIZE = (626, 111)

FIRST_POS = (100, 300)
FIRST_SIZE = (321, 334)

SECOND_POS = (450, 300)
SECOND_SIZE = (226, 334)

GREEN = (0, 255, 0)

class Menu():
    """A class to manage the menu."""

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

        # Image for start game button.
        self.start = pygame.image.load('images/start_game.png')
        self.start_rect = pygame.Rect(START_POS, START_SIZE)

        self.first = pygame.image.load('images/go_first.png')
        self.first_rect = pygame.Rect(FIRST_POS, FIRST_SIZE)

        self.second = pygame.image.load('images/go_second.png')
        self.second_rect = pygame.Rect(SECOND_POS, SECOND_SIZE)

        self.highlight = pygame.Surface(FIRST_SIZE)  
        self.highlight.set_alpha(128)          
        self.highlight.fill(GREEN)         
    
    def draw(self):
        # Draw menu buttons.
        self.screen.blit(self.start, START_POS)
        self.screen.blit(self.first, FIRST_POS)
        self.screen.blit(self.second, SECOND_POS)

        # Highlight menu selections.
        if self.game.turn.is_player_turn():
            self.highlight = pygame.Surface(FIRST_SIZE)
            self.highlight.set_alpha(128)          
            self.highlight.fill(GREEN)  
            self.screen.blit(self.highlight, (FIRST_POS))
        elif not self.game.turn.is_player_turn():
            self.highlight = pygame.Surface(SECOND_SIZE)
            self.highlight.set_alpha(128)          
            self.highlight.fill(GREEN)  
            self.screen.blit(self.highlight, (SECOND_POS))

    
    def update(self, mouse_pos):
        if self.start_rect.collidepoint(mouse_pos):
            self.game.turn.game_active = True   
            self.game.ai.__init__(self.game)

        if self.first_rect.collidepoint(mouse_pos):
            self.game.turn.set_human_first(True)

        if self.second_rect.collidepoint(mouse_pos):
            self.game.turn.set_human_first(False)     

