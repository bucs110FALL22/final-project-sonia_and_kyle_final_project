import pygame

pygame.init()
x = 600
y = 600

screen = pygame.display.set_mode((x,y))


bbq = pygame.image.load('assets/bbqsauce.png').convert_alpha()
bbq = pygame.transform.scale(bbq, (290,290))


screen.blit(bbq, (80,10))

pygame.display.flip()

status = True
while (status):
  for i in pygame.event.get():
    if i.type == pygame.QUIT:
      status == False