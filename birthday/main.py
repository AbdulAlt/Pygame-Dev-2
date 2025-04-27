import pygame
import time
import sys

pygame.init()

WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Birthday Greeting Card")

bg = pygame.image.load("images/bg.jpg")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
gift = pygame.image.load("images/gift.jpg")
cake = pygame.image.load("images/cake.jpg")

font = pygame.font.SysFont("Times New Roman", 72)
font2 = pygame.font.SysFont("Arial", 36)

screen.fill("white")
screen.blit(bg, (0, 0))
text = font.render("Happy", True, (0, 0, 0))
text2 = font.render("Birthday", True, (0, 0, 0))
screen.blit(text, (250, 180))
screen.blit(text2, (180, 300))
pygame.display.update()

start_time = time.time()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if time.time() - start_time > 2:
        screen.fill("white")
        screen.blit(gift, (0, 0))
        text3 = font2.render("I wish you a bright future ahead", True, (0, 0, 0))
        screen.blit(text3, (30, 30))
        pygame.display.update()
        time.sleep(2)

        screen.fill("white")
        screen.blit(cake, (0, 0))
        pygame.display.update()
        time.sleep(2)

        running = False

pygame.quit()
sys.exit()
