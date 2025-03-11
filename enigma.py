import walzen as wz

class Enigma:
    def __init__(self, walze_u: wz.Walze, walze_l: wz.Walze, walze_m: wz.Walze, walze_r: wz.Walze, stecker: list = []):
        self.walze_u: wz.Walze = walze_u
        self.walze_l: wz.Walze = walze_l
        self.walze_m: wz.Walze = walze_m
        self.walze_r: wz.Walze = walze_r
        self.stecker = stecker