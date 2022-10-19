import pygame
import character


class Camera:
    def __init__(self, startx, starty):
        self.x_scroll, self.y_scroll = startx, starty

    def x_pan(self, add_x):
        self.x_scroll += add_x

    def y_pan(self, add_y):
        self.y_scroll += add_y
