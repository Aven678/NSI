class Arbre:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def recherche(arbre, element):
    if arbre is None:
        return False
    if arbre.data == element:
        return True
    else:
        if arbre.data > element:
            return recherche(arbre.left, element)
        if arbre.data < element:
            return recherche(arbre.right, element)