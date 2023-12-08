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

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(black)
    
    pygame.draw.rect(screen, white, (width // 2 - 50, height // 2 - 50, 100, 100))

    pygame.display.update()
