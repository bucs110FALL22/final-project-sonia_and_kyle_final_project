import pygame

pygame.init()
x = 600
y = 600

screen = pygame.display.set_mode((x,y))


alfredo = pygame.image.load('assets/alfredosauce.png').convert_alpha()
alfredo = pygame.transform.scale(alfredo, (70,70))
screen.blit(alfredo, (25,0))

pygame.display.flip()

status = True
while (status):
  for i in pygame.event.get():
    if i.type == pygame.QUIT:
      status == False

