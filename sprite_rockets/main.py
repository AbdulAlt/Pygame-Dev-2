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
        self.rocket = pygame.image.load("images/rocket.png").convert_alpha()
        self.rocket = pygame.transform.scale(self.rocket, (70, 100))
        self.rect = self.rocket.get_rect()
        self.image = self.rocket

    # update function
    def update(self, pressed_key):
        # input
        if pressed_key[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_key[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_key[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_key[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)
        
        # limits
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT


sprites = pygame.sprite.Group()

# start game function
def start_game():
    # add object to game loop
    player = Player()
    sprites.add(player)

    # while loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pressed_key = pygame.key.get_pressed()
        player.update(pressed_key)
        
        screen.blit(pygame.image.load("images/bg.png"), (0, 0))
        sprites.draw(screen)
        
                
        pygame.display.update()

start_game()
