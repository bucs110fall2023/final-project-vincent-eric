import pygame

class Button:
    def __init__(self, x, y, image):
        self.image = pygame.image.load(str(image))
        self.x = x
        self.y = y
        
    def place(self, display):
        display.blit(self.image, (self.x, self.y))
        
    def play(self):
        pass
        
