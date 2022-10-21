from weapon import Weapon
from gun import Gun

class Inventory:
    def __init__(self, gun_list:list = None, melee_list:list = None, throwable:Weapon = None):
        if gun_list:
            self.gun_list_ = gun_list
        else:
            pistol = Gun("Default Pistol", 10, 500, 12, 30, 100, 100, 12)
            self.gun_list_ = [pistol]
        if melee_list:
            self.melee_list_ = melee_list
        else:
            self.melee_list_ = []

        self.throwable_ = throwable

    def add_gun(self, gun:Gun):
        self.gun_list_.append(gun)

    def add_melee(self, melee:Weapon):
        self.melee_list_.append(melee)
    
    def get_gun(self, gunName)->Gun:
        for gun in self.gun_list_:
            if gunName == gun.get_name():
                return gun