class Controller:
  
  def __init__(self):
    #setup pygame data
    pygame.init()
    pygame.display.init()
    window = pygame.display.set_mode(size = (500,300))
    windowsize = pygame.display.get_window_size()
    radius = int(windowsize[0]/2)
    center_of_screen = (windowsize[0]/2, windowsize[1]/2)
    print(center_of_screen[0])
    window.fill("darkslategrey")
  def mainloop(self):
    #select state loop
    
  
  ### below are some sample loop states ###

  def menuloop(self):
    
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
      #event loop

      #update data

      #redraw
