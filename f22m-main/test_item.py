'''

Test cases for Item class

Marcos Remy, December 2020

'''

import unittest
from item import Item
import pytest

from unittest.mock import MagicMock

class ItemTest(unittest.TestCase):

    def test_default(self):
        
        """
        Tests item's created with the default type are of their correct type
        """
        inroom = MagicMock()
        rand_item = Item(0, 0, "assets/images/items/coin_f0.png", 100, "DEFAULT", inroom, "PLAYER")

        assert rand_item.type == "DEFAULT"

    def test_coin(self):
        """
        Checks if the item is given the appropriate currency type when constructed with it
        """

        inroom = MagicMock()
        rand_item = Item(0, 0, "assets/images/items/coin_f0.png", 100, "Currency", inroom, "PLAYER")

        assert rand_item.type == "Currency"

    def test_potion(self):
        """
        Checks if the item is given the appropriate healable type when constructed with it
        """

        inroom = MagicMock()
        rand_item = Item(0, 0, "assets/images/items/coin_f0.png", 100, "Healable", inroom, "PLAYER")

        assert rand_item.type == "Healable"

    def test_no_strength(self):
        """
        Checks if the item is given the appropriate default type when constructed with it
        """

        inroom = MagicMock()
        rand_item = Item(0, 0, "assets/images/items/coin_f0.png", 0, "DEFAULT", inroom, "PLAYER")

        assert rand_item.strength == 0