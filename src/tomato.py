import pygame

pygame.init()
x = 600
y = 600

screen = pygame.display.set_mode((x,y))


tomato = pygame.image.load('assets/tomato.png').convert_alpha()
tomato = pygame.transform.scale(tomato, (30,30))


screen.blit(tomato, (0,0))

pygame.display.flip()

status = True
while (status):
  for i in pygame.event.get():
    if i.type == pygame.QUIT:
      status == False