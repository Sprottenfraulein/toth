import random
import tools
import particle
import hero


class Title:
    def __init__(self, screen_width, screen_height, hiscores, settings, pygame):
        self.pygame = pygame
        self.space_width = screen_width
        self.space_height = screen_height
        self.hiscores = hiscores
        self.start = False
        self.page = 0
        self.sound = None

    def launch(self, audio, settings, summary):
        self.hiscores.hiscores_read(settings)

        self.player = hero.Hero(self.space_width // 2, self.space_height // 3 * 2)
        self.img_bg = self.pygame.image.load(settings.system['title_img'])
        self.img_bg.set_palette(settings.system['palettes'][0])
        audio.play_music('menu')

    def events(self, pygame, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_x or event.key == pygame.K_j:
                self.start = True
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                exit()
            if event.key == pygame.K_a or event.key == pygame.K_LEFT or \
                event.key == pygame.K_w or event.key == pygame.K_UP:
                self.page -= 1
                self.sound = 'shot_e'
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT or \
                event.key == pygame.K_s or event.key == pygame.K_DOWN:
                self.page += 1
                self.sound = 'shot_e'

    def tick(self, counters, tiles, audio, settings):
        if self.start:
            audio.bank_sound['wound_e'].play()
            self.start = False
            self.page = 0

            self.player.max_lives = 5
            self.player.lives = 3
            self.player.blade = 0
            self.player.shots = 3
            self.player.keys = 1
            self.player.gems = 0
            self.player.coins = 0
            self.player.score = 0
            self.player.dist = 0
            self.player.stage = 0
            self.player.boss_keys = 0
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
            return 'maze', {'hero': self.player}

        if self.sound is not None:
            audio.bank_sound[self.sound].play()
            self.sound = None

    def stage_display(self, tiles, font, canvas, counters, pygame, settings,
                      mirror_h=False, mirror_v=False, palette=None):
        canvas.blit(self.img_bg, (0, 0))

        text = 'BY CEREAL KILLER'
        tools.draw_text(self.space_width // 2 - len(text) * 8 // 2, 48, text, font, 6, pygame, canvas, settings)
        text = '2020'
        tools.draw_text(self.space_width // 2 - len(text) * 8 // 2, 56, text, font, 6, pygame, canvas, settings)

        # tools.draw_tile(canvas, pygame, settings, 152, 72, tiles['gem'], 0, 0,
        #                 settings.system['palettes'][1])
        # tools.draw_tile(canvas, pygame, settings, 152, 84, tiles['coin'], 0, 0,
        #                 settings.system['palettes'][2])
        if self.page == 9:
            self.page = 0
        elif self.page == -1:
            self.page = 8

        if self.page != 0:
            canvas.fill((120, 0, 0), (0, 72, self.space_width, 128))
        if self.page == 0:
            text = 'ARROW KEYS FOR HELP'
            tools.draw_text(self.space_width // 2 - len(text) * 8 // 2, 180, text, font, 6, pygame, canvas, settings)
        elif self.page == 1:
            text = 'STORY:'
            tools.draw_text(self.space_width // 2 - len(text) * 8 // 2, 76, text, font, 4, pygame, canvas, settings)
            text = 'YOU ARE A HERALD.'
            tools.draw_text(self.space_width // 2 - len(text) * 8 // 2, 88, text, font, 6, pygame, canvas, settings)
            text = 'YOUR AIM IS TO SAFELY TRAVERSE'
            tools.draw_text(self.space_width // 2 - len(text) * 8 // 2, 96, text, font, 6, pygame, canvas, settings)
            text = 'THROUGH THE GOBLINS VALLEY'
            tools.draw_text(self.space_width // 2 - len(text) * 8 // 2, 104, text, font, 6, pygame, canvas, settings)
            text = 'OR MAKE IT AS FAR AS POSSIBLE.'
            tools.draw_text(self.space_width // 2 - len(text) * 8 // 2, 112, text, font, 6, pygame, canvas, settings)

            text = 'KEYBOARD CONTROLS:'
            tools.draw_text(self.space_width // 2 - len(text) * 8 // 2, 128, text, font, 4, pygame, canvas, settings)
            text = 'RUN FORWARD:  UP,    W'
            tools.draw_text(40, 140, text, font, 6, pygame, canvas, settings)
            text = 'RUN BACKWARD: DOWN,  S'
            tools.draw_text(40, 148, text, font, 6, pygame, canvas, settings)
            text = 'RUN LEFT:     LEFT,  A'
            tools.draw_text(40, 156, text, font, 6, pygame, canvas, settings)
            text = 'RUN RIGHT:    RIGHT, D'
            tools.draw_text(40, 164, text, font, 6, pygame, canvas, settings)
            text = 'SWING SWORD:  X,     J'
            tools.draw_text(40, 180, text, font, 6, pygame, canvas, settings)
            text = 'SHOOT BOW:    Z,     K'
            tools.draw_text(40, 188, text, font, 6, pygame, canvas, settings)
            pass

        elif self.page == 2:
            text = 'HAZARDS AND HOSTILES:'
            tools.draw_text(self.space_width // 2 - len(text) * 8 // 2, 76, text, font, 6, pygame, canvas, settings)

            text = '-GOBLIN-'
            tools.draw_text(56, 88, text, font, 4, pygame, canvas, settings)
            text = 'PATROLS SURROUNDINGS,'
            tools.draw_text(56, 96, text, font, 6, pygame, canvas, settings)
            text = 'SHOOTS ARROWS ON SIGHT.'
            tools.draw_text(56, 104, text, font, 6, pygame, canvas, settings)
            tools.draw_tile(canvas, pygame, settings, 32, 92, tiles['goblin_s'], 0, 0, settings.system['palettes'][10])

            text = '-PROJECTILE-'
            tools.draw_text(56, 116, text, font, 4, pygame, canvas, settings)
            text = 'GOBLINS ARROW,'
            tools.draw_text(56, 124, text, font, 6, pygame, canvas, settings)
            text = 'LOSE 1 HEART ON HIT.'
            tools.draw_text(56, 132, text, font, 6, pygame, canvas, settings)
            tools.draw_tile(canvas, pygame, settings, 32, 120, tiles['proj_nw'], 0, 0, settings.system['palettes'][2])

            text = '-PIT-'
            tools.draw_text(56, 144, text, font, 4, pygame, canvas, settings)
            text = 'BOTTOMLESS TRAP,'
            tools.draw_text(56, 152, text, font, 6, pygame, canvas, settings)
            text = 'VERY DANGEROUS!AVOID!'
            tools.draw_text(56, 160, text, font, 6, pygame, canvas, settings)
            tools.draw_tile(canvas, pygame, settings, 32, 148, tiles['pit'], 0, 0, settings.system['palettes'][2])

            text = '-FIRE-'
            tools.draw_text(56, 172, text, font, 4, pygame, canvas, settings)
            text = 'HOT FLAME, BE CAREFUL!'
            tools.draw_text(56, 180, text, font, 6, pygame, canvas, settings)
            text = 'LOSE 1 HEART ON HIT.'
            tools.draw_text(56, 188, text, font, 6, pygame, canvas, settings)
            tools.draw_tile(canvas, pygame, settings, 32, 176, tiles['fire'], 0, 0, settings.system['palettes'][3])

        elif self.page == 3:
            text = 'EQUIPMENT AND LIFE:'
            tools.draw_text(self.space_width // 2 - len(text) * 8 // 2, 76, text, font, 6, pygame, canvas, settings)

            text = '-ARROW-'
            tools.draw_text(56, 88, text, font, 4, pygame, canvas, settings)
            text = 'AMMO FOR YOUR BOW,'
            tools.draw_text(56, 96, text, font, 6, pygame, canvas, settings)
            text = 'MAX 5 ARROWS.'
            tools.draw_text(56, 104, text, font, 6, pygame, canvas, settings)
            tools.draw_tile(canvas, pygame, settings, 32, 92, tiles['arrow'], 0, 0, settings.system['palettes'][2])

            text = '-KEY-'
            tools.draw_text(56, 116, text, font, 4, pygame, canvas, settings)
            text = 'OPEN LOCKED CHESTS'
            tools.draw_text(56, 124, text, font, 6, pygame, canvas, settings)
            text = 'AND DOORS,MAX 5 KEYS.'
            tools.draw_text(56, 132, text, font, 6, pygame, canvas, settings)
            tools.draw_tile(canvas, pygame, settings, 32, 120, tiles['key'], 0, 0, settings.system['palettes'][4])

            text = '-LOCK-'
            tools.draw_text(56, 144, text, font, 4, pygame, canvas, settings)
            text = 'REQUIRES KEY TO REMOVE,'
            tools.draw_text(56, 152, text, font, 6, pygame, canvas, settings)
            text = 'FOUND ON DOORS, CHESTS'
            tools.draw_text(56, 160, text, font, 6, pygame, canvas, settings)
            tools.draw_tile(canvas, pygame, settings, 32, 148, tiles['lock'], 0, 0, settings.system['palettes'][7])

            text = '-HEART-'
            tools.draw_text(56, 172, text, font, 4, pygame, canvas, settings)
            text = 'WHEN YOU LOSE ALL'
            tools.draw_text(56, 180, text, font, 6, pygame, canvas, settings)
            text = 'IT IS GAME OVER.'
            tools.draw_text(56, 188, text, font, 6, pygame, canvas, settings)
            tools.draw_tile(canvas, pygame, settings, 32, 176, tiles['heart'], 0, 0, settings.system['palettes'][5])

        elif self.page == 4:
            text = 'FOOD AND POTIONS:'
            tools.draw_text(self.space_width // 2 - len(text) * 8 // 2, 76, text, font, 6, pygame, canvas, settings)

            text = '-FRUIT-'
            tools.draw_text(56, 88, text, font, 4, pygame, canvas, settings)
            text = 'RESTORE 1 HEART'
            tools.draw_text(56, 96, text, font, 6, pygame, canvas, settings)
            text = 'OR 50 BONUS PTS.'
            tools.draw_text(56, 104, text, font, 6, pygame, canvas, settings)
            tools.draw_tile(canvas, pygame, settings, 32, 92, tiles['apple'], 0, 0, settings.system['palettes'][8])

            text = '-CHICKEN-'
            tools.draw_text(56, 116, text, font, 4, pygame, canvas, settings)
            text = 'RESTORE 2 HEARTS,'
            tools.draw_text(56, 124, text, font, 6, pygame, canvas, settings)
            text = 'OR 100 BONUS PTS.'
            tools.draw_text(56, 132, text, font, 6, pygame, canvas, settings)
            tools.draw_tile(canvas, pygame, settings, 32, 120, tiles['chick'], 0, 0, settings.system['palettes'][2])

            text = '-MEAT-'
            tools.draw_text(56, 144, text, font, 4, pygame, canvas, settings)
            text = 'RESTORE FULL HEARTS,'
            tools.draw_text(56, 152, text, font, 6, pygame, canvas, settings)
            text = 'OR 500 BONUS PTS.'
            tools.draw_text(56, 160, text, font, 6, pygame, canvas, settings)
            tools.draw_tile(canvas, pygame, settings, 32, 148, tiles['meat'], 0, 0, settings.system['palettes'][5])

            text = '-POTION-'
            tools.draw_text(56, 172, text, font, 4, pygame, canvas, settings)
            text = 'CREATE UNKNOWN'
            tools.draw_text(56, 180, text, font, 6, pygame, canvas, settings)
            text = 'MAGICAL EFFECT.'
            tools.draw_text(56, 188, text, font, 6, pygame, canvas, settings)
            tools.draw_tile(canvas, pygame, settings, 32, 176, tiles['potion'], 0, 0, settings.system['palettes'][7])

        elif self.page == 5:
            text = 'BONUS ITEMS:'
            tools.draw_text(self.space_width // 2 - len(text) * 8 // 2, 76, text, font, 6, pygame, canvas, settings)

            text = '-COIN-'
            tools.draw_text(56, 88, text, font, 4, pygame, canvas, settings)
            text = 'GIVES 100 BONUS PTS.'
            tools.draw_text(56, 96, text, font, 6, pygame, canvas, settings)
            text = ' '
            tools.draw_text(56, 104, text, font, 6, pygame, canvas, settings)
            tools.draw_tile(canvas, pygame, settings, 32, 92, tiles['coin'], 0, 0, settings.system['palettes'][2])

            text = '-GEM-'
            tools.draw_text(56, 116, text, font, 4, pygame, canvas, settings)
            text = 'GIVES 1000 BONUS PTS.'
            tools.draw_text(56, 124, text, font, 6, pygame, canvas, settings)
            text = ' '
            tools.draw_text(56, 132, text, font, 6, pygame, canvas, settings)
            tools.draw_tile(canvas, pygame, settings, 32, 120, tiles['gem'], 0, 0, settings.system['palettes'][1])

            text = '-SKULL-'
            tools.draw_text(56, 144, text, font, 4, pygame, canvas, settings)
            text = 'REVEAL LOOT ITEM'
            tools.draw_text(56, 152, text, font, 6, pygame, canvas, settings)
            text = 'IF SLICED WITH SWORD.'
            tools.draw_text(56, 160, text, font, 6, pygame, canvas, settings)
            tools.draw_tile(canvas, pygame, settings, 32, 148, tiles['skull1'], 0, 0, settings.system['palettes'][7])

        elif self.page == 6:
            text = 'SUPER HERALD:'
            tools.draw_text(self.space_width // 2 - len(text) * 8 // 2, 76, text, font, 6, pygame, canvas, settings)

            text = '-DO NOT STOP-'
            tools.draw_text(56, 88, text, font, 4, pygame, canvas, settings)
            text = 'KEEP RUNNING TO GAIN'
            tools.draw_text(56, 96, text, font, 6, pygame, canvas, settings)
            text = '*2 SCORE MULTIPLIER'
            tools.draw_text(56, 104, text, font, 6, pygame, canvas, settings)
            tools.draw_tile(canvas, pygame, settings, 32, 92, tiles['hero_s'], 0, 0, settings.system['palettes'][4])

            text = '-BEING SUPERB-'
            tools.draw_text(56, 116, text, font, 4, pygame, canvas, settings)
            text = 'BE SAFE AND SCORING'
            tools.draw_text(56, 124, text, font, 6, pygame, canvas, settings)
            text = 'TO STAY SUPER HERALD.'
            tools.draw_text(56, 132, text, font, 6, pygame, canvas, settings)
            tools.draw_tile(canvas, pygame, settings, 32, 120, tiles['coin'], 0, 0, settings.system['palettes'][2])

        elif self.page == 7:
            text = 'USEFUL OBJECTS:'
            tools.draw_text(self.space_width // 2 - len(text) * 8 // 2, 76, text, font, 6, pygame, canvas, settings)

            text = '-TREE-'
            tools.draw_text(56, 88, text, font, 4, pygame, canvas, settings)
            text = 'CHOP IT TO GET TIMBER'
            tools.draw_text(56, 96, text, font, 6, pygame, canvas, settings)
            text = 'OR TO MAKE THROUGH.'
            tools.draw_text(56, 104, text, font, 6, pygame, canvas, settings)
            tools.draw_tile(canvas, pygame, settings, 32, 92, tiles['tree'], 0, 0, settings.system['palettes'][1])

            text = '-LOG-'
            tools.draw_text(56, 116, text, font, 4, pygame, canvas, settings)
            text = 'SOMETIMES TURNS'
            tools.draw_text(56, 124, text, font, 6, pygame, canvas, settings)
            text = 'INTO ARROW WHEN CUT.'
            tools.draw_text(56, 132, text, font, 6, pygame, canvas, settings)
            tools.draw_tile(canvas, pygame, settings, 32, 120, tiles['log'], 0, 0, settings.system['palettes'][2])

            text = '-GRASS-'
            tools.draw_text(56, 144, text, font, 4, pygame, canvas, settings)
            text = 'SOMETIMES TURNS'
            tools.draw_text(56, 152, text, font, 6, pygame, canvas, settings)
            text = 'INTO FRUIT WHEN CUT.'
            tools.draw_text(56, 160, text, font, 6, pygame, canvas, settings)
            tools.draw_tile(canvas, pygame, settings, 32, 148, tiles['grass'], 0, 0, settings.system['palettes'][1])

            text = '-ROCK-'
            tools.draw_text(56, 172, text, font, 4, pygame, canvas, settings)
            text = 'STRONG BUT NOT'
            tools.draw_text(56, 180, text, font, 6, pygame, canvas, settings)
            text = 'UNBREAKABLE.'
            tools.draw_text(56, 188, text, font, 6, pygame, canvas, settings)
            tools.draw_tile(canvas, pygame, settings, 32, 176, tiles['rock'], 0, 0, settings.system['palettes'][7])

        if self.page == 8:
            text = 'TOP AGENTS:'
            tools.draw_text(self.space_width // 2 - len(text) * 8 // 2, 84, text, font, 6, pygame, canvas, settings)
            for i in range(0, min(len(self.hiscores.hiscores), 8)):
                if i == 2:
                    palette = 2
                elif i == 1:
                    palette = 1
                elif i == 0:
                    palette = 4
                else:
                    palette = 6
                text = str(i + 1) + ' ' + str(self.hiscores.hiscores[i][0]) + ' ' + self.hiscores.hiscores[i][1]
                tools.draw_text(72, 96 + i * 12, text, font, palette, pygame, canvas, settings)

        text = 'HOW TO PLAY:LEFT OR RIGHT'
        tools.draw_text(self.space_width // 2 - len(text) * 8 // 2, self.space_height - 24, text, font, 6, pygame,
                        canvas, settings)
        text = 'START: ENTER,QUIT:ESCAPE'
        tools.draw_text(self.space_width // 2 - len(text) * 8 // 2, self.space_height - 16, text, font, 6, pygame, canvas, settings)