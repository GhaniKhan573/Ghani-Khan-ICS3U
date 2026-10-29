import pygame

pygame.init()






#Moving Walls

wall_x = 200  # Start off the right side of the screen
wall_y = 300 
wall_speed = 2  # Pixels to move per frame









# Set screen resolution
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400






# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PAIN to code")






# Set up colours
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)
BLUE = (50, 150, 255)
RED = (255, 80, 80)
BG_COLOR = (30, 30, 30)





won = False

# Set up the player
player_x = 30
player_y = 30
player_size = 25
speed = 3




#walls function

def check_collision(player, walls):
    """
    -------------------------------------------------------
    -------------------------------------------------------
    Parameters:
       player - the rectangle representing the player (pygame.Rect)
       walls - a list of rectangles representing the maze walls (list)
    Returns:
       collision - True if the player collides with a wall,
                   False otherwise (bool)
    -------------------------------------------------------
    """
    for wall in walls:
        if player.colliderect(wall):
            return True
    return False

# Set screen resolution
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Maze Game")





# Set up colours
WHITE = (255, 255, 255)
BLUE = (0, 0, 200)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)







# Create the exit
exit_rect = pygame.Rect(540, 340, 30, 30)



# Create the maze walls
walls = [
    pygame.Rect(100, 0, 20, 300),
    pygame.Rect(200, 100, 20, 300),
    pygame.Rect(300, 0, 20, 250),
    pygame.Rect(400, 100, 20, 300),
    pygame.Rect(500, 0, 20, 250)
]





# Set up the game
cexit_rect = pygame.Rect(540, 340, 30, 30)





# Set up the game
clock = pygame.time.Clock()
running = True
won = False




# Main game loop
while running:

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False





# 2. Update wall position (constant movement to the left)
    wall_x -= wall_speed

    # Reset wall to the right side if it moves completely off-screen
    if wall_x < 0:
        wall_x = 800





    # 3. Draw everything
    screen.fill((30, 30, 30))  # Clear screen with dark gray



    # Draw the wall using pygame.Rect
    wall_rect = pygame.Rect(wall_x, wall_y, 800, 600)
    pygame.draw.rect(screen, (255, 80, 80), wall_rect)  # Red wall




   # 1. Create rectangle objects for both the player and the enemy
    player_rect = pygame.Rect(player_x, player_y, 50, 50)
    tentical_rect = pygame.Rect(wall_x, wall_y, 30, 40)





    if player_rect.colliderect(tentical_rect):
        #running = False
        won = True  # Ends the game loop






    # Get the keys being pressed
    keys = pygame.key.get_pressed()

    if not won:

        # Move left
        if keys[pygame.K_LEFT]:
            player_x -= speed
            player = pygame.Rect(player_x, player_y, player_size, player_size)

            if check_collision(player,walls) == True:
                player_x += speed

        # Move right
        if keys[pygame.K_RIGHT]:
            player_x += speed
            player = pygame.Rect(player_x, player_y, player_size, player_size)

            if check_collision(player,walls) == True:
                player_x -= speed

        # Move up
        if keys[pygame.K_UP]:
            player_y -= speed
            player = pygame.Rect(player_x, player_y, player_size, player_size)

            if check_collision(player,walls) == True:
                player_y += speed

        # Move down
        if keys[pygame.K_DOWN]:
            player_y += speed
            player = pygame.Rect(player_x, player_y, player_size, player_size)

            if check_collision(player,walls) == True:
                player_y -= speed








        # Keep the player inside the screen
        if player_x < 0:
            player_x = 0

        if player_x > SCREEN_WIDTH - player_size:
            player_x = SCREEN_WIDTH - player_size

        if player_y < 0:
            player_y = 0

        if player_y > SCREEN_HEIGHT - player_size:
            player_y = SCREEN_HEIGHT - player_size






        # Update the player rectangle
        player = pygame.Rect(player_x, player_y, player_size, player_size)




        # Check if the player reaches the exit
        if player.colliderect(exit_rect):
            won = True




# 2. Update wall position (constant movement to the left)
    wall_x -= wall_speed

    # Reset wall to the right side if it moves completely off-screen
    if wall_x < 0:
        wall_x = 800





    # 3. Draw everything
    screen.fill((30, 30, 30))  # Clear screen with dark gray

    # Draw the wall using pygame.Rect
    wall_rect = pygame.Rect(wall_x, wall_y, 80, 60)
    pygame.draw.rect(screen, (255, 80, 80), wall_rect)  # Red wall





    # Draw the maze walls
    for wall in walls:
        pygame.draw.rect(screen, BLUE, wall)

    # Draw the exit
    pygame.draw.rect(screen, GREEN, exit_rect)

    # Draw the player
    player = pygame.Rect(player_x, player_y, player_size, player_size)
    pygame.draw.rect(screen, RED, player)






    # Display the winning message
    if won:
        font = pygame.font.SysFont(None, 48)
        message = font.render("YOU WIN!", True, BLACK)
        screen.blit(message, (220, 180))




    # Update the display
    pygame.display.flip()

    # Limit the game to 60 FPS
    clock.tick(60)

# Close Pygame
pygame.quit()