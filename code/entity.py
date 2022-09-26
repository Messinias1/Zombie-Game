import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__()
        self.xpos, self.ypos = x, y
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.xpos, self.ypos
        self.direction = 1

    def move(self):
        if self.direction == 1:
            self.change_pos(1, 0)
        elif self.direction == -1:
            self.change_pos(-1, 0)
        elif self.direction == 2:
            self.change_pos(0, 1)
        elif self.direction == -2:
            self.change_pos(0, -1)

    def change_pos(self, add_x, add_y):
        self.xpos += add_x
        self.ypos += add_y

    def check_for_collisions(self, walls):
        for wall in walls:
            pass
