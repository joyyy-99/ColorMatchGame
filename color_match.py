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


