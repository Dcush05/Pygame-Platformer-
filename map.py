import pygame, csv, os
from util import Spritesheets

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y, spritesheet):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.parse_sprite(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

class TileMap():
    def __init__(self, filename, spritesheet):
        self.tile_size = 16   #size of each tile aesprite 128x128 means tiles are 16x16
        self.spawn_x = 0
        self.spawn_y = -10
        self.spritesheet = spritesheet
        self.tiles = self.load_tiles(filename)
        self.map_surface = pygame.Surface((self.map_w, self.map_h))
        self.map_surface.set_colorkey((0, 0, 0))
        self.load_map()
#Renders map
    def draw_map(self, surface):
        surface.blit(self.map_surface, (0, 0))

    def load_map(self):
        for tile in self.tiles:
            tile.draw(self.map_surface)

    def read_csv(self, filename):
        map = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                map.append(list(row))
        return map
#Loads a tile from a picture and uses the csv to place the coordinate of where that tile is supposed to go
    def load_tiles(self, filename):
        tiles = []
        map = self.read_csv(filename)
        x, y = 0, 0
        for row in map:
            x = 0
            for tile in row:
                if tile == '-1': #−1,0,1,2,3,8,9,11,16,17,18,19 numbers for the assigned tiles in the csv file, the png is coming from parsing the data from the groundSet.json file this made my brain hurt
                 self.start_x, self.start_y = x * self.tile_size, y * self.tile_size
                elif tile == '0':
                    tiles.append(Tile('GroundSet-0.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '1':
                    tiles.append(Tile('GroundSet-1.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '2':
                    tiles.append(Tile('GroundSet-2.png', x*self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '3':
                    tiles.append(Tile('GroundSet-3.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '8':
                    tiles.append(Tile('GroundSet-4.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '9':
                    tiles.append(Tile('GroundSet-5.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '10':
                    tiles.append(Tile('GroundSet-6.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '11':
                    tiles.append(Tile('GroundSet-7.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '16':
                    tiles.append(Tile('GroundSet-8.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '17':
                    tiles.append(Tile('GroundSet-9.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '18':
                    tiles.append(Tile('GroundSet-10.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '19':
                    tiles.append(Tile('GroundSet-11.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                
                    # Move to next tile in current row
                x += 1

            # Move to next row
            y += 1
            # Store the size of the tile map
        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
        return tiles
