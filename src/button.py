import pygame

class Button(pygame.sprite.Sprite):
    
    def __init__(self, image, x = 0, y = 0):
        pygame.init()
        self.image = pygame.image.load(str(image))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.topleft = (x, y)
        '''
        Description:
            Initialization and variables.
        Arguments:
            x (int): x-coordinate, default = 0
            y (int): y-coordinate, defualt = 0
            image (str): the image of the button
        Return:
            None
        '''
        
    def place(self, display):
        display.blit(self.image, (self.x, self.y))
        '''
        Description: 
            Blits the image onto a surface.
        Arguments:
            display (pygame module): the surface for the image to be blitted on.
        Returns:
            None
        '''

    def clicked(self):
        mousePos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mousePos):
            if pygame.mouse.get_pressed()[0] == 1:
                return True
        '''
        Description:
            Triggers when the mouse button gets pressed.
        Arguments:
            None
        Returns:
            Boolean Value of True.
        '''
            

                

