import math

import pygame
import constants    
import os

class Currency(pygame.sprite.Sprite):
    def __init__(self):
        self.coins = 0
    
    def add(self, increase):
        self.coins = self.coins + increase
    
    def subtract(self, decrease):
        self.coins = self.coins - decrease
    
    def reset(self):
        self.coins = 0