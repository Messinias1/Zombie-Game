import pygame
import constants

import math
import time
import random

from item import Item
from character import Character
from zombie import Zombie
from zombie import Small_Zombie
from zombie import Big_Zombie
from world import World
from button import Button
from bullet import Bullet
from weapon import Weapon


def handle_input(player):
    for event in pygame.event.get():
        mouse_position_x, mouse_position_y = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet_list.append(Bullet( (player.xpos+world_room.camera.x_scroll), (player.ypos+world_room.camera.y_scroll), mouse_position_x, mouse_position_y))
            
        quit_button.perform_mouse_click(event, quit_game, screen, mouse_position_x, mouse_position_y)

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

def create_zombie(zombie_list,zombie_sprites):
    zombie_rand = random.randint(1,3)
    if zombie_rand == 1:
        new_zombie = Zombie(random.randint(33, constants.SCREEN_WIDTH - 33), random.randint(33, constants.SCREEN_HEIGHT - 33), "assets/images/characters/tiny_zombie", world_room)
    elif zombie_rand == 2:
        new_zombie = Small_Zombie(random.randint(33, constants.SCREEN_WIDTH - 33), random.randint(33, constants.SCREEN_HEIGHT - 33), "assets/images/characters/tiny_zombie", world_room)
    elif zombie_rand == 3:
        new_zombie = Big_Zombie(random.randint(33, constants.SCREEN_WIDTH - 33), random.randint(33, constants.SCREEN_HEIGHT - 33), "assets/images/characters/tiny_zombie", world_room)
    zombie_list.append(new_zombie)
    zombie_sprites.add(new_zombie)

# Initialize Pygame and create display screen
pygame.init()
clock = pygame.time.Clock()
#initialized time for attack timer
start_time = pygame.time.get_ticks()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Zombie Game")

# create the world
world_room = World("assets/rooms/layout2.json").init_room()
# create player
player = Character(150, 80, "assets/images/characters/elf", world_room)

#create pistol
pistol = Weapon(0, 0, "assets/images/weapons/pistol.png", world_room, player, "")


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


#Create Zombies:
zombie_list = [ Zombie(400, 300, "assets/images/characters/tiny_zombie", world_room),
                Small_Zombie(600, 400, "assets/images/characters/tiny_zombie", world_room)]

dead_enemy_list = []

bullet_list = []

#Create Sprite Groups:
item_sprites = pygame.sprite.Group()
for item in item_list:
    item_sprites.add(item)

#Create Zombie Groups:
zombie_sprites = pygame.sprite.Group()
for zombie in zombie_list:
    zombie_sprites.add(zombie)

create_zombie(zombie_list, zombie_sprites)

# main game loop
run = True

#Coin Text:
coin_font = pygame.font.SysFont('inkfree', 30, italic=False,bold=True)
coin_txt = coin_font.render('Coins: ' + str(player.coins.coins), True, (255, 255, 255))
coin_txt_rect = coin_txt.get_rect()
coin_txt_rect.center = (800-(coin_txt.get_rect().width), 0+(coin_txt.get_rect().height))

#Health Text:
health_font = pygame.font.SysFont('inkfree', 30, italic=False,bold=True)
health_txt = health_font.render('Health: ' + str(player.health.health), True, (255, 255, 255))
health_txt_rect = health_txt.get_rect()
health_txt_rect.center = (0+(health_txt.get_rect().width), 0+(health_txt.get_rect().height))

#Wave Text:
wave = 1
wave_font = pygame.font.SysFont('inkfree', 30, italic=False,bold=True)
wave_txt = coin_font.render('Wave: ' + str(wave), True, (255, 255, 255))
wave_txt_rect = wave_txt.get_rect()
wave_txt_rect.center = (600-(coin_txt.get_rect().width), 0+(coin_txt.get_rect().height))

while run:
    # Background Color
    clock.tick(constants.FPS)
    screen.fill(constants.SURFACE_COLOR)

    #Item Collision Handeling:
    hit_list = pygame.sprite.spritecollide(player, item_sprites, True)

    for item in hit_list:
        item.picked_up = True

    world_room.room_sprite_group.draw(screen)

    # create quit button
    quit_button.implement_button(screen)

    # event handler
    handle_input(player)

    for zombie in zombie_sprites:
        zombie.move_towards_player(player)

    # run the .update() functions for everything in the room
    world_room.update_room_sprites()

    if len(zombie_sprites) == 0:
        wave += 1
        zombie_list = []
        zombie_sprites.empty()
        add_rand_amount_zombies = random.randint(1,3)
        for x in range(len(dead_enemy_list) + add_rand_amount_zombies):
            create_zombie(zombie_list, zombie_sprites)
        dead_enemy_list = []

    for zombie in zombie_sprites:
        if zombie.current_health <= 0:
            zombie.alive = False
        if zombie.alive == False:
            dead_enemy_list.append(zombie)
            zombie.kill()

    if pygame.time.get_ticks() - start_time > constants.ZOMBIE_ATTACK_CD:
        for zombie in zombie_sprites:
            zombie.deal_damage(player)
        start_time = pygame.time.get_ticks()

    for item in item_list:
        item.update()

    for zombie in zombie_list:
        zombie.update()

    dead_zombies = []
    for bullet in bullet_list:
        bullet.update_position(screen)
        for z in zombie_list:
            z.take_proj_hit(bullet)
            if z.is_dead():
                dead_zombies.append(z)

    for z in dead_zombies:
        zombie_list.remove(z)
        world_room.room_sprite_group.remove(z)

    pistol.update(screen)

    world_room.camera.follow_character(player)

    #Text Display

    coin_txt = coin_font.render('Coins: ' + str(player.coins.coins), True, (255, 255, 255))
    health_txt = health_font.render('Health: ' + str(player.health.health), True, (255, 255, 255))
    wave_txt = coin_font.render('Wave: ' + str(wave), True, (255, 255, 255))

    screen.blit(coin_txt, coin_txt_rect)
    screen.blit(health_txt, health_txt_rect)
    screen.blit(wave_txt, wave_txt_rect)
    
    if player.is_touching(zombie):
        player.take_hit(zombie.attack)

    if player.health.health <= 0:
        run == False

    pygame.display.update()

pygame.quit()
