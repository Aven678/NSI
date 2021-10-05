def puissance(x,n):
    assert n > 0, "attention n doit être positif"
    if n == 1:
        return x
    else:
        return x * puissance(x,n-1)

print(puissance(4,3))

def pgcd(a,b):

    if b == 0:
        return a
    else:
        return pgcd(b, a%b)

print(pgcd(24,18))

def syracuse(n, vol=0):
    vol += 1

    if n == 1:
        return n, vol
    else:
        #print(n)
        return syracuse(n//2 if n%2==0 else n*3+1,vol)

best = 0
n_best = 0
for x in range(1,100):
    n,vol = syracuse(x)
    if best < vol:
        best = vol
        n_best = x

print(best,n_best)