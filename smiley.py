import pygame
pygame.init()

# display
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

while True:
    screen.fill("white")
    pygame.draw.circle(screen, "yellow", (400, 400), 60, 10)
    pygame.draw.circle(screen, "black", (400, 430), 20, 10, draw_bottom_right=True, draw_bottom_left=True)
    pygame.draw.circle(screen, "black", (370, 400), 20, 10)
    pygame.draw.circle(screen, "black", (420, 400), 20, 10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()