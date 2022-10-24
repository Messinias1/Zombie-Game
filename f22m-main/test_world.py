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

    def test_update_all(self):
        w = World()
        w.generate("assets/rooms/layout1.json")
        original_x = w.room_sprites[10].rect.x  # after .generate() the rect.x == 0
        w.update_room_sprites()                 # after .update_room_sprites() rect.x shouldn't be 0
        update_x = w.room_sprites[10].rect.x    # choosing [10] and rect.x instead of rect.y is arbitrary
        self.assertTrue(original_x == 0 and update_x != 0)
