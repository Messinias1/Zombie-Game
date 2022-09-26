import pygame
import random
import room
import entity
import camera

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    KEYUP,
    QUIT,
    K_w,
    K_a,
    K_s,
    K_d
)


# GLOBAL VARIABLES
COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)
WIDTH = 500
HEIGHT = 500

RED = (255, 0, 0)


class Main:
    def __init__(self):
        pygame.init()
        self.size = (WIDTH, HEIGHT)
        self.screen = pygame.display.set_mode(self.size)
        self.game_map = room.Room()
        self.player = entity.Entity(250, 250, "sprites/player/p.gif")
        self.game_map.generate("rooms/layout.json")
        self.game_map.tile_group.add(self.player)
        self.exit = False
        self.clock = pygame.time.Clock()
        self.curmove, self.SPEED = [0, 0], 2

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            return True
        elif event.type == KEYDOWN:
            if event.key == pygame.K_w:
                self.curmove = [self.curmove[0], self.SPEED]
            elif event.key == pygame.K_s:
                self.curmove = [self.curmove[0], -self.SPEED]
            elif event.key == pygame.K_a:
                self.curmove = [self.SPEED, self.curmove[1]]
            elif event.key == pygame.K_d:
                self.curmove = [-self.SPEED, self.curmove[1]]
        elif event.type == KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                self.curmove = [self.curmove[0], 0]
            else:
                self.curmove = [0, self.curmove[1]]
        return False

    def run(self):
        exit = False
        while not exit:
            for event in pygame.event.get():
                exit = self.handle_event(event)
            self.game_map.update_all_tiles()
            self.screen.fill(SURFACE_COLOR)
            self.game_map.tile_group.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)
            self.game_map.camera.x_scroll += self.curmove[0]
            self.game_map.camera.y_scroll += self.curmove[1]
        pygame.quit()


if __name__ == "__main__":
    m = Main()
    m.run()
