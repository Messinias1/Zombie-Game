import pygame
import json
import wall
import camera


class World:
    def __init__(self, layout_file: str):
        """Class for rooms. When creating a new room for a level, create a new World object.

        Running only the init will NOT prepare the map, it will only store the file where it will later load it from.
        To load the map run self.init_room()

        :param layout_file The json file where the map desired layout is stored."""
        self.camera = camera.Camera(100, 100)  # create a new camera & set its initial x and y

        # this will store all walls in the current room
        # when characters handle wall collision, this group will be used
        self.room_wall_group = pygame.sprite.Group()

        # this will store each pygame.sprite in the current room (including walls)
        # when everything in a room needs to .update(), this group will be used
        self.room_sprite_group = pygame.sprite.Group()
        self.ROOM_DIMENSIONS = [0, 0]
        self._layout_file = layout_file

    def init_room(self, enable_pathfinding: bool = True) -> None:
        """Set up the room to be drawn by the game
        :param enable_pathfinding specifies whether to load the layout file into Pathfinding"""
        self.load_room()

    def load_room(self) -> None:
        """Prepares the map and stores it in self.room_sprites & self.room_sprite_group"""
        with open(self._layout_file, "r") as f:
            layout = json.loads(f.read())
        y = 0
        for row in layout:
            x = 0
            for char in row:
                if char.lower() == "w":
                    this_tile = wall.Wall(x, y, "assets/images/walls/wood.jpg", self)
                    self.room_wall_group.add(this_tile)
                    self.room_sprite_group.add(this_tile)
                if char.lower() == "b":
                    this_tile = wall.Wall(x, y, "assets/images/walls/black.gif", self)
                    self.room_wall_group.add(this_tile)
                    self.room_sprite_group.add(this_tile)
                if char.lower() == "s":
                    this_tile = wall.Wall(x, y, "assets/images/walls/stone.gif", self)
                    self.room_wall_group.add(this_tile)
                    self.room_sprite_group.add(this_tile)
                x += 32  # each wall sprite is 32x32 pixels
            y += 32
        self.ROOM_DIMENSIONS = [x, y]

    def update_room_sprites(self) -> None:
        """Runs the update() method for each sprite stored in self.room_sprite_group"""
        for sprite in self.room_sprite_group:
            sprite.update()
