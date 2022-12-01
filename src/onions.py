import pygame
pygame.init()
window = pygame.display.set_mode 

def arc(surface, color, rect, start_angle, stop_angle):
  for i in range(15):
    pygame.draw.arc(window, '#CF5ACE',(xcoord, ycoord), (2,5))