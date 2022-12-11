import math

import pygame
import constants
import os
from currency import Currency
from health import Health


class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, images_path, in_room):
        # """x, y --> the character's starting position
        #    img --> image for the character sprite
        #    in_room --> world object where this character is drawn"""
        super().__init__()
        in_room.room_sprite_group.add(self)
        self.animation_list = []
        # append all the images in the directory to self.images
        [self.animation_list.append(images_path + "/idle/" + filename) for filename in os.listdir(images_path + "/idle/")]
        # the image path dir will have multiple images, where each one is a frame in the character's animation
        # I haven't coded anything that makes the animation play
        # I only set the main image to the first file found in the dir
        # convert all images
        for i in range(len(self.animation_list)):
            self.animation_list[i] = pygame.image.load(self.animation_list[i]).convert_alpha()
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.dmg_update_time = self.update_time
        self.dmg_cd = 1000  # time to wait between taking damage
        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.dir = "left"
        self.world = in_room
        self.xpos, self.ypos = x, y
        self.rect.center = (x, y)
        self.coins = Currency()
        self.health = Health()  # 200 starting health


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

    def is_touching(self, other: 'Character') -> bool:
        """If distance between self and 'other' is 0, they're touching"""
        dx, dy = self.rect.x - other.rect.x, self.rect.y - other.rect.y + 10
        dist = int(math.hypot(dx, dy))
        return dist == 0

    def take_hit(self, damage: int) -> int:
        """First, checks if player can take damage based on hit_cooldown, if true then take damage
        :param damage amount of health to lose if damage can be taken
        :returns how much damage was taken"""
        if pygame.time.get_ticks() - self.dmg_update_time > self.dmg_cd:
            self.dmg_update_time = pygame.time.get_ticks()
            self.health.health -= damage
            return damage
        else:
            return 0

    def check_for_collisions(self, try_x=None, try_y=None) -> (int, int):
        if try_x is None:
            try_x = 0
        if try_y is None:
            try_y = 0
        tiles = self.world.room_tile_group
        move_x, move_y = try_x, try_y
        for tile in tiles:
            if tile.collideable:
                if tile.collide_rect.collidepoint(self.rect.x, self.rect.y + try_y):  # collision going in y direction
                    move_y = 0
                if tile.collide_rect.collidepoint(self.rect.x + try_x, self.rect.y):  # collision going in x direction
                    move_x = 0

        return move_x, move_y

    def update(self):
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
        camera_ref = self.world.camera
        self.rect.x = self.xpos + camera_ref.x_scroll
        self.rect.y = self.ypos + camera_ref.y_scroll
