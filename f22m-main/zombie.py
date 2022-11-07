import pygame
import constants
import os
import math

from wall import Wall

class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y, imgpath, in_room):
        self.rect = pygame.Rect(32, 32, 16, 16)
        super().__init__()
        self.dir = "left"
        self.animation_list = []
        [self.animation_list.append(imgpath + "/idle/" + filename) for filename in os.listdir(imgpath + "/idle/")]
        # the image path dir will have multiple images, where each one is a frame in the character's animation
        # I haven't coded anything that makes the animation play
        # I only set the main image to the first file found in the dir
        self.image = pygame.image.load(self.animation_list[0])
        # convert all images
        for i in range(len(self.animation_list)):
            self.animation_list[i] = pygame.image.load(self.animation_list[i]).convert_alpha()
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.world = in_room
        self.xpos, self.ypos = x, y
        self.rect.center = (x, y)

    def move_towards_player(self, player):
        # Find direction vector (dx, dy) between enemy and player.
        dx, dy = player.rect.x - self.rect.x, player.rect.y - self.rect.y
        dist = math.hypot(dx, dy)
        # If dist becomes 0, the program crashes due to dividing 0
        if dist==0:
            dist = 0.1            
        dx, dy = dx / dist, dy / dist  # Normalize.
        # Move along this normalized vector towards the player at current speed.
        self.xpos += dx * 1
        self.ypos += dy * 1

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