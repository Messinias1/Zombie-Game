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
            if wall.rect.collidepoint(self.rect.x + (wall.width/2), self.rect.y + try_y + (wall.height/2)):  # collisioin going in y direction
                move_y = 0
            if wall.rect.collidepoint(self.rect.x + try_x + (wall.width/2), self.rect.y + (wall.height/2)):  # collision going in x direction
                move_x = 0

        return move_x, move_y
