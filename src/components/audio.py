from asyncore import loop
from pygame import mixer

class AudioManager:

    def __init__(self):
        self.sounds = {
            'nourriture' : mixer.Sound("src/assets/Serpent_NOURRITURE.wav"),
            'perdu' : mixer.Sound("src/assets/Serpent_PERDU.wav"),
            'music' : mixer.Sound("src/assets/music.wav")
        }

    def play(self,name_audio):
        self.sounds[name_audio].play().set_volume(0.25)
        if name_audio == "music":
            self.sounds[name_audio].play(-1).set_volume(0.75)
