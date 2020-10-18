system = {
    'color_bg': (0, 150, 0),
    'u_color_bg': (0, 100, 100),
    'title_img': 'data/title.png',
    'screen_width': 256,
    'screen_height': 240,
    'screen_scale': 3,
    'main_window_caption': 'Trial of the Herald, v1.1a',
    'view_x': 0,
    'view_y': 0,
    'fps': 60,
    'view_width_sq': 16,
    'view_height_sq': 15,
    'alarms': {            # Counters for animation frames
        'counters': (2,     4,      32),
        'timers':   (15,    10,     0),
        'steps':    (1,     1,      1)
    },
    'palettes': [
        (   # 0
            (255, 0, 255),      # Fuchsia, reserved for color key transparency
            (0, 0, 0),          # Black
            (255, 255, 255),    # White
            (100, 100, 100),    # Dark gray
            (200, 200, 200),    # Light gray
            (155, 75, 0),       # Dark wood
            (220, 150, 0),      # Light wood
            (120, 0, 0),        # Dark red
            (220, 0, 0),        # Bright red
            (0, 100, 100),      # Dark water
            (0, 200, 200),      # Light water
            (0, 150, 0),        # Dark leaves
            (0, 225, 0),        # Light leaves
            (0, 0, 150),        # Deep blue
            (0, 0, 220),        # Bright blue
            (230, 150, 100),    # Skin tone
            (250, 220, 0)       # Yellow
        ),
        (   # 1
            (0, 0, 0),          # Black
            (255, 0, 255),      # Fuchsia, reserved for color key transparency
            (0, 100, 100),      # Dark water
            (0, 200, 200),      # Light water
            (255, 255, 255),    # White
        ),
        (   # 2
            (0, 0, 0),          # Black
            (255, 0, 255),      # Fuchsia, reserved for color key transparency
            (155, 75, 0),       # Dark wood
            (220, 150, 0),      # Light wood
            (255, 255, 255),    # White
        ),
        (   # 3
            (0, 0, 0),          # Black
            (255, 0, 255),      # Fuchsia, reserved for color key transparency
            (220, 0, 0),        # Dark red
            (250, 220, 0),      # Bright yellow
            (255, 255, 255),    # White
        ),
        (   # 4
            (0, 0, 0),          # Black
            (255, 0, 255),      # Fuchsia, reserved for color key transparency
            (220, 150, 0),      # Light wood
            (250, 220, 0),      # Bright yellow
            (255, 255, 255),    # White
        ),
        (   # 5
            (0, 0, 0),          # Black
            (255, 0, 255),      # Fuchsia, reserved for color key transparency
            (120, 0, 0),        # Dark red
            (220, 0, 0),        # Bright red
            (230, 150, 100),    # Skin tone
        ),
        (   # 6
            (0, 100, 100),      # Dark water
            (255, 0, 255),      # Fuchsia, reserved for color key transparency
            (0, 200, 200),      # Light water
            (255, 255, 255),    # White
            (255, 255, 255),    # White
        ),
        (   # 7
            (0, 0, 0),          # Black
            (255, 0, 255),      # Fuchsia, reserved for color key transparency
            (100, 100, 100),    # Dark gray
            (200, 200, 200),    # Light gray
            (255, 255, 255),    # White
        ),
        (   # 8
            (0, 0, 0),          # Black
            (255, 0, 255),      # Fuchsia, reserved for color key transparency
            (120, 0, 0),        # Dark red
            (0, 225, 0),        # Light leaves
            (255, 255, 255),    # White
        ),
        (   # 9
            (0, 0, 0),          # Black
            (255, 0, 255),      # Fuchsia, reserved for color key transparency
            (0, 0, 220),        # Bright blue
            (0, 200, 200),      # Light water
            (255, 255, 255),    # White
        ),
        (   # 10
            (0, 0, 0),          # Black
            (255, 0, 255),      # Fuchsia, reserved for color key transparency
            (0, 150, 0),        # Dark leaves
            (0, 225, 0),        # Light leaves
            (255, 255, 255),    # White
        )
    ],
    'scoreboard': 'data/hiscores',
    'demo': 'data/demo'
}

