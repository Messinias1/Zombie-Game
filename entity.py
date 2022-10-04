import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, img, world):
        super().__init__()
        self.xpos, self.ypos = x, y
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.speed = 2
        self.room = world
        self.rect.x, self.rect.y = self.xpos, self.ypos

    def move(self, x, y):
        movex, movey = self.check_for_collisions(x, y)
        self.change_y(movey)
        self.change_x(movex)

    def change_x(self, add_x):
        self.xpos += add_x

    def change_y(self, add_y):
        self.ypos += add_y

    def update(self, camera_ref):
        # take into account camera scroll when setting position
        self.rect.x = self.xpos + camera_ref.x_scroll
        self.rect.y = self.ypos + camera_ref.y_scroll

    def check_for_collisions(self, try_x, try_y):
        walls = self.room.room_sprites
        move_x, move_y = try_x, try_y
        for wall in walls:
            if wall.collidepoint == self.collidepoint:
                move_y = -try_y
            if wall.collidepoint == try_y + self.ypos:
                move_x = -try_x

        return move_x, move_y
