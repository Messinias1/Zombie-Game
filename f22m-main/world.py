import pygame
import json
import wall
import camera


class World:
    def __init__(self):
        """Class for rooms. When creating a new room for a level, create a new World object"""
        self.camera = camera.Camera(100, 100)  # create a new camera & set its initial x and y

        # this will store all walls in the current room
        # when characters handle wall collision, this group will be used
        self.room_wall_group = pygame.sprite.Group()

        # this will store each pygame.sprite in the current room (including walls)
        # when everything in a room needs to .update(), this group will be used
        self.room_sprite_group = pygame.sprite.Group()

    def generate(self, layout_file: str) -> None:
        """Generates the map and stores it in self.room_sprites & self.room_sprite_group

        :param layout_file The json file where the map desired layout is stored."""
        with open(layout_file, "r") as f:
            layout = json.loads(f.read())
        y = 0
        for row in layout:
            x = 0
            for char in row:
                if char == "B":
                    this_tile = wall.Wall(x, y, "assets/images/walls/black.gif", self)
                    self.room_wall_group.add(this_tile)
                    self.room_sprite_group.add(this_tile)
                x += 32  # each wall sprite is 32x32 pixels
            y += 32

    def update_room_sprite_group(self) -> None:
        """Runs the update() method for each sprite stored in self.room_sprite_group"""
        for sprite in self.room_sprite_group:
            sprite.update()
