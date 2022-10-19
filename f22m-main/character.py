import pygame
import constants


class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, img, in_room):
        """x, y --> the character's starting position
           img --> image for the character sprite
           in_room --> world object where this character is drawn"""
        super().__init__()
        self.image = pygame.image.load(f"{img}/idle/0.png")
        self.rect = self.image.get_rect()
        self.world = in_room
        self.xpos, self.ypos = x, y
        self.rect.center = (x, y)

    def draw(self, surface):
        pygame.draw.rect(surface, constants.RED, self.rect)

    def move(self, x, y):
        movex, movey = self.check_for_collisions(x, y)
        self.change_y(movey)
        self.change_x(movex)

    def change_x(self, add_x):
        self.xpos += add_x

    def change_y(self, add_y):
        self.ypos += add_y

    def check_for_collisions(self, try_x, try_y):
        walls = self.world.room_sprites
        move_x, move_y = try_x, try_y
        for wall in walls:
            if wall.rect.collidepoint(self.rect.x + (wall.width/2), self.rect.y + try_y + (wall.height/2)):  # collisioin going in y direction
                move_y = 0
            if wall.rect.collidepoint(self.rect.x + try_x + (wall.width/2), self.rect.y + (wall.height/2)):  # collision going in x direction
                move_x = 0
        return move_x, move_y

    def update(self, camera_ref=None):
        # take into account camera scroll when setting position
        if camera_ref is None:
            camera_ref = self.world.camera
        self.rect.x = self.xpos + camera_ref.x_scroll
        self.rect.y = self.ypos + camera_ref.y_scroll
