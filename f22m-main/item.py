import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, img, strength, type, in_room):
        super().__init__()
        self.xpos = x
        self.ypos = y

        self.image = pygame.image.load(img)
        self.type = type
        self.strength = strength
        
        self.rect = self.image.get_rect()
        self.rect.x = self.xpos
        self.rect.y = self.ypos
        self.world = in_room

    def use(self):
        if self.type == "DEFAULT":
            print("Default item")
            print(self.strength)
            
        if self.type == "Healable":
            #Heal player by strength of item
            print("Healable item")

    def update(self, camera_ref=None):
        # take into account camera scroll when setting position
        if camera_ref is None:
            camera_ref = self.world.camera
        self.rect.x = self.xpos + camera_ref.x_scroll
        self.rect.y = self.ypos + camera_ref.y_scroll