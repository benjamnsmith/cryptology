class Cipher():
    def encrypt():
        pass

    def attack():
        pass

    def __repr__(self):
        return("{}".format(self.__class__.__name__))
    
    def printResult(self, text1, text2, key):
        print("\n{} => {}   ||   Key: {}".format(text1.upper(), text2.upper(), key))