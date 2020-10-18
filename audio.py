import os

class Audio:
    def __init__(self, pygame):
        self.pygame = pygame
        self.bank_sound = {
            'arrow': pygame.mixer.Sound('data/arrow.wav'),
            'clank': pygame.mixer.Sound('data/clank.wav'),
            'crack': pygame.mixer.Sound('data/crack.wav'),
            'multi': pygame.mixer.Sound('data/multi.wav'),
            'coin': pygame.mixer.Sound('data/coin.wav'),
            'drink': pygame.mixer.Sound('data/drink.wav'),
            'eat': pygame.mixer.Sound('data/eat.wav'),
            'gem': pygame.mixer.Sound('data/gem.wav'),
            'key': pygame.mixer.Sound('data/key.wav'),
            'open': pygame.mixer.Sound('data/open.wav'),
            'pierce': pygame.mixer.Sound('data/pierce.wav'),
            'shot': pygame.mixer.Sound('data/shot.wav'),
            'shot_e': pygame.mixer.Sound('data/shot_e.wav'),
            'slice': pygame.mixer.Sound('data/slice.wav'),
            'step': pygame.mixer.Sound('data/step.wav'),
            'unlock': pygame.mixer.Sound('data/unlock.wav'),
            'wound': pygame.mixer.Sound('data/wound.wav'),
            'wound_e': pygame.mixer.Sound('data/wound_e.wav')
        }

        self.bank_music = {
            'menu': 'data/just_a_jiff.ogg',
            'stage': 'data/among_the_trees.ogg',
            'under': 'data/descent.ogg',
            'tense': 'data/fairy_lights.ogg'
        }
        self.music_playing = None
        self.mute = False

    def play_music(self, name):
        if not self.mute and self.music_playing is not name:
            self.pygame.mixer.music.load(self.bank_music[name])
            self.pygame.mixer.music.play(-1)
        self.music_playing = name
