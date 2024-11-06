import pygame

from src.breakout.breakout_config import *
from src.breakout.game_objects.brick import Brick
from src.breakout.game_objects.paddle import Paddle
from src.breakout.game_objects.ball import Ball


class BreakoutGame:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Set up the display
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Breakout")

        # Set up the clock for controlling the frame rate
        self.clock = pygame.time.Clock()

        # Create bricks, paddle, and ball
        self.bricks = self.create_bricks()
        self.paddle = Paddle()
        self.ball = Ball()

        # Create a new sprite group for all sprites
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.bricks)
        self.all_sprites.add(self.paddle)
        self.all_sprites.add(self.ball)

        # Create a new sprite group for collidable sprites
        self.collidable_sprites = pygame.sprite.Group()
        self.collidable_sprites.add(self.paddle)
        self.collidable_sprites.add(self.bricks)

        # Game state
        self.running = True

    def create_bricks(self) -> pygame.sprite.Group:
        """Create and return a group of bricks."""
        x = 0
        bricks = pygame.sprite.Group()
        while x <= SCREEN_WIDTH - BRICK_WIDTH:
            brick = Brick(x=x + BRICK_PADDING, y=BRICK_HEIGHT)
            bricks.add(brick)
            x += BRICK_WIDTH + BRICK_PADDING
        return bricks

    def handle_collisions(self):
        """Detect and handle collisions between the ball and other objects."""
        collisions = pygame.sprite.spritecollide(self.ball, self.collidable_sprites, False)
        for sprite in collisions:
            if self.ball.collision(sprite):
                if isinstance(sprite, Brick):
                    sprite.destroy()  # Remove the brick upon collision

    def run(self):
        """Run the main game loop."""
        while self.running:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.all_sprites.update()
            self.handle_collisions()

            # Drawing logic
            self.screen.fill("black")
            self.all_sprites.draw(self.screen)
            pygame.display.flip()

            # Controls how many times this loop runs per second.
            self.clock.tick(FRAME_RATE)

        pygame.quit()


# Run the game
if __name__ == "__main__":
    game = BreakoutGame()
    game.run()
