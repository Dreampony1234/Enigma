import rotors as rt

class Enigma:
    def __init__(self, rotor_u: rt.Rotor, rotor_l: rt.Rotor, rotor_m: rt.Rotor, rotor_r: rt.Rotor, stecker: list = []):
        self.rotor_u = rt.Rotor(num=11, leftAdjacentRotor=None)
        self.rotor_l = rt.Rotor(num=1, leftAdjacentRotor=None)
        self.rotor_m = rt.Rotor(num=2, leftAdjacentRotor=self.rotor_l)
        self.rotor_r = rt.Rotor(num=3, leftAdjacentRotor=self.rotor_m)
        self.stecker = stecker