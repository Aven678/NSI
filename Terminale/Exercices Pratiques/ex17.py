#Exo 17.1

def indice_du_min(tab):
    indice_min = 0
    for k in range(len(tab)-1):
        if tab[indice_min] > tab[k]:
            indice_min = k

    return indice_min

#Exo 17.2
def separe(tab):
    i = 0
    j = len(tab)-1
    while i < j :
        if tab[i] == 0 :
            i = i+1
        else :
            tab[i], tab[j] = tab[j], tab[i]
            j = j-1
    return tab