import sys
import time
import pygame
from player import Player
from entities import PhysicsEntity
from spritesheet import Spritesheets
from map import TileMap
from SoundManager import SoundManager



#* means done
#TODO: 1. Movement(implement coyote time, dash, wall jummp :p)* 2. more sprites 3. Game map(atleast 2 levels) 4. Damage system 5.Award system 6.Score systm based on the time finished on a level and awards 7. animation 8. gammestates
#Coyote time is working but we just need to adjust it to what makes it feel better maybe asks someone to test it  
#MAKE SPRITESHEETS 128X128 PLEASE :p
#NEW - GAME CLASS IS RUNNING IN THE MAIN FILE, RESTRUCTURED THE FILES TO BE MORE ORGANIZED, CREATED A RESTART LEVEL FUNCTION
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
        self.info = pygame.display.Info()
        self.menu_start_time = 0
        self.menu_start_time
        self.is_menu_open = False
        self.paused = False
        

        #Game Variables (COMMENTED VARIABLES WERE USED IN EARLIER VERSIONS)
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
        self.spritesheets_path = "assets/Maps/GroundSet.png"
        self.spritesheets = Spritesheets(self.spritesheets_path)
        self.spritesheets.toJSON()   #CHANGES GroundSet.png to .json to go into the .json file to look for sprite data
        self.MapOne = 'assets/Maps/Map1.csv'
        self.map = TileMap(self.MapOne, self.spritesheets)
        #player_sprite_sheet = Spritesheets("assets/player.png")
       # self.cloud = Spritesheets(self.cloud_path).get_sprite(0,0,16,16)
        #self.background = pygame.image.load("assets/backgrounds/background-1.png").convert() 
        '''.convert() is used to convert pixel format to the one im using for the display of the game. 
        without it you would have to make pixel conversions everytime you blit a surfae onto the display which would be slower. TLDR; MAKES THE IMAGE FASTER TO LOAD'''
        #coins

        
        #Player
        self.player = Player()
        self.player.position.x, self.player.position.y = self.map.spawn_x, self.map.spawn_y #sets position of the player
        self.scroll = [0,0]



    def openMenu(self):
        self.menu_start_time = time.time()
        self.is_menu_open = True
        

    def closeMenu(self):
         self.start_time += (time.time() - self.menu_start_time)
         self.is_menu_open = False
         

    def drawMenu(self):
        pygame.draw.rect(self.window, (116, 102, 59), self.menu)
        pause_text = self.font.render("PAUSE", True, (255, 255, 255))
        unpause_text = self.font.render("PRESS ANY KEY TO RESUME", True, (255, 255, 255))
        quit_text = self.font.render("PRESS ESCAPE TO QUIT", True, (255, 255, 255))
        self.window.blit(pause_text, (0, self.height/2))
        self.window.blit(unpause_text, (0, self.height/2 + 20))
        self.window.blit(quit_text, (0, self.height/2 + 30))
        
    

    def run(self):
        #Game loop
        

        while self.running:
            framerate = self.clock.tick(self.targetFPS) #sets the Framerate
            self.dt = framerate * .001 * self.targetFPS #gets deltatime that makes the games speed consistent across different devices
            self.gameTime = time.time()-self.start_time
            seconds = int(self.gameTime)
            miliseconds = int((self.gameTime-seconds)*1000)
            self.GameTimeSTR = str(self.gameTime)
            
            if not self.is_menu_open:
                self.textSurface = self.font.render(f'Time:{seconds}.{miliseconds:02d}s', True, (0,0,0)) #sets up rendering how long the player is playing the game
            self.textSurface.set_alpha(255) #Makes it transparent
            self.fpsText = self.font.render(f'{self.clock}', True, (0,0,0))
            self.controlsText = self.font.render("Jump - Space    Left/Right - A/D", True, (255, 255, 153))
            self.scroll[0] += (self.player.rect.centerx - self.window.get_width() / 2 - self.scroll[0]) / 30 
            self.scroll[1] += (self.player.rect.centery - self.window.get_height()/2 - self.scroll[1]) / 30 
            render_scroll = (float(self.scroll[0]), float(self.scroll[1]))

            self.menu = pygame.Rect(0, self.height/2 , 200, 50)

     
           #CHECK PLAYER INPUTS
            for event in pygame.event.get():  
                if event.type  == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                    sys.exit()
                ########################### INPUTS #########################
                if event.type == pygame.KEYDOWN:
                    if self.is_menu_open and (event.key != pygame.K_ESCAPE):
                        self.closeMenu()
                    if event.key == pygame.K_a:
                        self.player.K_a = True 
                    elif event.key == pygame.K_d:
                        self.player.K_d = True
                        self.player.facingLeft = True
                    elif event.key == pygame.K_SPACE:
                        self.player.jump()
                    elif event.key == pygame.K_ESCAPE:
                            if self.is_menu_open:
                                 pygame.quit()
                                 sys.exit()
                            else:
                                 self.openMenu()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.player.K_a = False   
                    elif event.key == pygame.K_d:
                        self.player.K_d = False
                    elif event.key == pygame.K_SPACE:
                        if self.player.isJumping:
                            self.sound.play_sound('jump')  
                            self.player.velocity.y *= .25
                            self.player.isJumping = False
                        self.player.coyote_Time(self.dt)
                            
                
        


            #######UPDATING WINDOW##### (ORDER MATTERS)



            self.player.update(self.dt, self.map.tiles, self.map.spikes, self.map.flags)
            if self.player.isAlive == False: #checking player status in he future add game states 
                    Game.gameOver(self)
            if self.player.reset == True:
                    Game.restartLevel(self)
            if self.player.is_flag_touched == True:
                    map_filename = 'assets/maps/map2.csv'
                    Game.loadnewLevel(self, map_filename)
            self.window.fill((240, 255, 255))
           # self.window.blit(self.background,(0,0))
            #self.window.blit(self.background, (0, 0), (render_scroll[0], render_scroll[1], self.width, self.height))            
            self.player.draw(self.window,self.scroll)
            self.window.blit(self.textSurface, (self.window.get_width()/2,10))
            self.window.blit(self.fpsText, (0,0))
            self.window.blit(self.controlsText, (0, self.height - 50))
            if self.is_menu_open:
                self.drawMenu()
            self.map.draw_map(self.window,offset=render_scroll)
            
            #print(self.clock, '\n')
            #print("Hardware surface support:", self.info)
            pygame.display.update()
            #print(self.player.isAlive)


    def gameOver(self):
        print("Game over")
        pygame.quit()
       # print(self.gameTime)
        sys.exit()
    def restartLevel(self):
        #self.player.position.x, self.player.position.y = self.map.spawn_x, self.map.spawn_y
        Game().run()
    def loadnewLevel(self, new_map):
        self.map.spikes.clear()
        self.map.tiles.clear()
        self.map.flags.clear()
        self.map = TileMap(new_map, self.spritesheets)
        self.map_filename = new_map
        self.player.position.x, self.player.position.y = self.map.spawn_x, self.map.spawn_y
        self.player.isAlive = True
        self.player.reset = False
        self.player.is_flag_touched = False
        #self.player.update(self.dt, self.map.tiles, self.map.spikes,self.map.flags)

   





