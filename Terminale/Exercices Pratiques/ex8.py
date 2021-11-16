#Exo 8.1

def recherche(caractere, mot):
    n = 0
    
    for lettre in mot:
        if lettre == caractere:
            n += 1

    return n