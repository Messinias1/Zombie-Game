from button import Button
import pygame as pg

def test_draw_button():
    quit_button = Button(some_width = 75,
                     some_height = 30,
                     some_position_x = 10,
                     some_position_y = 560,
                     some_text = 'Quit',
                     some_text_position_x = 29)
    screen = pg.display.set_mode((600, 800))

    assert quit_button.draw_button('#000000', screen) == True

def test_perform_mouse_click():
    quit_button = Button(some_width = 75,
                     some_height = 30,
                     some_position_x = 10,
                     some_position_y = 560,
                     some_text = 'Quit',
                     some_text_position_x = 29)
    screen = pg.display.set_mode((600, 800))

    assert quit_button.draw_button('#000000', screen) == True

def test_implement_button():
    quit_button = Button(some_width = 75,
                     some_height = 30,
                     some_position_x = 10,
                     some_position_y = 560,
                     some_text = 'Quit',
                     some_text_position_x = 29)
    screen = pg.display.set_mode((600, 800))

    assert quit_button.draw_button('#000000', screen) == True
    