bitmaps = (
    './data/tileset01.png',  # Tileset #0
)

tiles = (
    {'name': 'brick', 'tileset': 0, 'tile_x': 0, 'tile_y': 32, 'tile_w': 16, 'tile_h': 16},
    {'name': 'fire', 'tileset': 0, 'tile_x': 16, 'tile_y': 0, 'tile_w': 16, 'tile_h': 16},
    {'name': 'log', 'tileset': 0, 'tile_x': 16, 'tile_y': 16, 'tile_w': 16, 'tile_h': 16},
    {'name': 'tree', 'tileset': 0, 'tile_x': 0, 'tile_y': 0, 'tile_w': 16, 'tile_h': 16},
    {'name': 'rock', 'tileset': 0, 'tile_x': 0, 'tile_y': 16, 'tile_w': 16, 'tile_h': 16},
    {'name': 'pit', 'tileset': 0, 'tile_x': 0, 'tile_y': 48, 'tile_w': 16, 'tile_h': 16},
    {'name': 'blade', 'tileset': 0, 'tile_x': 0, 'tile_y': 64, 'tile_w': 16, 'tile_h': 16},
    {'name': 'door', 'tileset': 0, 'tile_x': 16, 'tile_y': 32, 'tile_w': 16, 'tile_h': 16},
    {'name': 'gate', 'tileset': 0, 'tile_x': 16, 'tile_y': 48, 'tile_w': 16, 'tile_h': 16},
    {'name': 'bow', 'tileset': 0, 'tile_x': 16, 'tile_y': 64, 'tile_w': 16, 'tile_h': 16},
    {'name': 'lamp', 'tileset': 0, 'tile_x': 32, 'tile_y': 0, 'tile_w': 16, 'tile_h': 16},
    {'name': 'heart', 'tileset': 0, 'tile_x': 32, 'tile_y': 16, 'tile_w': 16, 'tile_h': 16},
    {'name': 'lock', 'tileset': 0, 'tile_x': 32, 'tile_y': 32, 'tile_w': 16, 'tile_h': 16},
    {'name': 'open', 'tileset': 0, 'tile_x': 32, 'tile_y': 48, 'tile_w': 16, 'tile_h': 16},
    {'name': 'arrow', 'tileset': 0, 'tile_x': 32, 'tile_y': 64, 'tile_w': 16, 'tile_h': 16},
    {'name': 'meat', 'tileset': 0, 'tile_x': 48, 'tile_y': 0, 'tile_w': 16, 'tile_h': 16},
    {'name': 'wound', 'tileset': 0, 'tile_x': 48, 'tile_y': 16, 'tile_w': 16, 'tile_h': 16},
    {'name': 'key', 'tileset': 0, 'tile_x': 48, 'tile_y': 32, 'tile_w': 16, 'tile_h': 16},
    {'name': 'slice_e', 'tileset': 0, 'tile_x': 48, 'tile_y': 48, 'tile_w': 16, 'tile_h': 16},
    {'name': 'slice_n', 'tileset': 0, 'tile_x': 48, 'tile_y': 64, 'tile_w': 16, 'tile_h': 16},
    {'name': 'chick', 'tileset': 0, 'tile_x': 64, 'tile_y': 0, 'tile_w': 16, 'tile_h': 16},
    {'name': 'apple', 'tileset': 0, 'tile_x': 64, 'tile_y': 16, 'tile_w': 16, 'tile_h': 16},
    {'name': 'chest_l', 'tileset': 0, 'tile_x': 64, 'tile_y': 32, 'tile_w': 16, 'tile_h': 16},
    {'name': 'pierce_e', 'tileset': 0, 'tile_x': 64, 'tile_y': 48, 'tile_w': 16, 'tile_h': 16},
    {'name': 'pierce_n', 'tileset': 0, 'tile_x': 64, 'tile_y': 64, 'tile_w': 16, 'tile_h': 16},
    {'name': 'plate', 'tileset': 0, 'tile_x': 80, 'tile_y': 0, 'tile_w': 16, 'tile_h': 16},
    {'name': 'potion', 'tileset': 0, 'tile_x': 80, 'tile_y': 16, 'tile_w': 16, 'tile_h': 16},
    {'name': 'chest_o', 'tileset': 0, 'tile_x': 80, 'tile_y': 32, 'tile_w': 16, 'tile_h': 16},
    {'name': 'coin', 'tileset': 0, 'tile_x': 80, 'tile_y': 48, 'tile_w': 16, 'tile_h': 16},
    {'name': 'gem', 'tileset': 0, 'tile_x': 80, 'tile_y': 64, 'tile_w': 16, 'tile_h': 16},
    {'name': 'skull1', 'tileset': 0, 'tile_x': 96, 'tile_y': 0, 'tile_w': 16, 'tile_h': 16},
    {'name': 'skull2', 'tileset': 0, 'tile_x': 96, 'tile_y': 16, 'tile_w': 16, 'tile_h': 16},
    {'name': 'stone', 'tileset': 0, 'tile_x': 96, 'tile_y': 32, 'tile_w': 16, 'tile_h': 16},
    {'name': 'grass', 'tileset': 0, 'tile_x': 96, 'tile_y': 48, 'tile_w': 16, 'tile_h': 16},
    {'name': 'proj_nw', 'tileset': 0, 'tile_x': 96, 'tile_y': 64, 'tile_w': 16, 'tile_h': 16},
    {'name': 'proj_w', 'tileset': 0, 'tile_x': 112, 'tile_y': 64, 'tile_w': 16, 'tile_h': 16},
    {'name': 'proj_n', 'tileset': 0, 'tile_x': 128, 'tile_y': 64, 'tile_w': 16, 'tile_h': 16},
    {'name': 'splash', 'tileset': 0, 'tile_x': 144, 'tile_y': 64, 'tile_w': 16, 'tile_h': 16},
    {'name': 'hero_n', 'tileset': 0, 'tile_x': 112, 'tile_y': 0, 'tile_w': 16, 'tile_h': 16},
    {'name': 'hero_s', 'tileset': 0, 'tile_x': 112, 'tile_y': 16, 'tile_w': 16, 'tile_h': 16},
    {'name': 'hero_e1', 'tileset': 0, 'tile_x': 112, 'tile_y': 32, 'tile_w': 16, 'tile_h': 16},
    {'name': 'hero_e2', 'tileset': 0, 'tile_x': 112, 'tile_y': 48, 'tile_w': 16, 'tile_h': 16},
    {'name': 'orc_n', 'tileset': 0, 'tile_x': 128, 'tile_y': 0, 'tile_w': 16, 'tile_h': 16},
    {'name': 'orc_s', 'tileset': 0, 'tile_x': 128, 'tile_y': 16, 'tile_w': 16, 'tile_h': 16},
    {'name': 'orc_e1', 'tileset': 0, 'tile_x': 128, 'tile_y': 32, 'tile_w': 16, 'tile_h': 16},
    {'name': 'orc_e2', 'tileset': 0, 'tile_x': 128, 'tile_y': 48, 'tile_w': 16, 'tile_h': 16},
    {'name': 'goblin_n', 'tileset': 0, 'tile_x': 144, 'tile_y': 0, 'tile_w': 16, 'tile_h': 16},
    {'name': 'goblin_s', 'tileset': 0, 'tile_x': 144, 'tile_y': 16, 'tile_w': 16, 'tile_h': 16},
    {'name': 'goblin_e1', 'tileset': 0, 'tile_x': 144, 'tile_y': 32, 'tile_w': 16, 'tile_h': 16},
    {'name': 'goblin_e2', 'tileset': 0, 'tile_x': 144, 'tile_y': 48, 'tile_w': 16, 'tile_h': 16},
    {'name': 'down', 'tileset': 0, 'tile_x': 160, 'tile_y': 0, 'tile_w': 16, 'tile_h': 16},
    {'name': 'up', 'tileset': 0, 'tile_x': 160, 'tile_y': 16, 'tile_w': 16, 'tile_h': 16},
    {'name': 'dust', 'tileset': 0, 'tile_x': 34, 'tile_y': 66, 'tile_w': 2, 'tile_h': 2},
    {'name': 10, 'tileset': 0, 'tile_x': 160, 'tile_y': 32, 'tile_w': 8, 'tile_h': 8},
    {'name': 20, 'tileset': 0, 'tile_x': 168, 'tile_y': 32, 'tile_w': 8, 'tile_h': 8},
    {'name': 50, 'tileset': 0, 'tile_x': 160, 'tile_y': 40, 'tile_w': 8, 'tile_h': 8},
    {'name': 100, 'tileset': 0, 'tile_x': 160, 'tile_y': 48, 'tile_w': 16, 'tile_h': 8},
    {'name': 200, 'tileset': 0, 'tile_x': 160, 'tile_y': 56, 'tile_w': 16, 'tile_h': 8},
    {'name': 500, 'tileset': 0, 'tile_x': 160, 'tile_y': 64, 'tile_w': 16, 'tile_h': 8},
    {'name': 1000, 'tileset': 0, 'tile_x': 160, 'tile_y': 72, 'tile_w': 16, 'tile_h': 8},
    {'name': 2000, 'tileset': 0, 'tile_x': 160, 'tile_y': 80, 'tile_w': 16, 'tile_h': 8},
    {'name': 5000, 'tileset': 0, 'tile_x': 160, 'tile_y': 88, 'tile_w': 16, 'tile_h': 8},
    {'name': 10000, 'tileset': 0, 'tile_x': 160, 'tile_y': 96, 'tile_w': 16, 'tile_h': 8}
)

