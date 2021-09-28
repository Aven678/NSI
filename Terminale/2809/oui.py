def prix(etage):
    if etage == 0:
        return 3
    else:
        return 2*prix(etage-1)

print(prix(4))

def fact_imp(n):
    fact = n

    while n > 1:
        n = n-1
        fact = fact*n

    return fact

print(fact_imp(5))

def fact_rec(n):
    if n == 1:
        return 1
    else:
        return n * fact_rec(n-1)

print(fact_rec(5)) 