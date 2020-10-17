class Particle:
    def __init__(self, x, y, tile, sp_x=0, sp_y=0, grav=0.3, life=15, palette=None, mirr_x=False, mirr_y=False):
        self.x = x
        self.y = y
        self.sp_x = sp_x
        self.sp_y = sp_y
        self.grav = grav
        self.life = life
        self.tile = tile
        self.palette = palette
        self.mirr_x = mirr_x
        self.mirr_y = mirr_y

    def move(self):
        if self.life > 0:
            self.life -= 1
            self.x += self.sp_x
            self.y += self.sp_y
            self.sp_y += self.grav
            return self.x, self.y
        else:
            return False