def invert():
    for i in range(1,27):
        try:
            pow(i, -1, 26)
            print(i, " is invertible under mod 26")
        except:
            continue

def test(nRange, kRange):
    for k in range(kRange):
        found = True
        for n in range(nRange):
            mod = 2*(n**2) + 1
            if (n*(k%mod)) != 2 * (n**2 + 1):
                found = False
                
        if found:
            print("Maybe: {}".format(k))

test(100, 100)