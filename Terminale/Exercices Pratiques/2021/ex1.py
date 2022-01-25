#Exo 1.1
def recherche(tab, n):
    indice = len(tab)
    for i in range(len(tab)):
        if tab[i] == n:
            indice = i

    return indice

#Exo 1.2
from math import sqrt

def distance(point1, point2):
    return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

assert distance((1, 0), (5, 3)) == 5.0, "erreur de calcul"

def plus_courte_distance(tab, depart):
    point = tab[0]
    min_dist = distance(depart, point)
    for i in range (1, len(tab)):
        if distance(tab[i], depart) < min_dist:
            point = tab[i]
            min_dist = distance(tab[i], depart)
    return point

assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 0)) == (2, 5), "erreur"