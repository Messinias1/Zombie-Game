import pygame
import json
import wall
import camera


class World:
    def __init__(self, layout_file: str):
        """Class for rooms. When creating a new room for a level, create a new World object,
           aka each World object is ONE room

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
        self.pathfinding_maze = []
        self.ROOM_DIMENSIONS = [0, 0]
        self._layout_file = layout_file

    def init_room(self) -> None:
        """Prepares the map and stores it in self.room_sprites & self.room_sprite_group
           & initiates pathfinding for the room as well"""
        with open(self._layout_file, "r") as f:
            layout = json.loads(f.read())
        y = 0
        for row in layout:
            x = 0
            this_row = []
            for char in row:
                if char == "-":
                    this_tile = wall.Wall(x, y, wall_type=None, in_room=self)  # img=None signifies this wall is a floor tile
                if char.lower() == "w":
                    this_tile = wall.Wall(x, y, "wood", self)
                if char.lower() == "b":
                    this_tile = wall.Wall(x, y, "black", self)
                if char.lower() == "s":
                    this_tile = wall.Wall(x, y, "stone", self)
                if this_tile.wall_type is not None:
                    self.room_wall_group.add(this_tile)
                    self.room_sprite_group.add(this_tile)
                this_row.append(this_tile)
                x += 32  # each wall sprite is 32x32 pixels
            y += 32
            self.pathfinding_maze.append(this_row)
        self.ROOM_DIMENSIONS = [x, y]

    def find_path(self, start_x, start_y, end_x, end_y) -> [(int, int)]:
        """Finds the best path between two points that avoids all walls in the room
        :param start_x the x position to start at
        :param start_y the y position to start at
        :param end_x the desired x pos to end at
        :param end_y the y pos to end at
        :returns a list of tuples of directions to move in, formatted [(move_x1, move_y1), ...]"""
        pass

    def update_room_sprites(self) -> None:
        """Runs the update() method for each sprite stored in self.room_sprite_group"""
        for sprite in self.room_sprite_group:
            sprite.update()
