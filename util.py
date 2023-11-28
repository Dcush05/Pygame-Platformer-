import pygame


class Spritesheets:
    def __init__(self, path):
        self.path = path 
        self.sprite_sheet = pygame.image.load(path).convert()
        #img.set_colorkey((0,0,0))
        

    def get_sprite(self,size,x, y, width, height):
        sprite = pygame.Surface((width, height))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sprite_sheet,(0,0),(x,y,width,height))
        sprite = pygame.transform.scale(sprite, size)

        return sprite