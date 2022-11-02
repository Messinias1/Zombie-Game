import item
from math import isclose
import pytest

class test_item:

    def test_default():
        rand_item = item(300, 200, "assets/images/items/coin_f0.png", 100, "DEFAULT")
        assert rand_item.type == "DEFAULT"

    def test_coin():
        rand_item = item(300, 200, "assets/images/items/coin_f0.png", 100, "Currency")
        assert rand_item.type == "Currency"

    def test_potion():
        rand_item = item(300, 200, "assets/images/items/coin_f0.png", 100, "Healable")
        assert rand_item.type == "Healable"

    def test_no_strength():
        rand_item = item(300, 200, "assets/images/items/coin_f0.png", 0, "Healable")

        with pytest.raises(ValueError):
            rand_item.strength == 0