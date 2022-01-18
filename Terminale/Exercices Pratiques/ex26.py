#Exo 26.1
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o,','p','q','r','s','t','u','v','w','x','y','z']
def occurrence_max(chaine):
    occurrence = [0]*26
    for i in range(26):
        

    k = 0
    for j in range(len(occurrence)-1):
        if occurrence[j] > occurrence[k]:
            k = j

    return k