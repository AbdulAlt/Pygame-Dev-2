import pygame
import os
pygame.font.init
pygame.mixer.init()

pygame.init()

# display
WIDTH = 900
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# fonts
health_font = pygame.font.SysFont("Comicsans", 40)
winner_fony = pygame.font.SysFont("Times New Roman", 100)

# constants
FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
YELLOW_HIT = pygame.USEREVENT+1
RED_HIT = pygame.USEREVENT+2
BORDER = pygame.Rect(WIDTH / 2 - 5, 0, 10, HEIGHT)

# images
red_image = pygame.image.load(os.path.join("images", "red_rocket.png"))
red_image_sp = pygame.transform.rotate(pygame.transform.scale(red_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
yellow_image = pygame.image.load(os.path.join("images", "yellow_rocket.png"))
yellow_image_sp = pygame.transform.rotate(pygame.transform.scale(yellow_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
bg = pygame.transform.scale(pygame.image.load(os.path.join("images", "bg.png")), (WIDTH, HEIGHT))

# draw window function
def draw_window(red, yellow, red_bullet, yellow_bullet, red_health, yellow_health):
    screen.blit(bg, (0, 0))
    pygame.draw.rect(screen, "black", BORDER)
    red_health_text = health_font.render("health: " + str(red_health), True, (0, 0, 0))
    yellow_health_text = health.font.render("health: " + str(yellow_health), True, (0, 0, 0))
    screen.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))

draw_window()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    pygame.display.update