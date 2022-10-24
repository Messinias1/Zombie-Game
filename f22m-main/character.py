import math

import pygame
import constants
import os

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, imgpath, in_room):
        """x, y --> the character's starting position
           img --> image for the character sprite
           in_room --> world object where this character is drawn"""
        super().__init__()
        self.images = []
        [self.images.append(imgpath + "/idle/" + filename) for filename in os.listdir(imgpath + "/idle/")]
        # the image path dir will have multiple images, where each one is a frame in the character's animation
        # I haven't coded anything that makes the animation play
        # I only set the main image to the first file found in the dir
        self.image = pygame.image.load(self.images[0])
        self.rect = self.image.get_rect()
        self.world = in_room
        self.xpos, self.ypos = x, y
        self.rect.center = (x, y)

    def draw(self, surface):
        pygame.draw.rect(surface, constants.RED, self.rect)

    def move(self, x, y):
        # control diagonal movement
        if x != 0 and y != 0:
            x = x * (math.sqrt(2) / 2)
            y = y * (math.sqrt(2) / 2)

        movex, movey = self.check_for_collisions(x, y)

        self.change_x(movex)
        self.change_y(movey)

    def change_x(self, add_x):
        self.xpos += add_x

    def change_y(self, add_y):
        self.ypos += add_y

    def check_for_collisions(self, try_x=None, try_y=None):
        if try_x is None:
            try_x = 0
        if try_y is None:
            try_y = 0
        walls = self.world.room_sprites
        move_x, move_y = try_x, try_y
        for wall in walls:
            if wall.rect.collidepoint(self.rect.x + (wall.width/2), self.rect.y + try_y + (wall.height/2)):  # collisioin going in y direction
                move_y = 0
            if wall.rect.collidepoint(self.rect.x + try_x + (wall.width/2), self.rect.y + (wall.height/2)):  # collision going in x direction
                move_x = 0
        return move_x, move_y

    def update(self, camera_ref=None):
        # take into account camera scroll when setting position
        if camera_ref is None:
            camera_ref = self.world.camera
        self.rect.x = self.xpos + camera_ref.x_scroll
        self.rect.y = self.ypos + camera_ref.y_scroll
