import pygame

RESIZE_HEIGHT, RESIZE_WIDTH = 1.5, 1.3
# scale each wall's collision rect by these values
SHIFT_Y, SHIFT_X = 1 / 1.8, 1 / 3.7
# shift each wall's collision rects by these values
# where do the actual values come from?
# I used trial and error to find values for
# just whatever will make the actual wall image match
# with a collision area between the walls and player that looks good


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, wall_type, in_room):
        """Class for wall tiles
            :param x initial x position
            :param y initial y position
            :param wall_type type of wall
            :param in_room the room object that this wall is in"""
        super().__init__()
        self.xpos, self.ypos = x, y
        self.world = in_room
        self.wall_type = wall_type
        if wall_type is not None:
            self.width, self.height = 32, 32
            self.image = pygame.image.load(f"assets/images/walls/{wall_type}.gif")
            self.rect = self.image.get_rect()
            self.collide_rect = self.image.get_rect(height=self.height*RESIZE_HEIGHT, width=self.width*RESIZE_WIDTH)

    def update(self, camera_ref=None) -> None:
        """Overrides pygame's default update() method with one that tales camera position into account"""
        if camera_ref is None:
            camera_ref = self.world.camera
        self.rect.x = self.xpos + camera_ref.x_scroll
        self.rect.y = self.ypos + camera_ref.y_scroll

        self.collide_rect.x = self.xpos + camera_ref.x_scroll - (self.collide_rect.width * SHIFT_X)
        self.collide_rect.y = self.ypos + camera_ref.y_scroll - (self.collide_rect.height * SHIFT_Y)
