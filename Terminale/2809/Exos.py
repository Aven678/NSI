def puissance(x,n):
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