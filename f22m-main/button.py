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
        self._fill_colors = {
            'normal': '#46943A',
            'hover': '#59bc4a',
            'pressed': '#023020',
            'side effect': '#306128'
        }

    def draw_button(self, background_color, display)->None:
        """
        Creates the button using the given values from the Button class.

        Parameters
        ----------
        background_color, display

        Returns
        ----------
        True
        """

        pg.draw.rect(display, background_color, (self.position_x, self.position_y, self.width, self.height), 0, 4)
        # ADD A VERTICAL LINE FOR SHADOW EFFECT
        pg.draw.rect(display, self._fill_colors['side effect'], ((self.position_x + self.width) - 5, self.position_y + 0.5, 5, self.height), 0, 4)
        # horizontal shadow
        pg.draw.rect(display, self._fill_colors['side effect'], (self.position_x + 1, self.position_y + 25, self.width - 4, self.height - 25), 0, 4)
        text_position = (self.text_position_x, (self.position_y + 1))
        
        # rendering the button and displaying the text on it
        button_text = self.font.render(self.text, False, '#000000')
        display.blit(button_text, text_position)

    def perform_mouse_click(self, event: pg.event, on_click_function: None, display: pg.surface)->None:
        """
        Handles the mouse being clicked while on top of the button.

        Parameters
        ----------
        event, on_click_function, display

        Returns
        ----------
        True
        """
        # handling the button click and calling the parameter function with the action
        mouse_position_x, mouse_position_y = pg.mouse.get_pos()

        ### CURRENTLY TRYING TO ADD FUNCTIONALITY FOR PRESSING BUTTON DOWN TO DARKEN BUTTON
        # FOR LOOP IN MAIN EVENT FOR LOOP CALLING THIS FUNCTION FROM BUTTON
        
        if event.type == pg.MOUSEBUTTONDOWN and mouse_position_x > self.position_x and mouse_position_x < (self.position_x + self.width) and mouse_position_y > self.position_y and mouse_position_y < (self.position_y + self.height):
            self.draw_button(self._fill_colors['pressed'], display)
        elif event.type == pg.MOUSEBUTTONUP and mouse_position_x > self.position_x and mouse_position_x < (self.position_x + self.width) and mouse_position_y > self.position_y and mouse_position_y < (self.position_y + self.height):
            on_click_function()

    def perform_mouse_hover(self, display)->None:
        """
        Changes the color of the button while mouse is hovering over it.

        Parameters
        ----------
        display

        Returns
        ----------
        True
        """
        mouse_position_x, mouse_position_y = pg.mouse.get_pos()

        # if mouse is within the button, change color to the darker hue
        if mouse_position_x > self.position_x and mouse_position_x < (self.position_x + self.width) and mouse_position_y > self.position_y and mouse_position_y < (self.position_y + self.height):
            self.draw_button(self._fill_colors['hover'], display)

    def implement_button(self, display)->None:
        """
        Implements the button onto the screen so it can be displayed.

        Parameters
        ----------
        display
        """
        self.draw_button(self._fill_colors['normal'], display)
        self.perform_mouse_hover(display)