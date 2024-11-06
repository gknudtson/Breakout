import pygame

from src.breakout.breakout_config import *


class Ball(pygame.sprite.Sprite):
    def __init__(self, x=SCREEN_WIDTH // 2, y=SCREEN_HEIGHT // 2, radius=BALL_RADIUS,
                 speed=BALL_SPEED, color='yellow'):
        super().__init__()
        self.radius = radius
        self.color = color
        self.speed_x = speed  # Horizontal speed
        self.speed_y = -speed  # Vertical speed

        # Create a surface with transparency for the circular appearance
        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)

        # Set rect for positioning and collision detection
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        """Continually moves ball and checks for wall collisions."""
        # Update ball position
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.wall_collision()

    def wall_collision(self):
        """Detect collisions with game borders."""

        # Bounce off the left and right walls
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed_x = -self.speed_x

        # Bounce off the top wall
        if self.rect.top <= 0:
            self.speed_y = -self.speed_y

        # Change logic to handle bottom wall collision (e.g., reset or lose life)
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y = -self.speed_y

    def collision(self, sprite):
        """Detect and respond to collisions with another sprite."""
        if pygame.sprite.collide_rect(self, sprite):
            # Check which side of the sprite the ball hit
            if abs(self.rect.bottom - sprite.rect.top) < BALL_COLLISION_BUFFER and self.speed_y > 0:
                # Ball hit the top of the sprite
                self.speed_y = -self.speed_y
                return True
            elif abs(self.rect.top - sprite.rect.bottom) < BALL_COLLISION_BUFFER and self.speed_y < 0:
                # Ball hit the bottom of the sprite
                self.speed_y = -self.speed_y
                return True

