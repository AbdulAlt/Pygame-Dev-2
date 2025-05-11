import pygame
pygame.init()

# display
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rocket = pygame.image.load("rocket.png").convert_alpha()
        self.rocket = pygame.transform.scale(self.rocket, (0, 0))
        self.rect = self.rocket.get_rect()
            

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    pygame.display.update