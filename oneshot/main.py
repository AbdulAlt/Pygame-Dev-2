import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Oneshot")

bg = pygame.image.load('images/bg.jpg')
alien = pygame.image.load('images/alien.png')
alien_rect = alien.get_rect()
alien_rect_x = 0
alien_rect_y = 0
font = pygame.font.SysFont("Arial", 35)
message = ""

def draw_text(text, pos):
     text1 = font.render(text, True, "white")
     screen.blit(text1, pos)

def place_alien():
    global alien_rect_x
    global alien_rect_y
    alien_rect_x = random.randint(50, WIDTH - 50)
    alien_rect_y = random.randint(50, HEIGHT - 50)

place_alien()

running = True
alien_alive = True


while running:
    screen.blit(bg, (0, 0))
    screen.blit(alien, (alien_rect_x, alien_rect_y))
    draw_text(message, (400, 300))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if alien_rect.collidepoint(event.pos):
                    message = "goodshot"
                    place_alien()
                    
                    alien_alive = False
            else:
                 message = "you missed"

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()