import pygame
import random

pygame.init()

# Set screen resolution
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Maze Game")

# Set up colours
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)
BLUE = (50, 150, 255)
RED = (255, 80, 80)
BG_COLOR = (30, 30, 30)

# Game state variables
won = False
lost = False
running = True
clock = pygame.time.Clock()

# Set up the player
player_x = 30
player_y = 30
player_size = 25
speed = 3

# Moving Walls variables
wall_vx = 0  
wall_vy = 0 
wall_hx = 300
wall_hy = 200
wall_speed = 2  # Pixels to move per frame
wall_width = 80
wall_height = 60

# Create the exit
exit_rect = pygame.Rect(540, 340, 30, 30)

# Random spawn function for the wall
def spawn_wall():   
    global wall_hx, wall_hy, wall_vx, wall_vy
 
    # Pick a random side: 0 = Top, 1 = Bottom, 2 = Left, 3 = Right
    side = random.randint(0, 3)
    
    if side == 0:  # Top (moving DOWN)
        wall_hx = random.randint(0, SCREEN_WIDTH - wall_width)
        wall_hy = -wall_height 
        wall_vx = 0
        wall_vy = wall_speed
        
    elif side == 1:  # Bottom (moving UP)
        wall_hx = random.randint(0, SCREEN_WIDTH - wall_width)
        wall_hy = SCREEN_HEIGHT 
        wall_vx = 0
        wall_vy = -wall_speed
        
    elif side == 2:  # Left (moving RIGHT)
        wall_hx = -wall_width  
        wall_hy = random.randint(0, SCREEN_HEIGHT - wall_height)
        wall_vx = wall_speed
        wall_vy = 0
        
    elif side == 3:  # Right (moving LEFT)
        wall_hx = SCREEN_WIDTH 
        wall_hy = random.randint(0, SCREEN_HEIGHT - wall_height)
        wall_vx = -wall_speed
        wall_vy = 0

# Spawn the first wall
spawn_wall()

# Main game loop
while running:

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update wall position if game is active
    if not won and not lost:
        wall_hx += wall_vx
        wall_hy += wall_vy

        # Check if the wall has moved completely off-screen, then respawn
        if (wall_hx > SCREEN_WIDTH + 100 or 
            wall_hx < -wall_width - 100 or 
            wall_hy > SCREEN_HEIGHT + 100 or 
            wall_hy < -wall_height - 100):
            spawn_wall()

    # Get the keys being pressed
    keys = pygame.key.get_pressed()

    if not won and not lost:
        # Move left
        if keys[pygame.K_LEFT]:
            player_x -= speed
        # Move right
        if keys[pygame.K_RIGHT]:
            player_x += speed
        # Move up
        if keys[pygame.K_UP]:
            player_y -= speed
        # Move down
        if keys[pygame.K_DOWN]:
            player_y += speed

        # Keep the player inside the screen
        if player_x < 0:
            player_x = 0
        if player_x > SCREEN_WIDTH - player_size:
            player_x = SCREEN_WIDTH - player_size
        if player_y < 0:
            player_y = 0
        if player_y > SCREEN_HEIGHT - player_size:
            player_y = SCREEN_HEIGHT - player_size

    # Update rectangle bounding boxes for collisions
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    tentical_rect = pygame.Rect(wall_hx, wall_hy, wall_width, wall_height)

    # Check collisions
    if player_rect.colliderect(tentical_rect):
        lost = True 

    if player_rect.colliderect(exit_rect):
        won = True

    # ==================== DRAW EVERYTHING (Done ONCE per frame) ====================
    screen.fill(BG_COLOR)  # Clear screen once with dark gray

    # Draw the exit
    pygame.draw.rect(screen, GREEN, exit_rect)

    # Draw the moving wall/tentacle
    pygame.draw.rect(screen, RED, tentical_rect)

    # Draw the player
    pygame.draw.rect(screen, BLUE, player_rect)

    # Display game status messages
    if won:
        font = pygame.font.SysFont(None, 48)
        message = font.render("YOU WIN!", True, GREEN)
        screen.blit(message, (220, 180))
    elif lost:
        font = pygame.font.SysFont(None, 48)
        message = font.render("GAME OVER", True, RED)
        screen.blit(message, (200, 180))

    # Update the display
    pygame.display.flip()

    # Limit the game to 60 FPS
    clock.tick(60)

pygame.quit()