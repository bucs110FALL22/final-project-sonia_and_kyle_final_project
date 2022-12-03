import pygame
import sys

pygame.init()
window = pygame.display.set_mode(size=(500, 300))
windowsize = pygame.display.get_window_size()

color_light = ('lightpink')
color_dark = ('palevioletred')

pygame.draw.rect(window, color_dark, [590, 315, 80])

smallfont = pygame.font.sysfont('corbel', 16)
text = smallfont.render('START', True, color_light)
window.blit(text, (600, 320))

mouse = pygame.mouse.get_pos()

while True:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      if 590 <= mouse[0] <= 670 and 315 <= mouse[1] <= 345:
        print("test works")
