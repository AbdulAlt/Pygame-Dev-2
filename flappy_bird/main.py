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

# variables
bg = pygame.image.load("images/bg.png")
ground = pygame.image.load("images/ground.png")
ground_scroll = 0
scroll_speed = 4
flying = False
game_over = False

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
        self.vel = 0
        self.clicked = False
    
    # update function
    def update(self):
        if flying == True:
            self.vel += 0.5

            if self.vel > 8:
                self.vel = 8

            if self.rect.bottom < 758:
                self.rect.y += int(self.vel)
        
        if game_over == False:
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.vel = -10
            
            if pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
                self.clicked = False

            self.counter += 1
            flap_cooldown = 5

            if self.counter > flap_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0

            self.image = self.images[self.index]
            self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90)

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/pipe.png")
        self.rect = self.image.get_rect()
        if pos == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y]
        if pos == -1:
            self.rect.bottomleft = [x, y]



# groups
bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()
flappy = Bird(100, int(WIDTH / 2))
bird_group.add(flappy)

while True:
    clock.tick(fps)

    screen.blit(bg, (0, 0))

    bird_group.draw(screen)
    bird_group.update()
    pipe_group.draw(screen)
    pygame.display.update()

    screen.blit(ground, (ground_scroll, 768))

    if flappy.rect.bottom > 758:
        game_over = True
        flying = False
        flappy.index = 0

    if game_over == False and flying == True:
        btm_pipe = Pipe(WIDTH, int(HEIGHT / 2), -1)
        top_pipe = Pipe(WIDTH, int(HEIGHT / 2), 1)
        pipe_group.add(btm_pipe)
        pipe_group.add(top_pipe)

        ground_scroll -= scroll_speed
        if abs(ground_scroll) > 35:
            ground_scroll = 0
        pipe_group.update()
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True
    
    pygame.display.update()
