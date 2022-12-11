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
        """Check if tiles can be correctly found by row number and column number"""
        world_obj = World("assets/rooms/layout1.json").init_room()
        test_row, test_col = 10, 10  # choose any numbers within bounds of the room dimensions
        testtile = world_obj.find_tile_by_row_col((test_row, test_col))
        assert testtile.row == test_row and testtile.col == test_col

    def test_find_tile_by_x_y(self, test_x=None, test_y=None):
        """Check if tiles can be correctly found by x y coords"""
        if test_x is None:
            test_x = 100
        if test_y is None:
            test_y = 110
        # choose any numbers within bounds of the room dimensions for test x & y

        world_obj = World("assets/rooms/layout1.json").init_room()
        testtile = world_obj.find_tile_by_x_y((test_x, test_y))
        # if the test_x and test_y values are between the actual x & y values + 32
        # the point at (test_x, test_y) will be inside the actual tile onscreen
        is_test_point_inside_tile = testtile.xpos <= test_x <= testtile.xpos + 32 and testtile.ypos <= test_y <= testtile.ypos + 32
        assert is_test_point_inside_tile

    def test_find_tile_by_char_pos(self):
        """the function this test is for ends up only relying on whether .find_tile_by_x_y() works correctly"""
        self.test_find_tile_by_x_y(100, 90)

    def test_update_room_sprites(self):
        """Test if .update_room_sprites sets the tile positions onscreen to the correct values"""
        world_obj = World("assets/rooms/layout1.json").init_room()
        testtile = world_obj.find_tile_by_row_col((1, 1))
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
