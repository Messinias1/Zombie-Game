import pygame
import json
import wall
import camera


class Room:
    def __init__(self):
        self.camera = camera.Camera(0, 0)  # set the camera x and y to 0
        self.tile_objects = []
        self.tile_group = pygame.sprite.Group()
        self.DIMENSIONS = [0, 0]

    def generate(self, layout_file):
        with open(layout_file, "r") as f:
            layout = json.loads(f.read())
        y = 0
        for row in layout:
            x = 0
            for char in row:
                if char == "W":
                    this_tile = wall.Wall(x, y, "sprites/walls/reg.gif")
                    self.tile_objects.append(this_tile)
                    self.tile_group.add(this_tile)
                x += 32  # each wall sprite is 32x32 pixels
            y += 32
        self.DIMENSIONS = [len(self.tile_objects) * 32, len(self.tile_objects) * 32]

    def update_all_tiles(self):
        for tile in self.tile_objects:
            tile.update(camera_ref=self.camera)

