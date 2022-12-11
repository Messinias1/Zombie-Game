import pygame
import math

"""A player's weapon object
"""
class Weapon(pygame.sprite.Sprite):
    """ Creates a weapon
    :param textures: {} | {'spritesheet': filepath to spritesheet}
    :param stats: {}    | {'damage': int (value of weapon damage), 'accuracy': int (spread of bullets), 'firerate': (time between shots in seconds), 'reload_speed': (Speed of reloading), 'ammo_size': int (amount of ammo weapon has), 'ammo_type': type of Bullet object (maybe not added but seems interesting?), 'guntype': (melee, ranged), 'name': (Name of the weapon)} 
    :param sounds {}    | {'shot': (sound for shooting), 'empty': (sound for shooting with no ammo), 'reloading': (sound for reloading)}
    """
    def __init__(self, x, y, img, in_room, player, sounds) -> None:
        super().__init__()
        self.xpos = x
        self.ypos = y

        self.player = player

        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = self.xpos
        self.rect.y = self.ypos

        self.world = in_room

        # Sound configuration
        self.sounds = sounds

        # Weapon stats configuration
        # self.damage = stats['damage']
        # self.accuracy = stats['accuracy']
        # self.firerate = stats['firerate']
        # self.reload_speed = stats['reloadspeed']
        # self.ammo_size = stats['ammosize']
        # self.ammo_type = stats['ammotype']
        # self.guntype = stats['guntype']
        # self.name = stats['name']
        # self.stats = stats

        # Melee Weapon handling
        # if self.guntype != 'melee':
        #     self.range = stats['range']
        # else:
        #     # Still working on melee weapons
        #     self.range = None

    # Performs the shooting animation 
    def shoot_animation(self):
        pass
    # Deals damage (Note: may be the job of the bullet class still considering whether bullets should travel or if shots should be instant)
    def damage(self):
        pass
    # Performs the reloading animation
    def reload_animation(self):
        pass
    # Displays the gun
    def draw(self):
        pass
    def get_name(self):
        return self.name

    def update(self, screen, camera_ref=None):
        #take into account camera scroll when setting position
        if camera_ref is None:
            camera_ref = self.world.camera

        mouse_x, mouse_y = pygame.mouse.get_pos()

        mouse_x = mouse_x - camera_ref.x_scroll
        mouse_y = mouse_y - camera_ref.y_scroll

        angle = (180 / math.pi) * -math.atan2((mouse_y - self.player.ypos), (mouse_x - self.player.xpos))

        rotated_image = pygame.transform.rotate(self.image, angle)

        #Trying to add flipped gun:
        # if (angle > -85 and angle < 150):
        #     rotated_image =  pygame.transform.flip(rotated_image, True, False)
        # else:
        #     rotated_image =  pygame.transform.flip(rotated_image, False, False)

        rotated_rect = rotated_image.get_rect()

        rotated_rect.x = self.player.xpos + camera_ref.x_scroll + self.xpos
        rotated_rect.y = self.player.ypos + camera_ref.y_scroll + self.ypos

            
        screen.blit(rotated_image, rotated_rect)