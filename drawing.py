import pygame
from config import *
from ray_casting import ray_casting


class Drawing:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.texture = pygame.image.load('texture/1.png').convert()

    def background(self):
        pygame.draw.rect(self.screen, SKYBLUE, (0, 0, WIDTH, HALF_HEIGHT))

    def world(self, world_objects):
        for obj in sorted(world_objects, key=lambda n: n[0], reverse=True):
            if obj[0]:
                _, object, object_pos = obj
                self.screen.blit(object, object_pos)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, RED)
        self.screen.blit(render, FPS_POS)
