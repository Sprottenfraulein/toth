class Goblin:
    def __init__(self, x, y, lives, speed=0.25, speed_arr=2, vision=6, score=100, max_cool=100, homing=False, palette=None):
        self.x = x
        self.y = y
        self.lives = lives
        self.direction = 0
        self.distance = 0
        self.speed = speed
        self.speed_arr = speed_arr
        self.vision = vision
        self.walking = False
        self.homing = homing
        self.slicing = 0
        self.anim_frame = 0
        self.cooldown = 0
        self.max_cool = 100
        self.score = score

        self.palette = palette

        self.visible = True
        self.sprites = {
            0: 'goblin_n',
            1: 'goblin_e',
            2: 'goblin_s',
            3: 'goblin_w',
        }