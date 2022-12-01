from button import Button
import unittest
from unittest.mock import patch, MagicMock
from pygame import draw, Color, Surface, event
import pygame as pg

class ButtonTest(unittest.TestCase):

    @patch('pygame.draw.rect')
    def test_draw_button(self, mock_rect):
        """
        Tests the Draw Button method is called with the correct color.

        Parameters
        ----------
        mock_rect
        """

        assert mock_rect is draw.rect

        # parameters for draw_button
        test_surface = Surface((800, 600))
        test_color = '#46943A'

        quit_button = Button(some_width = 75,
                        some_height = 30,
                        some_position_x = 10,
                        some_position_y = 560,
                        some_text = 'Quit',
                        some_text_position_x = 29)

        quit_button.draw_button(test_color, test_surface)

        # first index is the first call to draw.rect and the third
        # is the second parameter to draw.rect
        rectangle_color: Color = mock_rect.call_args_list[0][0][1]

        assert rectangle_color == test_color

    def test_perform_mouse_down(self):
        """
        Tests the if statement passes and the function is called when the mouse is pressed down and on the button.
        """

        pg.init()
        # parameters for perform_mouse_click
        test_surface = Surface((800, 600))
        test_event = event
        test_event.type = pg.MOUSEBUTTONDOWN
        test_mouse_position_x = 61
        test_mouse_position_y = 576

        # placeholder function to pass into perform_mouse_click that does nothing
        def pass_as_any_function() -> None:
            # do nothing
            pass

        # mocking draw_button method
        Button.draw_button = MagicMock()

        quit_button = Button(some_width = 75,
                        some_height = 30,
                        some_position_x = 10,
                        some_position_y = 560,
                        some_text = 'Quit',
                        some_text_position_x = 29)

        quit_button.perform_mouse_click(test_event, pass_as_any_function(), test_surface, test_mouse_position_x, test_mouse_position_y)

        # asserting that the draw_button method is being called once 
        # when the if statement for the down click passes
        Button.draw_button.assert_called_once()

    def test_perform_mouse_up(self):
        """
        Tests the if statement passes and the function is called when the mouse is released and on the button.
        """

        pg.init()
        # parameters for perform_mouse_click
        test_surface = Surface((800, 600))
        test_event = event
        test_event.type = pg.MOUSEBUTTONUP
        test_mouse_position_x = 61
        test_mouse_position_y = 576

        # placeholder function to pass into perform_mouse_click that does nothing
        def pass_as_any_function() -> None:
            # do nothing
            pass

        # mocking the placeholder method
        pass_as_any_function = MagicMock()

        quit_button = Button(some_width = 75,
                        some_height = 30,
                        some_position_x = 10,
                        some_position_y = 560,
                        some_text = 'Quit',
                        some_text_position_x = 29)

        quit_button.perform_mouse_click(test_event, pass_as_any_function(), test_surface, test_mouse_position_x, test_mouse_position_y)

        # asserting that the placeholder method is being called once 
        # when the if statement for the up click passes
        pass_as_any_function.assert_called_once()

    def test_mouse_hover(self):
        """
        Tests the if statement passes and the function is called when the mouse is on the button.
        """
        
        pg.init()

        # parameters for perform_mouse_hover
        test_surface = Surface((800, 600))
        test_mouse_position_x = 61
        test_mouse_position_y = 576
        quit_button = Button(some_width = 75,
                        some_height = 30,
                        some_position_x = 10,
                        some_position_y = 560,
                        some_text = 'Quit',
                        some_text_position_x = 29)

        # mocking draw_button method
        Button.draw_button = MagicMock()

        quit_button.perform_mouse_hover(test_mouse_position_x, test_mouse_position_y, test_surface)

        # asserting that the draw_button method is being called once
        Button.draw_button.assert_called_once()