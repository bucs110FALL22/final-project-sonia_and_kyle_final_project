import pygame

class Controller:
  
  def __init__(self):
    #setup pygame data
    pygame.init()
    pygame.display.init()
    self.screen = pygame.display.set_mode(size = (500,300))
    pygame.display.set_caption("Make Your Own Pizza")
    
   
    #self.controller = Screens()
    self.screen.fill("darkslategrey")
    
  def mainloop(self):
    #select state loop
        #event loop
    in_menu = True
      #update data
    while in_menu == True:
      pass
      #playerSelection = self.controller.update_menu(self.screen)
      #if playerSelection != 0:
        #self.gameloop(playerSelection)
      #redraw
      #pygame.display.flip()
    #return playerSelection
  
  ### below are some sample loop states ###

  def menuloop(self):
    pass
    #event loop

      #update data

      #redraw
  def gameloop(self):
    in_game = True
    in_pause = 'no'
      #event loop
    while in_game == True:
      if in_pause == 'no':
        in_pause = self.controller.update_game(self.screen, step)
      elif in_pause == 'yes':
        self.mainloop()
      #update data

      #redraw
    
