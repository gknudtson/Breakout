import pygame  # Import Pygame so we can use it for graphics and collisions

from src.breakout.breakout_config import SCREEN_HEIGHT, POWERUP_WIDTH, POWERUP_HEIGHT, POWERUP_SPEED


class PowerUp(pygame.sprite.Sprite):  # This line sets up our power-up as a "sprite"
    def __init__(self, x, y, width=POWERUP_WIDTH, height=POWERUP_HEIGHT, speed=POWERUP_SPEED, color='cyan'):
        """
        Parameters:
        x (int): The x-coordinate (horizontal position) where the power-up appears.
        y (int): The y-coordinate (vertical position) where the power-up appears.
        width (int): The width of the power-up display (default is POWERUP_WIDTH).
        height (int): The height of the power-up display (default is POWERUP_HEIGHT).
        speed (int): The speed at which the power-up moves down the screen (default is POWERUP_SPEED).
        color (str): The color of the power-up (default is 'purple').
        """
        super().__init__()  # Sets up the power-up as a sprite in Pygame

        # Create the power-up's appearance and position
        self.image = pygame.Surface((width, height))  # Define the size of the power-up
        self.image.fill(color)  # Set the color of the power-up
        self.rect = self.image.get_rect(center=(x, y))  # Set the initial position of the power-up

        self.speed_y = speed  # Controls the speed of the downward movement

    def update(self):
        """
        Move the power-up down the screen at a constant speed.
        If the power-up moves off the bottom of the screen, it is removed from the game.
        """
        self.rect.y += self.speed_y  # Each time update() runs, the power-up moves down by speed_y

        # Remove the power-up if it goes off the bottom of the screen
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()  # Remove the power-up from the game

    def activate_power(self):
        # TODO increase paddle size
        pass

# 1. how to get powerup to have a random chance to spawn
# 2. how to get powerup to collide with paddle
# 3. Implement activatePower
# 4. Additional features (bottom wall collision, score, more complex brick patterns, multiple levels, advanced ball collision, )