import string
import pygame as pg

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


# How to call button example:
# start_button = Button(some_width = 140, some_height = 50, some_position_x = 300, some_position_y = 300, some_text = 'Quit', some_on_click_function = myFunction, some_already_pressed = True)

    