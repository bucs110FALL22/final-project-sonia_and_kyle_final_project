import pygame
import random

pygame.init()

x = 600
y = 600

screen = pygame.display.set_mode((x,y))

for i in range(10):
  x = random.randrange(150, 250)
  y = random.randrange(160, 200)
  mushroom = pygame.image.load('assets/mushroom.png')
  mushroom = pygame.transform.scale(mushroom, (20,20))
  screen.blit(mushroom, (x,y))

pygame.display.flip()

status = True
while (status):
  for i in pygame.event.get():
    if i.type == pygame.QUIT:
      status == False