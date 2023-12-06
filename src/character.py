import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        self.image = pygame.image.load(str(image))
        self.x = x
        self.y = y

## character class (will have to be sprite) for both players
class fighter():
    # def __init__(self, player, x, y, flip, data, sprite_sheet, animation_steps, sound):
    # need to finish
        
  def move(self, screen_width, screen_height, surface, target, round_over):
    SPEED = 10
    GRAVITY = 2
    dx = 0
    dy = 0
    self.running = False
    self.attack_type = 0

    key = pygame.key.get_pressed()

    #player 1 & 2
    if self.attacking == False and self.alive == True and round_over == False:
      if self.player == 1:
        if key[pygame.K_a]:
          dx = -SPEED
          self.running = True
        if key[pygame.K_d]:
          dx = SPEED
          self.running = True
        if key[pygame.K_w] and self.jump == False:
          self.vel_y = -30
          self.jump = True
        if key[pygame.K_r] or key[pygame.K_t]:
          self.attack(target)
          if key[pygame.K_r]:
            self.attack_type = 1
          if key[pygame.K_t]:
            self.attack_type = 2
     

      if self.player == 2:
        if key[pygame.K_a]:
          dx = -SPEED
          self.running = True
        if key[pygame.K_d]:
          dx = SPEED
          self.running = True
        if key[pygame.K_w] and self.jump == False:
          self.vel_y = -30
          self.jump = True
        if key[pygame.K_r] or key[pygame.K_t]:
          self.attack(target)
          if key[pygame.K_r]:
            self.attack_type = 1
          if key[pygame.K_t]:
            self.attack_type = 2
            