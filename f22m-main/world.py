import pygame
import json
from tile import Tile
from camera import Camera
from pathfinding import Pathfinding


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
        self.ROOM_DIMENSIONS = [0, 0]
        self._layout_file = layout_file
        self.world_maze = None

    def init_room(self) -> None:
        """Prepares the map and stores it in self.room_sprites & self.room_sprite_group
           & initiates pathfinding for the room as well"""
        with open(self._layout_file, "r") as f:
            layout = json.loads(f.read())
        self.world_maze = Pathfinding(layout)
        y = 0
        for row in layout:
            x = 0
            for char in row:
                if char == "-":
                    this_tile = Tile(x, y, img=None, collideable=False, in_room=self)  # img=None signifies this wall is a floor tile
                if char.lower() == "w":
                    this_tile = Tile(x, y, f"assets/images/walls/wood.gif", True, self)
                if char.lower() == "b":
                    this_tile = Tile(x, y, f"assets/images/walls/black.gif", True, self)
                if char.lower() == "s":
                    this_tile = Tile(x, y, f"assets/images/walls/stone.gif", True, self)
                self.room_tile_group.add(this_tile)
                if this_tile.image is not None:
                    self.room_sprite_group.add(this_tile)
                x += 32  # each wall sprite is 32x32 pixels
            y += 32
        self.ROOM_DIMENSIONS = [x, y]

    def find_tile_by_row_col(self, row: int, col: int) -> 'Tile':
        """find wall by row & column number
        :param row the row of the wall
        :param col the column of the wall
        :returns wall object at the specified row, col"""
        for tile in self.room_tile_group:
            if tile.row == row and tile.col == col:
                return tile

    def find_next_moves(self, start_x, start_y, end_x, end_y) -> [(int, int)]:
        """Finds the best path between two points that avoids all walls in the room
        :param start_x the x position to start at
        :param start_y the y position to start at
        :param end_x the desired x pos to end at
        :param end_y the y pos to end at
        :returns a list of tuple of pixels to move in (move_x, move_y)"""
        start_row, start_col = int(start_x // 32), int(start_y // 32)
        end_row, end_col = int(end_x // 32), int(end_y // 32)
        print((start_row, start_col), (end_row, end_col))
        # all tiles have dimensions 32x32
        # so using integer division will convert (x, y) to (row, col)
        path = self.world_maze.astar((start_row, start_col), (end_row, end_col))
        if len(path) > 1:
            path.pop(0)  # remove first item because it == start_x, start_y
            return path
        else:
            return [(end_row, end_col)]

    def find_next_move(self, start_x, start_y, end_x, end_y) -> (int, int):
        return self.find_next_moves(start_x, start_y, end_x, end_y)[0]

    def update_room_sprites(self) -> None:
        """Runs the update() method for each sprite stored in self.room_sprite_group"""
        for sprite in self.room_sprite_group:
            sprite.update()
