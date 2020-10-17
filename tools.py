def pygame_setup(pygame, settings):
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode(
        (
            settings.system['screen_width'] * settings.system['screen_scale'],
            settings.system['screen_height'] * settings.system['screen_scale']
        ),
        pygame.HWPALETTE,
        depth=8
    )
    screen.set_palette(settings.system['palettes'][0])
    canvas = pygame.Surface(
        (settings.system['screen_width'], settings.system['screen_height']),
        pygame.HWPALETTE,
        depth=8
    )
    canvas.set_palette(settings.system['palettes'][0])

    pygame.display.set_caption(settings.system['main_window_caption'])
    fps = settings.system['fps']
    clock = pygame.time.Clock()

    return screen, canvas, fps, clock


def data_load(pygame, settings):
    bitmaps = []
    for filename in settings.bitmaps:
        bitmaps.append(pygame.image.load(filename).convert(8))
    font = {}
    for symbol in settings.font:
        new_symbol = pygame.Surface((symbol['tile_w'], symbol['tile_h']), pygame.HWPALETTE, depth=8)
        new_symbol.set_palette(bitmaps[symbol['tileset']].get_palette())
        new_symbol.set_colorkey((255, 0, 255))
        new_symbol.blit(
            bitmaps[symbol['tileset']],
            (0, 0),
            (symbol['tile_x'], symbol['tile_y'], symbol['tile_w'], symbol['tile_h'])
        )
        font[symbol['name']] = new_symbol
    tiles = {}
    for tile in settings.tiles:
        new_tile = pygame.Surface((tile['tile_w'], tile['tile_h']), pygame.HWPALETTE, depth=8)
        new_tile.set_palette(bitmaps[tile['tileset']].get_palette())
        new_tile.set_colorkey((255, 0, 255))
        new_tile.blit(
            bitmaps[tile['tileset']],
            (0, 0),
            (tile['tile_x'], tile['tile_y'], tile['tile_w'], tile['tile_h'])
        )
        tiles[tile['name']] = new_tile
    for key, value in settings.map_keys.items():
        if key < 100:  # Tiles
            settings.map_keys[key] = tiles[value]
        elif key < 200:
            settings.map_keys[key] = settings.mega_tiles[value]
        else:
            settings.map_keys[key] = settings.animations[value]
    pygame.display.set_icon(tiles['tree'])
    return bitmaps, tiles, font


def draw_tile(canvas, pygame, settings, x, y, tile, mirror_h=False, mirror_v=False, palette=None):
    if palette is not None:
        tile.set_palette(palette)
    mirrored_surface = pygame.transform.flip(tile, mirror_h, mirror_v)
    canvas.blit(mirrored_surface, (x, y))


def draw_megatile(tiles, canvas, pygame, settings, x, y, megatile, mirror_h=False, mirror_v=False, palette=None):
    for tile_ind in range(0, len(megatile['tiles'])):
        for xy in range(0, len(megatile['tile_xy'][tile_ind])):
            tile_x, tile_y = megatile['tile_xy'][tile_ind][xy]
            tile_mirror_h, tile_mirror_v = megatile['tile_mirror'][tile_ind]
            tile_mirror_h = (mirror_h + tile_mirror_h) == 1
            tile_mirror_v = (mirror_v + tile_mirror_v) == 1
            if palette is None:
                tile_palette = settings.system['palettes'][megatile['tile_palette'][tile_ind]]
            else:
                tile_palette = palette
            """if tile_mirror_h:
                tile_x *= -1
            if tile_mirror_v:
                tile_y *= -1"""
            draw_tile(
                canvas, pygame, settings,
                x + tile_x, y + tile_y,
                tiles[megatile['tiles'][tile_ind]],
                tile_mirror_h, tile_mirror_v,
                tile_palette
            )


def draw_animation(tiles, canvas, counters, pygame, settings, x, y, animation, mirror_h=False, mirror_v=False,
                   palette=None):
    anim_frame = counters[animation['counter']]
    mirror_h = (animation['mirror'][anim_frame][0] + mirror_h) == 1
    mirror_v = (animation['mirror'][anim_frame][1] + mirror_v) == 1
    if palette is None:
        frame_palette = settings.system['palettes'][animation['palettes'][anim_frame]]
    else:
        frame_palette = palette

    if animation['megatiles']:
        megatile = settings.mega_tiles[animation['mega_tiles'][anim_frame]]
        draw_megatile(
            tiles, canvas, pygame, settings,
            x, y, megatile,
            mirror_h, mirror_v, frame_palette
        )
    else:
        tile = tiles[animation['tiles'][anim_frame]]
        draw_tile(
            canvas, pygame, settings,
            x, y,
            tile,
            mirror_h, mirror_v,
            frame_palette
        )


def draw_maze(tiles, canvas, counters, pygame, settings,
              maze, keys, x, y, top, left, bottom, right, squaresize,
              mirror_h=False, mirror_v=False, palette=None):
    if mirror_v:
        start_y = bottom
        finish_y = top - 1
        step_y = -1
    else:
        start_y = top
        finish_y = bottom + 1
        step_y = 1
    if mirror_h:
        start_x = right
        finish_x = left - 1
        step_x = -1
    else:
        start_x = left
        finish_x = right + 1
        step_x = 1
    for i in range(start_y, finish_y, step_y):
        for j in range(start_x, finish_x, step_x):
            maze_stack = maze[i][j]
            if maze_stack is None:
                continue
            elif len(maze_stack) == 0:
                maze[i][j] = None
                continue
            for k in maze_stack:
                try:
                    maze_byte, byte_mirr_x, byte_mirr_y, palette_num = k
                except IndexError:
                    return -1
                if palette is None and palette_num is not None:
                    byte_palette = settings.system['palettes'][palette_num]
                else:
                    byte_palette = palette
                if maze_byte < 100:  # Tiles
                    tile = keys[maze_byte]
                    draw_tile(
                        canvas, pygame, settings,
                        x + abs(j - start_x) * squaresize, y + abs(i - start_y) * squaresize,
                        tile,
                        byte_mirr_x, byte_mirr_y, byte_palette
                    )
                elif maze_byte < 200:  # Mega tiles
                    megatile = keys[maze_byte]
                    draw_megatile(
                        tiles, canvas, pygame, settings,
                        x + abs(j - start_x) * squaresize, y + abs(i - start_y) * squaresize,
                        megatile,
                        byte_mirr_x, byte_mirr_y, byte_palette
                    )
                else:  # Animations
                    animation = keys[maze_byte]
                    draw_animation(tiles, canvas, counters, pygame, settings,
                                   x + abs(j - start_x) * squaresize, y + abs(i - start_y) * squaresize,
                                   animation)
    return 1


def sign(x):
    return (x > 0) - (x < 0)


def draw_text(x, y, text, font, palette, pygame, canvas, settings):
    if palette is not None:
        palette = settings.system['palettes'][palette]
    for i in range(0, len(text)):
        if text[i] == ' ':
            continue
        draw_tile(
            canvas, pygame, settings,
            x + i * 8, y,
            font[text[i]],
            False, False,
            palette=palette
        )

