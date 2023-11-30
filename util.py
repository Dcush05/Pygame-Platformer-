import pygame, json


class Spritesheets:
    def __init__(self, path):
        self.path = path 
        self.sprite_sheet = pygame.image.load(path).convert()
        #img.set_colorkey((0,0,0))


    def toJSON(self):
        self.meta_data = self.path.replace('png', 'json')
        with open(self.meta_data) as f:
            self.data = json.load(f)
        f.close()     

    def get_sprite(self,x, y, width, height):
        sprite = pygame.Surface((width, height))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sprite_sheet,(0,0),(x,y,width,height))
       #sprite = pygame.transform.scale(sprite, size)
        
        return sprite
    def parse_sprite(self, name):
        sprite = self.data['frames'][name]['frame']
        x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        image = self.get_sprite(x, y, w, h)
        return image