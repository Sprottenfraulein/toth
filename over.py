import random
import tools
import particle


class Over:
    def __init__(self, screen_width, screen_height, hiscores, settings):
        self.space_width = screen_width
        self.space_height = screen_height
        self.hiscores = hiscores
        self.score_place = 0
        self.restart = False
        self.quit = False

    def launch(self, audio, settings, summary):
        self.player = summary['hero']
        self.score_place = self.hiscores.hiscore_add(self.player.score)
        audio.play_music('menu')

    def events(self, pygame, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.restart = True
            elif event.key == pygame.K_ESCAPE:
                self.quit = True
            elif event.key == pygame.K_BACKSPACE:
                self.hiscores.hiscores[self.score_place][1] = self.hiscores.hiscores[self.score_place][1][:-1]
            if self.score_place < 8:
                if 65 <= event.key <= 90 or 97 <= event.key <= 122:
                    self.hiscores.hiscores[self.score_place][1] += pygame.key.name(event.key).upper()
                elif 48 <= event.key <= 57 or 44 <= event.key <= 46 or event.key in (33, 58, 63):
                    self.hiscores.hiscores[self.score_place][1] += pygame.key.name(event.key)

    def tick(self, counters, tiles, audio, settings):
        if self.restart:
            self.restart = False

            self.player.max_lives = 3
            self.player.lives = 3
            self.player.blade = 0
            self.player.shots = 3
            self.player.keys = 1
            self.player.gems = 0
            self.player.coins = 0
            self.player.score = 0
            self.player.dist = 0
            self.player.stage = 0
            self.multiplier = 1
            self.multi_limit = 60
            self.multi_level = 0

            self.player.direction = 0
            self.player.walking = False
            self.player.slicing = 0
            self.player.shotting = False
            self.player.anim_frame = 0
            self.player.visible = True
            self.player.blink = 0

            self.hiscores.hiscores_save(settings)
            return 'maze', {'hero': self.player}
        if self.quit:
            self.quit = False

            self.player.max_lives = 3
            self.player.lives = 3
            self.player.blade = 0
            self.player.shots = 3
            self.player.keys = 1
            self.player.gems = 0
            self.player.coins = 0
            self.player.score = 0
            self.player.dist = 0
            self.player.stage = 0
            self.multiplier = 1
            self.multi_limit = 60
            self.multi_level = 0

            self.player.direction = 0
            self.player.walking = False
            self.player.slicing = 0
            self.player.shotting = False
            self.player.anim_frame = 0
            self.player.visible = True
            self.player.blink = 0

            self.hiscores.hiscores_save(settings)
            return 'title', {'hero': self.player}

    def stage_display(self, tiles, font, canvas, counters, pygame, settings,
                      mirror_h=False, mirror_v=False, palette=None):
        canvas.fill(settings.system['color_bg'])

        text = 'GAME OVER'
        tools.draw_text(self.space_width // 2 - len(text) * 8 // 2, 36, text, font, 6, pygame, canvas, settings)

        text = 'YOUR SCORE:' + str(self.player.score) + ' PTS'
        tools.draw_text(self.space_width // 2 - len(text) * 8 // 2, 52, text, font, 6, pygame, canvas, settings)

        text = 'TRAVELLED DISTANCE:' + str(self.player.dist) + ' M'
        tools.draw_text(24, 64, text, font, 6, pygame, canvas, settings)

        text = '*' + str(self.player.gems)
        tools.draw_text(168, 76, text, font, 6, pygame, canvas, settings)

        text = '*' + str(self.player.coins)
        tools.draw_text(168, 88, text, font, 6, pygame, canvas, settings)

        tools.draw_tile(canvas, pygame, settings, 152, 72, tiles['gem'], 0, 0,
                        settings.system['palettes'][1])
        tools.draw_tile(canvas, pygame, settings, 152, 84, tiles['coin'], 0, 0,
                        settings.system['palettes'][2])

        text = 'TOP AGENTS:'
        tools.draw_text(self.space_width // 2 - len(text) * 8 // 2, 104, text, font, 6, pygame, canvas, settings)
        for i in range(0, min(len(self.hiscores.hiscores), 8)):
            if i == 2:
                palette = 2
            elif i == 1:
                palette = 1
            elif i == 0:
                palette = 4
            else:
                palette = 6
            if i == self.score_place:
                if counters[0] == 0:
                    text = str(i + 1) + ':' + str(self.hiscores.hiscores[i][0])
                    if self.hiscores.hiscores[i][1] == '':
                        text += ' -INPUT NAME-'
                    else:
                        text += (' ' + self.hiscores.hiscores[i][1])
                    tools.draw_text(72, 116 + i * 12, text, font, palette, pygame, canvas, settings)
            else:
                text = str(i + 1) + ' ' + str(self.hiscores.hiscores[i][0]) + ' ' + self.hiscores.hiscores[i][1]
                tools.draw_text(72, 116 + i * 12, text, font, palette, pygame, canvas, settings)

        text = 'RESTART: ENTER, QUIT: ESC'
        tools.draw_text(self.space_width // 2 - len(text) * 8 // 2, self.space_height - 16, text, font, 6, pygame, canvas, settings)
