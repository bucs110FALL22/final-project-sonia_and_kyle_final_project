import pygame

pygame.init()
x = 600
y = 600

screen = pygame.display.set_mode((x,y))


tomatosc = pygame.image.load('assets/tomatoscsauce.png').convert_alpha()
tomatosc = pygame.transform.scale(tomatosc, (290,290))


screen.blit(tomatosc, (80,10))

pygame.display.flip()

status = True
while (status):
  for i in pygame.event.get():
    if i.type == pygame.QUIT:
      status == False