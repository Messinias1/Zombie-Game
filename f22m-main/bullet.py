import pygame
import math

class Bullet:
    """This creats a new Bullet on screen
    """
    
    def __init__(self, x:int, y:int , mouse_x:int, mouse_y:int) -> None:
        """This creates a new Rational Object

            Parameters:
                x {int}: takes an integer
                y {int}: takes an integer
                mouse_x {int}: takes an integer
                mouse_y {int}: takes an integer
        """

        self.x_ = x
        self.y_ = y
        self.mouse_x_ = mouse_x
        self.mouse_y_ = mouse_y
        self.angle_ = math.atan2(y - mouse_y, x - mouse_x)
        self.speed_ = 15
        self.x_velocity_ = math.cos(self.angle_) * self.speed_
        self.y_velocity_ = math.sin(self.angle_) * self.speed_

    def get_position(self):
        """This Returns the position of the bullet
            Returns:
                pair: current x and y positions
        """
        
        position = (self.x_, self.y_)
        return position
    
    def update_position(self, screen):
        """This Updates the Bullet position on the screen

            Parameters:
                screen {Screen}: takes in the screen object 
        """

        self.x_ -= int(self.x_velocity_)
        self.y_ -= int(self.y_velocity_)
        black = 0, 0, 0

        pygame.draw.circle(screen, black, (self.x_, self.y_), 5)
