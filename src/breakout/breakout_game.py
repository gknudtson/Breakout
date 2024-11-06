import pygame
from src.breakout.breakout_config import SCREEN_WIDTH, SCREEN_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT, \
    BRICK_PADDING, SCREEN_BACKGROUND_COLOR, FRAME_RATE
from src.breakout.game_objects.brick import Brick
from src.breakout.game_objects.paddle import Paddle
from src.breakout.game_objects.ball import Ball


class BreakoutGame:
    def __init__(self):
        """
        Set up the game by initializing Pygame and creating all game objects.
        """
        pygame.init()  # Initialize Pygame and its modules

        # Create the game window
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Breakout")  # Set the window title

        # Set up a clock to control the frame rate
        self.clock = pygame.time.Clock()

        # Create game objects: bricks, paddle, and ball
        self.bricks = self.create_bricks()
        self.paddle = Paddle()
        self.ball = Ball()

        # Create a group to hold all game objects for easy updating and drawing
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.bricks)  # Add all brick objects
        self.all_sprites.add(self.paddle)  # Add the paddle object
        self.all_sprites.add(self.ball)  # Add the ball object

        # Create a group for objects that the ball can collide with
        self.collidable_sprites = pygame.sprite.Group()
        self.collidable_sprites.add(self.paddle)  # Add the paddle to the collidable group
        self.collidable_sprites.add(self.bricks)  # Add the bricks to the collidable group

        # Set the initial game state
        self.running = True

    def create_bricks(self) -> pygame.sprite.Group:
        """
        Create and return a group of brick objects.

        Returns:
        pygame.sprite.Group: A group containing all brick sprites.
        """
        bricks = pygame.sprite.Group()  # Group to store all brick objects
        x = 0  # Start position for drawing bricks along the x-axis

        # Create a row of bricks with padding between them
        while x <= SCREEN_WIDTH - BRICK_WIDTH:
            brick = Brick(x=x + BRICK_PADDING,
                          y=BRICK_HEIGHT)  # Create a brick at the given position
            bricks.add(brick)  # Add the brick to the group
            x += BRICK_WIDTH + BRICK_PADDING  # Move to the position for the next brick

        return bricks  # Return the group containing all the bricks

    def handle_collisions(self):
        """
        Check for and handle collisions between the ball and other game objects.
        """
        # Check for collisions between the ball and collidable objects
        collisions = pygame.sprite.spritecollide(self.ball, self.collidable_sprites, False)

        # Handle each collision detected
        for sprite in collisions:
            if self.ball.collision(sprite):  # Handle the ball's collision response
                if isinstance(sprite, Brick):  # If the collided object is a brick
                    sprite.destroy()  # Remove the brick from the game

    def run(self):
        """
        Run the main game loop to keep the game running and updated.
        """
        while self.running:
            # Handle user input events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Update all game objects (ball, paddle, bricks)
            self.all_sprites.update()

            # Handle any collisions detected
            self.handle_collisions()

            # Draw all game objects on the screen and refresh display
            self.screen.fill(SCREEN_BACKGROUND_COLOR)
            self.all_sprites.draw(self.screen)
            pygame.display.flip()

            # Game runs at FRAME_RATE times per second
            self.clock.tick(FRAME_RATE)

        # End the game and close the Pygame window
        pygame.quit()


# Run the game when this script is executed directly
if __name__ == "__main__":
    game = BreakoutGame()  # Create an instance of the game
    game.run()  # Start the game
