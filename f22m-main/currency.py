import math

import pygame
import constants    
import os

class Currency(pygame.sprite.Sprite):
    def __init__(self):
        """initializes a currency object at zero coins

        """
        self.coins = 0
    def add(self, add_number:int):
        """adds to coin

        Args:
            add_number (integer): integer being added

        Returns:
            Currency: added number
        """
        try:
            int(add_number)
        except TypeError:
            print("add_number must be an integer")

        if add_number < 0:
            raise ValueError("add_number must be positive")

        if self.coins + add_number > 9999:
            self.coins = 9999
        else:
            self.coins = self.coins + add_number
    
    def subtract(self, subtract_number:int):
        """subtracts from coin

        Args:
            subtract_number (integer): integer being removed

        Returns:
            Currency: subtracted number
        """
        try:
            int(subtract_number)
        except TypeError:
            print("subtract_number must be an integer")
        
        if subtract_number < 0:
            raise ValueError("subtract_number must be positive")

        if self.coins - subtract_number < 0:
            raise ValueError("Cannot subtract below 0")
        else:
            self.coins = self.coins - subtract_number
    
    def reset(self):
        """resets currency to zero

        """
        self.coins = 0
    
    def Value(self):
        """returns coins value

        """
        return self.coins


