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

        # dictionary holding the colors of the button
        self.fillColors = {
            'normal': '#46943A',
            'hover': '#306128',
            'pressed': '#023020'
        }

    def draw_button(self, background_color, display)->None:
        """
        Creates the button using the given values from the Button class.

        Parameters
        ----------
        background_color, display
        """

        pg.draw.rect(display, background_color, (self.position_x, self.position_y, self.width, self.height), 0, 4)
        # ADD A VERTICAL LINE FOR SHADOW EFFECT
        pg.draw.rect(display, self.fillColors['hover'], (self.position_x + 3, self.position_y + 25, self.width - 3, self.height - 25), 0, 4)
        text_position = (self.text_position_x, (self.position_y + 3))
        
        # rendering the button and displaying the text on it
        button_text = self.font.render(self.text, False, '#000000')
        display.blit(button_text, text_position)

    def mouse_is_working(self) -> bool:
        """
        Shows mouse is working.

        Returns
        ----------
        True
        """
        return True

    def mouse_is_not_working(self) -> bool:
        """
        Shows mouse is not working.

        Returns
        ----------
        False
        """
        return False

    def perform_mouse_click(self, on_click_function: None, display) -> bool:
        """
        Handles the mouse being clicked while on top of the button.

        Parameters
        ----------
        on_click_function, display

        Returns
        ----------
        True if the click effect is working or False if the click effect is not working
        """
        # handling the button click and calling the parameter function with the action
        mouse_position_x, mouse_position_y = pg.mouse.get_pos()
        if pg.mouse.get_pressed(num_buttons = 3)[0] and mouse_position_x > self.position_x and mouse_position_x < (self.position_x + self.width) and mouse_position_y > self.position_y and mouse_position_y < (self.position_y + self.height):
            on_click_function()
            return self.mouse_is_working()
        else:
            return self.mouse_is_not_working()

    def perform_mouse_hover(self, display) -> bool:
        """
        Changes the color of the button while mouse is hovering over it.

        Parameters
        ----------
        display

        Returns
        ----------
        True if the hovering effect is working or False if the hovering effect is not working
        """
        mouse_position_x, mouse_position_y = pg.mouse.get_pos()

        # if mouse is within the button, change color to the darker hue
        if mouse_position_x > self.position_x and mouse_position_x < (self.position_x + self.width) and mouse_position_y > self.position_y and mouse_position_y < (self.position_y + self.height):
            self.draw_button(self.fillColors['hover'], display)
            return self.mouse_is_working()
        else:
            return self.mouse_is_not_working()


    def implement_button(self, display, on_click_function: None) -> None:
        """
        Implements the button onto the screen so it can be displayed and clicked.

        Parameters
        ----------
        display, on_click_function
        """
        self.draw_button(self.fillColors['normal'], display)
        self.perform_mouse_click(on_click_function, display)
        self.perform_mouse_hover(display)
        


# How to call button example:
# start_button = Button(some_width = 140, some_height = 50, some_position_x = 300, some_position_y = 300, some_text = 'Quit', some_on_click_function = myFunction, some_already_pressed = True)

    