font = (
    {'name': 'A', 'tileset': 0, 'tile_x': 0, 'tile_y': 248, 'tile_w': 8, 'tile_h': 8},
    {'name': 'B', 'tileset': 0, 'tile_x': 8, 'tile_y': 248, 'tile_w': 8, 'tile_h': 8},
    {'name': 'C', 'tileset': 0, 'tile_x': 16, 'tile_y': 248, 'tile_w': 8, 'tile_h': 8},
    {'name': 'D', 'tileset': 0, 'tile_x': 24, 'tile_y': 248, 'tile_w': 8, 'tile_h': 8},
    {'name': 'E', 'tileset': 0, 'tile_x': 32, 'tile_y': 248, 'tile_w': 8, 'tile_h': 8},
    {'name': 'F', 'tileset': 0, 'tile_x': 40, 'tile_y': 248, 'tile_w': 8, 'tile_h': 8},
    {'name': 'G', 'tileset': 0, 'tile_x': 48, 'tile_y': 248, 'tile_w': 8, 'tile_h': 8},
    {'name': 'H', 'tileset': 0, 'tile_x': 56, 'tile_y': 248, 'tile_w': 8, 'tile_h': 8},
    {'name': 'I', 'tileset': 0, 'tile_x': 64, 'tile_y': 248, 'tile_w': 8, 'tile_h': 8},
    {'name': 'J', 'tileset': 0, 'tile_x': 72, 'tile_y': 248, 'tile_w': 8, 'tile_h': 8},
    {'name': 'K', 'tileset': 0, 'tile_x': 80, 'tile_y': 248, 'tile_w': 8, 'tile_h': 8},
    {'name': 'L', 'tileset': 0, 'tile_x': 88, 'tile_y': 248, 'tile_w': 8, 'tile_h': 8},
    {'name': 'M', 'tileset': 0, 'tile_x': 96, 'tile_y': 248, 'tile_w': 8, 'tile_h': 8},
    {'name': 'N', 'tileset': 0, 'tile_x': 104, 'tile_y': 248, 'tile_w': 8, 'tile_h': 8},
    {'name': 'O', 'tileset': 0, 'tile_x': 112, 'tile_y': 248, 'tile_w': 8, 'tile_h': 8},
    {'name': 'P', 'tileset': 0, 'tile_x': 120, 'tile_y': 248, 'tile_w': 8, 'tile_h': 8},
    {'name': 'Q', 'tileset': 0, 'tile_x': 128, 'tile_y': 248, 'tile_w': 8, 'tile_h': 8},
    {'name': 'R', 'tileset': 0, 'tile_x': 136, 'tile_y': 248, 'tile_w': 8, 'tile_h': 8},
    {'name': 'S', 'tileset': 0, 'tile_x': 144, 'tile_y': 248, 'tile_w': 8, 'tile_h': 8},
    {'name': 'T', 'tileset': 0, 'tile_x': 152, 'tile_y': 248, 'tile_w': 8, 'tile_h': 8},
    {'name': 'U', 'tileset': 0, 'tile_x': 160, 'tile_y': 248, 'tile_w': 8, 'tile_h': 8},
    {'name': 'V', 'tileset': 0, 'tile_x': 168, 'tile_y': 248, 'tile_w': 8, 'tile_h': 8},
    {'name': 'W', 'tileset': 0, 'tile_x': 176, 'tile_y': 248, 'tile_w': 8, 'tile_h': 8},
    {'name': 'X', 'tileset': 0, 'tile_x': 184, 'tile_y': 248, 'tile_w': 8, 'tile_h': 8},
    {'name': 'Y', 'tileset': 0, 'tile_x': 192, 'tile_y': 248, 'tile_w': 8, 'tile_h': 8},
    {'name': 'Z', 'tileset': 0, 'tile_x': 200, 'tile_y': 248, 'tile_w': 8, 'tile_h': 8},
    {'name': '!', 'tileset': 0, 'tile_x': 208, 'tile_y': 248, 'tile_w': 8, 'tile_h': 8},
    {'name': '?', 'tileset': 0, 'tile_x': 216, 'tile_y': 248, 'tile_w': 8, 'tile_h': 8},
    {'name': '.', 'tileset': 0, 'tile_x': 224, 'tile_y': 248, 'tile_w': 8, 'tile_h': 8},
    {'name': ',', 'tileset': 0, 'tile_x': 232, 'tile_y': 248, 'tile_w': 8, 'tile_h': 8},
    {'name': ':', 'tileset': 0, 'tile_x': 240, 'tile_y': 248, 'tile_w': 8, 'tile_h': 8},
    {'name': '-', 'tileset': 0, 'tile_x': 248, 'tile_y': 248, 'tile_w': 8, 'tile_h': 8},
    {'name': '1', 'tileset': 0, 'tile_x': 0, 'tile_y': 240, 'tile_w': 8, 'tile_h': 8},
    {'name': '2', 'tileset': 0, 'tile_x': 8, 'tile_y': 240, 'tile_w': 8, 'tile_h': 8},
    {'name': '3', 'tileset': 0, 'tile_x': 16, 'tile_y': 240, 'tile_w': 8, 'tile_h': 8},
    {'name': '4', 'tileset': 0, 'tile_x': 24, 'tile_y': 240, 'tile_w': 8, 'tile_h': 8},
    {'name': '5', 'tileset': 0, 'tile_x': 32, 'tile_y': 240, 'tile_w': 8, 'tile_h': 8},
    {'name': '6', 'tileset': 0, 'tile_x': 40, 'tile_y': 240, 'tile_w': 8, 'tile_h': 8},
    {'name': '7', 'tileset': 0, 'tile_x': 48, 'tile_y': 240, 'tile_w': 8, 'tile_h': 8},
    {'name': '8', 'tileset': 0, 'tile_x': 56, 'tile_y': 240, 'tile_w': 8, 'tile_h': 8},
    {'name': '9', 'tileset': 0, 'tile_x': 64, 'tile_y': 240, 'tile_w': 8, 'tile_h': 8},
    {'name': '0', 'tileset': 0, 'tile_x': 72, 'tile_y': 240, 'tile_w': 8, 'tile_h': 8},
    {'name': '*', 'tileset': 0, 'tile_x': 80, 'tile_y': 240, 'tile_w': 8, 'tile_h': 8},
)

