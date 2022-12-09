import pygame
import sys

pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 700, 500
screen = pygame.display.set_mode((width, height))


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
            'normal': '#FF9B42',
            'hover': '#F7A072',
            'pressed': '#F7A072',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, '#C4510C')

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

def myBack():
    print('test works')
    myBack = True
def myNext():
    print('test works')
  
back = Button(50, 290, 90, 30, '<<back', myBack)
next = Button(370, 290, 90, 30, 'next>>', myNext)



while True:
  screen.fill("#D9E5D6")
  font = pygame.font.SysFont('arial', 25, bold = pygame.font.Font.bold)
  text = font.render("YOUR SAUCE HAS BEEN ADDED", True, 'darkseagreen')
  textRect = text.get_rect()
  textRect.center = (250, 40)
  screen.blit(text,textRect)
  
  crust = pygame.image.load('assets/crust.png')
  crust = pygame.transform.scale(crust, (200,200))
  screen.blit(crust, (150,90))
  
  pesto = pygame.image.load('assets/pestosauce.png').convert_alpha()
  pesto = pygame.transform.scale(pesto, (190,190))
  screen.blit(pesto, (155,95))
  pygame.display.flip()

  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

  for object in objects:
    object.process()

  pygame.display.flip()
  fpsClock.tick(fps)

