from cipher import Cipher 

class Vignere(Cipher):
    def encrypt(self, text):
        key = input("key: ")

        encrypt = ""

        for i in range(len(text)):
            let1 = ord(text[i]) - 97
            let2 = ord(key[i%len(key)]) - 97
            encrypt += chr(((let1 + let2) % 26) + 97)

        self.printResult(text, encrypt, key)

        return
    
    def attack(self):
        return
    
    def __repr__(self):
        return("{}".format(self.__class__.__name__))