mega_tiles = {
    'wall': {
        'tiles': ('brick','brick'),
        'tile_xy': (
            (
                (0,0), (16,0), (32,0), (48,0), (64,0), (80,0), (96,0), (112,0)
            ),
            (
                (0,16), (16,16), (32,16), (48,16), (64,16), (80,16), (96,16), (112,16)
            )
        ),
        'tile_mirror': (
            (0,0), (0,0),
        ),
        'tile_palette': (
            1, 2,
        )
    },
    'fire': {
        'tiles': ('fire', ),
        'tile_xy': (
            (
                (0,0),
            ),
        ),
        'tile_mirror': (
            (0,0),
        ),
        'tile_palette': (
            1,
        )
    },
    'treegate': {
        'tiles': ('brick', 'door', 'door', 'tree', 'grass'),
        'tile_xy': (
            (
                (0,16), (16,16), (64,16), (80,16)
            ),
            (
                (32,16),
            ),
            (
                (48,16),
            ),
            (
                (16,0), (64,0), (16,32), (64,32)
            ),
            (
                (0,0), (0,32), (80,0), (80,32)
            )
        ),
        'tile_mirror': (
            (0,0), (0,0), (1,0), (0,0), (0,0)
        ),
        'tile_palette': (
            1, 1, 1, 1, 1
        )
    },
    'down_b': {
        'tiles': ('down', 'rock'),
        'tile_xy': (
            (
                (0,8),
            ),
            (
                (0,0),
            )
        ),
        'tile_mirror': (
            (0,0), (0,0),
        ),
        'tile_palette': (
            7,
        )
    },
    'up_b': {
        'tiles': ('up', 'rock'),
        'tile_xy': (
            (
                (0,8),
            ),
            (
                (0,0),
            )
        ),
        'tile_mirror': (
            (0,0), (0,0),
        ),
        'tile_palette': (
            7,
        )
    }
}

