import pygame

pygame.init()
x = 600
y = 600

screen = pygame.display.set_mode((x,y))


pineapple = pygame.image.load('assets/pineapple.png').convert_alpha()
pineapple = pygame.transform.scale(pineapple, (70,70))


screen.blit(pineapple, (25,0))

pygame.display.flip()

status = True
while (status):
  for i in pygame.event.get():
    if i.type == pygame.QUIT:
      status == False