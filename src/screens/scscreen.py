import sys
import pygame


pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
title = pygame.display.set_caption("choose a sauce")


font = pygame.font.SysFont('arial', 16)

objects = []

class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False,):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
    

        self.fillColors = {
            'normal': '#F786AF',
            'hover': '#F68393',
            'pressed': '#F68393',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, '#CB4154')

        self.alreadyPressed = False

        objects.append(self)

    def process(self):

        mousePos = pygame.mouse.get_pos()
        
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])

                if self.onePress:
                    self.onclickFunction()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)

def myFunction():
    print('test works')
def myNext():
    print('test works')
def myBack():
    print('test works')

tomato = Button(95 , 165, 120, 30, 'TOMATO', myFunction)
pesto = Button(95, 115, 120, 30, 'PESTO', myFunction)
alfredo = Button(235, 165, 120, 30, 'ALFREDO', myFunction)
barbecue = Button(235, 115, 120, 30, 'BARBECUE', myFunction)

next = Button(270, 290, 120, 30, 'NEXT', myNext)
back = Button(50, 290, 120, 30, 'BACK', myBack)

while True:
  screen.fill("#D9E5D6")
  font = pygame.font.SysFont('arial', 30)
  text = font.render("PICK YOUR SAUCE!", True, 'darkseagreen')
  textRect = text.get_rect()
  textRect.center = (225, 40)
  screen.blit(text,textRect)

  
  
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

  for object in objects:
        object.process()

  pygame.display.flip()
  fpsClock.tick(fps)
