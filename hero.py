class Hero:
    def __init__(self, x, y, max_lives=3, blade=1, max_shots=5, max_keys=5, gems=0, coins=0, score=0, dist=0):
        self.max_lives = max_lives
        self.lives = 3
        self.blade = blade
        self.max_shot = max_shots
        self.shots = 3
        self.max_keys = max_keys
        self.keys = 1
        self.gems = gems
        self.coins = coins
        self.score = score
        self.dist = dist
        self.stage = 0
        self.boss_keys = 0

        self.multiplier = 1
        self.multi_limit = 60
        self.multi_level = 0

        self.x = x
        self.y = y

        self.direction = 0
        self.speed = 1
        self.walking = False
        self.slicing = 0
        self.shotting = False
        self.anim_frame = 0

        self.visible = True
        self.blink = 0
        self.sprites = {
            0: 'hero_n',
            1: 'hero_e',
            2: 'hero_s',
            3: 'hero_w',
        }
