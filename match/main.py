import pygame
pygame.init()

# display
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill("white")
pygame.display.update()

# image loading
candy_crush = pygame.image.load("images/candy_crush.jpg")
ludo = pygame.image.load("images/ludo.png")
subway_surf = pygame.image.load("images/subway_surfers.png")
temple_run = pygame.image.load("images/temple_run.png")


# image bliting
screen.blit(candy_crush, (200, 200))
screen.blit(ludo, (200, 300))
screen.blit(subway_surf, (200, 400))
screen.blit(temple_run, (200, 500))

# font rendering
font = pygame.font.SysFont("Times New Roman", 36)
text1 = font.render("Ludo", True, (0, 0, 0))
text2 = font.render("Candy Crush", True, (0, 0, 0))
text3 = font.render("Subway Surfers", True, (0, 0, 0))
text4 = font.render("Temple Run", True, (0, 0, 0))

# text blitting
screen.blit(text3, (500, 200))
screen.blit(text4, (500, 300))
screen.blit(text1, (500, 400))
screen.blit(text2, (500, 500))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, "black", (pos), 10, 0)
        pygame.display.update()

    if event.type == pygame.MOUSEBUTTONUP:
        pos2 = pygame.mouse.get_pos()
        pygame.draw.line(screen, "black", (pos), (pos2), 5)
        pygame.draw.circle(screen, "black", (pos2), 10, 0)
        pygame.display.update()
            
    pygame.display.update()