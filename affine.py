"""
A PROGRAM TO DEAL WITH AFFINE CIPHERS
- ENCRYPTION
- KNOWN PLAINTEXT ATTACK
- coming soon...

"""
from cipher import Cipher
class Affine(Cipher):
    def encrypt(self, text):
        plain = text
        a = int(input("a: "))
        b = int(input("b: "))

        encrypt = ""

        for let in plain:
            encrypt += chr(((a*(ord(let)-97)+b)%26)+97)

        

        self.printResult(plain, encrypt, (a, b))

    def attack(self):
        print("\nAffine cipher known plaintext attack")
        plain = input("plaintext :  ").lower()
        cipher = input("ciphertext :  ").lower()
        plain_vals = []
        cipher_vals = []
        for i in range(len(plain)):
            plain_vals.append(ord(plain[i])-97)
            cipher_vals.append(ord(cipher[i])-97)
        
        print("plain : ", plain, plain_vals)
        print("cipher: ", cipher, cipher_vals)

        for a in range(26):
            for b in range(26):
                    solution = False
                    for i in range(len(plain_vals)):
                        if ((plain_vals[i]*a + b)%26) == cipher_vals[i]:
                            solution = True
                        else:
                            solution = False
                            break
                    if solution:
                        print("a: ", a, "\nb: ", b, "\n")


    def main(self):
        print("\nThis resource provides methods with affine ciphers\n")
        while True:
            
            print("Please choose what you would like to do:")
            print(" (e) encrypt a string using an affine cipher")
            print(" (a) perform a known plaintext attack against an affine ciphertext")
            print(" (q) quit")
            choice = input(">> ")
            if choice == "e":
                self.encrypt()
            elif choice == "a":
                self.attack()
            elif choice == "q":
                print("goodbye")
                exit(0)
            else:
                print("Command not recognized, please try again")