import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, img, in_room):
        """Class for wall tiles
            :param x initial x position
            :param y initial y position
            :param img image to load for this wall tile
            :param in_room the room object that this wall is in"""
        super().__init__()
        self.xpos, self.ypos = x, y
        self.width, self.height = 32, 32
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.world = in_room

    def update(self, camera_ref=None) -> None:
        """Overrides pygame's default update() method with one that tales camera position into account"""
        if camera_ref is None:
            camera_ref = self.world.camera
        self.rect.x = self.xpos + camera_ref.x_scroll
        self.rect.y = self.ypos + camera_ref.y_scroll
