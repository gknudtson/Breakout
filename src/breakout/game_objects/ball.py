import pygame

from src.breakout.breakout_config import (SCREEN_WIDTH, SCREEN_HEIGHT, BALL_RADIUS, BALL_SPEED,
                                          BALL_COLLISION_BUFFER)


class Ball(pygame.sprite.Sprite):
    def __init__(self, x=SCREEN_WIDTH // 2, y=SCREEN_HEIGHT // 2, radius=BALL_RADIUS,
                 speed=BALL_SPEED, color='yellow'):
        """
        Initialize a Ball object.

        Parameters:
        x (int): The x-coordinate of the ball's center (default is SCREEN_WIDTH // 2).
        y (int): The y-coordinate of the ball's center (default is SCREEN_HEIGHT // 2).
        radius (int): The radius of the ball (default is BALL_RADIUS).
        speed (int): The speed of the ball (default is BALL_SPEED).
        color (str or tuple): The color of the ball (default is 'yellow').
        """
        super().__init__()
        self.radius = radius
        self.color = color
        self.speed_x = speed
        self.speed_y = -speed
        diameter = radius * 2

        # Create a circular surface
        self.image = pygame.Surface(size=(diameter, diameter))
        pygame.draw.circle(surface=self.image, color=color, center=(radius, radius), radius=radius)

        # Set rect for positioning and collision detection
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        """
        Continually moves ball and checks for wall collisions.
        """
        # Update ball position
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self._wall_collision()

    def _wall_collision(self):
        """
        Detect collisions with game borders.
        """

        # Bounce off the left and right walls
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed_x = -self.speed_x

        # Bounce off the top wall
        if self.rect.top <= 0:
            self.speed_y = -self.speed_y

        # Change logic to handle bottom wall collision (e.g., reset or lose life)
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y = -self.speed_y

    def collision(self, sprite: pygame.sprite) -> bool:
        """
        Detect and respond to collisions with another sprite.
        """
        if pygame.sprite.collide_rect(self, sprite):
            # Check which side of the sprite the ball hit
            if self._collided_top(sprite) or self._collided_bottom(sprite):
                self._handle_vertical_collision()
                return True

    def _collided_top(self, sprite: pygame.sprite) -> bool:
        """
        Detects collisions between bottom of ball and top of sprite.
        """
        return abs(self.rect.bottom - sprite.rect.top) < BALL_COLLISION_BUFFER and self.speed_y > 0

    def _collided_bottom(self, sprite: pygame.sprite) -> bool:
        """
        Detects collisions between top of ball and bottom of sprite.
        """
        return abs(self.rect.top - sprite.rect.bottom) < BALL_COLLISION_BUFFER and self.speed_y < 0

    def _handle_vertical_collision(self):
        """
        Handles ball behavior when vertical collisions are detected.
        """
        self.speed_y = -self.speed_y
