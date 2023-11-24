import pygame



def load_image(path):
    img = pygame.image.load(path).convert()
    #img.set_colorkey((0,0,0))
    
    return img

def get_sprite(image, x, y, width, height):
    sprite = image.subsurface(pygame.Rect(x, y, width, height))
    
    return sprite