import pygame
import constants
import os
import math
from tile import Tile
from health import Health


class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y, imgpath, in_room):
        super().__init__()
        in_room.room_sprite_group.add(self)
        self.animation_list = []
        [self.animation_list.append(imgpath + "/idle/" + filename) for filename in os.listdir(imgpath + "/idle/")]
        # convert all images
        for i in range(len(self.animation_list)):
            self.animation_list[i] = pygame.image.load(self.animation_list[i]).convert_alpha()
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.dmg_update_time = self.update_time
        self.dmg_cd = 500  # time to wait between taking damage
        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.dir = "left"
        self.world = in_room
        self.xpos, self.ypos = x, y
        self.rect.center = (x, y)
        self.speed = 1.5
        self.health = Health(40)
        self.damage = 5
        self.alive = True

    def draw(self, surface):
        pygame.draw.rect(surface, constants.RED, self.rect)

    def flip_char(self):
        flipped_image = pygame.transform.flip(self.image, True, False)
        self.image = flipped_image

    def move_towards_player(self, player):
        # Find direction vector (dx, dy) between enemy and player.
        dx, dy = player.rect.x - self.rect.x, player.rect.y - self.rect.y + 10
        dist = math.hypot(dx, dy)
        # If dist becomes 0, the program crashes due to dividing by 0
        if dist==0:
            dist = 0.1            
        dx, dy = dx / dist, dy / dist  # Normalize.
        # Move along this normalized vector towards the player at current speed.
        move_x, move_y = self.check_for_collisions(player, dx, dy)
        self.change_x_and_y(move_x, move_y)

    def move_towards_tile(self, tile: 'Tile'):
        # Find direction vector (dx, dy) between enemy and player.
        dx, dy = tile.rect.x - self.rect.x, tile.rect.y - self.rect.y + 10
        dist = math.hypot(dx, dy)
        # If dist becomes 0, the program crashes due to dividing by 0
        if dist==0:
            dist = 0.1
        dx, dy = dx / dist, dy / dist  # Normalize.
        # Move along this normalized vector towards the player at current speed.
        self.change_x_and_y(dx, dy)

    def pathfind_towards_char(self, towards_who: 'Character') -> None:
        if self.dist_to_char(towards_who) < 46:
            # if it's within one tile, we don't need to pathfind
            self.move_towards_player(towards_who)
            return None

        path = self.world.find_next_move_towards(self, towards_who)
        t = self.world.find_tile_by_row_col(path)
        self.move_towards_tile(t)

    def dist_to_char(self, towards_who):
        return math.dist((towards_who.xpos, towards_who.ypos), (self.xpos, self.ypos))

    def rect_dist_to_point(self, pos: (int, int)):
        return math.dist((pos[0], pos[1]), (self.rect.x, self.rect.y))

    def change_x_and_y(self, add_x, add_y):
        # control diagonal movement
        if self.dir == "left" and add_x < 0:
            self.dir = "right"
            self.flip_char()
        if self.dir == "right" and add_x > 0:
            self.dir = "left"
            self.flip_char()
        if add_x != 0 and add_y != 0:
            add_x = add_x * self.speed
            add_y = add_y * self.speed

        self.xpos += add_x
        self.ypos += add_y

    def check_for_collisions(self,player, try_x=None, try_y=None):
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

    def deal_damage(self,player):
        if self.rect.colliderect(player.rect):
            player.health.subtract(self.damage)

    def take_proj_hit(self, proj: 'Bullet'):
        if self.rect_dist_to_point((proj.x_, proj.y_)) < 10 and (pygame.time.get_ticks() - self.dmg_update_time > self.dmg_cd):
            self.health.subtract(proj.damage)
            self.dmg_update_time = pygame.time.get_ticks()

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

class Small_Zombie(Zombie):
    def __init__(self, x, y, imgpath, in_room):
        super().__init__(x, y, imgpath, in_room)
        self.speed = 2
        self.damage = 2
        self.health = Health(20)

class Big_Zombie(Zombie):
    def __init__(self, x, y, imgpath, in_room):
        super().__init__(x, y, imgpath, in_room)
        self.speed = 1
        self.damage = 10
        self.health = Health(80)
