import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
SPHERE_RADIUS = 30
COLORS = [(255, 255, 0), (0, 0, 255)]
FPS = 60

# Difficulty levels
DIFFICULTY_LEVELS = {'easy': (3,50), 'medium': (5,30), 'hard': (7,15)}

# Game settings
lives = 3
fall_speed, spawn_rate = DIFFICULTY_LEVELS['medium']  # Default difficulty level

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Match")

# Set up the clock
clock = pygame.time.Clock()

# Define Button class for easier button handling
class Button:
    def __init__(self, text, x, y, width, height, color, action=None):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.action = action
        self.font = pygame.font.SysFont(None, 36)

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surf = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Define the Sphere class
class Sphere:
    def __init__(self):
        self.color = random.choice(COLORS)
        self.x = WIDTH // 2
        self.y = HEIGHT - 50
        self.flicker = False
        self.flicker_timer = 0

    def draw(self, transparency=255):
        transparency = 150 if self.flicker else 255
        color_with_alpha = (*self.color, transparency)
        surface = pygame.Surface((SPHERE_RADIUS*2, SPHERE_RADIUS*2), pygame.SRCALPHA)
        pygame.draw.circle(surface, color_with_alpha, (SPHERE_RADIUS, SPHERE_RADIUS), SPHERE_RADIUS)
        screen.blit(surface, (self.x - SPHERE_RADIUS, self.y - SPHERE_RADIUS))

        if self.flicker:
            self.flicker_timer -= 1
            if self.flicker_timer <= 0:
                self.flicker = False

    def change_color(self):
        self.color = random.choice(COLORS)

# Define the FallingObject class
class FallingObject:
    def __init__(self):
        self.color = random.choice(COLORS)
        self.x = random.randint(0, WIDTH - 20)
        self.y = 0
        self.x_velocity = random.choice([-3, 3])
        self.y_velocity = fall_speed

    def move(self):
        self.x += self.x_velocity
        self.y += self.y_velocity
        if self.x <= 0 or self.x >= WIDTH - 20:
            self.x_velocity *= -1
        # if self.y >= HEIGHT:
        #     self.y = 0

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 20, 20))

# Show difficulty selection menu
def select_difficulty():
    # Display game title
    title_font = pygame.font.SysFont(None, 64)
    title_text = title_font.render("Color Match", True, (0, 0, 0))
    difficulty_label_font = pygame.font.SysFont(None, 36)
    difficulty_label_text = difficulty_label_font.render("Select Difficulty Level", True, (0, 0, 0))

    easy_button = Button("Easy", WIDTH // 2 - 100, HEIGHT // 2 - 60, 200, 50, (0, 255, 0), 'easy')
    medium_button = Button("Medium", WIDTH // 2 - 100, HEIGHT // 2, 200, 50, (255, 255, 0), 'medium')
    hard_button = Button("Hard", WIDTH // 2 - 100, HEIGHT // 2 + 60, 200, 50, (255, 0, 0), 'hard')
    buttons = [easy_button, medium_button, hard_button]

    while True:
        screen.fill((255, 255, 255))
        # Draw game title and difficulty label
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4 - 80))
        screen.blit(difficulty_label_text, (WIDTH // 2 - difficulty_label_text.get_width() // 2, HEIGHT // 2 - 120))
        for button in buttons:
            button.draw()

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for button in buttons:
                    if button.is_clicked(pos):
                        return DIFFICULTY_LEVELS[button.action]

# Game loop
def game_loop():
    global fall_speed, spawn_rate, lives, screen
    fall_speed, spawn_rate = select_difficulty()  # Select difficulty before starting the game
    sphere = Sphere()
    falling_objects = []
    score = 0
    game_over = False
    paused = False
    lives = 3  # Reset lives when the game starts
    pause_button = Button("Pause", WIDTH - 220, 10, 100, 40, (200, 200, 200))
    restart_button = Button("Restart", WIDTH // 2 - 50, HEIGHT // 2 + 40, 100, 40, (0, 255, 0))

    while True:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pause_button.is_clicked(pos):
                    paused = not paused
                    pause_button.text = "Play" if paused else "Pause"
                elif game_over and restart_button.is_clicked(pos):
                    # Reset game variables for a restart
                    score = 0
                    lives = 3
                    game_over = False
                    falling_objects.clear()  # Clear falling objects
                    sphere = Sphere()  # Reset sphere position and color
                    fall_speed, spawn_rate = select_difficulty()  # Optionally reselect difficulty
                elif not paused and not game_over:
                    if event.button == 1:  # Left click to change color
                        sphere.change_color()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Space bar to change color
                    sphere.change_color()

        keys = pygame.key.get_pressed()
        if not game_over and not paused:
            if keys[pygame.K_LEFT] and sphere.x > SPHERE_RADIUS:
                sphere.x -= 5
            if keys[pygame.K_RIGHT] and sphere.x < WIDTH - SPHERE_RADIUS:
                sphere.x += 5

            if random.randint(1, spawn_rate) == 1:
                falling_objects.append(FallingObject())

            for obj in falling_objects[:]:
                obj.move()
                if obj.y > HEIGHT:
                    falling_objects.remove(obj)
                elif obj.y + 20 >= sphere.y - SPHERE_RADIUS and sphere.x - SPHERE_RADIUS < obj.x + 20 < sphere.x + SPHERE_RADIUS:
                    if obj.color == sphere.color:
                        score += 1
                    else:
                        lives -= 1
                        sphere.flicker = True
                        sphere.flicker_timer = FPS // 4
                        if lives == 0:
                            game_over = True
                    falling_objects.remove(obj)
                obj.draw()

            sphere.draw()

            # Display score and lives
            font = pygame.font.SysFont(None, 36)
            score_text = font.render(f'Score: {score}', True, (0, 0, 0))
            lives_text = font.render(f'Lives: {lives}', True, (255, 0, 0))
            screen.blit(score_text, (10, 10))
            screen.blit(lives_text, (WIDTH - 100, 10))

        elif paused:
            pause_text = pygame.font.SysFont(None, 48).render("Game Paused", True, (0, 0, 255))
            screen.blit(pause_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))

        else:
            game_over_text = pygame.font.SysFont(None, 48).render('Game Over!', True, (255, 0, 0))
            final_score_text = pygame.font.SysFont(None, 36).render(f'Final Score: {score}', True, (0, 0, 0))
            screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
            screen.blit(final_score_text, (WIDTH // 2 - 100, HEIGHT // 2))
            restart_button.draw()  # Draw the restart button when game over

        if not game_over:
            pause_button.draw()

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    game_loop()
