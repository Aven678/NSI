#Exo 26.1
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o,','p','q','r','s','t','u','v','w','x','y','z']
def occurrence_max(chaine):
    occurrence = [0]*26
    for i in range(26):
        for c in chaine:
            if c == alphabet[i]:
                occurrence[i]+=1

    k = 0
    for j in range(26):
        if occurrence[j] > occurrence[k]:
            k = j

    return alphabet[k]

#Exo 26.2
def nbLig(image):
    '''renvoie le nombre de lignes de l'image'''
    return len(image)

def nbCol(image):
    '''renvoie la largeur de l'image'''
    return len(image[0])

def negatif(image):
    '''renvoie le négatif de l'image sous la forme d'une liste de listes'''
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))] # on créé une image de 0 aux mêmes dimensions que le paramètre image
    for i in range(len(image)):
        for j in range(len(image[i])):
            L[i][j] = 255-image[i][j]
    return L

def binaire(image, seuil):
    '''renvoie une image binarisée de l'image sous la forme
    d'une liste de listes contenant des 0 si la valeur
    du pixel est strictement inférieure au seuil
    et 1 sinon'''
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))] # on crée une image de 0 aux mêmes dimensions que le paramètre image
    for i in range(len(image)):
        for j in range(len(image[i])):
            if image[i][j] < seuil:
                L[i][j] = 0
            else:
                L[i][j] = 1
    return L    
