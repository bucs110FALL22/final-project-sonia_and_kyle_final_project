import pygame

pygame.init()
x = 600
y = 600

screen = pygame.display.set_mode((x,y))


sausage = pygame.image.load('assets/sausage.png').convert_alpha()
sausage = pygame.transform.scale(sausage, (70,70))


screen.blit(sausage, (25,0))

pygame.display.flip()

status = True
while (status):
  for i in pygame.event.get():
    if i.type == pygame.QUIT:
      status == False