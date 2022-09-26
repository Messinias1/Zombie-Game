import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__()
        self.xpos, self.ypos = x, y
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()

    def change_pos(self, add_x, add_y):
        self.xpos += add_x
        self.ypos += add_y

