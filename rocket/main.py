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
player = pygame.image.load("C:\Users\44794\Music\Game Dev 2\images\rocket")
bg = pygame.image.load("bg.png")

while player_y < 600:
    # blit the images
    screen.blit(bg, (0, 0))
    screen.blit(player, (player_x, player_y))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    pygame.display.update()
