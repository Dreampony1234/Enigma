import rotors as rt

class Enigma:
    def __init__(self, walze_u: rt.Rotor, walze_l: rt.Rotor, walze_m: rt.Rotor, walze_r: rt.Rotor, stecker: list = []):
        self.walze_u: rt.Rotor = walze_u
        self.walze_l: rt.Rotor = walze_l
        self.walze_m: rt.Rotor = walze_m
        self.walze_r: rt.Rotor = walze_r
        self.stecker = stecker