import pygame
import math

"""This creats a new Bullet on screen
"""
class Bullet:
    """This creates a new Rational Object

        Parameters:
            x {int}: takes an integer
            y {int}: takes an integer
            mouse_x {int}: takes an integer
            mouse_y {int}: takes an integer
    """
    def __init__(self, x:int, y:int , mouse_x:int, mouse_y:int) -> None:
        self.x_ = x
        self.y_ = y
        self.mouse_x_ = mouse_x
        self.mouse_y_ = mouse_y
        self.angle_ = math.atan2(y - mouse_y, x - mouse_x)
        self.speed_ = 15
        self.x_velocity_ = math.cos(self.angle_) * self.speed_
        self.y_velocity_ = math.sin(self.angle_) * self.speed_

    """This Returns the position of the bullet
        Return:
            current position
    """
    def get_position(self):
        position = (self.x_, self.y_)
        return position
    
    """This Updates the Bullet position on the screen

        Parameters:
            screen {Screen}: takes in the screen object 
    """
    def updatePosition(self, screen):
        self.x_ -= int(self.x_velocity_)
        self.y_ -= int(self.y_velocity_)
        black = 0, 0, 0

        pygame.draw.circle(screen, black, (self.x_, self.y_), 5)
