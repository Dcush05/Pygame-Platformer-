import pygame
from spritesheet import Spritesheets
from map import TileMap


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Spritesheets("assets/player.png").get_sprite(0,0,16,16) 
        self.image = pygame.transform.scale(self.image, (25,25))
        self.rect = self.image.get_rect() 
        self.boundingBox = self.rect
        #self.outLine = self.rect.inflate(6,6)
        self.green = (100, 255, 0, 120)
        self.K_a = False
        self.K_d = False
        self.K_Space = False
        self.facingLeft = False
        self.spritefacingLeft = pygame.transform.flip(self.image, False, True)
        self.isJumping = False
        self.onGround = False
        self.isAlive = True
        self.points = 0
        self.maxCoyote_Time = .9
        self.coyoteTime = 0
        self.gravity = .35
        self.friction = -.12
        self.position, self.velocity = pygame.math.Vector2(0, 0), pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, self.gravity)


    def draw(self, display, offset=(0,0)):
        #pygame.draw.rect(display, self.green, self.boundingBox) #DISPLAYS HITBOX
        #pygame.display.set_colorkey(self.image, [255,0,255], pygame.RLEACCEL)
        display.blit(self.image, (self.rect.x-offset[0], self.rect.y-offset[1]))
        

    def update(self, dt, tiles, spike, flag):
        '''updates player'''
        self.horizontal_movement(dt)
        self.checkCollisions_X(tiles, flag)
        self.vertical_movement(dt)
        self.checkCollisions_Y(tiles, flag)
        self.spikeCollision(spike)
        #self.flagCollision(flag)
         

#PLAYER MOVEMENT CALCULATIONS - Mario like movement
    def horizontal_movement(self, dt):
        self.acceleration.x = 0
        if self.K_a:
            self.acceleration.x -= .3
        elif self.K_d:
            self.acceleration.x += .3
        self.acceleration.x += self.velocity.x * self.friction
        self.velocity.x += self.acceleration.x * dt
        self.limit_velocity(4)
        self.position.x += self.velocity.x * dt + (self.acceleration.x * .5) * (dt * dt)
        self.rect.x = self.position.x
    def coyote_Time(self, dt):
        self.coyoteTime = max(0, self.maxCoyote_Time- dt)

    def vertical_movement(self, dt):
        self.velocity.y += self.acceleration.y * dt
        if self.velocity.y > 7: self.velocity.y = 7
        if self.K_Space == True:
            self.coyoteTime = self.maxCoyote_Time
        
        self.position.y += self.velocity.y * dt + (self.acceleration.y * .5) * (dt * dt)
        if self.position.y > 1080: 
            self.onGround = True
            self.velocity.y = 0
            self.position.y = 1080 
        self.rect.bottom = self.position.y

    def limit_velocity(self, max_vel):
        min(-max_vel, max(self.velocity.x, max_vel))
        if abs(self.velocity.x) < .01: self.velocity.x = 0

    def jump(self):
        if self.onGround or self.coyoteTime > 0:
            self.isJumping = True
            self.velocity.y -= 8
            self.onGround = False
            self.coyoteTime = 0
    
    def getHits(self, tiles):
        hits = []
        for tile in tiles:
            if self.boundingBox.colliderect(tile):
                hits.append(tile)
        return hits

    def spikeCollision(self, spikes):
        hits = []
        for spike in spikes:
            if self.boundingBox.colliderect(spike):
                hits.append(spike)
                print("hit spike")
                self.isAlive =  False
        return hits
    def flagCollision(self, flags):
        hits = []
        for flag in flags:
            if self.boundingBox.colliderect(flag):
                hits.append(flag)
                self.IsAlive = False
        return hits
    
    



    def checkCollisions_X(self, tiles, flags):
        collisions = self.getHits(tiles)
        flagCollision = self.flagCollision(flags)
        for tile in collisions:
            if self.velocity.x > 0: #Collision to the right
                self.position.x = tile.rect.left - self.rect.w
                self.rect.x = self.position.x
                #print("hit right\n")
            elif self.velocity.x < 0: #Collision to the left
                self.position.x = tile.rect.right
                self.rect.x = self.position.x
        for flag in flagCollision:
            self.isAlive = False
      
            

            
    def checkCollisions_Y(self, tiles, flags):
        self.onGround = False
        self.rect.bottom += 1
        collisions = self.getHits(tiles)
        flagCollision = self.flagCollision(flags)
        for tile in collisions:
            if self.velocity.y > 0: #Collision to the top
                self.onGround = True
                self.isJumping = False
                self.velocity.y = 0
                self.position.y = tile.rect.top
                self.rect.bottom = self.position.y
                #print("hitting bottom\n")
            elif self.velocity.y < 0: #Collision to the bottom
                self.velocity.y = 0
                self.position.y = tile.rect.bottom + self.rect.height
                self.rect.bottom = self.position.y
        
        for flag in flagCollision:
            self.isAlive = False
            
                





