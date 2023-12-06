import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, image, display, x, y):
        self.image = pygame.image.load(str(image))
        self.display = display
        self.x = x
        self.y = y
        self.rect = pygame.Rect((x, y, 80, 100))

## character class (will have to be sprite) for both players
    # def __init__(self, player, x, y, flip, data, sprite_sheet, animation_steps, sound):
    # need to finish
        
    def place(self):
        pygame.draw.rect(self.display, (255, 0, 0), self.rect)
    
    def move(self, left, right, up): #left, right, jump are pygame inputs
        x_speed = 3
        y_speed = 2
        gravity = 1
        y_max = 30
        
        run_left = False
        run_right = False
        jump = False
        
        
        keypress = pygame.key.get_pressed()
        if keypress[left] == True:
            run_left = True
        if keypress[right] == True:
            run_right = True
        if keypress[up] == True:
            jump = True
        
        if run_left == True:
            self.rect.x = self.rect.x - x_speed
        if run_right == True:
            self.rect.x = self.rect.x + x_speed
        if jump == True:
            self.rect.y = self.rect.y - y_speed
            y_speed = y_speed - gravity
            if y_speed < y_max:
                jump = False
                y_speed = y_max

        
        
        



            