from inventory import Inventory
import pytest

class WeaponMock:
    def __init__(self, name) -> None:
        self.name = name
    
    def get_name(self)->str:
        return self.name

def test_add_different_gun():
    pistol = WeaponMock("Pistol")
    myInventory = Inventory()
    
    with pytest.raises(ValueError):
        myInventory.add_gun(pistol)
        
def test_add_different_melee():
    katana = WeaponMock("Katana")
    myInventory = Inventory()
    myInventory.add_melee(katana)
    
    with pytest.raises(ValueError):
        myInventory.add_melee(katana)