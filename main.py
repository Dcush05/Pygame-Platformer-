import sys
import pygame
from player import Player
#from entities import PhysicsEntity
from util import Spritesheets
from map import TileMap
#TODO: 1. Movement(implement coyote time :p) 2. more sprites 3. Game map(atleast 2 levels) 4. Damage system 5.Award system
#MAKE SPRITESHEETS 128X128 PLEASE :p
# FIX MOVEMENT DIMWIT DONT PUSH UNTIL MOVEMENT IS FIXED 



class Game:
    def __init__(self):
        pygame.init()
        #Window variables
        self.width = 1280
        self.height = 720
        self.targetFPS = 60
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Project")


        #Game Variables (COMMENTED VARIABLES WERE USED IN EARLIER CODE)
        self.clock = pygame.time.Clock()
        self.running = True
        #self.posx = 8 
        #self.posy = 8
        #self.player = PhysicsEntity(self, 'entity',(self.posx,self.posy))
        #self.movementx = 10
        #self.movementy = 10
        #self.vel = 5

        #AUDIO - putt this as its own file in the future
        self.jump = pygame.mixer.Sound("assets/jump.wav")


        #map
        spritesheets = pygame.image.load("assets/testtile.png")
        self.map = TileMap('assets/TestMap.csv', spritesheets)
        player_sprite_sheet = Spritesheets("assets/player.png")


        #Player
        self.player = Player()
        self.player.position.x, self.player.position.y = self.map.spawn_x, self.map.spawn_y #sets position of the player
        
    
#OLD CODE BUT COULD BE USED IN THE FUTURE
    '''self.assets = {
           "entity":  player_sprite_sheet.get_sprite(0,0,16,16)  
        }'''
       

    '''img = pygame.image.load("assets/player.png")
        self.img = pygame.transform.scale(img,(300,300))
        self.img_pos = [16,16]
        self.movement = [False, False]'''
################################################################

    def run(self):
        #Game loop
        while self.running:
            framerate = self.clock.tick(60) #sets the Framerate
            dt = framerate * .001 * self.targetFPS #gets deltatime that makes the games speed consistent across different devices





           

           #CHECK PLAYER INPUTS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    sys.exit()
                ########################### INPUTS #########################
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.player.K_a = True  
                    elif event.key == pygame.K_d:
                        self.player.K_d = True
                        self.player.facingLeft = True
                    elif event.key == pygame.K_SPACE:
                        self.player.jump()



                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.player.K_a = False
                    elif event.key == pygame.K_d:
                        self.player.K_d = False
                    elif event.key == pygame.K_SPACE:
                        if self.player.isJumping:
                            self.player.velocity.y *= .25
                            self.player.isJumping = False
                            pygame.mixer.Sound.play(self.jump) #TESTING SOUND TO BE CHANGED IN THE FUTURE



                

                    
                   


                

            #######UPDATING WINDOW##### (ORDER MATTERS)
            self.player.update(dt)
            self.window.fill((240, 255, 255))
            self.player.draw(self.window)
            self.map.draw_map(self.window)
            print(self.clock)
            pygame.display.update()

            


            
                
                


Game().run()

