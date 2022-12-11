import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, img, strength, type, in_room, player):
        super().__init__()
        in_room.room_sprite_group.add(self)
        self.xpos = x
        self.ypos = y

        self.image = pygame.image.load(img)
        self.type = type
        self.strength = strength
        self.picked_up = False
        
        self.rect = self.image.get_rect()
        self.rect.x = self.xpos
        self.rect.y = self.ypos
        self.world = in_room
        self.player = player

    def use(self):
        if self.type == "Coin":
            self.player.coins.coins += self.strength
            
        if self.type == "Healable":
            self.player.health.health += self.strength

    def update(self, camera_ref=None):
        # take into account camera scroll when setting position
        if camera_ref is None:
            camera_ref = self.world.camera
        self.rect.x = self.xpos + camera_ref.x_scroll
        self.rect.y = self.ypos + camera_ref.y_scroll

        if self.picked_up == True:
            self.use()
            self.picked_up = False
            self.kill()
            
    def get_type(self):
        return self.type
