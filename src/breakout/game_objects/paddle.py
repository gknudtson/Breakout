import pygame

from src.breakout.breakout_config import *


class Paddle(pygame.sprite.Sprite):
    def __init__(self, x=SCREEN_WIDTH//2, y=SCREEN_HEIGHT-PADDLE_HEIGHT, width=PADDLE_WIDTH, height=PADDLE_HEIGHT, speed=PADDLE_SPEED, color='white'):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed

    def update(self):
        """Handle paddle movement on key pressed."""
        keys = pygame.key.get_pressed()  # Get list of keys pressed
        if keys[PADDLE_MOVE_LEFT]:
            self.rect.x -= self.speed
        if keys[PADDLE_MOVE_RIGHT]:
            self.rect.x += self.speed

        # Prevent the paddle from going out of bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
