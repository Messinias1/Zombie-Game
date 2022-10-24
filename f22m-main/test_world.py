from unittest import TestCase
from world import World


class Test(TestCase):
    def test_world(self):
        w = World()
        self.assertTrue(w.room_sprites == [])

    def test_generate(self):
        w = World()
        w.generate("assets/rooms/layout1.json")
        self.assertFalse(w.room_sprites == [])
