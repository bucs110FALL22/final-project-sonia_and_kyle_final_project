import pygame

pygame.init()
x = 600
y = 600

screen = pygame.display.set_mode((x,y))


crust = pygame.image.load('assets/crust.png').convert_alpha()
crust = pygame.transform.scale(crust, (300,300))

screen.blit(crust, (80,10))

pygame.display.flip()

status = True
while (status):
  for i in pygame.event.get():
    if i.type == pygame.QUIT:
      status == False