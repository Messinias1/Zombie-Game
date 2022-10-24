import pygame
import character
import constants


class Camera:
    def __init__(self, startx, starty):
        self.x_scroll, self.y_scroll = startx, starty

    def x_pan(self, add_x):
        self.x_scroll += add_x

    def y_pan(self, add_y):
        self.y_scroll += add_y

    def follow_character(self, char):
        # make the camera follow the given character
        self.x_scroll, self.y_scroll = -char.xpos+(constants.SCREEN_WIDTH/2), -char.ypos+(constants.SCREEN_HEIGHT/2)
