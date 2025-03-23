import pygame
pygame.init()

# display
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill("white")
pygame.display.update()

# circle class
class Circle:
    def __init__(self, color, pos, radius, width):
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
green_circle = Circle("green", position, radius + 60, width)
yellow_circle = Circle("yellow", position, radius + 40, width)
orange_circle = Circle("orange", position, radius, 5)
purple_circle = Circle("purple", position, 20, width)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill("white")
            blue_circle.draw()
            pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            screen.fill("white")
            blue_circle.grow_circle(10)
            pygame.display.update()