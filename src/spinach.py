import pygame

pygame.init()
x = 600
y = 600

screen = pygame.display.set_mode((x,y))


spinach = pygame.image.load('assets/spinach.png')
spinach = pygame.transform.scale(spinach, (70,70))


screen.blit(spinach, (25,0))

pygame.display.flip()

status = True
while (status):
  for i in pygame.event.get():
    if i.type == pygame.QUIT:
      status == False