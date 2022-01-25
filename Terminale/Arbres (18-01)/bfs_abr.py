from queue import Queue

class Arbre:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bfs(tree):
    p = []
    file = Queue()
    file.put(tree)
    while not file.empty():
        tree = file.get()
        if tree is not None:
            p.append(tree.data)
            file.put(tree.left)
            file.put(tree.right)

    return p

def infixe(arbre, s = None):
    if s is None:
        s = []
    if arbre is None :
        return None
    infixe(arbre.left, s)
    s.append(arbre.data)
    infixe(arbre.right, s)
    return s


def est_ABR(arbre):
    '''renvoie un booléen indiquant si arbre est un ABR'''
    parcours = infixe(arbre)
    return parcours == sorted(parcours) # on regarde si le parcours est égal au parcours trié 

def contient_valeur(arbre, valeur):
    if arbre is None :
        return False
    if arbre.data == valeur :
        return True
    if valeur < arbre.data :
        return contient_valeur(arbre.left, valeur)
    else:
        return contient_valeur(arbre.right, valeur)

def insertion_abr(arbre, val):
    if arbre is None:
        return Arbre(val)
    
    if val <= arbre.data:
        arbre.left = insertion_abr(arbre.left, val)
    else:
        arbre.right = insertion_abr(arbre.right, val)

    return arbre
