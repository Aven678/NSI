def recherche(tab, n):
    indice_debut = 0
    indice_fin = len(tab)-1
    while indice_debut <= indice_fin:
        indice_milieu = (indice_debut + indice_fin)//2
        if tab[indice_milieu] == n:
            return indice_milieu
        elif tab[indice_milieu] > n:
            indice_fin -=1
        elif tab[indice_milieu] < n:
            indice_debut += 1
        
    
    return -1