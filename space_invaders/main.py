import pygame
import os
pygame.font.init()
pygame.mixer.init()

pygame.init()

# display
WIDTH = 900
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# fonts
health_font = pygame.font.SysFont("Comicsans", 40)
winner_font = pygame.font.SysFont("Times New Roman", 100)

# constants
FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
YELLOW_HIT = pygame.USEREVENT+1
RED_HIT = pygame.USEREVENT+2
BORDER = pygame.Rect(WIDTH / 2 - 5, 0, 10, HEIGHT)
BULLET_FIRE_SOUND = pygame.mixer.Sound('sounds/gun.mp3')
BULLET_HIT_SOUND = pygame.mixer.Sound("sounds/grenade.mp3")

# images
red_image = pygame.image.load(os.path.join("images", "red_rocket.png"))
red_image_sp = pygame.transform.rotate(pygame.transform.scale(red_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
yellow_image = pygame.image.load(os.path.join("images", "yellow_rocket.png"))
yellow_image_sp = pygame.transform.rotate(pygame.transform.scale(yellow_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
bg = pygame.transform.scale(pygame.image.load(os.path.join("images", "bg.png")), (WIDTH, HEIGHT))

# draw window function
def draw_window(red, yellow, red_bullet, yellow_bullet, red_health, yellow_health):
    screen.blit(bg, (0, 0))
    pygame.draw.rect(screen, "black", BORDER)

    red_health_text = health_font.render("health: " + str(red_health), True, "white")
    yellow_health_text = health_font.render("health: " + str(yellow_health), True, "white")

    screen.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    screen.blit(yellow_health_text, (10, 10))
    screen.blit(red_image_sp, (red.x, red.y))
    screen.blit(yellow_image_sp, (yellow.x, yellow.y))
    
    for i in red_bullet:
        pygame.draw.rect(screen, "red", i)
    for i in yellow_bullet:
        pygame.draw.rect(screen, "yellow", i)
    
    pygame.display.update()

# yellow movement
def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: # left
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL < HEIGHT - 15:
        yellow.y += VEL

# red movement
def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: # left
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH: # right
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15:
        red.y += VEL

# bullet stuff
def handle_bullet(red_bullet, yellow_bullet, red, yellow):
    for i in yellow_bullet:
        i.x += BULLET_VEL
        if red.colliderect(i):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullet.remove(i)
        elif i.x > WIDTH:
            yellow_bullet.remove(i)

    for i in red_bullet:
        i.x -= BULLET_VEL
        if yellow.colliderect(i):
            pygame.event.post(pygame.event.Event (YELLOW_HIT))
            red_bullet.remove(i)
        elif i.x < 0:
            red_bullet.remove(i)

# winning
def draw_winner(text):
    draw_text = winner_font.render(text, 1, "white")
    screen.blit(draw_text, (WIDTH / 2 - draw_text.get_width() / 2, HEIGHT / 2 - draw_text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(5000)

# game loop
def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    red_bullet = []
    yellow_bullet = []

    red_health = 10
    yellow_health = 10
    
    clock = pygame.time.Clock()

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullet) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2 - 2, 10, 5)
                    yellow_bullet.append(bullet)
                    BULLET_FIRE_SOUND.play()
                if event.key == pygame.K_RCTRL and len(red_bullet) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 10, 5)
                    red_bullet.append(bullet)  
                    BULLET_FIRE_SOUND.play()

            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()
        
        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow wins"
        if yellow_health <= 0:
            winner_text = "Red wins"
        
        if winner_text != "":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        red_handle_movement(keys_pressed, red)
        yellow_handle_movement(keys_pressed, yellow)

        handle_bullet(red_bullet, yellow_bullet, red, yellow)
        draw_window(red, yellow, red_bullet, yellow_bullet, red_health, yellow_health)
        pygame.display.update()

main()
if __name__ == "__main__":
    main()
