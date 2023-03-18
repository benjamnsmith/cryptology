from affine import Affine
from hill import Hill
from crt import CRT
from vignere import Vignere
import modularCongruence


class Driver():

    def __init__(self):
        self.ciphers = {}
        self.ciphers['affine'] = Affine()
        self.ciphers['hill'] = Hill()
        self.ciphers['vignere'] = Vignere()
        self.crtSolver = CRT()


    def attack(self, scheme):
        try:
            self.ciphers[scheme].attack()
            return
        except KeyError:
            return

    def invert(self, n, m):
        try:
            print("The inverse of {} mod {} is {}".format(n, m, pow(int(n), -1, int(m))))
        except ValueError:
            print("{} is not invertible over {}".format(n,m))

    def encrypt(self, scheme, text):
        try:
            self.ciphers[scheme].encrypt(text.lower())
            return
        except KeyError:
            return

    def doCRT(self):
        solver = CRT()
        solver.main()

    def numerals(self, text):
        print("(", end="")
        for i in range(len(text)):
            if text[i] == " ":
                print("-", end = "")
            else: 
                if i == len(text) - 1: 
                    print(ord(text[i])-97, end=")\n")
                else:
                    print(ord(text[i])-97, end=", ")
        return 

    def printUsage(self):
        print("Enter one of the following commands:")
        print("  - encrypt <plaintext> <cipher>")
        print("     where <cipher> is one of ['affine', 'hill', 'vignere'] to encrypt the given plaintext")
        print("  - attack <plaintext> <cipher>")
        print("     where <cipher> is one of ['affine', 'hill'] to perform a known plaintext attack on the ciphertext")
        print("  - crt ")
        print("      to solve a system of linear congruences using the Chinese remainder theorem")
        print("  - invert <num> <mod>")
        print("      to invert <num> over a given modulus <mod>")
        print("  - numerals <text>")
        print("       where <text> is a string of any length and may include spaces. Converts it to its numerical representation")

    def main(self):
        print("A program for computational cryptology methods\n")
        print("You've run this in INTERACTIVE mode\n")
        self.printUsage()
        while True:
            print()
            input_vector = input(">> ").split()
            cmd = input_vector[0]

            if cmd == "encrypt":
                # encrypt <plaintext> <cipher>
                if input_vector[2] not in ["affine", "hill", "vignere"]:
                    print("Cipher type '{}' not recognized".format(input_vector[1])) 
                    continue
                self.encrypt(input_vector[2], input_vector[1])

            elif cmd == "attack":
                # attack <plaintext> <cipher>
                if input_vector[1] not in ["affine", "hill"]:
                    print("Cipher type '{}' not recognized".format(input_vector[1])) 
                    continue
                self.attack(input_vector[1])

            elif cmd == "crt":
                self.crtSolver.main()

            elif cmd == "invert":
                # invert <num> <mod>
                self.invert(input_vector[1], input_vector[2])

            elif cmd == "numerals":
                # numerals <text1> <text2> <text3> ...
                self.numerals("".join(input_vector[1:]))

            elif cmd in ["q", "quit", "exit", "bye"]:
                break

            elif cmd in ["help", "h"]:
                self.printUsage()

            else:
                print("Command '{}' not supported".format(cmd))


d = Driver()
d.main()