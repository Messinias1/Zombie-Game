import pygame

class Door:
    def __init__(self, x: int, y: int, cost: int, facing_vert: bool, is_open: bool) -> None:
        """
        Constructor
            x used for x position of the door
            y used for y position of the door
            cost used to hold the price of the door
            facing used to hold whether door is in vertical or horizontal position on map
            isOpen used to hold whether the door has been opened (use for collision)
        """
        self.x = x
        self.y = y
        self.cost = cost
        self.facing_vert = facing_vert
        self.is_open = is_open

    # Displays pop-up window allowing player to interact with the door
    def interact(self):
        pass
    # Draws the door on the map
    def draw_door(self):
        pass
    # Changes the door state to open
    def open_door(self):
        pass
    # Performs animation when door is opened by player, helper for open_door()
    def open_animation(self):
        pass
    # Performs sound when door is opened by player, helper for open_door()
    def open_sound(self):
        pass
