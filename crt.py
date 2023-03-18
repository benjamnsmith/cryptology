"""
A PROGRAM TO COMPUTE SOLUTIONS TO SYSTEMS OF LINEAR CONGRUENCES USING THE CHINESE REMAINDER THEOREM

Solves systems of the form:
$x1 \equiv a1 \pmod{m1}$
$x2 \equiv a2 \pmod{m2}$
...
$xi \equiv ai \pmod{mi}$
"""

class CRT():

    def crt(self, arr_a, arr_n):
        big_n = 1
        arr_c = []
        arr_d = []
        resp = 0
        for i in range(len(arr_n)):
            big_n *= arr_n[i]


        for i in range(len(arr_n)):
            arr_c.append(int(big_n/arr_n[i]))
            arr_d.append(pow(arr_c[i], -1, arr_n[i]))

        for i in range(len(arr_n)):
            resp += arr_a[i]*arr_c[i]*arr_d[i]

        print("\n{} should work. {} is in the same equivalence class".format(resp, resp%big_n))

    

    def main(self):
        print("\nCalculate the solutions to systems of linear modular congruences")
        a = []
        n = []
        eq_count = 1
        while True:
            print("\nCongruence {}:".format(eq_count))
            a.append(int(input("x ≡ ")))
            n.append(int(input("mod ")))
            cont = input("continue? ")
            eq_count += 1
            if cont in ["n", "no"]:
                break
        try:
            self.crt(a,n)
        except Exception as e:
            print("Something went wrong. Please try again")
            print(e)
