import pygame
from .spritesheet import SpriteSheet

YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255,255,255)

class Character(pygame.sprite.Sprite):
    def __init__(self, idleimage, runimage, attackimage, jumpimage, fallimage, display, x = 0, y = 0, health = 100):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = 80
        self.height = 100
        self.rect = pygame.Rect((x, y, self.width, self.height))
        self.idleimage = SpriteSheet(idleimage[0],idleimage[1],self.width,self.height).get_images()
        self.runimage = SpriteSheet(runimage[0],runimage[1],self.width,self.height).get_images()
        self.jumpimage = SpriteSheet(jumpimage[0],jumpimage[1],self.width,self.height).get_images()
        self.attackimage = SpriteSheet(attackimage[0],attackimage[1],self.width,self.height).get_images()
        self.fallimage = SpriteSheet(fallimage[0],fallimage[1],self.width,self.height).get_images()
        self.image = None
        self.is_animating = False
        self.display = display
        
        self.y_velocity = 1.5
        
        self.image_list = self.idleimage
        self.image_index = 0
        
        # States
        self.is_jump = 0
        self.is_attack = 0
        self.flip = 0
        
        self.health = health

    
    def move(self, left, right, up): #left, right, jump are pygame inputs
        # Physics Data
        x_velocity = 3
        gravity = 0.5
        jump_height = 15
        
        # Invisible Wall
        x_min = 0
        x_max = self.display.get_width()
        y_min = 0
        y_max = 450
        
        # Movement Keybinds
        keypress = pygame.key.get_pressed()
        if keypress[left] == 1:
            self.rect.x = self.rect.x - x_velocity
        if keypress[right] == 1:
            self.rect.x = self.rect.x + x_velocity
        if self.is_jump == 0:
            if keypress[up] == 1:
                self.is_jump = 1
                
        # Jump
        if self.is_jump == 1:
            self.rect.y =  self.rect.y - self.y_velocity
            self.y_velocity = self.y_velocity - gravity
            if self.y_velocity < -jump_height:
                self.y_velocity = jump_height
                self.is_jump = 0
                
        # Invisible Wall       
        if self.rect.left < x_min:
            self.rect.left = x_min
        if self.rect.right > x_max:
            self.rect.right = x_max
        if self.rect.top < y_min:
            self.rect.top = y_min
        if self.rect.bottom > y_max:
            self.rect.bottom = y_max
            
        
    def attack(self, attack, target):
        # Face Each Other
        if self.rect.centerx < target.rect.centerx:
            self.flip = 0
        else:
            self.flip = 1
        
        #Attack
        shift_rect_attack = 2 * self.width * self.flip
        rect_attack = pygame.Rect(self.rect.centerx - shift_rect_attack, self.rect.y, 1.5 * self.rect.width, self.rect.height)
        
        keypress = pygame.key.get_pressed()
        pressed = keypress[attack]
        if pressed == 1 and self.is_attack == 0:
            self.animate(self.attackimage)
            if rect_attack.colliderect(target.rect):
                target.health -= 10
        self.is_attack = pressed
        
    def health_bar(self, x = 0, y = 0):
        ratio = self.health / 100
        pygame.draw.rect(self.display , WHITE , (x - 2, y - 2, 404, 34))
        pygame.draw.rect(self.display , RED , (x, y, 400, 30))
        pygame.draw.rect(self.display , YELLOW , (x, y, 400 * ratio, 30))
        return ratio
    
    def update(self):
        self.image = self.image_list[int(self.image_index)]
        self.image_index += 0.05
        if len(self.image_list) <= int(self.image_index):
            self.image_index = 0
            self.image_list = self.idleimage
            
    def animate(self,animation):
        self.image_index = 0
        self.image_list = animation
    
    
    
    
        
        

        
            
        
        
        



            