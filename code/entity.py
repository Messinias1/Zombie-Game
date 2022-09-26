import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__()
        self.xpos, self.ypos = x, y
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.xpos, self.ypos
        self.direction = 1

    def move(self, speed):
        if self.direction == 1:
            self.change_x(speed)
        elif self.direction == -1:
            self.change_x(-speed)
        elif self.direction == 2:
            self.change_y(speed)
        elif self.direction == -2:
            self.change_y(-speed)

    def change_x(self, add_x):
        self.xpos += add_x

    def change_y(self, add_y):
        self.ypos += add_y

    def check_for_collisions(self, walls):
        for wall in walls:
            #  idk how
            pass
