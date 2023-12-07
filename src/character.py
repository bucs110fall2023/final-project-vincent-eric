import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, image, display, x, y):
        self.image = pygame.image.load(str(image))
        self.display = display
        self.x = x
        self.y = y
        
        # Physics Data
        self.x_velocity = 3
        self.y_velocity = 1.5
        self.gravity = 0.5
        self.jump_height = 15
        
        # Movement States
        self.run_left = False
        self.run_right = False
        self.is_jump = False
        self.press = False
        
        # Invisible Wall
        self.x_min = 0
        self.x_max = self.display.get_width()
        self.y_min = 0
        self.y_max = 450
        
        # Attack States
        self.is_attack = False
        
        
        self.rect = pygame.Rect((x, y, 80, 100))

        #health
        self.health = 100
## character class (will have to be sprite) for both players
    # def __init__(self, player, x, y, flip, data, sprite_sheet, animation_steps, sound):
    # need to finish
        
    def place(self):
        pygame.draw.rect(self.display, (255, 0, 0), self.rect)
    
    def move(self, left, right, up): #left, right, jump are pygame inputs
 
        # Move and Jump
        keypress = pygame.key.get_pressed()
        if keypress[left] == True:
            self.run_left = True
        else:
            self.run_left = False
        if keypress[right] == True:
            self.run_right = True
        else:
            self.run_right = False
        if self.is_jump == False:
            if keypress[up] == True:
                self.is_jump = True


        if self.run_left == True:
            self.rect.x = self.rect.x - self.x_velocity
            
        if self.run_right == True:
            self.rect.x = self.rect.x + self.x_velocity
        
        if self.is_jump == True:
            self.rect.y =  self.rect.y - self.y_velocity
            self.y_velocity = self.y_velocity - self.gravity
            if self.y_velocity < -self.jump_height:
                self.y_velocity = self.jump_height
                self.is_jump = False
                
        # Barrier
               
        if self.rect.left < self.x_min:
            self.rect.left = self.x_min
        if self.rect.right > self.x_max:
            self.rect.right = self.x_max
        if self.rect.top < self.y_min:
            self.rect.top = self.y_min
        if self.rect.bottom > self.y_max:
            self.rect.bottom = self.y_max

    def attack(self, attack, target):
        rect_attack = pygame.Rect(self.rect.centerx, self.rect.y, 1.5 * self.rect.width, self.rect.height)
        hit = False
            
        keypress = pygame.key.get_pressed()
        
        pressed = keypress[attack]
        if pressed == True and self.is_attack == False:
            pygame.draw.rect(self.display, (0, 255, 0), rect_attack)
            if rect_attack.colliderect(target.rect):
                hit = True
                target.health -= 10
                print(hit)
        self.is_attack = pressed

        
            
        
        
        



            