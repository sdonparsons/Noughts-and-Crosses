# Import the pygame module.
import pygame
import random
import sys

from ai import AI
from board import Board
from endgame import Endgame
from menu import Menu
from settings import Settings
from turn import Turn

# Predefined colours.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class GameEngine:
    """Overarching class to manage game assets and behaviours."""

    def __init__(self):
        """Initialise the game and create game resources."""
        # Initialize the pygame module
        pygame.init()

        self.clock = pygame.time.Clock()

        # Set application window name.
        pygame.display.set_caption("Noughts and Crosses by Sam D Parsons")

        # load and set the logo
        logo = pygame.image.load("images/noughtsandcrosses.png")
        pygame.display.set_icon(logo)

        # Assign self settings to class storing the settings.
        self.settings = Settings()

        # Turn counter. True value means player moves first.
        self.turn = Turn(True)

        # Object assigned to self.screen is a Pygame "surface".
        self.screen = pygame.display.set_mode(self.settings.resolution)

        # Create start menu object.
        self.menu = Menu(self)

        # Create endgame menu object.
        self.endgame = Endgame(self)

        # Create board.
        self.board = Board(self)

        # Initiate computer player.
        self.ai = AI(self)


    def run_game(self):
        """Start the main loop for the game."""

        # Game loop.
        while True:

            if self.turn.game_active and not self.turn.game_end:
                # if AI turn then move.
                if not self.turn.is_player_turn():
                    self.ai.move()
                # Else do nothing and wait for player to move.

            # Update events → i.e. check player move.
            self._check_events()

            # Update graphics.
            self._update_screen()

            # Framerate.
            self.clock.tick(60)


    def _check_events(self):
        """Respond to inputs."""

        # Event loop.
        for event in pygame.event.get():  
            # Only do something if the event is of type QUIT.
            if event.type == pygame.QUIT:
                sys.exit()
            # Mouseclick events:
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # If game active:
                if self.turn.game_active and not self.turn.game_end:
                    # Update board, giving it location of mouse click in (x,y).
                    self.board.update(mouse_pos)
                # Show main menu.
                elif not self.turn.game_active and not self.turn.game_end:
                    self.menu.update(mouse_pos)
                # Show endgame screen.
                elif not self.turn.game_active and self.turn.game_end:
                    self.endgame.update(mouse_pos)


    def _debug(self, message):
        """System console messaging"""
        print(f"______SYSMSG: '{message}'")


    def _update_screen(self):
        """Update images on the screen and then flip to the new screen."""
        
        # Fill background colour.
        self.screen.fill(self.settings.bg_colour)

        # If game active:
        if self.turn.game_active and not self.turn.game_end:
            self.board.draw()
        elif not self.turn.game_active and not self.turn.game_end:
            self.menu.draw()
        elif not self.turn.game_active and self.turn.game_end: 
            self.endgame.draw()              

        # Make the most recently drawn screen visible.
        pygame.display.flip()  


def main():
    game = GameEngine()
    game.run_game()
     

# Run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    main()

