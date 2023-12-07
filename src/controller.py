import pygame
from src.button import Button
from src.character import Character

YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255,255,255)
class Controller:

    def __init__(self):
        pygame.init()
        
        # Load Assets
        self.bg = pygame.image.load("assets/background picture.png")
        self.play = Button(450, 200, 'assets/buttons/PlayButton.png')
        self.quit = Button(450, 400, 'assets/buttons/QuitButton.png')
        
        # Load Display
        width = self.bg.get_width()
        height = self.bg.get_height()
        self.display = pygame.display.set_mode((width, height))
        
        # Load Players
        self.p1 = Character('assets/Medieval King Pack/Idle.png', self.display, 70, 350)
        self.p2 = Character('assets/Medieval King Pack 2/Sprites/Idle.png', self.display, 600, 350)
        
        self.state = "MENU"
      

    def mainloop(self):
        while True:
            if self.state == "GAME":
                self.gameloop()
            elif self.state == "END":
                self.gameoverloop()
            elif self.state == "MENU":
                self.menuloop()
        
        

    def menuloop(self):
        menu_color = (173, 216, 230)
        self.display.fill(menu_color)
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
                
                
    
      
    def gameloop(self):
        p1_binds = [pygame.K_a, pygame.K_d, pygame.K_s, pygame.K_x]
        p1_health_coord = (25, 25)
        p2_binds = [pygame.K_j, pygame.K_l, pygame.K_k, pygame.K_n]
        p2_health_coord = (550, 25)
        
        self.display.blit(self.bg, (0,0))
        
        self.p1.move(p1_binds[0], p1_binds[1], p1_binds[2])
        self.p1.place()
        self.p2.move(p2_binds[0], p2_binds[1], p2_binds[2])
        self.p2.place()

        self.p1.attack(p1_binds[3], self.p2)
        self.p2.attack(p2_binds[3], self.p1)
        
        self.p1.health_bar(p1_health_coord[0], p1_health_coord[1])
        self.p2.health_bar(p2_health_coord[0], p2_health_coord[1])
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

                
        pygame.display.update()
            # for event in pygame.event.get():
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     self.state = "END"
      #event loop

      #update data
    

      #redraw
    
    def gameoverloop(self):
        print("gameover")
        while self.state == "END":
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.state = "MENU"
      #event loop

      #update data
      #function to draw the health bar
    
    
      #redraw