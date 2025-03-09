import pygame
pygame.init()

# display
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# rectangles class
class Rectangles:
    def __init__(self, x, y, width, height, color):
        self.screen = screen
        self.color = color
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.dim = (self.x, self.y, self.width, self.height) 
    def draw(self):
        self.rect_draw = pygame.draw.rect(self.screen, self.color, self.dim)

# object creations from rectangle class
red_rect = Rectangles(50, 50, 100, 300, "red")
yellow_rect = Rectangles(100, 100, 100, 300, "yellow")
green_rect = Rectangles(150, 150, 100, 300, "green")

while True:
    screen.fill("black")
    red_rect.draw()
    yellow_rect.draw()
    green_rect.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    pygame.display.update()