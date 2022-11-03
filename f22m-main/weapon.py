"""A player's weapon object
"""
class Weapon:
    """ Creates a weapon
    :param textures: {} | {'spritesheet': filepath to spritesheet}
    :param stats: {}    | {'damage': int (value of weapon damage), 'accuracy': int (spread of bullets), 'firerate': (time between shots in seconds), 'reload_speed': (Speed of reloading), 'ammo_size': int (amount of ammo weapon has), 'ammo_type': type of Bullet object (maybe not added but seems interesting?), 'guntype': (melee, ranged), 'name': (Name of the weapon)} 
    :param sounds {}    | {'shot': (sound for shooting), 'empty': (sound for shooting with no ammo), 'reloading': (sound for reloading)}
    """
    def __init__(self, textures, stats, sounds) -> None:
        # Spritesheet configuration
        self.spritesheet = pygame.image.load(None)

        # Sound configuration
        self.sounds = sounds

        # Weapon stats configuration
        self.damage = stats['damage']
        self.accuracy = stats['accuracy']
        self.firerate = stats['firerate']
        self.reload_speed = stats['reloadspeed']
        self.ammo_size = stats['ammosize']
        self.ammo_type = stats['ammotype']
        self.guntype = stats['guntype']
        self.name = stats['name']
        self.stats = stats

        # Melee Weapon handling
        if self.guntype != 'melee':
            self.range = stats['range']
        else:
            # Still working on melee weapons
            self.range = None

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