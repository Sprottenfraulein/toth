import random
import tools
import hero
import particle
import goblin
import missile
import audio


class Maze:
    def __init__(self, view_width_sq, view_height_sq, settings):
        self.square_size = 16

        self.space_width = view_width_sq
        self.space_height = view_height_sq + 1

        self.space_a = []
        self.space_b = []
        for i in range(0, self.space_height):
            self.space_a.append([None for j in range(0, self.space_width)])
            self.space_b.append([None for j in range(0, self.space_width)])

        self.onscreen, self.buff = self.space_a, self.space_b
        self.offset_v = 0
        self.pixel_offset_v = self.square_size * -1

        self.player = hero.Hero(self.space_width // 2 * self.square_size, self.space_height // 3 * 2 * self.square_size)
        self.ui_keys = True
        self.ui_lives = True
        self.ui_shots = True
        self.ui_gems = True
        self.ui_coins = True
        self.ui_score = True
        self.ui_dist = True

        self.particles = []
        self.encounters = []
        self.missiles = []

        self.kill_timer = None
        self.pause = False

    def build_square(self, space, top, left, bottom, right, build_stack, solid, percents=100):
        if solid:
            for i in range(left, right + 1):
                for j in range(top, bottom + 1):
                    if percents == 100 or random.randrange(1, 101) <= percents:
                        try:
                            space[j][i] = build_stack.copy()
                        except IndexError:
                            pass
        else:
            for i in range(left, right + 1):
                if percents == 100 or random.randrange(1, 101) <= percents:
                    try:
                        space[top][i] = build_stack.copy()
                    except IndexError:
                        pass
                if percents == 100 or random.randrange(1, 101) <= percents:
                    try:
                        space[bottom][i] = build_stack.copy()
                    except IndexError:
                        pass
            for i in range(top + 1, bottom):
                if percents == 100 or random.randrange(1, 101) <= percents:
                    try:
                        space[i][left] = build_stack.copy()
                    except IndexError:
                        pass
                if percents == 100 or random.randrange(1, 101) <= percents:
                    try:
                        space[i][right] = build_stack.copy()
                    except IndexError:
                        pass
                for j in range(left + 1, right):
                    if percents == 100 or random.randrange(1, 101) <= percents:
                        try:
                            space[i][j] = None
                        except IndexError:
                            pass

    def build_house(self, top, left, bottom, right, wall, door, wealth, master, num_w=1, percents=100):
        self.build_square(self.buff, top, left, bottom, right, wall, False, percents=percents)
        if door is not None:
            self.buff[top][random.randrange(left + 1, right)] = door.copy()
            self.buff[bottom][random.randrange(left + 1, right)] = door.copy()
        else:
            self.buff[top][random.randrange(left + 1, right)] = None
            self.buff[bottom][random.randrange(left + 1, right)] = None

        y = random.randrange(top + 1, bottom)
        x = random.randrange(left + 1, right)
        self.buff[y][x] = wealth
        # Generating enemy if master is not None

    def events(self, pygame, event):
        if event.type == pygame.KEYDOWN:
            if self.pause:
                if event.key == pygame.K_x or event.key == pygame.K_j or event.key == pygame.K_RETURN:
                    self.pause = False
                if event.key == pygame.K_ESCAPE:
                    self.pause = False
                if event.key == pygame.K_q:
                    self.pause = False
                    self.kill_timer = 1
            elif self.kill_timer is None:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.player.direction = 0
                    self.player.walking += 1
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.player.direction = 2
                    self.player.walking += 1
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.player.direction = 3
                    self.player.walking += 1
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.player.direction = 1
                    self.player.walking += 1
                if event.key == pygame.K_x or event.key == pygame.K_j:
                    self.player.slicing = 10
                    self.player.walking = 0
                if event.key == pygame.K_z or event.key == pygame.K_k:
                    self.player.shotting = True
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                    self.pause = True

        if event.type == pygame.KEYUP:
            if not self.pause and self.kill_timer is None:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.player.walking -= 1
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.player.walking -= 1
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.player.walking -= 1
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.player.walking -= 1

    def tick(self, counters, tiles, audio, settings):
        if self.pause:
            return
        for i in range(0, len(self.particles)):
            try:
                if not self.particles[i].move():
                    del self.particles[i]
                    i = max(0, i - 1)
            except IndexError:
                pass

        for i in range(0, len(self.missiles)):
            try:
                if not self.missiles[i].move():
                    for j in range(0, 4):
                        rnd_sp = random.randrange(-1, 2)
                        self.particles.append(particle.Particle(self.missiles[i].x + self.square_size // 2,
                                                                self.missiles[i].y + self.square_size // 2,
                                                                tiles['dust'], sp_x=rnd_sp, sp_y=-2,
                                                                palette=settings.system['palettes'][2]))
                    del self.missiles[i]
                    audio.bank_sound['pierce'].play()
                    i = max(0, i - 1)
                elif self.missiles[i].foe and abs(self.missiles[i].x - self.player.x) < 8 and \
                        abs(self.missiles[i].y - self.player.y) < 8 and self.player.blink == 0:
                    self.player.lives = max(0, self.player.lives - 1)
                    self.player.multiplier = 1
                    self.player.multi_level = 0
                    self.player.blink = max(60, self.player.blink)
                    for j in range(0, 4):
                        rnd_sp = random.randrange(-1, 2)
                        self.particles.append(particle.Particle(self.missiles[i].x + self.square_size // 2,
                                                                self.missiles[i].y + self.square_size // 2,
                                                                tiles['dust'], sp_x=rnd_sp, sp_y=-2,
                                                                palette=settings.system['palettes'][5]))
                    del self.missiles[i]
                    audio.bank_sound['wound'].play()
                    i = max(0, i - 1)
                    if self.player.lives == 0:
                        # Game restart
                        self.kill_timer = 300
                elif not self.missiles[i].foe:
                    for j in range(0, len(self.encounters)):
                        if abs(self.missiles[i].x - self.encounters[j].x) < 8 and abs(self.missiles[i].y - self.encounters[j].y) < 8:
                            for k in range(0, 4):
                                rnd_sp = random.randrange(-1, 2)
                                self.particles.append(particle.Particle(self.missiles[i].x + self.square_size // 2,
                                                                        self.missiles[i].y + self.square_size // 2,
                                                                        tiles['dust'], sp_x=rnd_sp, sp_y=-2,
                                                                        palette=settings.system['palettes'][5]))
                            del self.missiles[i]
                            self.encounters[j].lives -= 2
                            audio.bank_sound['pierce'].play()
                            if self.encounters[j].lives <= 0:
                                enc_view_x, enc_view_y = self.calculate_offsets(round(self.encounters[j].x),
                                                                                round(self.encounters[j].y), settings)
                                square = self.square_get(enc_view_x // self.square_size, enc_view_y // self.square_size)
                                if square is not None:
                                    square.append(settings.object_keys['skull_c'])
                                else:
                                    self.square_set(enc_view_x // self.square_size, enc_view_y // self.square_size,
                                                    settings.object_keys['skull_c'])
                                self.player.score += 100 * self.player.multiplier
                                if self.player.multiplier > 1:
                                    self.player.multi_level = self.player.multi_limit - 1
                                self.particles.append(particle.Particle(self.encounters[j].x,
                                                                        self.encounters[j].y - self.square_size // 2,
                                                                        tiles[100 * self.player.multiplier], 0, 0, life=60, grav=0,
                                                                        palette=settings.system['palettes'][3]))
                                del self.encounters[j]
                                audio.bank_sound['wound_e'].play()
                            break
            except IndexError:
                pass

        if counters[2] in (0, 8, 16, 24):
            if self.player.multiplier == 1:
                self.player.multi_level -= 1
                audio.play_music(self.stage_music)
            else:
                self.player.multi_level -= 2
            if self.player.multi_level <= 0:
                self.player.multiplier = 1
                self.player.multi_level = 0

        # self.pixel_offset_v += 2
        if self.player.walking < 0:
            self.player.walking = 0
        if self.player.walking:
            self.player.slicing = 0
            self.player.anim_frame = counters[0]
            player_view_x, player_view_y = self.calculate_offsets(self.player.x, self.player.y, settings)
            if self.player.direction == 0:
                sq_x = player_view_x // self.square_size
                sq_y = (player_view_y - self.player.speed) // self.square_size
                mv_x = 0
                mv_y = -1 * self.player.speed
            elif self.player.direction == 1:
                sq_x = (player_view_x + self.square_size // 3 + self.player.speed) // self.square_size
                sq_y = player_view_y // self.square_size
                mv_x = self.player.speed
                mv_y = 0
            elif self.player.direction == 2:
                sq_x = player_view_x // self.square_size
                sq_y = (player_view_y + self.square_size // 3 + self.player.speed) // self.square_size
                mv_x = 0
                mv_y = self.player.speed
            elif self.player.direction == 3:
                sq_x = (player_view_x - self.square_size // 3 - self.player.speed) // self.square_size
                sq_y = player_view_y // self.square_size
                mv_x = -1 * self.player.speed
                mv_y = 0

            square = self.square_get(sq_x, sq_y)
            if self.square_passable(settings, square) and self.square_size < self.player.x + mv_x < (self.space_width - 2) * self.square_size \
                and self.square_size < self.player.y + mv_y < (self.space_height - 3) * self.square_size:
                self.player.x += mv_x
                self.player.y += mv_y
            else:
                self.player.walking = False

            if square is not None:
                new_objs, del_obj, score = self.object_trigger(square[-1], 0, audio, settings)
                if del_obj:
                    del square[-1]
                if new_objs is not None:
                    square.extend(new_objs)
                if score is not None:
                    sc_x, sc_y = self.deduce_offsets(sq_x * self.square_size, sq_y * self.square_size, settings)
                    self.player.score += score * self.player.multiplier
                    if self.player.multiplier > 1:
                        self.player.multi_level = self.player.multi_limit - 1
                    self.particles.append(particle.Particle(sc_x, sc_y,
                                                            tiles[score * self.player.multiplier], 0, 0, life=60, grav=0,
                                                            palette=settings.system['palettes'][3]))

            if counters[2] in (0,16):
                audio.bank_sound['step'].play()

        if self.player.slicing:
            self.player.anim_frame = counters[0]
            self.player.slicing -= 1
            if self.player.slicing == 5:
                self.player_slice(tiles, audio, settings)
                audio.bank_sound['slice'].play()

        if self.player.shotting:
            if self.player.shots > 0:
                self.player.anim_frame = counters[0]
                self.player.shots -= 1
                self.player_shot(self.player.direction, tiles, settings)
                audio.bank_sound['shot'].play()
            self.player.shotting = False

        if self.player.blink > 0:
            self.player.blink -= 1
            self.player.visible = counters[1] in (0, 2)
            if self.player.blink == 0:
                self.player.visible = True

        for enc in self.encounters:
            if self.player.blink == 0 and self.kill_timer is None and abs(self.player.x - enc.x) < 8 and abs(self.player.y - enc.y) < 8:
                enc.lives -= 1
                if enc.lives == 0:
                    self.encounters.remove(enc)
                    audio.bank_sound['wound_e'].play()
                self.player.lives = max(0, self.player.lives - 1)
                self.player.multiplier = 1
                self.player.multi_level = 0
                self.player.blink = max(60, self.player.blink)
                audio.bank_sound['wound'].play()
                if self.player.lives == 0:
                    # Game restart
                    self.kill_timer = 300
            if enc.cooldown == 0:
                if enc.speed_arr > 0 and self.encounter_sight(enc, tiles, audio, settings):
                    enc.cooldown = enc.max_cool
                    continue
            else:
                enc.cooldown -= 1
                continue
            if enc.walking:
                enc.anim_frame = counters[0]
                if enc.direction == 0:
                    enc.y -= min(enc.speed, enc.distance)
                    enc.distance -= min(enc.speed, enc.distance)
                elif enc.direction == 1:
                    enc.x += min(enc.speed, enc.distance)
                    enc.distance -= min(enc.speed, enc.distance)
                elif enc.direction == 2:
                    enc.y += min(enc.speed, enc.distance)
                    enc.distance -= min(enc.speed, enc.distance)
                elif enc.direction == 3:
                    enc.x -= min(enc.speed, enc.distance)
                    enc.distance -= min(enc.speed, enc.distance)
                enc.distance = max(0, enc.distance)
                enc.walking = enc.distance > 0
            else:
                enc_view_x, enc_view_y = self.calculate_offsets(round(enc.x), round(enc.y), settings)
                paths = self.encounter_paths(enc_view_x, enc_view_y, settings)
                if enc.direction not in paths or random.randrange(0, 3) == 0:
                    enc.direction = random.choice(paths)
                if enc.homing:
                    to_player = self.dir_to_player(enc, self.player)
                    if to_player in paths:
                        enc.direction = to_player

                enc.walking = True
                enc.distance = self.square_size

        self.view_follow(tiles, counters, audio, self.player.y, settings)

        if self.pixel_offset_v == 0:
            self.offset_v += 1
            self.player.dist += 1
            self.player.score += 10 * (self.player.multiplier - 1)
            self.pixel_offset_v = self.square_size * -1

        if self.offset_v >= self.space_height:
            self.onscreen, self.buff = self.buff, self.onscreen
            self.offset_v = 0

            if self.player.stage == 0:
                self.world_generate(settings)
            elif self.player.stage == 1:
                self.underworld_generate(settings)

        if self.kill_timer is not None:
            audio.pygame.mixer.music.stop()
            self.player.visible = False
            self.player.walking = False
            self.player.slicing = False
            self.player.shotting = False
            if self.kill_timer == 0:
                return 'over', {'hero': self.player}
            self.kill_timer -= 1

    def encounter_paths(self, enc_view_x, enc_view_y, settings):
        dirs = (
            (enc_view_x, (enc_view_y - self.square_size), 0),
            ((enc_view_x + self.square_size), enc_view_y, 1),
            (enc_view_x, (enc_view_y + self.square_size), 2),
            ((enc_view_x - self.square_size), enc_view_y, 3)
        )
        paths = []
        for sq_x, sq_y, direction in dirs:
            try:
                square = self.square_get(sq_x // self.square_size, sq_y // self.square_size)
                if self.square_passable(settings, square):
                    paths.append(direction)
            except IndexError:
                pass
        if len(paths) == 0:
            paths.append(2)
        return paths

    def encounter_sight(self, enc, tiles, audio, settings):
        if self.player.blink > 0 or self.kill_timer is not None:
            return False
        enc_sq_x = (round(enc.x) + self.square_size // 2 - settings.system['view_x']) // self.square_size
        enc_sq_y = (round(enc.y) + self.square_size // 2 - settings.system[
            'view_y'] - self.pixel_offset_v) // self.square_size
        player_sq_x = (self.player.x + self.square_size // 2 - settings.system['view_x']) // self.square_size
        player_sq_y = (self.player.y + self.square_size // 2 - settings.system[
            'view_y'] - self.pixel_offset_v) // self.square_size
        if abs(enc_sq_x - player_sq_x) > enc.vision or abs(enc_sq_y - player_sq_y) > enc.vision:
            return False
        dist_x = player_sq_x - enc_sq_x
        dist_y = player_sq_y - enc_sq_y
        dir_x = tools.sign(dist_x)
        dir_y = tools.sign(dist_y)
        if dir_x == 0 and dir_y == 0:
            return False
        if (dir_y > 0 and enc.direction == 0) or (dir_x > 0 and enc.direction == 3) \
                or (dir_y < 0 and enc.direction == 2) or (dir_x < 0 and enc.direction == 1):
            return False
        if enc_sq_x == player_sq_x or enc_sq_y == player_sq_y or abs(dist_x) == abs(dist_y):
            if self.arrow_path(enc_sq_x, enc_sq_y, max(abs(dist_x), abs(dist_y)),
                               tools.sign(dir_x), tools.sign(dir_y), settings):
                self.foe_shot(enc, dir_x, dir_y, tiles, settings)
                audio.bank_sound['shot_e'].play()
                return True
        return False

    def dir_to_player(self, enc, player):
        x_dif = player.x - enc.x
        y_dif = player.y - enc.y
        if abs(x_dif) > abs(y_dif):
            if x_dif > 0:
                return 1
            elif x_dif < 0:
                return 3
            else:
                return -1
        else:
            if y_dif > 0:
                return 2
            elif y_dif < 0:
                return 0
            else:
                return -1


    def arrow_path(self, enc_sq_x, enc_sq_y, steps_num, dir_x, dir_y, settings):
        arr_sq_x, arr_sq_y = enc_sq_x, enc_sq_y
        for i in range(0, steps_num):
            arr_sq_x += dir_x
            arr_sq_y += dir_y
            square = self.square_get(arr_sq_x, arr_sq_y)
            if not self.square_passable(settings, square):
                return False
        return True

    def foe_shot(self, enc, dir_x, dir_y, tiles, settings):
        if dir_x == 0 and dir_y < 0:
            tile = tiles['proj_n']
            mirr_x = mirr_y = False
            enc.direction = 0
        elif dir_x > 0 and dir_y < 0:
            tile = tiles['proj_nw']
            mirr_x = True
            mirr_y = False
            enc.direction = 0
        elif dir_x > 0 and dir_y == 0:
            tile = tiles['proj_w']
            mirr_x = True
            mirr_y = False
            enc.direction = 1
        elif dir_x > 0 and dir_y > 0:
            tile = tiles['proj_nw']
            mirr_x = mirr_y = True
            enc.direction = 2
        elif dir_x == 0 and dir_y > 0:
            tile = tiles['proj_n']
            mirr_x = False
            mirr_y = True
            enc.direction = 2
        elif dir_x < 0 and dir_y > 0:
            tile = tiles['proj_nw']
            mirr_x = False
            mirr_y = True
            enc.direction = 2
        elif dir_x < 0 and dir_y == 0:
            tile = tiles['proj_w']
            mirr_x = mirr_y = False
            enc.direction = 3
        elif dir_x < 0 and dir_y < 0:
            tile = tiles['proj_nw']
            mirr_x = mirr_y = False
            enc.direction = 0
        self.missiles.append(missile.Missile(enc.x + dir_x * self.square_size, enc.y + dir_y * self.square_size,
                                             tile, dir_x * enc.speed_arr, dir_y * enc.speed_arr, palette=settings.system['palettes'][2],
                                             mirr_x=mirr_x, mirr_y=mirr_y, life=60, grav=0, foe=True))

    def player_shot(self, direction, tiles, settings):
        if direction == 0:
            tile = tiles['pierce_n']
            mirr_x = mirr_y = False
            dir_x = 0
            dir_y = -1
        if direction == 1:
            tile = tiles['pierce_e']
            mirr_x = mirr_y = False
            dir_x = 1
            dir_y = 0
        if direction == 2:
            tile = tiles['pierce_n']
            mirr_x = mirr_y = True
            dir_x = 0
            dir_y = 1
        if direction == 3:
            tile = tiles['pierce_e']
            mirr_x = mirr_y = True
            dir_x = -1
            dir_y = 0
        self.missiles.append(missile.Missile(self.player.x + dir_x * self.square_size, self.player.y + dir_y * self.square_size,
                                             tile, dir_x * 4, dir_y * 4, palette=settings.system['palettes'][2],
                                             mirr_x=mirr_x, mirr_y=mirr_y, life=24, grav=0, foe=False))

    def player_slice(self, tiles, audio, settings):
        player_view_x, player_view_y = self.calculate_offsets(self.player.x, self.player.y, settings)
        if self.player.direction == 0:
            sq_x, sq_y = player_view_x, (player_view_y - self.square_size)
        elif self.player.direction == 1:
            sq_x, sq_y = (player_view_x + self.square_size), player_view_y
        elif self.player.direction == 2:
            sq_x, sq_y = player_view_x, (player_view_y + self.square_size)
        elif self.player.direction == 3:
            sq_x, sq_y = (player_view_x - self.square_size), player_view_y
        for i in range(0, len(self.encounters)):
            try:
                enc_view_x, enc_view_y = self.calculate_offsets(round(self.encounters[i].x),
                                                                round(self.encounters[i].y), settings)
                if abs(sq_x - enc_view_x) < 8 and abs(sq_y - enc_view_y) < 8:
                    self.encounters[i].lives -= 1
                    for j in range(0, 4):
                        rnd_sp = random.randrange(-1, 2)
                        self.particles.append(particle.Particle(self.encounters[i].x + self.square_size // 2,
                                                                self.encounters[i].y + self.square_size // 2,
                                                                tiles['dust'], sp_x=rnd_sp, sp_y=-2,
                                                                palette=settings.system['palettes'][10]))
                    if self.encounters[i].lives == 0:
                        square = self.square_get(enc_view_x // self.square_size, enc_view_y // self.square_size)
                        if square is not None:
                            square.append(settings.object_keys['skull_c'])
                        else:
                            self.square_set(enc_view_x // self.square_size, enc_view_y // self.square_size,
                                            settings.object_keys['skull_c'])
                        self.player.score += 100 * self.player.multiplier
                        if self.player.multiplier > 1:
                            self.player.multi_level = self.player.multi_limit - 1
                        self.particles.append(particle.Particle(self.encounters[i].x,
                                                                self.encounters[i].y - self.square_size // 2,
                                                                tiles[100 * self.player.multiplier], 0, 0, life=60, grav=0,
                                                                palette=settings.system['palettes'][3]))
                        del self.encounters[i]
                        audio.bank_sound['wound_e'].play()
                        i = max(0, i - 1)
                    return
            except IndexError:
                pass
        square = self.square_get(sq_x // self.square_size, sq_y // self.square_size)
        if square is not None:
            for i in range(0, 3):
                rnd = random.randrange(self.square_size // -4, self.square_size // 4)
                rnd_sp = random.randrange(-1, 2)
                self.particles.append(
                    particle.Particle(sq_x + rnd, sq_y - round(self.square_size / 1.5) + rnd, tiles['dust'],
                                      sp_x=rnd_sp, sp_y=-2,
                                      palette=settings.system['palettes'][square[-1][3]]))
            new_objs, del_obj, score = self.object_trigger(square[-1], 1, audio, settings)
            if del_obj:
                del square[-1]
            if new_objs is not None:
                square.extend(new_objs)
            if score is not None:
                sc_x, sc_y = self.deduce_offsets(sq_x, sq_y, settings)
                self.player.score += score * self.player.multiplier
                if self.player.multiplier > 1:
                    self.player.multi_level = self.player.multi_limit - 1
                self.particles.append(particle.Particle(sc_x, sc_y,
                                                        tiles[score * self.player.multiplier], 0, 0, life=60, grav=0,
                                                        palette=settings.system['palettes'][3]))


    def view_follow(self, tiles, counters, audio, y, settings):
        if y < self.space_height * self.square_size // 2:
            self.pixel_offset_v += 1
            self.player.y += 1
            if counters[2] in (0, 8, 16, 24) and self.player.multi_level < self.player.multi_limit:
                self.player.multi_level += 2
                if self.player.multi_level >= self.player.multi_limit and self.player.multiplier == 1:
                    self.player.multiplier = 2
                    audio.bank_sound['multi'].play()
                    audio.play_music('tense')
                    for j in range(0, 16):
                        rnd_x = random.randrange(-5, 6)
                        rnd_y = random.randrange(-5, 0)
                        self.particles.append(particle.Particle(self.player.x + self.square_size // 2,
                                                                self.player.y + self.square_size // 2,
                                                                tiles['dust'], sp_x=rnd_x, sp_y=rnd_y,
                                                                palette=settings.system['palettes'][4]))
            for i in range(0, len(self.encounters)):
                try:
                    self.encounters[i].y += 1
                    if self.encounters[i].y > self.space_height * self.square_size:
                        del self.encounters[i]
                        i = max(0, i - 1)
                except IndexError:
                    pass
            for i in range(0, len(self.missiles)):
                try:
                    self.missiles[i].y += 1
                    if self.missiles[i].y > self.space_height * self.square_size:
                        del self.missiles[i]
                        i = max(0, i - 1)
                except IndexError:
                    pass
            for i in range(0, len(self.particles)):
                try:
                    self.particles[i].y += 1
                    if self.particles[i].y > self.space_height * self.square_size:
                        del self.particles[i]
                        i = max(0, i - 1)
                except IndexError:
                    pass

    def square_get(self, x, y):
        if y < self.offset_v:
            return self.buff[self.space_height - (self.offset_v - y)][x]
        else:
            return self.onscreen[y - self.offset_v][x]

    def square_set(self, x, y, square_stack):
        if y < self.offset_v:
            self.buff[self.space_height - (self.offset_v - y)][x] = [square_stack]
        else:
            self.onscreen[y - self.offset_v][x] = [square_stack]

    def square_passable(self, settings, square_stack):
        if square_stack is None:
            return True
        for i in range(0, len(square_stack)):
            if square_stack[i][0] in settings.tiles_solid:
                return False
        return True

    def object_trigger(self, object, tr_type, audio, settings):
        if object[0] == 2 and tr_type == 1:  # log
            if random.randrange(0, 2) == 0:
                audio.bank_sound['crack'].play()
                if random.randrange(0, 6) == 0:
                    return [settings.object_keys['arrow']], True, None
                else:
                    return None, True, None
        elif object[0] == 3 and tr_type == 1:  # tree
            if random.randrange(0, 2) == 0:
                audio.bank_sound['crack'].play()
                return [settings.object_keys['log']], True, None
        elif object[0] == 4 and tr_type == 1:  # rock
            if random.randrange(0, 16) == 0:
                audio.bank_sound['crack'].play()
                if random.randrange(0, 11) == 0:
                    return [settings.object_keys['gem_fl']], True, None
                else:
                    return None, True, None
            else:
                audio.bank_sound['clank'].play()
        elif object[0] == 5 and tr_type == 0:
            self.player.lives = 0
            audio.bank_sound['wound'].play()
            self.kill_timer = 300
            return None, False, None
        elif object[0] == 8:
            if tr_type == 0:  # door shut
                audio.bank_sound['open'].play()
                return [settings.object_keys['door_o']], True, None
            elif tr_type == 1:
                audio.bank_sound['crack'].play()
                return [settings.object_keys['door_o']], True, None
        elif object[0] == 9:
            if tr_type == 0 and self.player.keys > 0:
                self.player.keys -= 1
                audio.bank_sound['unlock'].play()
                audio.bank_sound['open'].play()
                return [settings.object_keys['door_o']], True, 500
            elif tr_type == 1:
                audio.bank_sound['clank'].play()
        elif object[0] == 13 and self.player.keys > 0 and tr_type == 0:  # lock
            self.player.keys -= 1
            audio.bank_sound['unlock'].play()
            return None, True, 100
        elif object[0] == 15:
            if tr_type == 0:  # arrow
                audio.bank_sound['arrow'].play()
                if self.player.shots == self.player.max_shot:
                    return None, True, 50
                else:
                    self.player.shots += 1
                    return None, True, None
            else:
                audio.bank_sound['pierce'].play()
                return None, True, None
        elif object[0] == 16:
            if tr_type == 0:  # meat
                audio.bank_sound['eat'].play()
                if self.player.lives == self.player.max_lives:
                    return None, True, 500
                else:
                    self.player.lives = self.player.max_lives
                    return None, True, None
            else:
                audio.bank_sound['pierce'].play()
                return None, True, None
        elif object[0] == 18:
            if tr_type == 0:  # key
                audio.bank_sound['key'].play()
                if self.player.keys == self.player.max_keys:
                    return None, True, 200
                else:
                    self.player.keys += 1
                    return None, True, None
        elif object[0] == 21:
            if tr_type == 0:  # chick
                audio.bank_sound['eat'].play()
                if self.player.lives == self.player.max_lives:
                    return None, True, 100
                else:
                    self.player.lives = min(self.player.max_lives, self.player.lives + 2)
                    return None, True, None
            else:
                audio.bank_sound['pierce'].play()
                return None, True, None
        elif object[0] == 22:
            if tr_type == 0:  # apple
                audio.bank_sound['eat'].play()
                if self.player.lives == self.player.max_lives:
                    return None, True, 50
                else:
                    self.player.lives += 1
                    return None, True, None
            else:
                audio.bank_sound['pierce'].play()
                return None, True, None
        elif object[0] == 23 and tr_type == 0:  # chest shut
            audio.bank_sound['open'].play()
            return [settings.object_keys['chest_o'], self.roll_chest(settings, min=20)], True, None
        elif object[0] == 27:
            if tr_type == 0:  # potion_bl
                audio.bank_sound['drink'].play()
                if object[3] == 9:
                    self.player.blink = 600
                    return None, True, 1000
            else:
                audio.bank_sound['crack'].play()
                return None, True, None
        elif object[0] == 31:
            if tr_type == 1:  # skull common
                audio.bank_sound['crack'].play()
                return [self.roll_drop(settings, min=20)], True, None
        elif object[0] == 34 and tr_type == 1:
            if random.randrange(0, 2) == 0:
                audio.bank_sound['crack'].play()
                if random.randrange(0, 11) == 0:
                    return [settings.object_keys['apple']], True, None
                else:
                    return None, True, None
        elif object[0] == 51:
            if tr_type == 0:
                self.player.stage = 1
                self.underworld_initial(audio, settings)
                pl_view_x, pl_view_y = self.calculate_offsets(self.player.x, self.player.y, settings)
                self.square_set(pl_view_x // self.square_size, pl_view_y // self.square_size + 1,
                                    settings.object_keys['up_b'])
        elif object[0] == 52:
            if tr_type == 0:
                self.player.stage = 0
                self.world_initial(audio, settings)
                pl_view_x, pl_view_y = self.calculate_offsets(self.player.x, self.player.y, settings)
                self.square_set(pl_view_x // self.square_size, pl_view_y // self.square_size + 1,
                                settings.object_keys['down_b'])
        elif object[0] == 151:
            if tr_type == 1:
                audio.bank_sound['clank'].play()
        elif object[0] == 152:
            if tr_type == 1:
                audio.bank_sound['clank'].play()
        elif object[0] == 201 and tr_type == 0 and self.player.blink == 0:
            self.player.lives = max(0, self.player.lives - 1)
            self.player.multiplier = 1
            self.player.multi_level = 0
            audio.bank_sound['wound'].play()
            self.player.blink = 60
            if self.player.lives == 0:
                self.kill_timer = 300
            return None, False, None
        elif object[0] == 229:
            if tr_type == 0:  # coin
                audio.bank_sound['coin'].play()
                self.player.coins += 1
                return None, True, 100
        elif object[0] == 230:
            if tr_type == 0:  # gem shut
                audio.bank_sound['gem'].play()
                self.player.gems += 1
                return None, True, 1000
            elif tr_type == 1:
                audio.bank_sound['crack'].play()
                return None, True, None

        return None, False, None

    def roll_chest(self, settings, min=0):
        roll = random.randrange(min, 101)
        treasure = (
            (90, 'gem_fl'),
            (70, 'potion_bl'),
            (60, 'meat'),
            (50, 'chick'),
            (40, 'coin_fl'),
            (30, 'apple'),
            (20, 'arrow'),
            (15, 'plate'),
            (10, 'stone'),
            (5, 'grass'),
            (0, 'fire_a'),
        )
        for item in treasure:
            if roll >= item[0]:
                return settings.object_keys[item[1]]
        return None

    def roll_drop(self, settings, min=0):
        roll = random.randrange(min, 101)
        treasure = (
            (95, 'fire_a'),
            (60, 'key'),
            (50, 'chick'),
            (40, 'coin_fl'),
            (30, 'apple'),
            (20, 'arrow'),
            (15, 'plate'),
            (10, 'stone'),
            (5, 'grass')
        )
        for item in treasure:
            if roll >= item[0]:
                return settings.object_keys[item[1]]
        return None

    def world_generate(self, settings):
        for i in self.buff:
            for j in range(0, len(i)):
                i[j] = None

        for i in range(0, self.space_height):
            self.buff[i][random.randrange(0, 2)] = [settings.object_keys['rock_i_h']]
        for i in range(0, self.space_height):
            self.buff[i][self.space_width - 1 - random.randrange(0, 2)] = [settings.object_keys['rock']]

        top = 0
        bottom = self.space_height
        left = 4
        right = self.space_width - 4
        self.build_square(self.buff, top, left, bottom, right, [settings.object_keys['grass']], True, percents=15)

        top = 0
        bottom = self.space_height
        left = 0
        right = self.space_width
        if self.player.dist > 800:
            obs_rnd = 2
        elif self.player.dist > 400:
            obs_rnd = 5
        else:
            obs_rnd = None
        if obs_rnd is not None and random.randrange(0, obs_rnd) == 0:
            self.build_square(self.buff, top, left, bottom, right, [settings.object_keys['rock']], True, percents=15)
            for i in range(0, self.player.dist // 100):
                self.buff[random.randrange(top, bottom)][random.randrange(left + 1, right - 1)] = [
                    settings.object_keys['fire_a']]
        else:
            self.build_square(self.buff, top, left, bottom, right, [settings.object_keys['tree']], True, percents=15)
        self.buff[random.randrange(top, bottom)][random.randrange(left + 1, right - 1)] = [settings.object_keys['coin_fl']]
        self.buff[random.randrange(top, bottom)][random.randrange(left + 1, right - 1)] = [settings.object_keys['pit']]

        enc_x = random.randrange(self.square_size * 3, self.space_width * self.square_size - self.square_size * 4, self.square_size)
        enc_y = random.randrange(-1 * self.space_height * self.square_size, self.square_size * -1, self.square_size)

        if self.player.dist > 800:
            enc_rnd = 3
        elif self.player.dist > 400:
            enc_rnd = 5
        else:
            enc_rnd = None
        if enc_rnd is not None and random.randrange(0, enc_rnd) == 0:
            self.encounters.append(
                goblin.Goblin(
                    enc_x, enc_y, 2, speed=0.5, speed_arr=3, vision=8, max_cool=120,
                    score=500, palette=settings.system['palettes'][9]
                )
            )
        else:
            self.encounters.append(goblin.Goblin(enc_x, enc_y, 2, score=100))

        if self.player.dist == 400 or self.player.dist == 800:
            rnd_h = random.randrange(0, self.space_height)
            for i in range(0, self.space_width):
                self.buff[rnd_h][i] = [settings.object_keys['brick']]
            self.buff[rnd_h][random.choice((self.space_width // 4, self.space_width // 4 * 3))] = [settings.object_keys['rock']]
            self.buff[rnd_h][self.space_width // 2] = [settings.object_keys['gate']]
        elif self.player.dist == 608 or self.player.dist == 1008:
            self.buff[random.randrange(top, bottom)][random.randrange(left + 3, right - 3)] = [settings.object_keys['down']]
        elif random.randrange(0, 2) == 0:
            top = random.randrange(1, self.space_height - 8)
            bottom = top + random.randrange(4, 8)
            left = random.randrange(1, self.space_width - 8)
            right = left + random.randrange(4, 8)
            door = [settings.object_keys['door']]
            wall = [settings.object_keys['brick']]
            wealth = [settings.object_keys['chest_l'], settings.object_keys['lock']]
            if random.randrange(0, 3) == 0:
                wall = [settings.object_keys['rock']]
            if random.randrange(0, 5) == 0:
                wealth = [settings.object_keys['chest_l']]
            if random.randrange(0, 5) == 0 and wealth is None:
                door = None
            self.build_house(top, left, bottom, right,
                             wall,
                             door,
                             wealth,
                             None, percents=100)

    def underworld_generate(self, settings):
        for i in self.buff:
            for j in range(0, len(i)):
                i[j] = None

        for i in range(0, self.space_height):
            self.buff[i][random.randrange(0, 2)] = [settings.object_keys['brick']]
        for i in range(0, self.space_height):
            self.buff[i][self.space_width - 1 - random.randrange(0, 2)] = [settings.object_keys['brick']]

        top = 0
        bottom = self.space_height
        left = 4
        right = self.space_width - 4
        self.build_square(self.buff, top, left, bottom, right, [settings.object_keys['stone']], True, percents=15)

        top = 0
        bottom = self.space_height
        left = 0
        right = self.space_width
        if self.player.dist > 800:
            obs_rnd = 2
        elif self.player.dist > 400:
            obs_rnd = 5
        else:
            obs_rnd = None
        if obs_rnd is not None and random.randrange(0, obs_rnd) == 0:
            self.build_square(self.buff, top, left, bottom, right, [settings.object_keys['rock']], True, percents=15)
            for i in range(0, self.player.dist // 100):
                self.buff[random.randrange(top, bottom)][random.randrange(left + 1, right - 1)] = [
                    settings.object_keys['fire_a']]
        else:
            self.build_square(self.buff, top, left, bottom, right, [settings.object_keys['rock']], True, percents=15)

        self.buff[random.randrange(top, bottom)][random.randrange(left + 1, right - 1)] = [settings.object_keys['skull_c']]
        for i in range(0, 2):
            self.buff[random.randrange(top, bottom)][random.randrange(left + 1, right - 1)] = [settings.object_keys['pit']]
        if random.randrange(0, 5) == 0:
            rnd_up_x = random.randrange(left + 3, right - 3)
            rnd_up_y = random.randrange(top + 1, bottom)
            self.buff[rnd_up_y-1][rnd_up_x] = [settings.object_keys['brick']]
            self.buff[rnd_up_y][rnd_up_x] = [settings.object_keys['up']]

        for i in range(0, self.player.dist // 500):
            enc_x = random.randrange(self.square_size * 3, self.space_width * self.square_size - self.square_size * 4, self.square_size)
            enc_y = random.randrange(-1 * self.space_height * self.square_size, self.square_size * -1, self.square_size)
            self.encounters.append(
                goblin.Goblin(
                    enc_x, enc_y, 2, speed=1, speed_arr=0, vision=0, homing=True, max_cool=120,
                    score=500, palette=settings.system['palettes'][5]
                )
            )

        if random.randrange(0, 8) == 0:
            rnd_h = random.randrange(0, self.space_height)
            for i in range(0, self.space_width):
                self.buff[rnd_h][i] = [settings.object_keys['brick']]
            self.buff[rnd_h][random.choice((self.space_width // 4, self.space_width // 4 * 3))] = [settings.object_keys['rock']]
            self.buff[rnd_h][self.space_width // 2] = [settings.object_keys['gate']]
        elif random.randrange(0, 2) == 0:
            top = random.randrange(1, self.space_height - 8)
            bottom = top + random.randrange(4, 8)
            left = random.randrange(1, self.space_width - 8)
            right = left + random.randrange(4, 8)
            door = [settings.object_keys['door']]
            wall = [settings.object_keys['brick']]
            wealth = [settings.object_keys['chest_l'], settings.object_keys['lock']]
            self.build_house(top, left, bottom, right,
                             wall,
                             door,
                             wealth,
                             None, percents=100)

    def world_initial(self, audio, settings):
        self.stage_music = 'stage'
        self.objects_clear()

        for i in self.buff:
            for j in range(0, len(i)):
                i[j] = None
        for i in self.onscreen:
            for j in range(0, len(i)):
                i[j] = None

        for i in range(0, self.space_height):
            self.buff[i][random.randrange(0, 2)] = [settings.object_keys['rock_i_h']]
            self.onscreen[i][random.randrange(0, 2)] = [settings.object_keys['rock_i_h']]
        for i in range(0, self.space_height):
            self.buff[i][self.space_width - 1 - random.randrange(0, 2)] = [settings.object_keys['rock']]
            self.onscreen[i][self.space_width - 1 - random.randrange(0, 2)] = [settings.object_keys['rock']]

        top = 0
        bottom = self.space_height
        left = 0
        right = self.space_width
        self.build_square(self.buff, top, left, bottom, right, [settings.object_keys['grass']], True, percents=15)
        self.build_square(self.onscreen, top, left, bottom, right, [settings.object_keys['grass']], True, percents=15)

        top = 0
        bottom = self.space_height // 2
        left = 0
        right = self.space_width
        self.build_square(self.buff, top, left, bottom, right, [settings.object_keys['tree']], True, percents=15)

    def underworld_initial(self, audio, settings):
        self.stage_music = 'under'
        self.objects_clear()
        for i in self.buff:
            for j in range(0, len(i)):
                i[j] = None
        for i in self.onscreen:
            for j in range(0, len(i)):
                i[j] = None

        for i in range(0, self.space_height):
            self.buff[i][random.randrange(0, 2)] = [settings.object_keys['brick']]
            self.onscreen[i][random.randrange(0, 2)] = [settings.object_keys['brick']]
        for i in range(0, self.space_height):
            self.buff[i][self.space_width - 1 - random.randrange(0, 2)] = [settings.object_keys['brick']]
            self.onscreen[i][self.space_width - 1 - random.randrange(0, 2)] = [settings.object_keys['brick']]

        top = 0
        bottom = self.space_height
        left = 4
        right = self.space_width - 4
        self.build_square(self.buff, top, left, bottom, right, [settings.object_keys['stone']], True, percents=15)
        self.build_square(self.onscreen, top, left, bottom, right, [settings.object_keys['stone']], True, percents=15)

        top = 0
        bottom = self.space_height
        left = 0
        right = self.space_width
        if self.player.dist > 800:
            obs_rnd = 2
        elif self.player.dist > 400:
            obs_rnd = 5
        else:
            obs_rnd = None
        if obs_rnd is not None and random.randrange(0, obs_rnd) == 0:
            self.build_square(self.buff, top, left, bottom, right, [settings.object_keys['rock']], True, percents=15)
            for i in range(0, self.player.dist // 100):
                self.buff[random.randrange(top, bottom)][random.randrange(left + 1, right - 1)] = [
                    settings.object_keys['fire_a']]
        else:
            self.build_square(self.buff, top, left, bottom, right, [settings.object_keys['rock']], True, percents=15)

        if random.randrange(0, 2) == 0:
            self.buff[random.randrange(top, bottom)][random.randrange(left + 1, right - 1)] = [settings.object_keys['skull_c']]
        for i in range(0, 2):
            self.buff[random.randrange(top, bottom)][random.randrange(left + 1, right - 1)] = [settings.object_keys['pit']]

    def objects_clear(self):
        self.encounters.clear()
        self.particles.clear()
        self.missiles.clear()

    def stage_display(self, tiles, font, canvas, counters, pygame, settings,
                      mirror_h=False, mirror_v=False, palette=None):
        if self.player.stage == 0:
            canvas.fill(settings.system['color_bg'])
        elif self.player.stage == 1:
            canvas.fill(settings.system['u_color_bg'])

        if self.player.stage == 1:
            palette = settings.system['palettes'][1]

        tools.draw_maze(tiles, canvas, counters, pygame, settings,
                        self.buff, settings.map_keys,
                        settings.system['view_x'], settings.system['view_y'] + self.pixel_offset_v,
                        self.space_height - self.offset_v, 0, self.space_height - 1, self.space_width - 1,
                        self.square_size, mirror_h=mirror_h, mirror_v=mirror_v, palette=palette)
        tools.draw_maze(tiles, canvas, counters, pygame, settings,
                        self.onscreen, settings.map_keys,
                        settings.system['view_x'],
                        settings.system['view_y'] + self.offset_v * self.square_size + self.pixel_offset_v,
                        0, 0, self.space_height - 1 - self.offset_v, self.space_width - 1,
                        self.square_size, mirror_h=mirror_h, mirror_v=mirror_v, palette=palette)

        if self.kill_timer is not None:
            tools.draw_tile(canvas, pygame, settings, self.player.x, self.player.y, tiles['skull1'], 0, 0,
                            settings.system['palettes'][5])

        for enc in self.encounters:
            if enc.visible:
                enc_x = round(enc.x)
                enc_y = round(enc.y)
                enc_sprite = tiles[
                    settings.animations[enc.sprites[enc.direction]]['tiles'][enc.anim_frame]]
                enc_mirror_x = \
                    settings.animations[enc.sprites[enc.direction]]['mirror'][enc.anim_frame][0]
                if enc.palette is None:
                    enc_palette = settings.system['palettes'][
                    settings.animations[enc.sprites[enc.direction]]['palettes'][enc.anim_frame]]
                else:
                    enc_palette = enc.palette
                tools.draw_tile(canvas, pygame, settings, enc_x, enc_y, enc_sprite, enc_mirror_x, 0,
                                enc_palette)

        if self.player.visible:
            player_x = self.player.x
            player_y = self.player.y
            player_sprite = tiles[
                settings.animations[self.player.sprites[self.player.direction]]['tiles'][self.player.anim_frame]]
            player_mirror_x = \
                settings.animations[self.player.sprites[self.player.direction]]['mirror'][self.player.anim_frame][0]
            player_palette = settings.system['palettes'][
                settings.animations[self.player.sprites[self.player.direction]]['palettes'][self.player.anim_frame]]
            if self.player.multiplier > 1:
                player_palette = settings.system['palettes'][4]
            tools.draw_tile(canvas, pygame, settings, player_x, player_y, player_sprite, player_mirror_x, 0,
                            player_palette)

        if self.player.slicing:
            player_x = self.player.x
            player_y = self.player.y
            if self.player.direction == 0:
                tools.draw_tile(canvas, pygame, settings, player_x, player_y - self.square_size, tiles['slice_n'], 0, 0,
                                settings.system['palettes'][6])
            if self.player.direction == 1:
                tools.draw_tile(canvas, pygame, settings, player_x + self.square_size, player_y, tiles['slice_e'], 0, 0,
                                settings.system['palettes'][6])
            if self.player.direction == 2:
                tools.draw_tile(canvas, pygame, settings, player_x, player_y + self.square_size, tiles['slice_n'], 1, 1,
                                settings.system['palettes'][6])
            if self.player.direction == 3:
                tools.draw_tile(canvas, pygame, settings, player_x - self.square_size, player_y, tiles['slice_e'], 1, 1,
                                settings.system['palettes'][6])

        for i in self.particles:
            tools.draw_tile(canvas, pygame, settings, i.x, i.y, i.tile, i.mirr_x, i.mirr_y, i.palette)
        for i in self.missiles:
            tools.draw_tile(canvas, pygame, settings, i.x, i.y, i.tile, i.mirr_x, i.mirr_y, i.palette)

        if self.ui_keys:
            for i in range(0, self.player.keys):
                key_x = settings.system['screen_width'] - (i + 1) * self.square_size
                key_y = settings.system['screen_height'] - self.square_size
                tools.draw_tile(canvas, pygame, settings, key_x, key_y, tiles['key'], 0, 0,
                                settings.system['palettes'][4])

        if self.ui_lives:
            for i in range(0, self.player.lives):
                live_x = (i + 6) * self.square_size
                live_y = settings.system['screen_height'] - self.square_size
                tools.draw_tile(canvas, pygame, settings, live_x, live_y, tiles['heart'], 0, 0,
                                settings.system['palettes'][5])
            for i in range(self.player.lives, self.player.max_lives):
                live_x = (i + 6) * self.square_size
                live_y = settings.system['screen_height'] - self.square_size
                tools.draw_tile(canvas, pygame, settings, live_x, live_y, tiles['wound'], 0, 0,
                                settings.system['palettes'][5])

        if self.ui_shots:
            for i in range(0, self.player.shots):
                shot_x = settings.system['screen_width'] - (i + 1) * self.square_size
                shot_y = settings.system['screen_height'] - self.square_size * 2
                tools.draw_tile(canvas, pygame, settings, shot_x, shot_y, tiles['arrow'], 0, 0,
                                settings.system['palettes'][2])

        if self.ui_gems:
            gem_y = settings.system['screen_height'] - self.square_size
            tools.draw_tile(canvas, pygame, settings, 0, gem_y, tiles['gem'], 0, 0,
                            settings.system['palettes'][1])
            tools.draw_text(16, gem_y + 4, '*' + str(self.player.gems), font, 6, pygame, canvas, settings)

        if self.ui_coins:
            coin_y = settings.system['screen_height'] - self.square_size * 2
            tools.draw_tile(canvas, pygame, settings, 0, coin_y, tiles['coin'], 0, 0,
                            settings.system['palettes'][2])
            tools.draw_text(16, coin_y + 4, '*' + str(self.player.coins), font, 6, pygame, canvas, settings)

        if self.ui_score:
            text = 'SCR:' + str(self.player.score)
            if self.player.multiplier > 1 and counters[1] in (0, 2):
                text += (' *' + str(self.player.multiplier))
            tools.draw_text(0, 0, text, font, 6, pygame, canvas, settings)

        if self.ui_dist:
            tools.draw_text(0, 8, 'WLK:' + str(self.player.dist), font, 6, pygame, canvas, settings)

        if self.pause:
            text = 'PAUSE'
            tools.draw_text(self.space_width * self.square_size // 2 - len(text) * 8 // 2, 88, text, font, 4, pygame, canvas, settings)
            text = 'CONTINUE: ENTER'
            tools.draw_text(self.space_width * self.square_size // 2 - len(text) * 8 // 2, 96, text, font, 6, pygame, canvas, settings)
            text = 'TOGGLE MUSIC: M'
            tools.draw_text(self.space_width * self.square_size // 2 - len(text) * 8 // 2, 104, text, font, 6, pygame,
                            canvas, settings)
            text = 'QUIT: Q'
            tools.draw_text(self.space_width * self.square_size // 2 - len(text) * 8 // 2, 112, text, font, 6, pygame,
                            canvas, settings)

    def calculate_offsets(self, x, y, settings):
        proper_x = (x + self.square_size // 2 - settings.system['view_x'])
        proper_y = (y + self.square_size // 2 - settings.system['view_y'] - self.pixel_offset_v)
        return proper_x, proper_y

    def deduce_offsets(self, off_x, off_y, settings):
        proper_x = off_x + settings.system['view_x']
        proper_y = off_y + settings.system['view_y'] + self.pixel_offset_v
        return proper_x, proper_y

    def launch(self, audio, settings, summary):
        self.space_a = []
        self.space_b = []
        for i in range(0, self.space_height):
            self.space_a.append([None for j in range(0, self.space_width)])
            self.space_b.append([None for j in range(0, self.space_width)])

        self.onscreen, self.buff = self.space_a, self.space_b
        self.offset_v = 0
        self.pixel_offset_v = self.square_size * -1

        if summary is not None:
            self.player = summary['hero']

        self.ui_keys = True
        self.ui_lives = True
        self.ui_shots = True
        self.ui_gems = True
        self.ui_coins = True
        self.ui_score = True
        self.ui_dist = True

        self.particles = []
        self.encounters = []
        self.missiles = []

        self.kill_timer = None

        random.seed(10)
        self.world_initial(audio, settings)
