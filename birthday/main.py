import pygame
import time
import sys
pygame.init()

WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Birthday Greeting Card")
bg = pygame.image.load("images/bg.jpg")
image_bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

while True:
    font = pygame.font.SysFont("Times New Roman", 72)
    text = font.render("Happy", True, (0, 0, 0))
    text2 = font.render("Birthday", True, (0, 0, 0))
    screen.fill("White")
    screen.blit(image_bg, (0, 0))
    screen.blit(text, (250, 180))
    screen.blit(text2, (180, 160))
    pygame.display.update()
    time.sleep(10)

    gift = pygame.image.load("images/gift.jpg")
    font2 = pygame.font.SysFont("Arial", 36)
    text3 = font2.render("I wish you a bright future ahead", True, (0, 0, 0))
    screen.fill("white")
    screen.blit(gift, (0, 0))
    screen.blit(text3, (30, 30))
    pygame.display.update()
    time.sleep(2)

    cake = pygame.image.load("images/cake.jpg")
    screen.fill("white")
    screen.blit(cake, (0, 0))
    pygame.display.update()
    time.sleep(2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
