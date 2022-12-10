import math

import pygame
import constants    
import os

class Health(pygame.sprite.Sprite):
    def __init__(self):
        self.health = 200
    
    def add(self, increase):
        self.health = self.health + increase
    
    def subtract(self, decrease):
        self.health = self.health - decrease
    