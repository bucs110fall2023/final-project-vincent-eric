import pygame

YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255,255,255)

class Character(pygame.sprite.Sprite):
    def __init__(self, image, display, x = 0, y = 0):
        self.image = pygame.image.load(str(image))
        self.display = display
        self.x = x
        self.y = y
        
        # Physics Data
        self.x_velocity = 3
        self.y_velocity = 1.5
        self.gravity = 0.5
        self.jump_height = 15
        
        # Jump States
        self.is_jump = False
        
        # Invisible Wall
        self.x_min = 0
        self.x_max = self.display.get_width()
        self.y_min = 0
        self.y_max = 450
        
        # Attack States
        self.is_attack = False
        
        
        self.rect = pygame.Rect((x, y, 80, 100))

        #health for characters
        self.health = 100
        #to make sure they can attack both sides
        self.flip = False

        
    def place(self):
        pygame.draw.rect(self.display, (255, 0, 0), self.rect)
    
    def move(self, left, right, up): #left, right, jump are pygame inputs
 
        # Movement Keybinds
        keypress = pygame.key.get_pressed()
        if keypress[left] == True:
            self.rect.x = self.rect.x - self.x_velocity
        if keypress[right] == True:
            self.rect.x = self.rect.x + self.x_velocity
        if self.is_jump == False:
            if keypress[up] == True:
                self.is_jump = True
                
        # Jump
        if self.is_jump == True:
            self.rect.y =  self.rect.y - self.y_velocity
            self.y_velocity = self.y_velocity - self.gravity
            if self.y_velocity < -self.jump_height:
                self.y_velocity = self.jump_height
                self.is_jump = False
        
        # Players Always Facing Each Other
        
                
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
        
    def health_bar(self,x,y):
        ratio = self.health / 100
        pygame.draw.rect(self.display , WHITE , (x - 2, y - 2, 404, 34))
        pygame.draw.rect(self.display , RED , (x, y, 400, 30))
        pygame.draw.rect(self.display , YELLOW , (x, y, 400 * ratio, 30))
        
        

        
            
        
        
        



            