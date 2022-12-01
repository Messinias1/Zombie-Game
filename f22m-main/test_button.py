from button import Button
import unittest
import os
from unittest.mock import patch, MagicMock
from unittest import mock
from pygame import draw, Color, Surface, event
import pygame as pg

class ButtonTest(unittest.TestCase):

    @patch('pygame.draw.rect')
    def test_draw_button(self, mock_rect):
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

    def pass_as_any_function(self) -> None:
        # do nothing
        pass

    def test_perform_mouse_click(self):

        pg.init()
        # parameters for perform_mouse_click
        test_surface = Surface((800, 600))
        test_event = event
        test_event.type = pg.MOUSEBUTTONUP
        test_mouse_position_x = 61
        test_mouse_position_y = 576

        on_click_function = MagicMock()

        quit_button = Button(some_width = 75,
                        some_height = 30,
                        some_position_x = 10,
                        some_position_y = 560,
                        some_text = 'Quit',
                        some_text_position_x = 29)

        quit_button.perform_mouse_click(test_event, self.pass_as_any_function(), test_surface, test_mouse_position_x, test_mouse_position_y)

        on_click_function.assert_called_once()

    def test_implement_button(self):
        
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