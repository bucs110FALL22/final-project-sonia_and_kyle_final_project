import sys
import pygame

pygame.init()
width, height = 700, 500
screen = pygame.display.set_mode((width, height))
screen.fill("#D9E5D6")
font = pygame.font.SysFont('arial', 25, bold = pygame.font.Font.bold)
text = font.render("YOUR PIZZA IS BEING MADE!", True, 'darkseagreen')
textRect = text.get_rect()
textRect.center = (250, 40)
screen.blit(text,textRect)
  
crust = pygame.image.load('assets/crust.png')
crust = pygame.transform.scale(crust, (200,200))
screen.blit(crust, (150,90))
  
tomatosc = pygame.image.load('assets/tomatosauce.png').convert_alpha()
tomatosc = pygame.transform.scale(tomatosc, (190,190))
screen.blit(tomatosc, (150,90))

cheese = pygame.image.load('assets/cheese.png').convert_alpha()
cheese = pygame.transform.scale(cheese, (190,190))
screen.blit(cheese, (150,90))

pygame.display.flip()





