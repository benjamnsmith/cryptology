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
        
    
