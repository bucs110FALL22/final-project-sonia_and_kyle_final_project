import sys
import pygame


pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

#title = pygame.font.SysFont('arial', 50)
#pygame.title.Font.set_bold()
#title.render("PICK YOUR TOPPINGS!", True, 'darkseagreen')
 


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

def myFunction():
    print('test works')



tomato = Button(95 , 95, 120, 30, 'TOMATOES', myFunction,)
spinach = Button(95, 145, 120, 30, 'SPINACH', myFunction)
mushroom = Button(235, 95, 120, 30, 'MUSHROOM', myFunction)
pineapple = Button(235, 145, 120, 30, 'PINEAPPLE', myFunction)
pepperoni = Button(95, 195, 120, 30, 'PEPPERONI', myFunction)
sausage = Button(235, 195, 120, 30, 'SAUSAGE', myFunction)
ham = Button(155, 245, 120, 30, 'HAM', myFunction)

while True:
  screen.fill("#D9E5D6")
  font = pygame.font.SysFont('arial', 30)
  text = font.render("PICK YOUR TOPPINGS!", True, 'darkseagreen')
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



exit.onclick()