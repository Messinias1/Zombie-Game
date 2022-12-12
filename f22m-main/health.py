import math

import pygame
import constants    
import os

class Health(pygame.sprite.Sprite):
    def __init__(self, start_at=200):
        self.health = start_at
    
    def add(self, increase):
        self.health = self.health + increase
    
    def subtract(self, decrease):
        self.health = self.health - decrease

    def get_hp(self):
        return self.health
    