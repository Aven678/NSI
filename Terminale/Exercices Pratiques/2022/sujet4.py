#Ex 4.1
def recherche(tab):
    lst = []
    old = tab[0]
    for i in range(1, len(tab)):
        if old + 1 == tab[i]:
            lst.append((old, tab[i]))

        old = tab[i]

    return lst

def propager(M, i, j, val):
    if M[i][j]== 0:
        return None # 

    M[i][j] = val

    # l'élément en haut fait partie de la composante
    if ((i-1) >= 0 and M[i-1][j] == 1):
        propager(M, i-1, j, val)

    # l'élément en bas fait partie de la composante
    if ((i+1) < len(M) and M[i+1][j] == 1):
        propager(M, i+1, j, val)

    # l'élément à gauche fait partie de la composante
    if ((j-1) >= 0 and M[i][j-1] == 1):
        propager(M, i, j-1, val)

    # l'élément à droite fait partie de la composante
    if ((j+1) < len(M) and M[i][j+1] == 1):
        propager(M, i, j+1, val)
