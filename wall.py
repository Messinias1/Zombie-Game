import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__()
        self.xpos, self.ypos = x, y
        self.width, self.height = 32, 32
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()

    def change_pos(self, add_x, add_y):
        # moveable walls?
        self.xpos += add_x
        self.ypos += add_y

    def update(self, camera_ref):
        # take into account camera scroll when setting position
        self.rect.x = self.xpos + camera_ref.x_scroll
        self.rect.y = self.ypos + camera_ref.y_scroll

