import pygame
import math

class PlayerBullet:
    def __init__(self, x:int, y:int , mouse_x, mouse_y) -> None:
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.angle = math.atan2(y - mouse_y, x - mouse_x)
        self.speed = 15
        self.x_velocity = math.cos(self.angle) * self.speed
        self.y_velocity = math.sin(self.angle) * self.speed

    def get_position(self):
        position = (self.x, self.y)
        return position
        
    def main(self, screen):
        self.x -= int(self.x_velocity)
        self.y -= int(self.y_velocity)
        black = 0, 0, 0

        pygame.draw.circle(screen, black, (self.x, self.y), 5)