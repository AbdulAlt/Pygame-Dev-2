import pygame
import sys
pygame.init()

# display
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill("white")
pygame.display.update()

# circle class
class Circle:
    def __init__(self, color, pos, radius, width = 0):
        self.screen = screen
        self.color = color
        self.width = width
        self.radius = radius
        self.pos = pos
    def draw(self):
        self.my_circle = pygame.draw.circle(self.screen, self.color, self.pos, self.radius, self.width)
    def grow_circle(self, r):
        self.radius += r
        self.my_circle = pygame.draw.circle(self.screen, self.color, self.pos, self.radius, self.width)


position = (300, 300)
radius = 50
width = 2
pygame.draw.circle(screen, "red", position, radius, width)
pygame.display.update()

# circle object
green_circle = Circle("green", position, radius + 60)
yellow_circle = Circle("yellow", position, radius + 40)
orange_circle = Circle("orange", position, radius, 5)
purple_circle = Circle("purple", position, 20)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill("white")
            green_circle.draw()
            yellow_circle.draw()
            orange_circle.draw()
            purple_circle.draw()
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.fill("white")
            screen.fill("white")
            green_circle.grow_circle(10)
            yellow_circle.grow_circle(10)
            orange_circle.grow_circle(10)
            purple_circle.grow_circle(10)
            pygame.display.update()
