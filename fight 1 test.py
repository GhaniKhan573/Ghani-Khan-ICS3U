import pygame
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SIZE = 40

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Maze Game")

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
GRASS_LIGHT = (24, 100, 73)
GRASS_DARK = (18, 84, 57)
YELLOW = (150, 150, 0)
BLACK = (0, 0, 0)
BLUE = (50, 150, 255)
RED = (255, 80, 80)
BG_COLOR = (30, 30, 30)
ORANGE = (255, 165, 0)

won = False
lost = False
running = True
clock = pygame.time.Clock()

player_x = 30
player_y = 30
player_size = 25
speed = 6

wall_vx = 0  
wall_vy = 0 
wall_hx = 300
wall_hy = 200
wall_speed = 5  
wall_width = 80
wall_height = 60

attack_number = 0
player_dmg = 0
dmg_block = False
speed_block = False

exit_rect = pygame.Rect(540, 340, 30, 30)
dmg_rect = pygame.Rect(500, 300, 30, 30)
speed_rect = pygame.Rect(200, 300, 30, 30)


def spawn_wall():   
    global wall_hx, wall_hy, wall_vx, wall_vy
 
    side = random.randint(0, 3)
    
    if side == 0:  
        wall_hx = random.randint(0, SCREEN_WIDTH - wall_width)
        wall_hy = -wall_height 
        wall_vx = 0
        wall_vy = wall_speed
        
    elif side == 1:  
        wall_hx = random.randint(0, SCREEN_WIDTH - wall_width)
        wall_hy = SCREEN_HEIGHT 
        wall_vx = 0
        wall_vy = -wall_speed
        
    elif side == 2:  
        wall_hx = -wall_width  
        wall_hy = random.randint(0, SCREEN_HEIGHT - wall_height)
        wall_vx = wall_speed
        wall_vy = 0
        
    elif side == 3:  
        wall_hx = SCREEN_WIDTH 
        wall_hy = random.randint(0, SCREEN_HEIGHT - wall_height)
        wall_vx = -wall_speed
        wall_vy = 0

spawn_wall()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not won and not lost:
        if attack_number not in [3, 7, 14, 20]:

            wall_hx += wall_vx
            wall_hy += wall_vy

            if (wall_hx > SCREEN_WIDTH + 100 or 
                wall_hx < -wall_width - 100 or 
                wall_hy > SCREEN_HEIGHT + 100 or 
                wall_hy < -wall_height - 100):
                spawn_wall()
                attack_number += 1
                power = random.randint (0,11)
                if power == 0:
                    speed_block = True


        elif attack_number >= 20:
            player_dmg += 1 

        else: 
            dmg_block = True

    keys = pygame.key.get_pressed()

    if not won and not lost:
        if keys[pygame.K_LEFT]:
            player_x -= speed
        if keys[pygame.K_RIGHT]:
            player_x += speed
        if keys[pygame.K_UP]:
            player_y -= speed
        if keys[pygame.K_DOWN]:
            player_y += speed

        if player_x < 0:
            player_x = 0
        if player_x > SCREEN_WIDTH - player_size:
            player_x = SCREEN_WIDTH - player_size
        if player_y < 0:
            player_y = 0
        if player_y > SCREEN_HEIGHT - player_size:
            player_y = SCREEN_HEIGHT - player_size

    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    tentical_rect = pygame.Rect(wall_hx, wall_hy, wall_width, wall_height)

    if dmg_block:
        if player_rect.colliderect(dmg_rect):
            player_dmg += 1
            attack_number += 1
            wall_speed += 1
            dmg_block = False

        
    if player_rect.colliderect(tentical_rect):
        lost = True 

    if speed_block == True:
        if player_rect.colliderect(speed_rect):
            speed += 1 
            speed_block = False

    if player_dmg >= 4:
        if player_rect.colliderect(exit_rect):
            won = True

    screen.fill(GRASS_DARK)  


    for i in range(0, 800 * 600, SIZE):
        x_cube = i % 800
        y_cube = (i // 800) * SIZE

        # Offsets the light squares every other row to create the grid
        if ((x_cube // SIZE) + (y_cube // SIZE)) % 2 == 1:
         pygame.draw.rect(screen, GRASS_LIGHT, (x_cube, y_cube, SIZE, SIZE))






    if player_dmg >= 4:
        pygame.draw.rect(screen, GREEN, exit_rect)

    if dmg_block:
        pygame.draw.rect(screen, RED, dmg_rect)

    if speed_block == True:
        pygame.draw.rect(screen, ORANGE, speed_rect)


    pygame.draw.rect(screen, YELLOW, tentical_rect)

    player_image = pygame.image.load("alive heart.png")
    player_image = pygame.transform.scale(30, 30)

    player_rect = player_image.get_rect()
    player_rect.topleft = (player_x, player_y)





 



    font = pygame.font.SysFont("Arial", 24)
    if player_dmg == 0:
        info = font.render("[O][O][O][0]", True, GREEN)
    elif player_dmg == 1:
        info = font.render("[O][O][O]", True, GREEN)        
    elif player_dmg == 2:
        info = font.render("[O][O][X]", True, YELLOW)
    elif player_dmg >= 3 and won == False:
        info = font.render("[O][X][X]", True, ORANGE)
    else:
        info = font.render("[X][X][X]", True, RED) 

    screen.blit(info, (10, 360))



    if won:
        win_font = pygame.font.SysFont(None, 48)
        message = win_font.render("YOU WIN!", True, GREEN)
        screen.blit(message, (220, 180))
    elif lost:
        lose_font = pygame.font.SysFont(None, 48)
        message = lose_font.render("GAME OVER", True, RED)
        screen.blit(message, (200, 180))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()