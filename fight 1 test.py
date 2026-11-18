import pygame
import random
import time




def spawn_wall_2():   
    global wall_hx, wall_hy, wall_vx, wall_vy
 
    side = 3
    

        
    if side == 3:  
        wall_hx = SCREEN_WIDTH 
        wall_hy = random.randint(0, SCREEN_HEIGHT - wall_height)
        wall_vx = -wall_speed
        wall_vy = 0



def check_collision(player_rect, walls):
    
    for wall in walls:
        if player_rect.colliderect(wall):
            return True
    return False


pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("seabattle1.mp3")
pygame.mixer.music.play(-1)
pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SIZE = 40
p_pos = 1




seeweed_image = pygame.image.load("seeweed.png")
seeweed_image = pygame.transform.scale(seeweed_image, (80, 80))


attack_image = pygame.image.load("attack.png")
attack_image = pygame.transform.scale(attack_image, (40, 40))

speed_image = pygame.image.load("speed.png")
speed_image = pygame.transform.scale(speed_image, (50, 50))

monster_image = pygame.image.load("monster.png")
monster_image = pygame.transform.scale(monster_image, (95, 70))

player_image = pygame.image.load("alive heart.png")
player_image = pygame.transform.scale(player_image, (30, 30)) #You had this in your loop which was loading the photo each time. ok thanks mr brimly

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Maze Game")




WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
GRASS_LIGHT = (24, 73, 100)
GRASS_DARK = (18, 57, 84)
YELLOW = (250, 250, 0)
BLACK = (0, 0, 0)
BLUE = (50, 150, 255)
RED = (255, 80, 80)
BG_COLOR = (30, 30, 30)
ORANGE = (255, 165, 0)
HITBOX = (150, 150, 50)




won = False
lost = False
running = False
running_2 = True
clock = pygame.time.Clock()

player_x = 30
player_y = 30
player_size = 25
speed = 6




wall_vx = 0  
wall_vy = 0 
wall_hx = 300
wall_hy = 200
wall_speed = 4  
wall_width = 80
wall_height = 60

speed_x = 300
speed_y = 200

attack_number = 0
player_dmg = 0
dmg_block = False
speed_block = False

exit_rect = pygame.Rect(540, 340, 30, 30)
dmg_rect = pygame.Rect(500, 300, 30, 30)
speed_rect = pygame.Rect(speed_x, speed_y, 30, 30)












if running_2 == True:

    spawn_wall_2()
#else:
#     spawn_wall()



while running or running_2:

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
                if running_2 == True:
                    spawn_wall_2()
#                else:
#                    spawn_wall()

                attack_number += 1
                power = random.randint (0,5)
                if power == 0 and running == True:
                    speed_x = random.randint (100,500)
                    speed_y = random.randint (100,300)
                    speed_block = True


        elif attack_number >= 20:
            player_dmg += 1 

        else: 
            dmg_block = True

    if player_dmg >= 4:
        running == False
        running_2 == True
        player_x = 30
        player_y = 30
        player_size = 25
        speed = 6
        wall_vx = 0  
        wall_vy = 0 
        wall_hx = 300
        wall_hy = 200
        wall_speed = 4  
        wall_width = 80
        wall_height = 60


    keys = pygame.key.get_pressed()

    if not won and not lost:
        if keys[pygame.K_LEFT]:
            player_x -= speed
            player_rect = pygame.Rect(player_x, player_y, player_size, player_size)

            if check_collision(player_rect,walls) == True:
                player_x += speed 

        if keys[pygame.K_RIGHT]:
            player_x += speed
            player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
            if check_collision(player_rect,walls) == True:
                player_x -= speed 

        if keys[pygame.K_UP]:
            player_y -= speed
            player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
            if check_collision(player_rect,walls) == True:
                player_y += speed 


        if keys[pygame.K_DOWN]:
            player_y += speed
            player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
            if check_collision(player_rect,walls) == True:
                player_y -= speed 



        if player_x < 0:
            player_x = 0
        if player_x > SCREEN_WIDTH - player_size:
            player_x = SCREEN_WIDTH - player_size
        if player_y < 0:
            player_y = 0
        if player_y > SCREEN_HEIGHT - player_size:
            player_y = SCREEN_HEIGHT - player_size



