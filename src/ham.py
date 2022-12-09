import pygame

pygame.init()
x = 600
y = 600

screen = pygame.display.set_mode((x,y))


ham = pygame.image.load('assets/ham.png')
ham = pygame.transform.scale(ham, (70,70))


screen.blit(ham, (25,0))

pygame.display.flip()

status = True
while (status):
  for i in pygame.event.get():
    if i.type == pygame.QUIT:
      status == False