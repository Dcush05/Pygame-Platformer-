import csv
import os
import pygame
from spritesheet import Spritesheets




class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y, spritesheet):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.parse_sprite(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
        

class Spikes(pygame.sprite.Sprite):
    def __init__(self, filename,x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = Spritesheets(filename).get_sprite(0,0,18,18)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

class Flag(pygame.sprite.Sprite):
    def __init__(self, filename,x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = Spritesheets(filename).get_sprite(0,0,18,16)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
       

class TileMap(pygame.sprite.Sprite):
    def __init__(self, filename, spritesheet): #(,object)
        self.tile_size = 16   #size of each tile aesprite 128x128 means tiles are 16x16
        self.spawn_x = 0
        self.spawn_y = -10
        self.spritesheet = spritesheet
        self.tiles = self.load_tiles(filename)
        self.spikes = self.load_spikes(filename)
        self.flags = self.load_flag(filename)
        self.map_surface = pygame.Surface((self.map_w, self.map_h))
        self.map_surface.set_colorkey((0, 0, 0))
        self.load_map()
        self.coins_to_remove = []


    def draw_map(self, surface,offset=(0,0)):
        """renders map"""
        surface.blit(self.map_surface, (0-offset[0], 0-offset[1]))
    
           
    def load_map(self):
        """renders the entire map"""
        for tile in self.tiles:
            tile.draw(self.map_surface)
        for spike in self.spikes:
            spike.draw(self.map_surface)
        for flag in self.flags:
            flag.draw(self.map_surface)

        
    
    def read_csv(self, filename):
        """Reads the .csv file and returns the map thats given in the .csv"""
        map = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                map.append(list(row))
        return map
    

    def load_tiles(self, filename):

        """renders tile and assign sprites to each tile"""
        tiles = []
        tile_mapping = {
        '-1': None,  # No image for -1
        '0': 'GroundSet-0.png',
        '1': 'GroundSet-1.png',
        '2': 'GroundSet-2.png',
        '3': 'GroundSet-3.png',
        '8': 'GroundSet-4.png',
        '9': 'GroundSet-5.png',
        '10': 'GroundSet-6.png',
        '11': 'GroundSet-7.png',
        '16': 'GroundSet-8.png',
        '17': 'GroundSet-9.png',
        '18': 'GroundSet-10.png',
        '19': 'GroundSet-11.png',
                        }

        #coins = []
        map_data = self.read_csv(filename)     
        for y, row in enumerate(map_data):
                for x, tile in enumerate(row):
                    if tile == '-1':
                        self.start_x, self.start_y = x * self.tile_size, y * self.tile_size
                    elif tile in tile_mapping:
                        image_fileName = tile_mapping[tile]
                        if image_fileName:
                            tiles.append(Tile(image_fileName, x*self.tile_size, y*self.tile_size, self.spritesheet)) 
            
            # Store the size of the tile map
        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
        return tiles
    

    def load_spikes(self, filename):
        """assigns the spike sprite to a tile"""
        spikes = [] 
       # self.coins_group = pygame.sprite.Group()
        map = self.read_csv(filename)
        x, y = 0 , 0
        for row in map:
            x = 0
            for spike in row:
                if spike == '21':
                    spikes.append(Spikes('assets/objects/spikes.png', x * self.tile_size, y * self.tile_size))
                x += 1
            y += 1
        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
        return spikes
    

    def load_flag(self, filename):
        """assigns the flag sprite to a tile"""
        flags = [] 
       # self.coins_group = pygame.sprite.Group()
        map = self.read_csv(filename)
        x, y = 0 , 0
        for row in map:
            x = 0
            for flag in row:
                if flag == '22':
                    flags.append(Flag('assets/objects/flag.png', x * self.tile_size, y * self.tile_size))
                x += 1
            y += 1
        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
        return flags
    

    
