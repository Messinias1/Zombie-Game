import pygame
import constants
import math

from item import Item
from character import Character
from world import World


def handle_input(player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        exit()

    # WASD --> player movement
    dx = 0
    dy = 0
    if keys[pygame.K_a]:
        dx = -constants.PLAYER_SPEED
    if keys[pygame.K_d]:
        dx = constants.PLAYER_SPEED
    if keys[pygame.K_w]:
        dy = -constants.PLAYER_SPEED
    if keys[pygame.K_s]:
        dy = constants.PLAYER_SPEED

    player.move(dx, dy)


# Initialize Pygame and create display screen
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Zombie Game")

# create the world
world_room = World()
world_room.generate("assets/rooms/layout1.json")
# create player
player = Character(400, 300, "assets/images/characters/elf", world_room)

# Create Items:
coin = Item(400, 300, "assets/images/items/coin_f0.png", 100, "DEFAULT", world_room)



# Add sprites to world sprite group here so that they can be drawn:
world_room.room_sprite_group.add(player)
world_room.room_sprite_group.add(coin)


# main game loop
run = True

while run:
    # Background Color
    clock.tick(constants.FPS)
    screen.fill(constants.SURFACE_COLOR)

    # event handler
    handle_input(player)

    # run the .update() functions for everything in the room
    world_room.update_room_sprites()
    world_room.camera.follow_character(player)
    # draw everything in the room on screen
    world_room.room_sprite_group.draw(screen)
    pygame.display.update()

pygame.quit()
