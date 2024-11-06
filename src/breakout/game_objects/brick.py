import pygame

from src.breakout.breakout_config import BRICK_HEIGHT, BRICK_WIDTH


class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, width=BRICK_WIDTH, height=BRICK_HEIGHT, color='red'):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

    def destroy(self):
        """Handle the destruction of the brick (e.g., removing it from groups)."""
        self.kill()  # Removes the sprite from all sprite groups it's a part of
