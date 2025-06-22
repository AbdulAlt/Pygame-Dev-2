import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
TITLE = 'bumble bee'
WIDTH = 600
HEIGHT = 500
FPS = 60

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

# Load images
bg = pygame.image.load('images/bg.png').convert()
bee = pygame.image.load('images/bee.png').convert_alpha()
flower = pygame.image.load('images/flower.png').convert_alpha()

# Set positions
bee_rect = bee.get_rect(topleft=(100, 100))
flower_rect = flower.get_rect(topleft=(200, 200))

# Variables
score = 0
game_over = False

# Font
font = pygame.font.SysFont(None, 36)

# Timer
TIME_UP = pygame.USEREVENT + 1
pygame.time.set_timer(TIME_UP, 60000)  # 60 seconds

# Function to place flower randomly
def place_flower():
    flower_rect.x = random.randint(70, WIDTH - 70)
    flower_rect.y = random.randint(70, HEIGHT - 70)

# Main game loop
running = True
while running:
    if not game_over:
        screen.blit(bg, (0, 0))
        screen.blit(bee, bee_rect)
        screen.blit(flower, flower_rect)
        score_text = font.render(f'score: {score}', True, (0, 0, 0))
        screen.blit(score_text, (10, 10))
    else:
        screen.fill((255, 192, 203))  # pink
        game_over_text = font.render('game over!', True, (255, 0, 0))
        screen.blit(game_over_text, game_over_text.get_rect(midtop=(WIDTH / 2, 10)))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == TIME_UP:
            game_over = True

    # Movement
    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_LEFT]:
            bee_rect.x -= 2
        if keys[pygame.K_RIGHT]:
            bee_rect.x += 2
        if keys[pygame.K_UP]:
            bee_rect.y -= 2
        if keys[pygame.K_DOWN]:
            bee_rect.y += 2

        if bee_rect.colliderect(flower_rect):
            score += 10
            place_flower()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
