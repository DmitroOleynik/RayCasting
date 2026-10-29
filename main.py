import pygame
from config import *
from player import Player
from drawing import Drawing
from sprite_objects import *
from ray_casting import ray_casting


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

sprites = Sprites()
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    screen.fill(BACKGROUND_COLOR)

    drawing.background()
    walls = ray_casting(player, drawing.texture)
    drawing.world(walls + [obj.object_locate(player, walls) for obj in sprites.list_of_objects])
    drawing.fps(clock)

    pygame.display.update()
    clock.tick(FPS)
