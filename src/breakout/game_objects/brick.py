import pygame

from src.breakout.breakout_config import BRICK_HEIGHT, BRICK_WIDTH


class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, width=BRICK_WIDTH, height=BRICK_HEIGHT, color='purple'):
        """
        Initialize a Brick object.

        Parameters:
        x (int): The x-coordinate of the brick's top-left corner.
        y (int): The y-coordinate of the brick's top-left corner.
        width (int): The width of the brick (default is BRICK_WIDTH).
        height (int): The height of the brick (default is BRICK_HEIGHT).
        color (str or tuple): The color of the brick (default is 'purple').
        """
        super().__init__()

        # Create the brick surface with the given width and height
        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        # Set the rectangle for positioning and collision detection
        self.rect = self.image.get_rect(topleft=(x, y))
