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

def syracuse(n):
    if n == 1:
        return n
    else:
        print(n)
        return syracuse(n = n/2 if n%2==0 else n*3+1)

print(syracuse(100))