animations = {
    'example01': {
        'tiles': ('wall', 'wall'),
        'megatiles': True,
        'counter': 0,
        'mirror': (
            (0,0), (0,1),
        ),
        'palettes': (1, 1, )
    },
    'fire': {
        'tiles': ('fire', 'fire', ),
        'megatiles': False,
        'counter': 0,
        'mirror': (
            (0,0), (1,0),
        ),
        'palettes': (3, 3)
    },
    'heart': {
        'tiles': ('heart', 'heart'),
        'megatiles': False,
        'counter': 0,
        'mirror': (
            (0,0), (1,0),
        ),
        'palettes': (5, 5)
    },
    'coin': {
        'tiles': ('coin', 'coin', 'coin', 'coin',),
        'megatiles': False,
        'counter': 1,
        'mirror': (
            (0,0), (0,0), (0,0), (0,0),
        ),
        'palettes': (2, 4, 2, 2)
    },
    'gem': {
        'tiles': ('gem', 'gem', 'gem', 'gem',),
        'megatiles': False,
        'counter': 1,
        'mirror': (
            (0,0), (0,0), (0,0), (0,0),
        ),
        'palettes': (1, 6, 1, 1)
    },
    'splash': {
        'tiles': ('splash', 'splash', 'splash', 'splash',),
        'megatiles': False,
        'counter': 1,
        'mirror': (
            (0,0), (1,0), (1,1), (0,1),
        ),
        'palettes': (3, 3, 3, 3)
    },
    'hero_n': {
        'tiles': ('hero_n', 'hero_n'),
        'megatiles': False,
        'counter': 0,
        'mirror': (
            (0,0), (1,0),
        ),
        'palettes': (2, 2)
    },
    'hero_s': {
        'tiles': ('hero_s', 'hero_s'),
        'megatiles': False,
        'counter': 0,
        'mirror': (
            (0,0), (1,0),
        ),
        'palettes': (2, 2)
    },
    'hero_e': {
        'tiles': ('hero_e1', 'hero_e2'),
        'megatiles': False,
        'counter': 0,
        'mirror': (
            (0,0), (0,0),
        ),
        'palettes': (2, 2)
    },
    'hero_w': {
        'tiles': ('hero_e1', 'hero_e2'),
        'megatiles': False,
        'counter': 0,
        'mirror': (
            (1,0), (1,0),
        ),
        'palettes': (2, 2)
    },
    'goblin_n': {
        'tiles': ('goblin_n', 'goblin_n'),
        'megatiles': False,
        'counter': 0,
        'mirror': (
            (0,0), (1,0),
        ),
        'palettes': (10, 10)
    },
    'goblin_s': {
        'tiles': ('goblin_s', 'goblin_s'),
        'megatiles': False,
        'counter': 0,
        'mirror': (
            (0,0), (1,0),
        ),
        'palettes': (10, 10)
    },
    'goblin_e': {
        'tiles': ('goblin_e1', 'goblin_e2'),
        'megatiles': False,
        'counter': 0,
        'mirror': (
            (0,0), (0,0),
        ),
        'palettes': (10, 10)
    },
    'goblin_w': {
        'tiles': ('goblin_e1', 'goblin_e2'),
        'megatiles': False,
        'counter': 0,
        'mirror': (
            (1,0), (1,0),
        ),
        'palettes': (10, 10)
    }
}

