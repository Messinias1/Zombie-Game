import pygame
import json
import wall
import camera


class World:
    def __init__(self, layout_file):
        self.camera = camera.Camera(100, 100)  # set the camera x and y to 0
        self.room_sprites = []
        self.room_sprite_group = pygame.sprite.Group()
        self.DIMENSIONS = [0, 0]  # keep track of dimensions of all walls in the room?
        with open(layout_file, "r") as f:
            layout = json.loads(f.read())
        y = 0
        for row in layout:
            x = 0
            for char in row:
                if char == "W":
                    this_tile = wall.Wall(x, y, "assets/images/walls/reg.gif", self)
                    self.room_sprites.append(this_tile)
                    self.room_sprite_group.add(this_tile)
                x += 32  # each wall sprite is 32x32 pixels
            y += 32

    def update_room_sprites(self):
        for sprite in self.room_sprite_group:
            sprite.update()
