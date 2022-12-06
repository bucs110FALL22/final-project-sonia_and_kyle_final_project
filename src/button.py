import pygame
import sys

pygame.init()
screen_width=500
screen_height=500
screen = pygame.display.set_mode([screen_width, screen_height])
screensize = pygame.display.get_screen_size()

color_light = ('lightpink')
color_dark = ('palevioletred')

pygame.draw.rect(screen, color_dark, [590, 315, 80])

smallfont = pygame.font.sysfont('corbel', 16)
text = smallfont.render('START', True, color_light)
screen.blit(text, (600, 320))

mouse = pygame.mouse.get_pos()

while True:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      if 590 <= mouse[0] <= 670 and 315 <= mouse[1] <= 345:
        print("test works")
