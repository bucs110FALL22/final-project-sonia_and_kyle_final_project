class Controller:
  
  def __init__(self):
    #setup pygame data
    pygame.init()
    pygame.display.init()
    self.screen = pygame.display.set_mode(size = (500,300))
    windowsize = pygame.display.get_window_size()
    radius = int(windowsize[0]/2)
    center_of_screen = (windowsize[0]/2, windowsize[1]/2)
    self.controller = Screens()
    window.fill("darkslategrey")
    
  def mainloop(self):
    #select state loop
        #event loop
    in_menu = True
      #update data
    while in_menu == True:
      playerSelection = self.controller.update_menu(self.screen))
      if playerSelection != 0:
        self.gameloop(playerSelection)
      #redraw
      pygame.display.flip()
    return playerSelection
  
  ### below are some sample loop states ###

  def menuloop(self):
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
    