map_keys = {
    0: 'brick',
    1: 'fire',
    2: 'log',
    3: 'tree',
    4: 'rock',
    5: 'pit',
    6: 'log',
    7: 'blade',
    8: 'door',
    9: 'gate',
    10: 'bow',
    11: 'lamp',
    12: 'heart',
    13: 'lock',
    14: 'open',
    15: 'arrow',
    16: 'meat',
    17: 'wound',
    18: 'key',
    19: 'slice_e',
    20: 'slice_n',
    21: 'chick',
    22: 'apple',
    23: 'chest_l',
    24: 'pierce_e',
    25: 'pierce_n',
    26: 'plate',
    27: 'potion',
    28: 'chest_o',
    29: 'coin',
    30: 'gem',
    31: 'skull1',
    32: 'skull2',
    33: 'stone',
    34: 'grass',
    35: 'proj_nw',
    36: 'proj_w',
    37: 'proj_n',
    38: 'splash',
    39: 'hero_n',
    40: 'hero_s',
    41: 'hero_e1',
    42: 'hero_e2',
    43: 'orc_n',
    44: 'orc_s',
    45: 'orc_e1',
    46: 'orc_e2',
    47: 'goblin_n',
    48: 'goblin_s',
    49: 'goblin_e1',
    50: 'goblin_e2',
    51: 'down',
    52: 'up',
    151: 'down_b',
    152: 'up_b',
    201: 'fire',
    212: 'heart',
    229: 'coin',
    230: 'gem',
    238: 'splash',
    239: 'hero_n',
    240: 'hero_s',
    241: 'hero_e',
    242: 'hero_w',
}

