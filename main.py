from src import Controller
import pygame
import random
#import your controller

pygame.init()

xcoord = random.randrange(0, windowsize[0])
ycoord = random.randrange(0, windowsize[1])

def main():
    pygame.init()
    controller = Controller()
    #Call your mainloop
    controller.mainloop()
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()



#pizzacrust
pygame.draw.circle(window, '#C29973', center_of_screen, radius)
  
#pepperoni
def circle(surface, color, center, radius):
  for i in range(15):
    pygame.draw.circle(window, '#AB3E24',(xcoord, ycoord), 6)

#sausage
def rectangle(surface, color, rect, border_radius):
  for i in range(15):
    pygame.draw.rectangle(window, '#643C15', (xcoord, ycoord), 2)


