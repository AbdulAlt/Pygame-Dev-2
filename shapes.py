import pygame
pygame.init()

# display
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

while True:
    screen.fill("white")
    pygame.draw.circle(screen, "blue", (400, 400), 60, 10)
    pygame.draw.circle(screen, "green", (400, 400), 60, 10, draw_top_right=True, draw_bottom_left=True)
    pygame.draw.rect(screen, "red", (300, 300, 50, 100), 10, border_bottom_right_radius=50, border_bottom_left_radius=25)
    pygame.draw.rect(screen, "red", (600, 300, 100, 100), 10)
    pygame.draw.line(screen, "orange", (400, 300), (560, 300), 10)
    pygame.draw.ellipse(screen, "black", (450, 500, 50, 100), 10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()