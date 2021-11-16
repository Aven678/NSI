#Exo 2.1

def moyenne(tab):
    if len(tab) == 0:
        return 'erreur'

    somme_notes = 0
    for note in tab:
        somme_notes += note

    return somme_notes / len(tab)

#Exo 2.2
def tri(tab):
    i = 0
    j = len(tab)-1
    while i != j :
        if tab[i]== 0:
            i = i+1
        else :
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i] = valeur
            j = j-1
    return tab