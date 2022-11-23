from unittest import TestCase
from world import World
import pytest


class TestWorld(TestCase):
    def test_init_room(self):
        """Test if .room_sprite_group is empty at first, and then if it's filled after .init_room() is called."""
        non_init_world = World("assets/rooms/layout1.json").room_sprite_group
        init_world = World("assets/rooms/layout1.json").init_room().room_sprite_group
        # "not non_init_world" should return True if the sprite group is empty
        # which it should be if the world is non initialized (init_room() hasn't been called)

        # and simply "init_world" should return True if the sprite group is not empty
        # and after init_room() has been called, it shouldn't be empty anymore
        assert not non_init_world and init_world

    def test_find_tile_by_row_col(self):
        """Check if the room tiles are generated correctly after .init_room is called"""
        world_obj = World("assets/rooms/layout1.json").init_room()
        testtile = world_obj.find_tile_by_row_col(1, 1)
        # the tile at row 1 and column 1 should have xpos & ypos equal to the
        # origin of the whole room (0, 0) + (tile.width, tile.height)
        # because all tiles have the same dimensions and the room is generated by adding
        # these dimensions after each tile is placed
        assert testtile.xpos == testtile._width and testtile.ypos == testtile._height

    def test_find_next_move(self):
        self.fail()

    def test_update_room_sprites(self):
        """Test if .update_room_sprites sets the tile positions onscreen to the correct values"""
        world_obj = World("assets/rooms/layout1.json").init_room()
        testtile = world_obj.find_tile_by_row_col(1, 34)
        # for testtile let's choose a tile whose xpos and ypos aren't 0

        # The x & y it really is at (tile.rect.x, tile.rect.y) will start at 0 after .init_room()
        # and will be set to the (tile.xpos, tile.ypos) after .update_room_sprites() is called

        should_be_at = (testtile.xpos + world_obj.camera.x_scroll, testtile.ypos + world_obj.camera.y_scroll)
        # this is what the game code sets the tile positions to

        real_pos = (testtile.rect.x, testtile.rect.y)
        # this should be (0, 0) right now

        correct_pos_before = should_be_at == real_pos  # this should be False

        world_obj.update_room_sprites()  # this should set the tile.rects to the correct x & y pos's
        real_pos = (testtile.rect.x, testtile.rect.y)

        correct_pos_after = should_be_at == real_pos  # this should be True
        assert not correct_pos_before and correct_pos_after
