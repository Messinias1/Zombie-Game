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
        
        #performs click event for the quit button
        quit_button.perform_mouse_click(event, quit_game, screen)

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
item_list = [ Item(400, 200, "assets/images/items/coin_f0.png", 1, "Coin", world_room, player), 
              Item(300, 200, "assets/images/items/coin_f0.png", 1, "Coin", world_room, player),
              Item(200, 200, "assets/images/items/potion_red.png", 100, "Healable", world_room, player)

]

#Create Sprite Groups:
item_sprites = pygame.sprite.Group()

#Add sprites to respective sprite groups here so that they can be drawn:
world_room.room_sprite_group.add(player)
world_room.room_sprite_group.add(zombie)

for item in item_list:
    world_room.room_sprite_group.add(item)
    item_sprites.add(item)

# main game loop
run = True

#Coin Text:
coin_font = pygame.font.SysFont('inkfree', 30, italic=False,bold=True)
coin_txt = coin_font.render('Coins: ' + str(player.coins), True, (255, 255, 255))
coin_txt_rect = coin_txt.get_rect()
coin_txt_rect.center = (800-(coin_txt.get_rect().width), 0+(coin_txt.get_rect().height))

#Health Text:
health_font = pygame.font.SysFont('inkfree', 30, italic=False,bold=True)
health_txt = health_font.render('Health: ' + str(player.health), True, (255, 255, 255))
health_txt_rect = health_txt.get_rect()
health_txt_rect.center = (0+(health_txt.get_rect().width), 0+(health_txt.get_rect().height))

while run:
    # Background Color
    clock.tick(constants.FPS)
    screen.fill(constants.SURFACE_COLOR)

    #Item Collision Handeling:
    hit_list = pygame.sprite.spritecollide(player, item_sprites, True)

    for item in hit_list:
        item.picked_up = True

    item_sprites.draw(screen)
    world_room.room_sprite_group.draw(screen)

    # create quit button
    quit_button.implement_button(screen, quit_game)

    # event handler
    handle_input(player)

    # run the .update() functions for everything in the room
    world_room.update_room_sprites()

    for item in item_list:
        item.update()

    world_room.camera.follow_character(player)

    #Text Display
    coin_txt = coin_font.render('Coins: ' + str(player.coins), True, (255, 255, 255))
    health_txt = health_font.render('Health: ' + str(player.health), True, (255, 255, 255))

    screen.blit(coin_txt, coin_txt_rect)
    screen.blit(health_txt, health_txt_rect)

    pygame.display.update()

pygame.quit()
