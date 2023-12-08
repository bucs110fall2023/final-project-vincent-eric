import pygame
from src.Spritesheet import SpriteSheet
from src.button import Button
from src.character import Character

# Constants
CAPTION = 'streetfighterswords.exe'

YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255,255,255)
LIGHT_BLUE = (173, 216, 230)

P1_INITPOS = (70, 350)
P2_INITPOS = (600, 350)
BUTTON1_POS = (240, 200)
BUTTON2_POS = (240, 400)


BACKGROUND_IMG = 'assets/background picture.png'
PLAY_IMG = 'assets/buttons/PlayButton.png'
QUIT_IMG = 'assets/buttons/QuitButton.png'
REPLAY_IMG = 'assets/buttons/ReplayButton.png'
RETURN_IMG = 'assets/buttons/ReturnButton.png'

P1_IDLE = 'assets/Medieval King Pack/Idle.png'
P1_RUN = 'assets/Medieval King Pack/Run/png'
P1_ATTACK = 'assets/Medieval King Pack/Attack_1.png'
P1_JUMP = 'assets/Medieval King Pack/Jump.png'
P1_FALL = 'assets/Medieval King Pack/Fall.png'

P2_IDLE = 'assets/Medieval King Pack 2/Sprites/Idle.png'
P2_RUN = 'assets/Medieval King Pack 2/Sprites/Run.png'
P2_ATTACK = 'assets/Medieval King Pack 2/Sprites/Attack2.png'
P2_JUMP = 'assets/Medieval King Pack 2/ s/Jump.png'
P2_FALL = 'assets/Medieval King Pack 2/Sprites/Fall.png'


class Controller:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(CAPTION)
        
        # Load Assets
        self.bg = pygame.image.load(BACKGROUND_IMG)
        self.play = Button(BUTTON1_POS[0], BUTTON1_POS[1], PLAY_IMG)
        self.quit = Button(BUTTON2_POS[0], BUTTON2_POS[1], QUIT_IMG)
        self.replay = Button(BUTTON1_POS[0], BUTTON1_POS[1], REPLAY_IMG)
        self.return_button = Button(BUTTON2_POS[0], BUTTON2_POS[1], RETURN_IMG)
        
        # Load Display
        width = self.bg.get_width()
        height = self.bg.get_height()
        self.display = pygame.display.set_mode((width, height))
        
        # Load Players        
        self.p1 = Character(P1_IDLE, self.display, P1_INITPOS[0], P1_INITPOS[1])
        self.p2 = Character(P2_IDLE, self.display, P2_INITPOS[0], P2_INITPOS[1])
        
    #    #creating an animation list 
    #     animation_list = []
    #     animation_steps = [6,6,11,2,4,6,2,8]
    #     last_update = pygame.time.get_ticks()
    #     animation_cool = 350
    #     frame = 0
    #     step_counter = 0

    #     #this basically uses the animation steps and moves it frame by frame using the step_counter for every extra frmae
    #     for animation in animation_steps:
    #         temp_img = []  
    #         for _ in range(animation):
    #             temp_img.append(SpriteSheet.get_image(step_counter, 24,24, 3, 1, YELLOW))
    #             step_counter += 1
    #         animation_list.append(temp_img)
    #     print(animation_list) #theoretically if this were to work, then it would print out the movement"
    #     run = True
    #     while run:  
            
    #         #updating animation
    #         current_time = pygame.time.get_ticks()
    #         if current_time > last_update >= animation_cool:
    #             frame+= 1
    #             last_update = current_time
    #             if frame >= len(animation_list):
    #                 frame = 0   
    #     #show each frame image
    #     self.display(animation_list[frame], (0 , 0)) #stopped around the part of 17:52
            
        # Logic
        self.p1_wins = 0
        self.p2_wins = 0
        self.is_p1win = 0
        self.is_p2win = 0
        
        self.state = "MENU"


    def mainloop(self):
        while True:
            if self.state == "GAME":
                self.gameloop()
            elif self.state == "END":
                self.gameoverloop()
            elif self.state == "ROUND":
                self.roundloop()
            elif self.state == "MENU":
                self.menuloop()
        '''
        Description:
            The mainloop that determines which state the game is in.
        Arguments:
            None
        Return:
            None
        '''
        

    def menuloop(self):
        self.display.fill(LIGHT_BLUE)
        self.play.place(self.display)
        self.quit.place(self.display)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.play.clicked() == 1:
                    self.state = "GAME"
                if self.quit.clicked() == 1:
                    pygame.quit()
                    exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        return self.state
        '''
        Description:
            Shows the menu when the game state is "MENU"
        Arguments:
            None
        Return:
            Returns state of program as a string.
        '''               
      
    def gameloop(self):
        p1_binds = [pygame.K_a, pygame.K_d, pygame.K_s, pygame.K_x]
        p2_binds = [pygame.K_j, pygame.K_l, pygame.K_k, pygame.K_n]
        p1_health_coord = (25, 25)
        p2_health_coord = (550, 25)
        
        self.display.blit(self.bg, (0,0))
        
        self.p1.move(p1_binds[0], p1_binds[1], p1_binds[2])
        self.p1.place(self.display)
        self.p2.move(p2_binds[0], p2_binds[1], p2_binds[2])
        self.p2.place(self.display)

        self.p1.attack(p1_binds[3], self.p2)
        self.p2.attack(p2_binds[3], self.p1)
        
        if self.p1.health_bar(p1_health_coord[0], p1_health_coord[1]) == 0:
            self.is_p2win = 1
            self.state = "ROUND"     
        if self.p2.health_bar(p2_health_coord[0], p2_health_coord[1]) == 0:
            self.is_p1win = 1
            self.state = "ROUND"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()
        return self.state
        '''
        Description:
            Shows the game and allows players to play when state is "GAME"
        Arguments:
            None
        Return:
            Returns state of program as a string.
        '''
        
    def roundloop(self):
        if self.is_p1win == 1:
            self.is_p1win == 0
            self.p1_wins = self.p1_wins + 1
            self.p1 = Character(P1_IDLE, self.display, P1_INITPOS[0], P1_INITPOS[1])
            self.p2 = Character(P2_IDLE, self.display, P2_INITPOS[0], P2_INITPOS[1])
            self.state = "GAME"
            if self.p1_wins == 2:
                self.state = "END"
        elif self.is_p2win == 1:
            self.is_p2win == 0
            self.p2_wins = self.p2_wins + 1
            self.p1 = Character(P1_IDLE, self.display, P1_INITPOS[0], P1_INITPOS[1])
            self.p2 = Character(P2_IDLE, self.display, P2_INITPOS[0], P2_INITPOS[1])
            self.state = "GAME"
            if self.p2_wins == 2:
                self.state = "END"
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
        pygame.display.update()
        
        print('round end')
        print(f'player 1 has {self.p1_wins} wins')
        print(f'player 2 has {self.p2_wins} wins')
        return self.state
        '''
        Description:
            Resets the player positions when one player wins, unless the player that won has two wins. In that case, that player wins.
        Arguments:
            None
        Return:
            Returns state of program as a string.
        '''
            
    
    def gameoverloop(self):
        self.display.fill(LIGHT_BLUE)
        self.replay.place(self.display)
        self.return_button.place(self.display)
        
        self.p1_wins = 0
        self.p2_wins = 0
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.replay.clicked() == 1:
                    self.state = "GAME"
                if self.return_button.clicked() == 1:
                    self.state = "MENU"
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        return self.state
        '''
        Description:
            Shows the end of game screen. Offers the choice to replay the game, or return to menu.
        Arguments:
            None
        Return:
            Returns state of program as a string.
        '''