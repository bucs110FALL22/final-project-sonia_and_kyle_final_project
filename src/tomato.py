import pygame
import random

pygame.init()
x = 600
y = 600

screen = pygame.display.set_mode((x,y))

for i in range(10):
  x = random.randrange(150, 250)
  y = random.randrange(160, 200)
  tomato = pygame.image.load('assets/tomato.png')
  tomato = pygame.transform.scale(tomato, (30,30))
  screen.blit(tomato, (x,y))


screen.blit(tomato, (0,0))

pygame.display.flip()

status = True
while (status):
  for i in pygame.event.get():
    if i.type == pygame.QUIT:
      status == False