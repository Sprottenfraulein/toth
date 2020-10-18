import sys
import pygame
import settings
import tools
import alarms
import maze
import over
import title
import hiscores
import random
import audio
import math


class Bigloop:
    def __init__(self):
        self.screen, self.canvas, self.fps, self.clock = tools.pygame_setup(pygame, settings)
        self.audio = audio.Audio(pygame)
        self.tileset, self.tiles, self.font = tools.data_load(pygame, settings)
        self.alarms = alarms.Alarms(settings.system['alarms']['counters'],
                                    settings.system['alarms']['timers'],
                                    settings.system['alarms']['steps'])
        self.hiscores = hiscores.Hiscores(settings)
        game_blocks = {
            'title': title.Title(settings.system['screen_width'], settings.system['screen_height'], self.hiscores, settings, pygame),
            'maze': maze.Maze(settings.system['view_width_sq'], settings.system['view_height_sq'], settings),
            'over': over.Over(settings.system['screen_width'], settings.system['screen_height'], self.hiscores, settings)
        }

        game_block = game_blocks['title']
        game_block.launch(self.audio, settings, None)
        while True:
            counters = self.alarms.tick()

            # Check app input events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        if self.audio.mute:
                            self.audio.mute = False
                            pygame.mixer.music.load(self.audio.bank_music[self.audio.music_playing])
                            pygame.mixer.music.play(-1)
                        else:
                            self.audio.mute = True
                            pygame.mixer.music.stop()
                game_block.events(pygame, event)

            # Game modules
            block_response = game_block.tick(counters, self.tiles, self.audio, settings)
            if block_response is not None:
                game_block = game_blocks[block_response[0]]
                game_block.launch(self.audio, settings, block_response[1])
                continue
            # print(self.clock.get_fps())

            # Scene drawing
            game_block.stage_display(self.tiles, self.font, self.canvas, counters, pygame, settings,
                                     mirror_h=False, mirror_v=False, palette=None)

            # Scaling and displaying a frame
            pygame.transform.scale(self.canvas, (
                settings.system['screen_width'] * settings.system['screen_scale'],
                settings.system['screen_height'] * settings.system['screen_scale']
            ), self.screen)
            pygame.display.flip()

            # self.clock.tick(settings.system['fps'])
            self.clock.tick_busy_loop(settings.system['fps'])
