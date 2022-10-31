import string
import pygame as pg

pg.font.init()

class Button:
    font = pg.font.SysFont('Arial', 20)
    width:int
    height:int
    position_x:int
    position_y:int
    text:string
    text_position_x: int

    def __init__(self, some_width:int, some_height:int, some_position_x:int, some_position_y:int, some_text:string, some_text_position_x: int):
        """
        Adds values to the parameters when a new Button is created.

        Parameters
        ----------
        some_width, some_height, some_position_x, some_position_y, some_text, some_text_position_x
        """
        self.width = some_width
        self.height = some_height
        self.position_x = some_position_x
        self.position_y = some_position_y
        self.text = some_text
        self.text_position_x = some_text_position_x

        self.fillColors = {
            'normal': '#46943A',
            'hover': '#46933A',
            'pressed': '#306128'
        }

    def draw_button(self, display)->None:
        """
        Creates the button using the given values from the Button class.

        Parameters
        ----------
        display
        """

        button = pg.draw.rect(display, self.fillColors['normal'], (self.position_x, self.position_y, self.width, self.height), 0)
        text_position = (self.text_position_x, (self.position_y + 3))
        
        # rendering the button and displaying the text on it
        button_text = self.font.render(self.text, False, '#000000')
        display.blit(button_text, text_position)

        

    def perform_mouse_click(self, on_click_function: None, display)->None:
        """
        Handles the mouse being clicked while on top of the button.

        Parameters
        ----------
        on_click_function, display
        """
        # handling the button click and calling the parameter function with the action
        # if pg.mouse.get_pressed(num_buttons = 3)[0] and pg.rect((self.position_x, self.position_y, self.width, self.height), 0).collidepoint(pg.mouse.get_pos()):
        mouse_position_x, mouse_position_y = pg.mouse.get_pos()
        if pg.mouse.get_pressed(num_buttons = 3)[0] and mouse_position_x > self.position_x and mouse_position_x < (self.position_x + self.width) and mouse_position_y > self.position_y and mouse_position_y < (self.position_y + self.height):
            on_click_function()

    def implement_button(self, display, on_click_function: None) -> None:
        """
        Implements the button onto the screen so it can be displayed and clicked.

        Parameters
        ----------
        display, on_click_function
        """
        self.draw_button(display)
        self.perform_mouse_click(on_click_function, display)
        


# How to call button example:
# start_button = Button(some_width = 140, some_height = 50, some_position_x = 300, some_position_y = 300, some_text = 'Quit', some_on_click_function = myFunction, some_already_pressed = True)

    