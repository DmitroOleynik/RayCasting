import pygame
from config import *


class Sprites:
    def __init__(self):
        self.sprite_types = {
            # 'bosinn': pygame.image.load('sprites/bosinn/BoSinn.png').convert_alpha(),
            'rostanuk': pygame.image.load('sprites/rostanuk/photo_2024-10-01_21-52-12.png').convert_alpha(),
            # 'miky': pygame.image.load('sprites/miky/pngegg.png').convert_alpha(),
            'tomas': pygame.image.load('sprites/tomas/pngwing.com.png').convert_alpha(),
            # 'hasbulla': pygame.image.load('sprites/hasbulla/hasbulla.png').convert_alpha(),
            'petya': pygame.image.load('sprites/petya/petya.png').convert_alpha()
        }
        self.list_of_objects = [
            # SpriteObject(self.sprite_types['bosinn'], True, (7.1, 3.1), 0.4, 0.8),
            SpriteObject(self.sprite_types['rostanuk'], True, (7.6, 2.1), 0.4, 0.8),
            SpriteObject(self.sprite_types['tomas'], True, (6.1, 4.1), 0.8, 0.8),
            # SpriteObject(self.sprite_types['miky'], True, (7.4, 3.1), 0.8, 0.8),
            # SpriteObject(self.sprite_types['hasbulla'], True, (6.2, 4.2), 1.2, 0.8),
            SpriteObject(self.sprite_types['petya'], True, (7.2, 1.1), 0.4, 0.8)
        ]


class SpriteObject:
    def __init__(self, object, static, pos, shift, scale):
        self.object = object
        self.static = static
        self.pos = self.x, self.y = pos[0] * TILE, pos[1] * TILE
        self.shift = shift
        self.scale = scale

    def object_locate(self, player, walls):
        dx, dy = self.x - player.x, self.y - player.y
        distance_to_sprite = math.sqrt(dx ** 2 + dy ** 2)

        theta = math.atan2(dy, dx)
        gamma = theta - player.angle
        if dx > 0 and 180 <= math.degrees(player.angle) <= 360 or dx < 0 and dy < 0:
            gamma += DOUBLE_PI

        delta_rays = int(gamma / DELTA_ANGLE)
        current_ray = CENTER_RAY + delta_rays
        distance_to_sprite *= math.cos(HALF_FOV - current_ray * DELTA_ANGLE)

        if 0 <= current_ray <= NUM_RAYS - 1 and distance_to_sprite < walls[current_ray][0]:
            proj_height = int(PROJ_COEFF / distance_to_sprite * self.scale)
            half_proj_height = proj_height // 2
            shift = half_proj_height * self.shift

            sprite_pos = (current_ray * SCALE - half_proj_height, HALF_HEIGHT - half_proj_height + shift)
            sprite = pygame.transform.scale(self.object,(proj_height, proj_height))
            return (distance_to_sprite, sprite, sprite_pos)
        else:
            return (False,)
