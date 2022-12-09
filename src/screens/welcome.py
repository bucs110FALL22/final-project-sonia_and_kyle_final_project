import sys
import pygame

pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
title = pygame.display.set_caption("welcome")

font = pygame.font.SysFont('arial', 28)
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
            'normal': '#D9E5D6',
            'hover': '#EDDEA4',
            'pressed': '#EDDEA4',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, '#91AB8B')

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

def startButton():
    print('test works')
    startButton = True
  
startButton = Button(180 , 300, 250, 110, 'START', startButton)


while True:
  screen.fill("#0FA3B1")
  font = pygame.font.SysFont('arial', 35, bold = pygame.font.Font.bold)
  text = font.render("MAKE YOUR OWN PIZZA", True, '#05808C')

  textRect = text.get_rect()
  textRect.center = (300, 40)
  screen.blit(text,textRect)

  mascot = pygame.image.load('assets/mascot.png')
  mascot = pygame.transform.scale(mascot, (200,200))
  screen.blit(mascot, (220,100))
  pygame.display.flip()
  
  
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

  for object in objects:
        object.process()

  pygame.display.flip()
  fpsClock.tick(fps)
