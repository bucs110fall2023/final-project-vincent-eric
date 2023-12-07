import pygame
from src.character import Character

YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255,255,255)
class Health:
    def __init__(self,x,y):
        self.health = 100

def health_bar(self,x,y):
    pygame.draw.rect(self.display , YELLOW , (x, y, 400, 30))
    
    
health_bar(self.p1.health, 20,20)
health_bar(self.p2.health, 500,20)
## health bar