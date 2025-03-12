class Walze:
    def __init__(self, num):
        self.num = num
        self.alphabet = self.getAlphabet()

    def getAlphabet(self) -> str:
        # Get´s the substitution alphabet for the different rotors
        # Source: https://kryptografie.de/kryptografie/chiffre/enigma.htm
        match self.num:
            case 1:
                return "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
            case 2:
                return "AJDKSIRUXBLHWTMCQGZNPYFVOE"
            case 3:
                return "BDFHJLCPRTXVZNYEIWGAKMUSQO"
            case 4:
                return "ESOVPZJAYQUIRHXLNFTGKDCMWB"
            case 5:
                return "VZBRGITYUPSDNHLXAWMJQOFECK"
            case 6:
                return "JPGVOUMFYQBENHZRDKASXLICTW"
            case 7:
                return "NZJHGRCXMYSWBOUFAIVLPEKQDT"
            case 8:
                return "FKQHTLXOCBJSPDZRAMEWNIUYGV"
            case 9:
                return "LEYJVCNIXWPBQMDRTAKZGFUHOS"
            case 10:
                return "FSOKANUERHMBTIYCWLQPZXVGJD"
            case 11:
                return "EJMZALYXVBWFCRQUONTSPIKHGD"
            case 12:
                return "YRUHQSLDPXNGOKMIEBFZCWVJAT"
            case 13:
                return "FVPJIAOYEDRZXWGCTKUQSBNMHL"
            case _:
                return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"