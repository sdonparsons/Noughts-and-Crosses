class Settings:
    """A class to store all of the settings for the game engine."""

    def __init__(self):
        """Initialise the game's settings."""
        # Screen settings.
        self.screen_width = 800
        self.screen_height = 800
        self.resolution = (self.screen_width, self.screen_height)
        self.bg_colour = (255, 255, 255)