object_keys = {
    'door': (8, 0, 0, 2),
    'door_o': (14, 0, 0, 2),
    'gate': (9, 0, 0, 7),
    'chest_l': (23, 0, 0, 2),
    'chest_o': (28, 0, 0, 2),
    'gem_fl': (230, 0, 0, 1),
    'tree': (3, 0, 0, 1),
    'grass': (34, 0, 0, 1),
    'brick': (0, 0, 0, 2),
    'rock': (4, 0, 0, 7),
    'rock_i_h': (4, 1, 0, 7),
    'log': (2, 0, 0, 2),
    'arrow': (15, 0, 0, 2),
    'heart': (12, 0, 0, 5),
    'lock': (13, 0, 0, 7),
    'apple': (22, 0, 0, 8),
    'stone': (33, 0, 0, 7),
    'plate': (26, 0, 0, 6),
    'fire_a': (201, 0, 0, 3),
    'coin_fl': (229, 0, 0, 2),
    'chick': (21, 0, 0, 2),
    'meat': (16, 0, 0, 5),
    'potion_bl': (27, 0, 0, 9),
    'skull_c': (31, 0, 0, 7),
    'key': (18, 0, 0, 4),
    'pit': (5, 0, 0, 2),
    'down': (51, 0, 0, 7),
    'up': (52, 0, 0, 7),
    'down_b': (151, 0, 0, 7),
    'up_b': (152, 0, 0, 7),
}


tiles_solid = (0, 3, 4, 8, 9, 13, 23, 151, 152)