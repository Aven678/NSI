from logging import NullHandler
from black import nullcontext


class Arbre:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def prefixe(tree):
    if tree is None:
        return None
    
    print(tree.data, end=" ")
    prefixe(tree.left)
    prefixe(tree.right)

def infixe(tree):
    if tree is None:
        return None

    infixe(tree.left)
    print(tree.data, end=" ")
    infixe(tree.right)

def infixe_it(tree):
    s = []
    while (len(s) > 0) or (tree != None):
        if tree != None:
            s.append(tree)
            tree = tree.left

        else:
            tree = s.pop()
            print(tree.data)
            tree = tree.right

def postfix(tree):
    if tree is None:
        return None
    
    postfix(tree.left)
    postfix(tree.right)
    print(tree.data, end=" "  )

def taille(tree):
    if tree is None:
        return 0

    return 1 + taille(tree.left) + taille(tree.right)

def hauteur(tree):
    if tree is None:
        return 0

    return 1 + max(hauteur(tree.left), hauteur(tree.right))

def nbfeuilles(tree):
    if tree is None:
        return 0
    if tree.left is None and tree.right is None:
        return 1
    return nbfeuilles(tree.left) + nbfeuilles(tree.right)

def recherche(tree, val):
    if tree is None:
        return False
    if tree.data == val:
        return True

    return recherche(tree.left, val) or recherche(tree.right, val)