#Exo 10.1

def maxi(tab):
    max_indice = 0
    for i in range(len(tab)):
        if tab[max_indice] < tab[i]:
            max_indice = i

    return (tab[max_indice], max_indice)

#Exo 10.2

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