"""
My scratch doc to brute force check congruence
"""


def checkCongruence():
    total = {}
    for mod in range(2,4):
        total[mod] = 0
        for x in range(mod):
            for y in range(mod):
                for z in range(mod):
                    val = (x**2 + 6*(y**4) + 3*(z**7))
                    print("({}, {}, {}) | {}".format(x,y,z, val%mod))
                    #print("({})^2 + 6({})^4 + 3({})^7 = {}".format(x, y, z, val))
                    #print("{}%{} = {}".format(val, mod, val%mod))
                    if val%mod != 11%mod:
                        total[mod] += 1

        print("(mod {}): {}".format(mod, total[mod]/mod**3))


def homework6_congruences():
    for x in range(15):
        for y in range(15):
            exp1 = (9 * x + 12 * y) % 21 == 3
            exp2 = (11 * x + 5 * y) % 21 == 12
            if exp1 and exp2:
                print("Found ({},{})".format(x, y))
        
homework6_congruences()
    
