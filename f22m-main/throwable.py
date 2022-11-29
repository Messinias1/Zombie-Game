import pygame

class Throwable:
    def __init__(self, x:int, y:int, mouse_x:int, mouse_y:int, name:str):
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
        
    def get_position(self) -> tuple:
        """This Returns the position of the throwable
            Returns:
                pair: current x and y positions
        """
        
        position = (self.x_, self.y_)
        return position
    
    def update_position(screen) -> None:
        """This Updates the throwable position on the screen

            Parameters:
                screen {Screen}: takes in the screen object
        """
        pass