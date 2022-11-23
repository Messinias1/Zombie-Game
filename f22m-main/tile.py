import pygame

RESIZE_HEIGHT, RESIZE_WIDTH = 1.5, 1.3
# scale each wall's collision rect by these values
SHIFT_Y, SHIFT_X = 1 / 1.8, 1 / 3.7
# shift each wall's collision rects by these values
# where do the actual values come from?
# I used trial and error to find values for
# just whatever will make the actual wall image match
# with a collision area between the walls and player that looks good


class Tile(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, img: str, collideable: bool, in_room: 'World'):
        """Class for wall tiles
            :param x initial x position
            :param y initial y position
            :param img image to load for this wall tile
            :param in_room the room object that this wall is in"""
        super().__init__()
        self.xpos, self.ypos = x, y
        self._world = in_room
        self.collideable = collideable
        self._width, self._height = 32, 32
        self.row, self.col = self.xy_to_rowcol(self.xpos, self.ypos, self._width, self._height)
        self.position = (self.row, self.col)
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.collide_rect = self.image.get_rect(height=self._height * RESIZE_HEIGHT, width=self._width * RESIZE_WIDTH)

    @staticmethod
    def xy_to_rowcol(x=None, y=None, width=None, height=None) -> (int, int):
        if width is None:
            width = 32
        if height is None:
            height = 32
        return int(x // width) + 1, int(y // height)

    def get_neighbors(self) -> ['Tile']:
        neighbors = []
        maze = self._world.pathfinding_maze
        # north
        if self.row > 0:
            neighbors.append(self._world.find_tile_by_row_col(self.row - 1, self.col))
        # south
        if self.row < len(maze) - 1:
            neighbors.append(self._world.find_tile_by_row_col(self.row + 1, self.col))
        # east
        if self.col < len(maze[self.row]) - 1:
            neighbors.append(self._world.find_tile_by_row_col(self.row, self.col + 1))
        # west
        if self.col > 0:
            neighbors.append(self._world.find_tile_by_row_col(self.row, self.col - 1))
        return neighbors

    def update(self) -> None:
        """Overrides pygame's default update() method with one that tales camera position into account"""
        camera_ref = self._world.camera
        self.rect.x = self.xpos + camera_ref.x_scroll
        self.rect.y = self.ypos + camera_ref.y_scroll

        self.collide_rect.x = self.xpos + camera_ref.x_scroll - (self.collide_rect.width * SHIFT_X)
        self.collide_rect.y = self.ypos + camera_ref.y_scroll - (self.collide_rect.height * SHIFT_Y)
