import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, img, strength, type):
        super().__init__()
        self.x = x
        self.y = y

        self.image = pygame.image.load(img)
        self.type = type
        self.strength = strength
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def use(self):
        if self.type == "DEFAULT":
            print("Default item")
            print(self.strength)
            
        if self.type == "Healable":
            #Heal player by strength of item
            print("Healable item")