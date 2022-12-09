from tpscreen import myTomato
from tpscreen import mySpinach
from tpscreen import myMushroom
from tpscreen import myPineapple
from tpscreen import myPepperoni
from tpscreen import mySausage
from tpscreen import myHam

import sys
import pygame

pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

while True:
  screen.fill("#D9E5D6")
  font = pygame.font.SysFont('arial', 30)
  text = font.render("YOUR PIZZA IS BEING MADE!", True, 'darkseagreen')
  textRect = text.get_rect()
  textRect.center = (225, 40)
  screen.blit(text,textRect)

crust = pygame.image.load('assets/crust.png').convert_alpha()
crust = pygame.transform.scale(crust, (300,300))
screen.blit(crust, (80,10))
  
tomatosc = pygame.image.load('assets/tomatosauce.png').convert_alpha()
tomatosc = pygame.transform.scale(tomatosc, (70,70))
screen.blit(tomatosc, (25,0))



