import pygame
import time
pygame.init()

# display
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Birthday Greeting Card")
bg = pygame.image.load("images/bg.png")
image = pygame.transform.scale(bg, (WIDTH, HEIGHT))

while True:
    font = pygame.font.SysFont()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    pygame.display.update