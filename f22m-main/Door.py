import pygame

class Door(pygame.sprite.Sprite):
    def __init__(self, x:int, y:int, img, in_room:int, cost:int, facing_vert:bool, is_open:bool):
        """Class for wall tiles
            :param x initial x position
            :param y initial y position
            :param img image to load for this wall tile
            :param in_room the room object that this wall is in
            :param cost refers to cost of opening the door
            :param facing_vert used to hold whether door is in vertical or horizontal position on map,
                i.e. facing_vert = True if the door can be walked through from north to south
            :param isOpen used to hold whether the door has been opened (use for collision)
        """
        super().__init__()
        self.x = x
        self.y = y
        self.width, self.height = 32, 32
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.world = in_room

        self.cost = cost
        self.facing_vert = facing_vert
        self.is_open = is_open

    def update(self, camera_ref = None) -> None:
        """Overrides pygame's default update method with one that takes camera position into account"""
        if camera_ref is None:
            camera_ref = self.world.camera
        self.rect.x = self.x + camera_ref.x_scroll
        self.rect.y = self.y + camera_ref.y_scroll

    def buy_door(self) -> None:
        # Function to open the door, trigger when player tries to buy the door
        """
        if player.currency >= self.cost:
            player.currency = player.currency - self.cost
            self.isOpen = True
        """
            # door open animation
        else:
            # print (" Not Enough Coins ")
