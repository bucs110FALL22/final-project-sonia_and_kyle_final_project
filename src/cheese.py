import pygame

pygame.init()
x = 600
y = 600

screen = pygame.display.set_mode((x,y))


cheese = pygame.image.load('assets/cheesesauce.png').convert_alpha()
cheese = pygame.transform.scale(cheese, (290,290))


screen.blit(cheese, (80,10))

pygame.display.flip()

status = True
while (status):
  for i in pygame.event.get():
    if i.type == pygame.QUIT:
      status == False