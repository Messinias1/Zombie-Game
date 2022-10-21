import pygame
import constants

from item import Item
from character import Character
from world import World

display_scroll = [0,0]

def handle_input():

    display_scroll[0], display_scroll[1] = 0, 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        exit()

    # WASD --> player movement
    if keys[pygame.K_a]:
        display_scroll[0] += player.check_for_collisions(try_x=-constants.PLAYER_SPEED)[0]
    if keys[pygame.K_d]:
        display_scroll[0] += player.check_for_collisions(try_x=constants.PLAYER_SPEED)[0]
    if keys[pygame.K_w]:
        display_scroll[1] -= player.check_for_collisions(try_y=constants.PLAYER_SPEED)[1]
    if keys[pygame.K_s]:
        display_scroll[1] += player.check_for_collisions(try_y=constants.PLAYER_SPEED)[1]

#Initialize Pygame and create display screen
pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Zombie Game")

# create the world
world_room = World("assets/rooms/layout1.json")
# create player
player = Character(400, 300, "assets/images/characters/elf", world_room)

#Create Items:
coin = Item(400, 300, "assets/images/items/coin_f0.png", 100, "DEFAULT", world_room)

#Add sprites to world sprite group here so that they can be drawn:
world_room.room_sprite_group.add(player)
world_room.room_sprite_group.add(coin)

# main game loop
run = True
while run:

    #Background Color
    screen.fill(constants.SURFACE_COLOR)

    # event handler
    handle_input()

    world_room.camera.x_scroll -= display_scroll[0]
    world_room.camera.y_scroll -= display_scroll[1]

    # run the .update() functions for everything in the room
    world_room.update_room_sprites()
    coin.update()
    player.update()
    # draw everything in the room on screen
    world_room.room_sprite_group.draw(screen)
    pygame.display.update()

pygame.quit()


