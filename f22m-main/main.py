import pygame
import constants
import math

from item import Item
from character import Character
from zombie import Zombie
from world import World
from button import Button


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
player = Character(150, 80, "assets/images/characters/elf", world_room)
zombie = Zombie(400, 300, "assets/images/characters/tiny_zombie", world_room)

# create quit button
quit_button = Button(some_width = 75,
                     some_height = 30,
                     some_position_x = 10,
                     some_position_y = 560,
                     some_text = 'Quit',
                     some_text_position_x = 27)

# quit button function
def quit_game():
    pygame.quit()
    exit()

# Create Items:
coin_list = [ Item(400, 200, "assets/images/items/coin_f0.png", 100, "DEFAULT", world_room), 
              Item(300, 200, "assets/images/items/coin_f0.png", 100, "DEFAULT", world_room)
]

#Create Sprite Groups:
coin_sprites = pygame.sprite.Group()

#Add sprites to respective sprite groups here so that they can be drawn:
world_room.room_sprite_group.add(player)
world_room.room_sprite_group.add(zombie)

for coin in coin_list:
    world_room.room_sprite_group.add(coin)
    coin_sprites.add(coin)

# main game loop
run = True

while run:
    # Background Color
    clock.tick(constants.FPS)
    screen.fill(constants.SURFACE_COLOR)

    #Coin Collision Handeling:
    if pygame.sprite.spritecollide(player, coin_sprites, True):
        player.coins += 1
        print(player.coins)

    # event handler 
    handle_input(player)
    zombie.move_towards_player(player)

    # run the .update() functions for everything in the room
    world_room.update_room_sprites()

    for coin in coin_list:
        coin.update()

    world_room.camera.follow_character(player)
    # draw everything in the room on screen
    coin_sprites.draw(screen)
    world_room.room_sprite_group.draw(screen)
    # quit button actions
    quit_button.implement_button(screen, quit_game)

    pygame.display.update()

pygame.quit()
