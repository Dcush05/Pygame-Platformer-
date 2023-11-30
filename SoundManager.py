import pygame



class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {"jump":pygame.mixer.Sound("assets/sounds/jump.wav")}


    def play_sound(self, soundName):
        if soundName in self.sounds:
            self.sounds[soundName].play()
        
