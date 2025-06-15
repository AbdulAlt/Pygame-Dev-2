import pygame
from pygame.locals import *

pygame.init()

# displays
WIDTH = 864
HEIGHT = 936
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
fps = 60

# images
bg = pygame.image.load("images/bg.png")
ground = pygame.image.load("images/ground.png")
ground_scroll = 0
scroll_speed = 4

# player sprite
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for i in range(1, 4):
            bird_image = pygame.image.load(f"images/bird{i}.png")
            self.images.append(bird_image)
            self.image = self.images[self.index]
            self.rect = self.image.get_rect()
            self.rect.center = [x, y]
    
    # update function
    def update(self):
        self.counter += 1
        flap_cooldown = 5
        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]



# bird group
bird_group = pygame.sprite.Group()
flappy = Bird(100, int(WIDTH / 2))
bird_group.add(flappy)

while True:
    clock.tick(fps)

    screen.blit(bg, (0, 0))

    bird_group.draw(screen)
    bird_group.update()

    screen.blit(ground, (ground_scroll, 768))
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll = 0
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    pygame.display.update()