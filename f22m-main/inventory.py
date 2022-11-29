from weapon import Weapon
from item import Item

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
        self.item_list_ = []

    def add_gun(self, gun:Weapon)->None:
        """This adds a gun into the gun list

            Parameters:
                gun {Weapon}: takes in a gun
        """
        newGunName = gun.get_name()
        
        if self.get_gun(newGunName).get_name() == newGunName:
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
        
    def add_item(self, item:Item)->None:
        """Adds items to a list

        Args:
            item (Item): takes in an item
        """
        self.melee_list_.append(item)
    
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
        
    def get_item(self, itemType:str)->Item:
        """Looks for an item the player might have

        Args:
            itemName (str): takes in the name of an item

        Returns:
            Item: the found item
        """
        for item in self.item_list_:
            if itemType == item.get_type():
                return item
            return None
        pass