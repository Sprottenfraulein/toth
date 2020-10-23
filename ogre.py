class Ogre:
    def __init__(self, x, y, lives, speed_arr=2, vision=6, score=100, max_cool=100,
                 homing=False, palette=None, drop=None):
        self.x = x
        self.y = y
        self.drop = drop
        self.lives = lives
        self.direction = 0
        self.distance = 0
        self.speed_slow = 0.5
        self.speed_fast = 1
        self.speed = self.speed_fast
        self.speed_arr = speed_arr
        self.vision = vision
        self.walking = False
        self.homing = homing
        self.slicing = 0
        self.anim_frame = 0
        self.cooldown = 0
        self.max_cool = max_cool
        self.score = score

        self.palette = palette

        self.visible = True
        self.sprites = {
            0: 'ogre_n',
            1: 'ogre_e',
            2: 'ogre_s',
            3: 'ogre_w',
        }
