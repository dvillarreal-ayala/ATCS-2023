import pygame

class Player:
    def __init__(self, x = 50, y = 450):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 60
        self.y_vel = 5
        self.x_vel = 5
    
    def set_cords(self, x, y):
        self.x = x
        self.y = y
    
    def move_left(self):
        self.x -= self.x_vel
    
    def move_right(self):
        self.x += self.x_vel

    def move_up(self):
        self.y -= self.y_vel
    
    def move_down(self):
        self.y += self.y_vel

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))
