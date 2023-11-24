import sys
import pygame
from entities import PhysicsEntity
from util import load_image, get_sprite

#TODO: 1. Movement(implement coyote time :p) 2. more sprites 3. Game map(atleast 2 levels) 4. Damage system 5. Award system 



class Game:
    def __init__(self):
        pygame.init()
        #resolution
        width = 1280
        height = 720
        self.loop = True
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Project")
        self.clock = pygame.time.Clock()
        self.posx = 8 
        self.posy = 8
        self.player = PhysicsEntity(self, 'player',(self.posx,self.posy), (16,16) )
        self.movementx = 10
        self.movementy = 10
        self.vel = 5
        sprite_sheet = load_image("assets/player.png")
    

        self.assets = {
            'player': get_sprite(sprite_sheet,0,0,16,16)  
        } 
        #get_sprite makes you able to find the specific sprite you want to use from your sprite sheet instead of having multiple sprite 
        #files we could put all sprites related to each othher on their own spritesheet'''
         





    '''img = pygame.image.load("assets\player.png")
        self.img = pygame.transform.scale(img,(300,300))
        self.img_pos = [16,16]
        self.movement = [False, False]'''
        

    def run(self):
        #Game loop
        while self.loop:
            self.clock.tick(60) #sets the Framerate

            #self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5
            #self.window.blit(self.img, self.img_pos)
            self.player.update((self.movementx - self.movementy,0))
            self.player.render(self.window)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.loop = False
                    sys.exit()
                #Scuffed movement change if possible
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        self.movementx += self.vel
                    elif event.key == pygame.K_a:
                        self.movementx -= self.vel
                    

            # Check for key releases
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        movement = 0
                        #self.movementy = 0

            pygame.display.update() #every game update or render have to be under update
            self.window.fill((240,255,255)) #changes the color of the background to the window
            print(self.clock , "\n")
 


Game().run()