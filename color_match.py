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

# Define the FallingObject class with bouncing effect
class FallingObject:
    def _init_(self):
        self.color = random.choice(COLORS)
        self.x = random.randint(0, WIDTH - 20)
        self.y = 0
        self.x_velocity = random.choice([-3, 3])  # Random horizontal speed
        self.y_velocity = FALL_SPEED              # Falling speed

    def move(self):
        # Update position
        self.x += self.x_velocity
        self.y += self.y_velocity

        # Bounce off the walls
        if self.x <= 0 or self.x >= WIDTH - 20:
            self.x_velocity *= -1  # Reverse x direction

        # Bounce off the top and bottom
        if self.y <= 0 or self.y >= HEIGHT - 20:
            self.y_velocity *= -1  # Reverse y direction

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 20, 20))

# Game loop
def game_loop():
    sphere = Sphere()
    falling_objects = []
    score = 0
    speed_up_counter = 0
    game_over = False

    while True:
        screen.fill((255, 255, 255))  # Clear screen

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Controls
        keys = pygame.key.get_pressed()
        if not game_over:
            if keys[pygame.K_LEFT] and sphere.x > SPHERE_RADIUS:
                sphere.x -= 5
            if keys[pygame.K_RIGHT] and sphere.x < WIDTH - SPHERE_RADIUS:
                sphere.x += 5
            if keys[pygame.K_SPACE]:  # Change color
                sphere.change_color()

            # Create new falling object
            if random.randint(1, 50) == 1:
                falling_objects.append(FallingObject())

            # Update and draw falling objects
            for obj in falling_objects[:]:
                obj.move()
                if obj.y > HEIGHT:  # Check if object missed the sphere
                    falling_objects.remove(obj)

                if obj.y + 20 >= sphere.y - SPHERE_RADIUS and \
                   sphere.x - SPHERE_RADIUS < obj.x + 20 < sphere.x + SPHERE_RADIUS:
                    if obj.color == sphere.color:
                        score += 1  # Increase score on match
                    else:
                        # Game over if the colors do not match
                        game_over = True
                    falling_objects.remove(obj)

                obj.draw()

            # Draw the sphere
            sphere.draw()