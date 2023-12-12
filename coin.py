from typing import Any
import pygame
from  spritesheet import Spritesheets




class Coins(pygame.sprite.Sprite):

    def __init__(self, spawn_x, spawn_y,):
        pygame.sprite.Sprite.__init__(self)
        self.image = Spritesheets("assets\coin.png").get_sprite(0,0,16,16)
        self.rect = self.image.get_rect()
        self.rect.x = spawn_x
        self.rect.y = spawn_y
        self.collected = False
        self.points = 1
        

    def draw(self, surface, offset=(0,0)):
        surface.blit(self.image, (self.rect.x, self.rect.y))
    def update(self):
        self.kill()
    





