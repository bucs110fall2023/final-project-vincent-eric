import pygame
from src.button import Button
from src.character import Character

class Controller:

    def __init__(self):
        pygame.init()
        
        # Load Assets
        self.background = pygame.image.load("assets/background picture.png")
        self.play = Button(450, 200, 'assets/PlayButton.png')
        self.quit = Button(450, 400, 'assets/QuitButton.png')
        
        # Load Display
        width = self.background.get_width()
        height = self.background.get_height()
        self.display = pygame.display.set_mode((width, height))
        
        # Load Players
        self.p1 = Character('assets/ReplayButton.png', self.display, 70, 350)
        self.p2 = Character('assets/ReturnButton.png', self.display, 600, 350)
    
        self.bgcolor = "light blue"
        
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
        self.display.fill(self.bgcolor)
        self.play.place(self.display)
        self.quit.place(self.display)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.play.clicked() == True:
                    self.state = "GAME"
                if self.quit.clicked() == True:
                    pygame.quit()
                    exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
                
    
      
    def gameloop(self):
        self.display.blit(self.background, (0,0))
        
        self.p1.move(pygame.K_a, pygame.K_d, pygame.K_s)
        self.p1.place()
        self.p2.move(pygame.K_j, pygame.K_l, pygame.K_k)
        self.p2.place()

        self.p1.attack(pygame.K_x, self.p2)
        
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