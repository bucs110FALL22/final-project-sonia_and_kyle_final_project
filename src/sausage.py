import pygame
pygame.init()
window = pygame.display.set_mode 

def rectangle(surface, color, rect, border_radius):
  for i in range(15):
    pygame.draw.rectangle(window, '#643C15', (xcoord, ycoord), 2)
