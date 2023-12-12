import pygame

#AI Generated and edited by Damian Villarreal-Ayala

class Gate:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)

    def set_cords(self, x, y):
        self.x = x
        self.y = y
        
    def draw(self, screen):
        pygame.draw.rect(screen, (125, 125, 125), (self.x, self.y, self.width, self.height))

    def check_collision(self, player_rect):
        return self.rect.colliderect(player_rect)
