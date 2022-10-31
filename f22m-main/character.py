import math

import pygame
import constants
import os

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, in_room, animation_list):
        # """x, y --> the character's starting position
        #    img --> image for the character sprite
        #    in_room --> world object where this character is drawn"""
        super().__init__()


        # self.images = []
        # [self.images.append(imgpath + "/idle/" + filename) for filename in os.listdir(imgpath + "/idle/")]
        # the image path dir will have multiple images, where each one is a frame in the character's animation
        # I haven't coded anything that makes the animation play
        # I only set the main image to the first file found in the dir
        # for i in range(4):
        #     self.image = pygame.image.load(self.images[i])
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.animation_list = animation_list
        self.image = animation_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.dir = "left"
        self.world = in_room
        self.xpos, self.ypos = x, y
        self.rect.center = (x, y)

    def draw(self, surface):
        pygame.draw.rect(surface, constants.RED, self.rect)

    def flip_char(self):
        flipped_image = pygame.transform.flip(self.image, True, False)
        self.image = flipped_image

    def move(self, dx, dy):
        move_x, move_y = self.check_for_collisions(dx, dy)
        self.change_x_and_y(move_x, move_y)

    def change_x_and_y(self, add_x, add_y):
        # control diagonal movement
        if self.dir == "left" and add_x < 0:
            self.dir = "right"
            self.flip_char()
        if self.dir == "right" and add_x > 0:
            self.dir = "left"
            self.flip_char()
        if add_x != 0 and add_y != 0:
            add_x = add_x * (math.sqrt(2) / 2)
            add_y = add_y * (math.sqrt(2) / 2)

        self.xpos += add_x
        self.ypos += add_y

    def check_for_collisions(self, try_x=None, try_y=None):
        if try_x is None:
            try_x = 0
        if try_y is None:
            try_y = 0
        walls = self.world.room_wall_group
        move_x, move_y = try_x, try_y
        for wall in walls:
            if wall.rect.collidepoint(self.rect.x + (wall.width/2), self.rect.y + try_y + (wall.height/2)):  # collisioin going in y direction
                move_y = 0
            if wall.rect.collidepoint(self.rect.x + try_x + (wall.width/2), self.rect.y + (wall.height/2)):  # collision going in x direction
                move_x = 0
        return move_x, move_y

    def update(self, camera_ref=None):
        animation_cooldown = 70
        self.image = self.animation_list[self.frame_index]
        if self.dir == "right":
            self.flip_char()
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0

        # take into account camera scroll when setting position
        if camera_ref is None:
            camera_ref = self.world.camera
        self.rect.x = self.xpos + camera_ref.x_scroll
        self.rect.y = self.ypos + camera_ref.y_scroll
