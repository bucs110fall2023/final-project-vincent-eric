import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.init()
        self.image = pygame.image.load(str(image))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.topleft = (x, y)
        
    def place(self, display):
        display.blit(self.image, (self.x, self.y))

    def clicked(self):
        mousePos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mousePos):
            if pygame.mouse.get_pressed()[0] == 1:
                return True
            

                

