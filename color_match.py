import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
SPHERE_RADIUS = 30
FALL_SPEED = 3  # Initial falling speed
COLORS = [ (255, 255, 0), (255, 165, 0)]
FPS = 60

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Match Sphere")

# Set up the clock
clock = pygame.time.Clock()


# Define the Sphere class
class Sphere:
    def _init_(self):
        self.color = random.choice(COLORS)
        self.x = WIDTH // 2
        self.y = HEIGHT - 50

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), SPHERE_RADIUS)

    def change_color(self):
        self.color = random.choice(COLORS)

