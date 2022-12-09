import pygame

pygame.init()
x = 600
y = 600

screen = pygame.display.set_mode((x,y))


pepperoni = pygame.image.load('assets/pepperoni.png').convert_alpha()
pepperoni = pygame.transform.scale(pepperoni, (70,70))


screen.blit(pepperoni, (25,0))

pygame.display.flip()

status = True
while (status):
  for i in pygame.event.get():
    if i.type == pygame.QUIT:
      status == False