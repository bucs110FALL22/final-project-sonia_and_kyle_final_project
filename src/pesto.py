import pygame

pygame.init()
x = 600
y = 600

screen = pygame.display.set_mode((x,y))


pesto = pygame.image.load('assets/pestosauce.png').convert_alpha()
pesto = pygame.transform.scale(pesto, (70,70))


screen.blit(pesto, (25,0))

pygame.display.flip()

status = True
while (status):
  for i in pygame.event.get():
    if i.type == pygame.QUIT:
      status == False