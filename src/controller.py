import pygame

class Controller:

    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode()
        self.state = "MENU"
        

    def mainloop(self):
        while True:
            if self.state == "GAME":
                self.gameloop()
            elif self.state == "END":
                self.gameoverloop()
            else:
                self.menuloop()
  
  ### below are some sample loop states ###

    def menuloop(self):
        print("menu")
        while self.state == "MENU":
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.state = "GAME"
      #event loop

      #update data

      #redraw
      
    def gameloop(self):
        print("game")
        while self.state == "GAME":
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.state = "END"
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

      #redraw
