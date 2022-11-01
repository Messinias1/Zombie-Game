from multiprocessing.sharedctypes import Value
from weapon import Weapon

class Inventory:
    """This Class creates an inventory to store various items and weapons
    """
    def __init__(self)->None:
        """This creates a new Inventory Object with a default pistol
        """

        textures = {'spritesheet': 'No/path/for/now'}
        stats = {
            'damage': 25,
            'accuracy': 2,
            'firerate': .1,
            'reloadspeed': .5,
            'ammosize': 300,
            'ammotype': 'None',
            'guntype': 'ranged',
            'name': 'Pistol',
            'range': 100
        }
        sounds = {
            'shot': 'None',
            'empty': 'None',
            'reloading': 'None',
        }
        
        pistol = Weapon(textures, stats, sounds)
        
        self.gun_list_ = [pistol]
        self.melee_list_ = []
        self.throwable_ = None

    def add_gun(self, gun:Weapon)->None:
        """This adds a gun into the gun list

            Parameters:
                gun {Weapon}: takes in a gun
        """
        if self.get_gun(gun.get_name()).get_name() == gun.get_name():
            raise ValueError("This gun is already in the inventory")
        
        self.gun_list_.append(gun)

    def add_melee(self, melee:Weapon)->None:
        """This adds a melee weapon to the melee list

            Parameters:
                melee {Weapon}: takes in a melee weapon
        """
        if self.get_melee_weapon(melee.get_name()) != None:
            if self.get_melee_weapon(melee.get_name()).get_name() == melee.get_name():
                raise ValueError("This gun is already in the inventory")
        
        self.melee_list_.append(melee)
    
    def get_gun(self, gunName:str)->Weapon:
        """This returns a gun

            Parameters:
                gunName {string}: takes in the gun's name
            
            Returns:
                Weapon: the found gun
        """

        for gun in self.gun_list_:
            if gunName == gun.get_name():
                return gun
    
    def get_melee_weapon(self, meleeWeaponName:str)->Weapon:
        """This returns a melee weapon

            Parameters:
                meleeWeaponName {string}: takes in the melee weapon's name
            
            Returns:
                Weapon: the found melee weapon
        """

        for meleeWeapon in self.melee_list_:
            if meleeWeaponName == meleeWeapon.get_name():
                return meleeWeapon
            return None