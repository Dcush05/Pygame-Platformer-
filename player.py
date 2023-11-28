import pygame
from util import Spritesheets

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Spritesheets("assets/player.png").get_sprite((26,26),0,0,16,16) #gets specific sprite coordinates in a spritesheet to find the sprite
        self.rect = self.image.get_rect()
        self.K_a = False
        self.K_d = False
        self.facingLeft = False
        self.isJumping = False
        self.onGround = False
        self.gravity = .35
        self.friction = -.12
        self.position, self.velocity = pygame.math.Vector2(0, 0), pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, self.gravity)

    def draw(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, dt):
        self.horizontal_movement(dt)
        self.vertical_movement(dt)


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

    def vertical_movement(self, dt):
        self.velocity.y += self.acceleration.y * dt
        if self.velocity.y > 7: self.velocity.y = 7
        self.position.y += self.velocity.y * dt + (self.acceleration.y * .5) * (dt * dt)
        if self.position.y > 128: #DETERMINES HOW FAR IT DROPS 
            self.onGround = True
            self.velocity.y = 0
            self.position.y = 128  #MUST BE THE SAME SO IT DOESNT SEEM LIKE THE PLAYER IS TELEPORTING
        self.rect.bottom = self.position.y


    def limit_velocity(self, max_vel):
        min(-max_vel, max(self.velocity.x, max_vel))
        if abs(self.velocity.x) < .01: self.velocity.x = 0

    def jump(self):
        if self.onGround:
            self.isJumping = True
            self.velocity.y -= 8
            self.onGround = False
