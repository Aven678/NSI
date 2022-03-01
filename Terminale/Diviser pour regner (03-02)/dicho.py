def recherche_dichotomique(tab,val):
    i_debut = 0
    i_fin = len(tab) -1
    while i_debut <= i_fin:
        i_centre = (i_debut+i_fin)//2
        v = tab[i_centre]
        if v == val:
            return True

        if v < val:
            i_debut = i_centre+1
        else:
            i_fin = i_centre-1

    return False

def dicho_rec(tab, val):
    if len(tab) == 0:
        return False

    i_centre = len(tab)//2
    v = tab[i_centre]
    if v == val:
        return True
    if v < val:
        return dicho_rec(tab[i_centre+1:], val)
    else:
        return dicho_rec(tab[:i_centre], val)