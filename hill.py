"""
A PROGRAM TO DEAL WITH HILL CIPHERS
- ENCRYPTION
- KNOWN PLAINTEXT ATTACK
- coming soon...

"""
from numpy import array, linalg, matmul
from cipher import Cipher


class Hill(Cipher):

    def check_invertibility(self, key):
        return


    def divide(self, text, size):
        ret_arr = []
        low = 0
        high = size

        while True:
            row = []
            for let in text[low:high]:
                row.append(ord(let) - 97)
            ret_arr.append(row)
            low += size
            high += size


            if high > len(text):
                last_chunk = text[low:len(text)]
                if last_chunk != "":
                    if len(last_chunk) != size:
                        last_chunk = last_chunk + ("z"*(size-len(last_chunk)))

                    row = []
                    for let in last_chunk:
                        row.append(ord(let) - 97)
                    ret_arr.append(row)
                return ret_arr


    def encrypt(self, text):
        plain = text
        print("Key/block size:")
        key_size = int(input(">> "))
        print("Please enter each row of the key matrix separated by spaces")
        key = []
        for i in range(key_size):
            row = []
            vals = input().split()
            for val in vals:
                row.append(int(val))
            key.append(row)

        key = array(key)
        try: 
            det = linalg.det(key)
        except Exception as e:
            print("KEY ERROR: {}".format(e))
            return

        if det == 0:
            print("WARNING: uninvertible key (determinant is 0)")

        vectors = self.divide(plain, key_size)
        output = []

        for vector in vectors:
            output.append(matmul(key, vector))

        encrypt = ""

        for arr in output:
            arr = arr.tolist()
            for val in arr:
                encrypt += chr((val%26)+97)

        self.printResult(plain, encrypt, key.tolist())

    def attack(self):
        print("Not implemented")
        return


    def main(self):
        print("\nThis resource provides methods with hill ciphers\n")
        while True:
            
            print("Please choose what you would like to do:")
            print(" (e) encrypt a string using a hill cipher")
            print(" (a) perform a known plaintext attack against a hill ciphertext")
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
