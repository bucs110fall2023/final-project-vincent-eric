import pygame, random

#Initialize pygame
pygame.init()

#Set display window
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Monster Wrangler")

#Set FPS and Clock
FPS = 60
clock = pygame.time.Clock()

#Define Classes
class Game():
    """A class to control gameplay"""
    def __init__(self, player, monster_group):
        """Initilize the game object"""
        #Set game values
        self.score = 0
        self.round_number = 0
        self.round_time = 0
        self.frame_count = 0

        self.player = player
        self.monster_group = monster_group

        #set sounds and music
        self.next_level_sound = pygame.mixer.Sound("next_level.wav")

        #Set font
        self.font = pygame.font.Font("Abrushow.ttf")

        #Set images
        blue_image = pygame.image.load("blue_monster.png")
        green_image = pygame.image.load("green_monster.png")
        purple_image = pygame.image.load("purple_monster.png")
        yellow_image = pygame.image.load("yellow_monster.png")

        self.target_monster_images = [blue_image, green_image, purple_image, yellow_image]

        self.target_monster_type = random.randint(0,3)
        self.target_monster_image = self.target_monster_images[self.target_monster_type]

        self.target_monster_rect = self.target_monster_image.get_rect()
        self.target_monster_rect.centerx = WINDOW_WIDTH//2
        self.target_monster_rect.top = 30


    def update(self):
        """Update the game object"""
        self.frame_count += 1
        if self.frame_count == FPS:
            self.round_time += 1
            self.frame_count = 0

        #Check for collisions
        self.check_collisions()

    def draw(self):
        """Draw the HUD and other items to the display"""
        pass

    def check_collisions(self):
        """Check for collisions between player and monsters"""
        # Check for collision between a player and an indiviaual monster
        # WE must test the type of the monster to see if it matches the type of our target monster
        collided_monster = pygame.sprite.spritecollideany(self.player, self.monster_group)

        # We collided with a monster
        if collided_monster:
            # Caught the correct monster
            if collided_monster.type == self.target_monster_type:
                self.score += 100 * self.round_number
                # Remove caught monster
                collided_monster.remove(self.monster_group)
                if (self.monster_group):
                    # There are more monsters to catch
                    self.player.catch_sound.play()
                    self.choose_new_target()
                else:
                    # The round is complete
                    self.player.reset()
                    self.start_new_round()
            # Caught the wrong monster
            else:
                self.player.die_sound.play()
                self.player.lives -= 1
                # Check for game over
                if self.player.lives <= 0:
                    self.pause_game("Final Score: " + str(self.score), "Press 'Enter' to play again")
                    self.reset_game()
                self.player.reset()

    def start_new_round(self):
        """Populate the board with new monsters (Buro's)"""
        pass

    def choose_new_target(self):
        """choose a new target monster for the player"""
        pass

    def pause_game(self):
        """Pauses the current game"""
        pass

    def reset_game(self):
        """resets the game to the beginning"""
        pass


class Player(pygame.sprite.Sprite):
    """A player class that the user can control"""
    def __init__(self):
        """Initialize the player"""
        super().__init__()
        self.image = pygame.image.load("knight.jpg")
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH//2
        self.rect.bottom = WINDOW_HEIGHT

        self.lives = 5
        self.warps = 3
        self.velocity = 8

        self.catch_sound = pygame.mixer.Sound("catch.wav")
        self.die_sound = pygame.mixer.Sound("die.wav")
        self.warp_sound = pygame.mixer.Sound("warp.wav")

    def update(self):
        """Updates the player"""
        keys = pygame.key.get_pressed()

        #Move the player within the bounds of the screen
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.velocity
        if keys[pygame.K_UP] and self.rect.top > 100:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN] and self.rect.bottom < WINDOW_HEIGHT - 100:
            self.rect.y += self.velocity


    def warp(self):
        """Warp the player back to the safe space at the bottom of the screen"""
        if self.warps > 0:
            self.warps -= 1
            self.warp_sound.play()
            self.rect.bottom = WINDOW_HEIGHT

    def reset(self):
        """Resets the players position"""
        self.rect.centerx = WINDOW_WIDTH//2
        self.rect.bottom = WINDOW_HEIGHT

class Monster(pygame.sprite.Sprite):
    """A class to create an enemy monster object(s)"""
    def __init__(self, x, y, image, monster_type):
        """Initialize the monster"""
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        #Monster type is an INT 0 -> blue, 1 -> green, 2 -> purple, 3 -> yellow
        self.type = monster_type

        #Set random motion
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])
        self.velocity = random.randint(1, 5)


    def update(self):
        """Updates the monster"""

        self.rect.x += self.dx*self.velocity
        self.rect.y += self.dy*self.velocity

        #Bounce off the edges of the screen
        if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
            self.dx = -1*self.dx
        if self.rect.top <= 100 or self.rect.bottom >= WINDOW_HEIGHT - 100:
            self.dy = -1*self.dy

#Create a player group and Player object
my_player_group = pygame.sprite.Group()
my_player = Player()
my_player_group.add(my_player)

#Create a monster group.
my_monster_group = pygame.sprite.Group()

#Create a game object
my_game = Game(my_player, my_monster_group)
my_game.pause_game("Monster Wrangler", "Press 'Enter' to begin")
my_game.start_new_round()


#The main game loop
running = True
while running:
    #Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Player wants to warp
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                my_player.warp()

    #Fill the display
    display_surface.fill(0, 0, 0)

    #Update and draw the sprite groups
    my_player_group.update()
    my_player_group.draw(display_surface)

    my_monster_group.update()
    my_monster_group.draw(display_surface)

    #Update and draw the Game
    my_game.update()
    my_game.draw()

    #update the display and tick the clock
    pygame.display.update()
    clock.tick(FPS)



#End the game
pygame.quit()