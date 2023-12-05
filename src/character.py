import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        self.image = pygame.image.load(str(image))
        self.x = x
        self.y = y

## character class (will have to be sprite) for both players