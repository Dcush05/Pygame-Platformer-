import sys
import pygame
import time

from player import Player
#from entities import PhysicsEntity - future use
from util import Spritesheets
from map import TileMap
from SoundManager import SoundManager



#* means done
#TODO: 1. Movement(implemented coyote time :p)* 2. more sprites 3. Game map(atleast 2 levels) 4. Damage system 5.Award system 6.Score systm based on the time finished on a level and awards
#Coyote time is working but we just need to adjust it to what makes it feel better maybe asks someone to test it
#MAKE SPRITESHEETS 128X128 PLEASE :p
#NEW - BETTER MAP AND MAP RENDERER, BETTER MOVEMENT(COYOTE TIME), SOUND MANAGER CLASS, ABLE TO PARSE SPRITES FROM A .JSON FILE(not for player yet idk), created a dat folder for the future
#Some variables are going to be used in the future, for the next commits i will try to remove some code that are old and dont make sense. For now I will keep them so you guys understand the vision.
#NOTE: AS OF RIGHT NOW PLEASE DO NOT TOUCH .TSJ , .TMX, .JSON, .CSV FILES AS IT WILL ALTER THE WAY THE MAP LOOKS OR THE DATA FOR THE SPRITES WHICH WILL RESULT ALTER THE WAY THE SPRITES LOOK




class Game:
    def __init__(self):
        pygame.init()
        #Window variables
        self.width = 1280
        self.height = 720
        self.targetFPS = 60
        self.window = pygame.display.set_mode((self.width, self.height))
        #self.fullscreen = False
        pygame.display.set_caption("Project")
        self.font = pygame.font.Font("assets/fonts/PixelFont.ttf") #sets up font to print text on the window
        




        #Game Variables (COMMENTED VARIABLES WERE USED IN EARLIER CODE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.start_time=time.time() #gives time

        
        #self.posx = 8 
        #self.posy = 8
        #self.player = PhysicsEntity(self, 'entity',(self.posx,self.posy))
        #self.movementx = 10
        #self.movementy = 10
        #self.vel = 5

        #AUDIO - putt this as its own file in the future
        self.sound = SoundManager()

        #map
        spritesheets_path = "assets/Maps/GroundSet.png"
        spritesheets = Spritesheets(spritesheets_path)
        spritesheets.toJSON()   #CHANGES GroundSet.png to .json to go into the .json file to look for sprite data
        self.map = TileMap('assets/Maps/MapOne.csv', spritesheets)
        #player_sprite_sheet = Spritesheets("assets/player.png")


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
    ##############################################################

    def run(self):
        #Game loop
        while self.running:
            framerate = self.clock.tick(60) #sets the Framerate
            dt = framerate * .001 * self.targetFPS #gets deltatime that makes the games speed consistent across different devices
            self.gameTime = time.time()-self.start_time
            seconds = int(self.gameTime)
            miliseconds = int((self.gameTime-seconds)*1000)
            self.GameTimeSTR = str(self.gameTime)
            self.textSurface = self.font.render(f'Time:{seconds}.{miliseconds:02d}s', True, (0,0,0)) #sets up rendering how long the player is playing the game
            self.textSurface.set_alpha(255) #Makes it transparent
            self.fpsText = self.font.render(f'{self.clock}', True, (0,0,0))






           

           #CHECK PLAYER INPUTS
            for event in pygame.event.get():  
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
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
                            self.sound.play_sound('jump')  
                            self.player.velocity.y *= .25
                            self.player.coyoteTime = self.player.maxCoyote_Time #Gives player more time to jump off the edge of a platformer instead of being exact
                            self.player.isJumping = False
                            
                self.player.coyote_Time(dt)
                    
                    






                


                

                    
                   


                

            #######UPDATING WINDOW##### (ORDER MATTERS)
            self.player.update(dt, self.map.tiles)
            if self.player.isAlive == False: #checking player status in he future add game states 
                    Game.gameOver(self)
            self.window.fill((240, 255, 255))
            self.player.draw(self.window)
            self.window.blit(self.textSurface, (self.window.get_width()/2,10))
            self.window.blit(self.fpsText, (0,0))
            self.map.draw_map(self.window)
            print(self.clock, '\n')
            pygame.display.update()



    def gameOver(self):
        print("Game over")
        pygame.quit()
        sys.exit()

            


            
                
                


Game().run()

