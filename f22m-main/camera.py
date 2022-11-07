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
        in_room = char.world
        # don't let the camera go further to the right
        if self.x_scroll - constants.SCREEN_WIDTH < -in_room.ROOM_DIMENSIONS[0]:
            self.x_scroll = -in_room.ROOM_DIMENSIONS[0] + constants.SCREEN_WIDTH
        # don't let the camera go further to the left
        if self.x_scroll > 0:
            self.x_scroll = 0
        # don't let the camera go further below
        if self.y_scroll - constants.SCREEN_HEIGHT < -in_room.ROOM_DIMENSIONS[1]:
            self.y_scroll = -in_room.ROOM_DIMENSIONS[1] + constants.SCREEN_HEIGHT
        # don't let the camera go further above
        if self.y_scroll > 0:
            self.y_scroll = 0
