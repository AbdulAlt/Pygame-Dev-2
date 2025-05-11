import pygame
pygame.init()

# display
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Polygons:
    def __init__(self, color, pos, width = 0):
        self.screen = screen
        self.color = color
        self.pos = pos
        self.width = width
    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.pos, self.width)

# objects
triangle = Polygons("green", [(300, 100), (200, 300), (350, 300)], 0)
triangle2 = Polygons("red", [(300, 400), (200, 600), (350, 600)], 10)

while True:
    screen.fill("white")
    triangle.draw(screen)
    triangle2.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    pygame.display.update()