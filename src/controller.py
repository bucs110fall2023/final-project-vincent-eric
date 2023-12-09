import pygame
from src.spritesheet import SpriteSheet
from src.button import Button
from src.character import Character

# Constants
CAPTION = 'streetfightermedievalplsdontsue.exe'

YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255,255,255)
LIGHT_BLUE = (173, 216, 230)

P1_INITPOS = (70, 350)
P2_INITPOS = (600, 350)
BUTTON1_POS = (500, 200)
BUTTON2_POS = (500, 400)
ICON_POS = (0, 50)

ICON_IMG = 'assets/Icon.png'
BACKGROUND_IMG = 'assets/background picture.png'
PLAY_IMG = 'assets/buttons/PlayButton.png'
QUIT_IMG = 'assets/buttons/QuitButton.png'
REPLAY_IMG = 'assets/buttons/ReplayButton.png'
RETURN_IMG = 'assets/buttons/ReturnButton.png'
P1_WIN_IMG = 'assets/victory images/PLAYER 1 WINS.png'
P2_WIN_IMG = 'assets/victory images/PLAYER 2 WINS.png'

P1_IDLE = ('assets/Medieval King Pack/Idle.png', 6)
P1_RUN = ('assets/Medieval King Pack/Run.png',8)
P1_ATTACK = ('assets/Medieval King Pack/Attack_1.png', 4)
P1_JUMP = ('assets/Medieval King Pack/Jump.png', 2)
P1_FALL = ('assets/Medieval King Pack/Fall.png', 2)

P2_IDLE = ('assets/Medieval King Pack 2/Sprites/Idle.png', 8)
P2_RUN = ('assets/Medieval King Pack 2/Sprites/Run.png', 8)
P2_ATTACK = ('assets/Medieval King Pack 2/Sprites/Attack2.png', 4)
P2_JUMP = ('assets/Medieval King Pack 2/Sprites/Jump.png', 2)
P2_FALL = ('assets/Medieval King Pack 2/Sprites/Fall.png', 2)


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
        self.icon = Button(ICON_POS[0], ICON_POS[1], ICON_IMG)
        self.p1win = Button(ICON_POS[0], ICON_POS[1], P1_WIN_IMG)
        self.p2win = Button(ICON_POS[0], ICON_POS[1], P2_WIN_IMG)
        
        # Load Display
        width = self.bg.get_width()
        height = self.bg.get_height()
        self.display = pygame.display.set_mode((width, height))
        
        # Load Players        
        self.p1 = Character(P1_IDLE, P1_RUN, P1_ATTACK, P1_JUMP, P1_FALL,  self.display, P1_INITPOS[0], P1_INITPOS[1])
        self.p2 = Character(P2_IDLE, P2_RUN, P2_ATTACK, P2_JUMP, P2_FALL, self.display, P2_INITPOS[0], P2_INITPOS[1])
        self.players = pygame.sprite.Group(self.p1, self.p2)
        
        self.clock = pygame.time.Clock()
            
        # Logic
        self.is_p1win = 0
        self.is_p2win = 0
        self.player_needload = False
        
        self.state = "MENU"


    def mainloop(self):
        while True:
            if self.state == "GAME":
                self.gameloop()
            elif self.state == "END":
                self.endgameloop()
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
        self.icon.place(self.display)
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
            Returns the state of the program as a string.
        '''               
      
    def gameloop(self):
        p1_binds = [pygame.K_a, pygame.K_d, pygame.K_s, pygame.K_x]
        p2_binds = [pygame.K_j, pygame.K_l, pygame.K_k, pygame.K_n]
        p1_health_coord = (25, 25)
        p2_health_coord = (550, 25)
        
        self.display.blit(self.bg, (0,0))
        
        if self.player_needload == True:
            self.p1 = Character(P1_IDLE, P1_RUN, P1_ATTACK, P1_JUMP, P1_FALL,  self.display, P1_INITPOS[0], P1_INITPOS[1])
            self.p2 = Character(P2_IDLE, P2_RUN, P2_ATTACK, P2_JUMP, P2_FALL, self.display, P2_INITPOS[0], P2_INITPOS[1])
            self.player_needload = False
        
        self.p1.move(p1_binds[0], p1_binds[1], p1_binds[2])
        self.p2.move(p2_binds[0], p2_binds[1], p2_binds[2])

        self.p1.attack(p1_binds[3], self.p2)
        self.p2.attack(p2_binds[3], self.p1)
        
        if self.p1.health_bar(p1_health_coord[0], p1_health_coord[1]) == 0:
            self.is_p2win = 1
            self.state = "END"    
        if self.p2.health_bar(p2_health_coord[0], p2_health_coord[1]) == 0:
            self.is_p1win = 1
            self.state = "END"
            
        self.p1.update()
        self.p2.update()
        
        self.players.draw(self.display)
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
    
    def endgameloop(self):
        self.display.fill(LIGHT_BLUE)
        self.replay.place(self.display)
        self.return_button.place(self.display)
        if self.is_p1win == 1:
            self.p1win.place(self.display)
        if self.is_p2win == 1:
            self.p2win.place(self.display)
        self.player_needload = True
        
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