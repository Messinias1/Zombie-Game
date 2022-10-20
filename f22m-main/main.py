import pygame
import constants
from character import Character
from world import World

pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Zombie Game")

# create the world
world_room = World("assets/rooms/layout1.json")
# create player
player = Character(40, 28, "assets/images/characters/elf", world_room)
world_room.room_sprite_group.add(player)
# main game loop
run = True
while run:
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # run the .update() functions for everything in the room
    world_room.update_room_sprites()
    player.update()
    # draw everything in the room on screen
    world_room.room_sprite_group.draw(screen)
    pygame.display.update()

pygame.quit()
