import pygame

pygame.init()
width, height = 700, 500
screen = pygame.display.set_mode((width, height))
screen.fill("#D9E5D6")
font = pygame.font.SysFont('arial', 25, bold = pygame.font.Font.bold)
text = font.render("YOUR SAUCE HAS BEEN ADDED", True, 'darkseagreen')
textRect = text.get_rect()
textRect.center = (250, 40)
screen.blit(text,textRect)
  
crust = pygame.image.load('assets/crust.png')
crust = pygame.transform.scale(crust, (200,200))
screen.blit(crust, (150,90))
  
pesto = pygame.image.load('assets/pestosauce.png').convert_alpha()
pesto = pygame.transform.scale(pesto, (190,190))
screen.blit(pesto, (155,95))


pygame.display.flip()
