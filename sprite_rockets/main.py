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
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

    def update(self, pressed_key):
        if pressed_key[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_key[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_key[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_key[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)   

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

# apple
class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.apple = pygame.image.load("images/apple.png").convert_alpha()
        self.apple = pygame.transform.scale(self.apple, (50, 50))
        self.rect = self.apple.get_rect()
        self.image = self.apple
        self.rect.topleft = (100, 100)

    def update(self, pressed_key):
        if pressed_key[pygame.K_w]:
            self.rect.move_ip(0, -5)
        if pressed_key[pygame.K_s]:
            self.rect.move_ip(0, 5)
        if pressed_key[pygame.K_a]:
            self.rect.move_ip(-5, 0)
        if pressed_key[pygame.K_d]:
            self.rect.move_ip(5, 0)

# banana
class Banana(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.banana = pygame.image.load("images/banana.png").convert_alpha()
        self.banana = pygame.transform.scale(self.banana, (50, 50))
        self.rect = self.banana.get_rect()
        self.image = self.banana
        self.rect.topleft = (200, 150)

# orange
class Orange(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.orange = pygame.image.load("images/orange.png").convert_alpha()
        self.orange = pygame.transform.scale(self.orange, (50, 50))
        self.rect = self.orange.get_rect()
        self.image = self.orange
        self.rect.topleft = (300, 200)

# strawberry
class Strawberry(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.strawberry = pygame.image.load("images/strawberry.png").convert_alpha()
        self.strawberry = pygame.transform.scale(self.strawberry, (50, 50))
        self.rect = self.strawberry.get_rect()
        self.image = self.strawberry
        self.rect.topleft = (400, 250)

# watermelon
class Watermelon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.watermelon = pygame.image.load("images/watermelon.png").convert_alpha()
        self.watermelon = pygame.transform.scale(self.watermelon, (50, 50))
        self.rect = self.watermelon.get_rect()
        self.image = self.watermelon
        self.rect.topleft = (500, 300)

# start game function
def start_game():
    player = Player()
    apple = Apple()
    banana = Banana()
    orange = Orange()
    strawberry = Strawberry()
    watermelon = Watermelon()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        pressed_key = pygame.key.get_pressed()
        player.update(pressed_key)
        apple.update(pressed_key)

        screen.blit(pygame.image.load("images/bg.png"), (0, 0))
        screen.blit(player.image, player.rect)
        screen.blit(apple.image, apple.rect)
        screen.blit(banana.image, banana.rect)
        screen.blit(orange.image, orange.rect)
        screen.blit(strawberry.image, strawberry.rect)
        screen.blit(watermelon.image, watermelon.rect)

        pygame.display.update()

start_game()
