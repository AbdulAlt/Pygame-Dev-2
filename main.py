import pygame
from pygame.locals import *
from time import *
pygame.init()

# display
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
center = (WIDTH / 2, HEIGHT / 2)

# variables
player_x = 200
player_y = 200
keys = [False, False, False, False]
player = pygame.image.load("images/rocket.png")
bg = pygame.image.load("images/bg.png")

while player_y < 600:
    # blit the images
    screen.blit(bg, (0, 0))
    screen.blit(player, (player_x, player_y))
    pygame.display.update()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # detect player input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                keys[0] = True
            elif event.key == pygame.K_LEFT:
                keys[1] = True
            elif event.key == pygame.K_DOWN:
                keys[2] = True
            elif event.key == pygame.K_RIGHT:
                keys[3] = True
        
        # if key released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys[0] = False
            elif event.key == pygame.K_LEFT:
                keys[1] = False
            elif event.key == pygame.K_DOWN:
                keys[2] = False
            elif event.key == pygame.K_RIGHT:
                keys[3] = False

    # movement
    if keys[0]:
        if player_y > 0:
            player_y -= 7
    elif keys[2]:
        if player_y < 536:
            player_y += 7
    elif keys[1]:
        if player_x > 0:
            player_y -= 2
    elif keys[3]:
        if player_x < 536:
            player_y += 2


    player_y += 5
    sleep(0.05)

print("Game Over!")