#all my collision rectangle are made here
    if running_2:

        walls = [
            pygame.Rect(100, 0, 20, 300),
            pygame.Rect(200, 100, 20, 300),
            pygame.Rect(300, 0, 20, 250),
            pygame.Rect(400, 100, 20, 300),
            pygame.Rect(500, 0, 20, 250)
        ]

    exit_rect = pygame.Rect(540, 340, 30, 30)
    seeweed_rect = pygame.Rect(80, 120, 40, 40)

    dmg_rect = pygame.Rect(500, 300, 30, 30)
    speed_rect = pygame.Rect(speed_x, speed_y, 30, 30)
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    tentical_rect = pygame.Rect(wall_hx, wall_hy, wall_width, wall_height)

        
    if player_rect.colliderect(tentical_rect):
        lost = True 

    if speed_block == True and running == True:
        if player_rect.colliderect(speed_rect):
            speed += 1 
            speed_block = False

    if player_dmg >= 4 and running_2 == True:
        if player_rect.colliderect(exit_rect):
            won = True








    screen.fill(GRASS_DARK)  


    for i in range(0, 800 * 600, SIZE):
        x_cube = i % 800
        y_cube = (i // 800) * SIZE

    # Offsets the light squares every other row to create the grid
        if ((x_cube // SIZE) + (y_cube // SIZE)) % 2 == 1:
         pygame.draw.rect(screen, GRASS_LIGHT, (x_cube, y_cube, SIZE, SIZE))





#Final attack imaging
    if player_dmg >= 4 and running_2 == True:
        exit_rect = player_image.get_rect()
        exit_rect.topleft = (540,340)

        screen.blit(attack_image, exit_rect)

#attack imaging
    if dmg_block == True:
        dmg_rect = player_image.get_rect()
        dmg_rect.topleft = (500,300)

        screen.blit(attack_image, dmg_rect)

#power imaging
    if speed_block == True:
        speed_rect = player_image.get_rect()
        speed_rect.topleft = (speed_x - 10, speed_y - 10)

        screen.blit(speed_image, speed_rect)


#monster imaging
    tentical_rect = player_image.get_rect()
    tentical_rect.topleft = (wall_hx - 10, wall_hy - 10)

    screen.blit(monster_image, tentical_rect)


#player imaging
    player_rect = player_image.get_rect()
    player_rect.topleft = (player_x, player_y)

    screen.blit(player_image, player_rect)

    for wall in walls:
        pygame.draw.rect(screen, BLUE, wall)


#Seeweed
    if running == True:
        seeweed_rect = player_image.get_rect()
        seeweed_rect.topleft = (80, 120)
        screen.blit(seeweed_image, seeweed_rect)


        seeweed_rect = player_image.get_rect()
        seeweed_rect.topleft = (240, 280)
        screen.blit(seeweed_image, seeweed_rect)

        seeweed_rect = player_image.get_rect()
        seeweed_rect.topleft = (80, 280)
        screen.blit(seeweed_image, seeweed_rect)


        seeweed_rect = player_image.get_rect()
        seeweed_rect.topleft = (320, 120)
        screen.blit(seeweed_image, seeweed_rect)


        seeweed_rect = player_image.get_rect()
        seeweed_rect.topleft = (0, 200)
        screen.blit(seeweed_image, seeweed_rect)

        seeweed_rect = player_image.get_rect()
        seeweed_rect.topleft = (400, 0)
        screen.blit(seeweed_image, seeweed_rect)

        seeweed_rect = player_image.get_rect()
        seeweed_rect.topleft = (380, 320)
        screen.blit(seeweed_image, seeweed_rect)

        seeweed_rect = player_image.get_rect()
        seeweed_rect.topleft = (260, 40)
        screen.blit(seeweed_image, seeweed_rect)











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
        time.sleep(5)
        p_pos = 2
    elif lost:
        lose_font = pygame.font.SysFont(None, 48)
        message = lose_font.render("GAME OVER RESTART", True, RED)
        screen.blit(message, (110, 180))


    pygame.display.flip()
    clock.tick(45)















pygame.quit()