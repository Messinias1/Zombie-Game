import string, sys
import pygame as pg

# helper website https://www.thepythoncode.com/article/make-a-button-using-pygame-in-python

pg.init()
fps = 60
fpsClock = pg.time.Clock()
width, height = 800, 600
screen = pg.display.set_mode((width, height))
objects = []

class Button:
    font = pg.font.SysFont('Arial', 30)
    
    width:int
    height:int
    position_x:int
    position_y:int
    text:string
    on_click_function = None
    one_press = False
    already_pressed:bool

    def __init__(self, some_width:int, some_height:int, some_position_x:int, some_position_y:int, some_text:string, some_on_click_function, some_already_pressed):
        """
        Adds values to the parameters when a new Button is created.

        Parameters
        ----------
        some_width, some_height, some_position_x, some_position_y, some_text, some_on_click_function, some_already_pressed
        """
        self.width = some_width
        self.height = some_height
        self.position_x = some_position_x
        self.position_y = some_position_y
        self.text = some_text
        self.on_click_function = some_on_click_function
        self.already_pressed = some_already_pressed

        self.fillColors = {
            'normal': (255, 255, 255),
            'hover': (150, 150, 150),
            'pressed': (100, 100, 100)
        }

        self.buttonSurface = pg.Surface((self.width, self.height))
        self.buttonRect = pg.Rect(self.position_x, self.position_y, self.width, self.height)

        self.buttonSurf = self.font.render(self.text, True, (20, 20, 20))

        objects.append(self)

    def process(self):
        mousePos = pg.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pg.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.one_press:
                    self.on_click_function()
                elif not self.alreadyPressed:
                    self.on_click_function()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)

def myFunction():
    print('Goodbye :(')
    pg.quit()

start_button = Button(some_width = 140, some_height = 50, some_position_x = 300, some_position_y = 300, some_text = 'Quit', some_on_click_function = myFunction, some_already_pressed = True)

while True:
    screen.fill((20, 20, 20))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    for object in objects:
        object.process()
    pg.display.flip()
    fpsClock.tick(fps)

    