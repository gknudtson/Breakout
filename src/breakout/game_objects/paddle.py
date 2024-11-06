import pygame

from src.breakout.breakout_config import (SCREEN_WIDTH, SCREEN_HEIGHT, PADDLE_HEIGHT, PADDLE_WIDTH,
                                          PADDLE_SPEED, PADDLE_MOVE_LEFT, PADDLE_MOVE_RIGHT)


class Paddle(pygame.sprite.Sprite):
    def __init__(self, x=SCREEN_WIDTH // 2, y=SCREEN_HEIGHT - PADDLE_HEIGHT, width=PADDLE_WIDTH,
                 height=PADDLE_HEIGHT, speed=PADDLE_SPEED, color='white'):
        """
        Initialize a Paddle object.

        Parameters:
        x (int): The x-coordinate of the paddle's center (default is SCREEN_WIDTH // 2).
        y (int): The y-coordinate of the paddle's center (default is SCREEN_HEIGHT - PADDLE_HEIGHT).
        width (int): The width of the paddle (default is PADDLE_WIDTH).
        height (int): The height of the paddle (default is PADDLE_HEIGHT).
        speed (int): The speed at which the paddle moves (default is PADDLE_SPEED).
        color (str or tuple): The color of the paddle (default is 'white').
        """
        super().__init__()
        self.image = pygame.Surface(size=(width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed

    def update(self):
        """
        Handle paddle movement on key pressed.
        """
        # Get list of keys pressed
        keys = pygame.key.get_pressed()

        # Move left if the left key is pressed
        if keys[PADDLE_MOVE_LEFT]:
            self.rect.x -= self.speed

        # Move right if the right key is pressed
        if keys[PADDLE_MOVE_RIGHT]:
            self.rect.x += self.speed

        # Prevent the paddle from going out of bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
