from weapon import Weapon

class Inventory:
    """This Class creates an inventory to store various items and weapons
    """
    def __init__(self, gun_list:list = None, melee_list:list = None, throwable:Weapon = None):
        """This creates a new Inventory Object

            Parameters:
                gun_list {list}: takes in a list
                melee_list {list}: takes in a list
                throwable {Weapon}: takes in a Weapon
        """
        if gun_list:
            self.gun_list_ = gun_list
        else:
            textures = {'spritesheet': 'No/path/for/now'}
            stats = {
                'damage': 25,
                'accuracy': 2,
                'firerate': .1,
                'reload_speed': .5,
                'ammo_size': 300,
                'ammo_type': 'None',
                'guntype': 'ranged',
                'name': 'Pistol'
            }
            sounds = {
                'shot': 'None',
                'empty': 'None',
                'reloading': 'None',
            }
            
            pistol = Weapon(self, textures, stats, sounds)
            self.gun_list_ = [pistol]
        if melee_list:
            self.melee_list_ = melee_list
        else:
            self.melee_list_ = []

        self.throwable_ = throwable

    def add_gun(self, gun:Weapon):
        """This adds a gun into the gun list

            Parameters:
                gun {Weapon}: takes in a Weapon
        """

        self.gun_list_.append(gun)

    def add_melee(self, melee:Weapon):
        """This adds a melee weapon to the melee list

            Parameters:
                melee {Weapon}: takes in a Weapon
        """

        self.melee_list_.append(melee)
    
    def get_gun(self, gunName)->Weapon:
        """This returns a gun

            Parameters:
                gunName {string}: takes in a string
            
            Returns:
                Weapon: a gun object
        """

        for gun in self.gun_list_:
            if gunName == gun.get_name():
                return gun