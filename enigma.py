import rotors as rt

class Enigma:
    def __init__(self, rotor_u: int, rotor_l: int, rotor_m: int, rotor_r: int):
        self.rotor_u = rt.Rotor(num=rotor_u, leftAdjacentRotor=None)
        self.rotor_l = rt.Rotor(num=rotor_l, leftAdjacentRotor=None)
        self.rotor_m = rt.Rotor(num=rotor_m, leftAdjacentRotor=self.rotor_l)
        self.rotor_r = rt.Rotor(num=rotor_r, leftAdjacentRotor=self.rotor_m)
        self.plugBoard = rt.Rotor(14, None)
        self.plugBoard.setAlphabet(self.setPlugBoard())

    def setPlugBoard(self) -> str:
        inpt = input("Please enter the plug connections:\n").upper()
        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        if not inpt.isalpha():
            print("Error with choosing connections, connections contain non alphabetic characters! ")
            return ""
        for i in range(len(inpt) // 2):
            alphabet[alphabet.index(inpt[i * 2])], alphabet[alphabet.index(inpt[i * 2 + 1])] = inpt[i * 2 + 1], inpt[i * 2]
        return str("".join(alphabet))