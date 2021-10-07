def F(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    else:
        return F(n-1) + F(n-2)

print(F(2))

def F_imperatif(n, dict={0:0, 1:1}):
    if n in dict:
        return dict[n]

    else:
        dict[n] = F_imperatif(n-1, dict) + F_imperatif(n-2, dict)
    
    return F_imperatif(n-1, dict) + F_imperatif(n-2, dict)

print(F_imperatif(10))