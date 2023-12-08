import pygame
import sys
from player import Player


pygame.init()
"The code used to initialize the screen was written by ChatGPT"
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Example")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

player1 = Player()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(black)
    
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player1.x > 0:
        player1.move_left()
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player1.x + player1.width < 800:
        player1.move_right()
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and player1.y > 0:
        player1.move_up()
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and player1.y + player1.height < 600:
        player1.move_down()

    player1.draw(screen)
    
    pygame.draw.rect(screen, white, (width // 2 - 50, height // 2 - 50, 100, 100))

    pygame.display.update()
