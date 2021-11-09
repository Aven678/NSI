def positif(T):
    T2 = list(T)
    T3 = []
    while T2 != []:
        x = T2.pop()
        if x >= 0:
            T3.append(x)
        
    while T3 != []:
        x = T3.pop()
        T2.append(x)
    print('T = ',T)
    return T2

def fibonnaci_recursvite(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)
    
def fibonnaci(n):
    resultats = {1:1, 2:1}
    for i in range(3,n+1):
        resultats[i] = resultats[i-1] + resultats[i-2]
        
    print(resultats[n])