import pygame

pygame.init()
x = 600
y = 600

screen = pygame.display.set_mode((x,y))


mushroom = pygame.image.load('assets/mushroom.png').convert_alpha()
mushroom = pygame.transform.scale(mushroom, (70,70))


window.blit(mushroom, (25,0))

screen.display.flip()

status = True
while (status):
  for i in pygame.event.get():
    if i.type == pygame.QUIT:
      status == False