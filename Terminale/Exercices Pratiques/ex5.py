def convertir(T):
    """
    T est un tableau d'entiers, dont les éléments sont 0 ou 1 et
    représentant un entier écrit en binaire. Renvoie l'écriture
    décimale de l'entier positif dont la représentation binaire
    est donnée par le tableau T
    """
    result = 0
    for i in range(len(T)-1, -1, -1):
        if T[(len(T)-1)-i] == 1:
            result += 2**i

    return result