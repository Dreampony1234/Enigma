class Rotor:
    def __init__(self, num: int, leftAdjacentRotor = None):
        self.num = num
        self.leftAdjacentRotor = leftAdjacentRotor
        self.alphabet = self.getAlphabet()
        self.switchPos = self.getSwitchPos()

    def getAlphabet(self) -> str:
        # Get´s the substitution alphabet for the different rotors.
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
                print(f"Error with choosing substitution alphabet! Input was {self.num} of type {type(self.num)}")
                return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def getSwitchPos(self) -> str:
        match self.num:
            case 1:
                return "Q"
            case 2:
                return "E"
            case 3:
                return "V"
            case 4:
                return "J"
            case 5:
                return "Z"
            case 6:
                return "ZM"
            case 7:
                return "ZM"
            case 8:
                return "ZM"
            case 9:
                return "Z"
            case 10:
                return "Z"
            case 11:
                return "Z"
            case 12:
                return "Z"
            case 13:
                return "Z"
            case _:
                print(f"Error with choosing switching position! Input was {self.num} of type {type(self.num)}")
                return "Z"

    def turn(self, num: int = 1) -> None:
        # Appends the first num letters to the end of
        # the Alphabet to simulate a rotation of the rotor.
        self.alphabet = self.alphabet[num % 26:] + self.alphabet[:num % 26]
        if self.alphabet[-1] == self.switchPos and self.leftAdjacentRotor:
            self.leftAdjacentRotor.turn()

    def setAlphabet(self, alphabet) -> None:
        self.alphabet = alphabet

    def forward(self, char) -> str:
        return self.alphabet[ord(char.upper()) - 65]

    def backward(self, char) -> str:
        return chr(list(self.alphabet).index(char) + 65)