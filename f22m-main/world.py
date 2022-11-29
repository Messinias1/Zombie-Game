import pygame
import json
from tile import Tile
from camera import Camera


class World:
    def __init__(self, layout_file: str):
        """Class for rooms. When creating a new room for a level, create a new World object,
           aka each World object is ONE room

        Running only the init will NOT prepare the map, it will only store the file where it will later load it from.
        To load the map run self.init_room()

        :param layout_file The json file where the map desired layout is stored."""
        self.camera = Camera(100, 100)  # create a new camera & set its initial x and y

        # this will store all tiles (walls & floor tiles) in the current room
        # when characters handle wall collision, this group will be used
        self.room_tile_group = pygame.sprite.Group()

        # this will store each pygame.sprite in the current room (including walls)
        # when everything in a room needs to .update(), this group will be used
        self.room_sprite_group = pygame.sprite.Group()
        self.pathfinding_maze = []
        self.ROOM_DIMENSIONS = [0, 0]
        self._layout_file = layout_file
        self.maze = None
        self._layout_json = None

    def init_room(self) -> 'World':
        """Prepares the map and stores it in self.room_sprites & self.room_sprite_group
           & initiates pathfinding for the room as well"""
        with open(self._layout_file, "r") as f:
            self._layout_json = json.loads(f.read())
        self.maze = self._layout_json
        y = 0
        for row in self._layout_json:
            x = 0
            this_row = []
            for char in row:
                this_tile = Tile(x, y, f"assets/images/walls/grass.gif", False, self)   # default is blank tile
                if char.lower() == "w":
                    this_tile = Tile(x, y, f"assets/images/walls/wood.gif", True, self)
                if char.lower() == "b":
                    this_tile = Tile(x, y, f"assets/images/walls/black.gif", True, self)
                if char.lower() == "s":
                    this_tile = Tile(x, y, f"assets/images/walls/stone.gif", True, self)
                if char.lower() == "r":
                    this_tile = Tile(x, y, f"assets/images/walls/road_side.gif", False, self)
                if char.lower() == "d":
                    this_tile = Tile(x, y, f"assets/images/walls/road_down.gif", False, self)
                self.room_tile_group.add(this_tile)
                self.room_sprite_group.add(this_tile)
                this_row.append(this_tile)
                x += 32  # each wall sprite is 32x32 pixels
            y += 32
            self.pathfinding_maze.append(this_row)
        self.ROOM_DIMENSIONS = [x, y]
        return self

    def find_tile_by_row_col(self, row_col: (int, int)) -> 'Tile':
        """find wall by row & column number
        :param row_col the (row, column) of the wall
        :returns wall object at the specified row, col"""
        for tile in self.room_tile_group:
            if tile.position == row_col:
                return tile
        raise IndexError  # no tile found

    def find_tile_by_x_y(self, x_y: (int, int)) -> Tile:
        return self.find_tile_by_row_col(Tile.xy_to_rowcol(x_y))

    def find_tile_by_char_pos(self, who: 'Character') -> Tile:
        return self.find_tile_by_x_y((who.xpos, who.ypos))

    def update_room_sprites(self) -> None:
        """Runs the update() method for each sprite stored in self.room_sprite_group"""
        for sprite in self.room_sprite_group:
            sprite.update()
